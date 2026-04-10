import copy
from xml.etree.ElementTree import Element
import sys
from enum import Enum

import inspect
from collections.abc import Mapping
from collections import namedtuple
from dataclasses import is_dataclass

from typing import Any, Dict, List, Optional, Sequence, Tuple, Type, TypeVar, Union

# get_origin / get_args were added in Python 3.8; provide a shim for 3.6/3.7
try:
    from typing import get_origin, get_args  # novermin
except ImportError:
    def get_origin(tp):
        return getattr(tp, '__origin__', None)

    def get_args(tp):
        return getattr(tp, '__args__', ())

from .types import (
    Color,
    Font,
    Action,
    ObservableDict,
    ObservableList,
    ValidListTypeT,
    ObservableDataclass
)

Primitive = Union[int, float, str, bool]
PropertyType = Union[
    int, float, str, bool,
    Tuple,
    Enum,
    Color,
    Font,
    ObservableDict,
    ObservableList,
    ObservableDataclass,
]
PropertyTypeT = TypeVar('PropertyTypeT', bound=PropertyType)

PropertyInfo = namedtuple('PropertyInfo', ['type', 'default_value'])


def _create_element(prop_name: str, value: Optional[str] = None) -> Element:
    element = Element(prop_name)
    if value is not None:
        element.text = str(value)
    return element


def _find_getter_setter_by_type(property_type: Type[PropertyType], func: str = 'getter') -> str:
    if func not in ['getter', 'setter']:
        raise ValueError("Func arg must must be either 'getter' or 'setter'!")

    if hasattr(property_type, '__origin__'):
        property_type = property_type.__origin__

    property_type_str = property_type.__name__.lower()

    if hasattr(sys.modules[__name__], f'_{func[:-3]}_{property_type_str}_property'):
        return property_type_str
    elif issubclass(property_type, Action):
        return 'action'
    elif property_type is ObservableList:
        return 'list'
    elif property_type is ObservableDict:
        return 'dict'
    elif issubclass(property_type, Enum):
        return 'enum'
    elif is_dataclass(property_type):
        return 'dataclass'
    elif property_type in get_args(Primitive):
        return 'primitive'
    else:
        return property_type_str


def _get_primitive_property(element: Element, prop_type: Type[Primitive]) -> Primitive:

    if element.text is None:
        raise ValueError(f"XML element for primitive property '{element.tag}' has no text value!")

    if prop_type is bool:
        return element.text.lower() == 'true'
    else:
        return prop_type(element.text)

def _set_primitive_property(prop_name: str, value: Primitive) -> Element:
    if isinstance(value, bool):
        return _create_element(prop_name, str(value).lower())
    return _create_element(prop_name, str(value))

def _get_enum_property(element: Element, enum_type: Type[Enum]) -> Enum:
    if element.text is None:
        raise ValueError('Enum property element has no text value!')

    actual_value = element.text
    if issubclass(enum_type, int):
        actual_value = int(actual_value)

    return enum_type(actual_value)


def _set_enum_property(prop_name: str, value: Enum) -> Element:
    return _create_element(prop_name, value.value)


def _get_color_property(element: Element) -> Color:
    color_elem = element.find('color')
    if color_elem is None:
        raise ValueError('Color property element has no color child element!')

    red = color_elem.attrib.get('red', 0)
    green = color_elem.attrib.get('green', 0)
    blue = color_elem.attrib.get('blue', 0)
    alpha = color_elem.attrib.get('alpha', 255)
    if alpha == 255:
        return Color((int(red), int(green), int(blue)))
    else:
        return Color((int(red), int(green), int(blue), int(alpha)))


def _set_color_property(prop_name: str, value: Union[Color, Tuple[int, int, int], Tuple[int, int, int, int], str]) -> Element:

    if not isinstance(value, Color):
        value = Color(value)

    element = _create_element(prop_name)
    color_elem = _create_element('color')
    color_elem.attrib['red'] = str(value[0])
    color_elem.attrib['green'] = str(value[1])
    color_elem.attrib['blue'] = str(value[2])

    if len(value) == 4:
        color_elem.attrib['alpha'] = str(value[3])
    else:
        color_elem.attrib['alpha'] = str(255)

    element.append(color_elem)
    return element


def _get_dataclass_property(element: Element, dataclass_type: Type[ObservableDataclass]) -> ObservableDataclass:

    field_values = {}
    for field in dataclass_type.fields():
        field_elem = element.find(field)
        field_type = dataclass_type.fields()[field].type
        if field_elem is None and field in element.attrib:
            field_values[field] = field_type(element.attrib[field])
        elif field_elem is not None and (field_elem.text is not None or field_type not in get_args(Primitive)):
            getter_name = _find_getter_setter_by_type(field_type, func='getter')
            getter = getattr(sys.modules[__name__], f'_get_{getter_name}_property')
            getter_args = [field_elem]
            if len(inspect.signature(getter).parameters) > 1:
                getter_args.append(field_type)
            field_values[field] = getter(*getter_args)

    return dataclass_type(**field_values)

def _set_dataclass_property(prop_name: str, value: ObservableDataclass) -> Element:

    element = _create_element(prop_name)

    property_cls = type(value)

    for field in value.fields():
        field_value = getattr(value, field)
        field_type = property_cls.fields()[field].type
        if field_value is not None:
            if field in value._attrib_fields:
                if field_type in get_args(Primitive):
                    element.attrib[field] = str(field_value)
                elif isinstance(field_value, Enum):
                    element.attrib[field] = field_value.value
                else:
                    raise TypeError('Only primitive types or enums can be set as attributes!')
            else:
                setter_name = _find_getter_setter_by_type(field_type, func='setter')
                setter = getattr(sys.modules[__name__], f'_set_{setter_name}_property')
                sub_elem = setter(field, field_value)
                element.append(sub_elem)
    return element

def _get_action_property(element: Element) -> Action:
    action_type = ''.join([word.capitalize() for word in element.attrib.get('type', '').split('_')])
    action_cls_name = f'{action_type}Action'
    action_cls = getattr(sys.modules['phoebusgen.v4.properties.types'], action_cls_name, None)

    if action_cls is None or not issubclass(action_cls, Action):
        raise ValueError(f'Action type {action_type} is not recognized.')

    action = _get_dataclass_property(element, action_cls)
    if not isinstance(action, Action):
        raise ValueError(f'Failed to create action of type {action_type}.')

    return action

def _set_action_property(prop_name: str, value: Action) -> Element:
    element = _set_dataclass_property('action', value)
    action_type = ''.join(['_' + c.lower() if c.isupper() and i != 0 else c.lower() for i, c in enumerate(type(value).__name__[:-6])])
    element.attrib['type'] = action_type
    return element

def _get_dict_property(element: Element) -> ObservableDict:

    result = ObservableDict()

    for item in element:
        result[item.tag] = item.text

    return result

def _set_dict_property(prop_name: str, value: Mapping) -> Element:
    dict_elem = _create_element(prop_name)
    for k, v in value.items():
        item_elem = _create_element(str(k), str(v))
        dict_elem.append(item_elem)
    return dict_elem

def _get_list_property(element: Element, item_type: Type[ValidListTypeT]) -> ObservableList:

    result = ObservableList[ValidListTypeT]()
    if element is not None:
        for item_elem in element:
            getter_name = _find_getter_setter_by_type(item_type, func='getter')
            getter = getattr(sys.modules[__name__], f'_get_{getter_name}_property')
            getter_args: List[Any] = [item_elem]
            if len(inspect.signature(getter).parameters) > 1:
                getter_args.append(item_type)
            result.append(getter(*getter_args))
    return result

def _set_list_property(prop_name: str, values: Sequence[ValidListTypeT]) -> Element:

    list_elem = _create_element(prop_name)
    for item in values:
        # For lists, the item element name is usually the singular form of the list property name
        # The only exception is for properties ending in "axis", which become "axes"
        if prop_name.endswith('axes'):
            list_item_name = prop_name.replace('axes', 'axis')
        else:
            list_item_name = prop_name[:-1]

        setter_name = _find_getter_setter_by_type(type(item), func='setter')
        setter = getattr(sys.modules[__name__], f'_set_{setter_name}_property')
        list_elem.append(setter(list_item_name, item))
    return list_elem

def is_set_value_valid(value: PropertyType, expected_type: Type[PropertyType]) -> bool:
    def _validate_element(value: PropertyType, expected_type: Type[PropertyType]) -> bool:
        if expected_type is Color:
            return Color.is_color(value)
        elif expected_type is ObservableDict:
            return isinstance(value, Mapping)
        elif expected_type is float:
            return isinstance(value, (float, int))
        else:
            return isinstance(value, expected_type)

    if get_origin(expected_type) is ObservableList:
        expected_type = get_args(expected_type)[0]
        if not isinstance(value, Sequence):
            return False
        else:
            return all(_validate_element(v, expected_type) for v in value)

    return _validate_element(value, expected_type)


class PropertyMetaclass(type):
    def __new__(mcs, name, bases, attrs):

        all_properties = {}
        cls = super().__new__(mcs, name, bases, attrs)

        def getter(self, prop_name: str, property_type: Type[PropertyType]) -> PropertyType:
            prop_element = self.root.find(prop_name)

            if prop_element is not None:

                getter_name = _find_getter_setter_by_type(property_type, func='getter')
                typed_getter = getattr(sys.modules[__name__], f'_get_{getter_name}_property')

                # For lists, we pass the item type instead
                if get_origin(property_type) is ObservableList:
                    property_type = get_args(property_type)[0]

                getter_args = [prop_element]

                if len(inspect.signature(typed_getter).parameters) != len(getter_args):
                    getter_args.append(property_type)

                new_val = typed_getter(*getter_args)
            else:
                # If element for property was not found, use the default value. Make it a
                # deep copy so that mutable types don't share references.
                new_val = copy.deepcopy(self._all_properties[cls][prop_name].default_value)

            # For compound types, set up a change callback to update the XML when compoents are modified
            # i.e. a list element is added/removed, a dict item is changed, or a dataclass field is updated
            if isinstance(new_val, (ObservableDataclass, ObservableDict, ObservableList)) and hasattr(new_val, '_on_change_callback'):
                def setter_wrapper(new_value: PropertyType) -> None:
                    self.__setattr__(prop_name, new_value)
                new_val._on_change_callback = setter_wrapper

            return new_val

        def setter(self, prop_name: str, property_type: Type[PropertyType], value: PropertyType) -> None:
            setter_name = _find_getter_setter_by_type(property_type, func='setter')

            if not is_set_value_valid(value, property_type):
                raise TypeError(f"Value {value} is of invalid type for property '{prop_name}': must be of type {property_type}")

            # Remove existing property element if found
            if self.root.find(prop_name) is not None:
                self.root.remove(self.root.find(prop_name))

            new_elem = getattr(sys.modules[__name__], f'_set_{setter_name}_property')(prop_name, value)
            self.root.append(new_elem)

        # Only create dynamic properties for classes that directly inherit from PropertyBase, not for subclasses of those classes.
        # This way we can have property classes that inherit from other property classes without overwriting the properties defined in the parent class.
        if name not in ['PropertyBase', 'Widget', 'Screen'] and not any(base.__name__ in ['Widget', 'Screen'] for base in bases):
            all_properties[cls] = {}
            for prop_name, annotation in cls.__annotations__.items():
                if hasattr(annotation, '__origin__'):
                    property_type = annotation.__origin__
                else:
                    property_type = annotation
                default_value = attrs.get(prop_name, property_type() if not issubclass(property_type, Enum) else list(property_type)[0])

                def prop_getter(self, prop_name=prop_name, prop_type=annotation):
                    return getter(self, prop_name, prop_type)
                def prop_setter(self, value, prop_name=prop_name, prop_type=annotation):
                    return setter(self, prop_name, prop_type, value)

                setattr(cls, prop_name, property(prop_getter, prop_setter))
                all_properties[cls][prop_name] = PropertyInfo(property_type, default_value)

        # Collect property names and types from base classes to keep a running dictionary
        # of all property classes and the individual properties they define
        for base in bases:
            if hasattr(base, '_all_properties'):
                all_properties.update(base._all_properties)

        if '_all_properties' in attrs:
            all_properties.update(attrs['_all_properties'])
        setattr(cls, '_all_properties', all_properties)

        return cls


class PropertyBase(metaclass=PropertyMetaclass):
    root: Element
    _all_properties: Dict[Type['PropertyBase'], Dict[str, PropertyInfo]] = {}

    @classmethod
    def get_property_classes(cls) -> List[Type['PropertyBase']]:
        return list(cls._all_properties.keys())

    @classmethod
    def get_property_names(cls, property_cls: Optional[Type['PropertyBase']] = None) -> List[str]:
        if property_cls is not None:
            if property_cls not in cls._all_properties:
                raise ValueError(f'Property class {property_cls.__name__} not found in class {cls.__name__}!')
            return list(cls._all_properties[property_cls].keys())
        else:
            property_names = []
            for property_cls in cls._all_properties:
                property_names.extend(cls._all_properties[property_cls].keys())
            return property_names

    @classmethod
    def get_property_type_by_name(cls, property_name: str) -> Type[PropertyType]:
        for property_cls in cls._all_properties:
            if property_name in cls._all_properties[property_cls]:
                return cls._all_properties[property_cls][property_name].type
        raise ValueError(f'Property {property_name} not found in class {cls.__name__}!')
