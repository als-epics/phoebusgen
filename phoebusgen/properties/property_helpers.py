from xml.etree.ElementTree import Element, SubElement
import sys
from typing import Any, Union, get_origin
from enum import Enum

from collections.abc import Sequence, Mapping

from .types import (
    Color,
    Font,
    Action,
    ObservableDict,
    ObservableList,
    ValidListTypeT,
    ObservableDataclass,
    _validate_color_value
)
from typing import Tuple, TypeVar, Generic, get_args
import inspect
from dataclasses import is_dataclass
from abc import ABC

from collections import namedtuple

Primitive = int | float | str | bool
PropertyType = (
    Primitive
    | Tuple[Primitive, ...]
    | Enum
    | Color
    | Font
    | ObservableDict
    | ObservableList
    | ObservableDataclass
)
PropertyTypeT = TypeVar("PropertyTypeT", bound=PropertyType)

PropertyInfo = namedtuple("PropertyInfo", ["name", "type"])


def _create_element(prop_name: str, value: str | None = None) -> Element:
    element = Element(prop_name)
    if value is not None:
        element.text = str(value)
    return element


def _find_getter_setter_by_type(property_type: type[PropertyType], func: str = "getter") -> str:
    if func not in ["getter", "setter"]:
        raise ValueError("Func arg must must be either 'getter' or 'setter'!")

    property_type_str = property_type.__name__.lower()

    if hasattr(sys.modules[__name__], f"_{func[:-3]}_{property_type_str}_property"):
        return property_type_str
    elif issubclass(property_type, Action):
        return "action"
    elif get_origin(property_type) is ObservableList:
        return "list"
    elif property_type is ObservableDict:
        return "dict"
    elif issubclass(property_type, Enum):
        return "enum"
    elif is_dataclass(property_type):
        return "dataclass"
    elif property_type in get_args(Primitive):
        return "primitive"
    else:
        return property_type_str


def _get_primitive_property(element: Element, prop_type: type[Primitive], default_value: Primitive | None = None) -> Primitive:
    if element is None or element.text is None:
        if default_value is not None:
            return default_value
        return prop_type()

    if prop_type is bool:
        return element.text.lower() == "true"
    else:
        return prop_type(element.text)

def _set_primitive_property(prop_name: str, value: Primitive) -> Element:
    if isinstance(value, bool):
        return _create_element(prop_name, str(value).lower())
    return _create_element(prop_name, str(value))

def _get_enum_property(element: Element, enum_type: type[Enum], default_value: Enum | None = None) -> Enum:
    if element is None or element.text is None:
        if default_value is not None:
            return default_value
        return enum_type(list(enum_type)[0])

    actual_value = element.text
    try:
        actual_value = int(actual_value)
    except ValueError:
        pass

    try:
        return enum_type(actual_value)
    except ValueError:
        print(f"Enum value {element.text} is not valid for property {element.tag}. Using default.")
        return enum_type(list(enum_type)[0])


def _set_enum_property(prop_name: str, value: Enum) -> Element:
    return _create_element(prop_name, value.value)


def _get_color_property(element: Element | None, default_value: Color | None = None) -> Color:
    if element is None:
        if default_value is not None:
            return default_value
        return Color((0, 0, 0))

    color_elem = element.find("color")
    if color_elem is None:
        if default_value is not None:
            return default_value
        return Color((0, 0, 0))

    red = color_elem.get("red", 0)
    green = color_elem.get("green", 0)
    blue = color_elem.get("blue", 0)
    alpha = color_elem.get("alpha", 255)
    if alpha == 255:
        return Color((int(red), int(green), int(blue)))
    else:
        return Color((int(red), int(green), int(blue), int(alpha)))


def _set_color_property(prop_name: str, value: Color | tuple[int, int, int] | tuple[int, int, int, int] | str) -> Element:

    if not isinstance(value, Color):
        value = Color(value)

    element = _create_element(prop_name)
    color_elem = _create_element("color")
    color_elem.attrib["red"] = str(value[0])
    color_elem.attrib["green"] = str(value[1])
    color_elem.attrib["blue"] = str(value[2])

    if len(value) == 4:
        color_elem.attrib["alpha"] = str(value[3])
    else:
        color_elem.attrib["alpha"] = str(255)

    element.append(color_elem)
    return element


def _get_dataclass_property(element: Element | None, dataclass_type: type[ObservableDataclass], default_value: ObservableDataclass | None = None) -> ObservableDataclass:
    if element is None:
        if default_value is not None:
            return default_value
        return dataclass_type()

    field_values = {}
    for field in dataclass_type.fields():
        field_elem = element.find(field)
        field_type = dataclass_type.fields()[field].type
        if field_elem is None and field in element.attrib:
            field_values[field] = field_type(element.attrib[field])
        else:
            getter_name = _find_getter_setter_by_type(field_type, func="getter")
            getter = getattr(sys.modules[__name__], f"_get_{getter_name}_property")
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
                    raise TypeError("Only primitive types or enums can be set as attributes!")
            else:
                setter_name = _find_getter_setter_by_type(field_type, func="setter")
                setter = getattr(sys.modules[__name__], f"_set_{setter_name}_property")
                sub_elem = setter(field, field_value)
                element.append(sub_elem)
    return element

def _get_action_property(element: Element | None, default_value: Action | None = None) -> Action | None:
    if element is None:
        return default_value

    action_type = "".join([word.capitalize() for word in element.attrib.get("type", "").split("_")])
    action_cls_name = f"{action_type}Action"
    action_cls = getattr(sys.modules["phoebusgen.properties.types"], action_cls_name, None)

    if action_cls is None or not issubclass(action_cls, Action):
        raise ValueError(f"Action type {action_type} is not recognized.")

    action = _get_dataclass_property(element, action_cls)
    if not isinstance(action, Action):
        raise ValueError(f"Failed to create action of type {action_type}.")

    return action

def _set_action_property(prop_name: str, value: Action) -> Element:
    print(value)
    element = _set_dataclass_property(prop_name, value)
    action_type = "".join(["_" + c.lower() if c.isupper() and i != 0 else c.lower() for i, c in enumerate(type(value).__name__[:-6])])
    element.attrib["type"] = action_type
    return element

def _get_dict_property(element: Element | None, default_value: ObservableDict | None = None) -> ObservableDict:
    result = ObservableDict()

    if element is None:
        if default_value is not None:
            return default_value
        return result

    for item in element:
        result[item.tag] = item.text

    return result

def _set_dict_property(prop_name: str, value: Mapping) -> Element:
    dict_elem = _create_element(prop_name)
    for k, v in value.items():
        item_elem = _create_element(str(k), str(v))
        dict_elem.append(item_elem)
    return dict_elem

def _get_list_property(element: Element | None, item_type: type[ValidListTypeT], list_item_name: str | None = None, default_value: ObservableList[ValidListTypeT] | None = None) -> ObservableList[ValidListTypeT]:
    if element is None:
        if default_value is not None:
            return default_value
        return ObservableList[ValidListTypeT]()

    result = ObservableList[ValidListTypeT]()
    if element is not None:
        if list_item_name is not None:
            list_prop_name = list_item_name
        elif item_type in get_args(Primitive):
            list_prop_name = element.tag[:-1]  # crude plural to singular
        else:
            list_prop_name = item_type.__name__.lower()
        for item_elem in element.findall(list_prop_name):
            getter_name = _find_getter_setter_by_type(item_type, func="getter")
            getter = getattr(sys.modules[__name__], f"_get_{getter_name}_property")
            getter_args: list[Any] = [item_elem]
            if len(inspect.signature(getter).parameters) > 1:
                getter_args.append(item_type)
            result.append(getter(*getter_args))
    return result

def _set_list_property(prop_name: str, values: Sequence[ValidListTypeT], list_item_name: str | None = None) -> Element:

    list_elem = _create_element(prop_name)
    for item in values:
        if list_item_name is not None:
            list_prop_name = list_item_name
        elif type(item) in get_args(Primitive):
            list_prop_name = prop_name[:-1]  # crude plural to singular
        else:
            list_prop_name = type(item).__name__.lower()
        setter_name = _find_getter_setter_by_type(type(item), func="setter")
        setter = getattr(sys.modules[__name__], f"_set_{setter_name}_property")
        list_elem.append(setter(list_prop_name, item))
    return list_elem

def dynamic_property(prop_name: str, property_type: type[PropertyTypeT], list_item_name: str | None = None, default_value: PropertyTypeT | None = None):

    def decorator(cls):

        element_type = None
        if get_origin(property_type) is ObservableList:
            element_type = get_args(property_type)[0]

        def getter(self) -> PropertyTypeT:

            getter_name = _find_getter_setter_by_type(property_type, func="getter")
            getter_args = [self.root.find(prop_name)]
            getter_kwargs: dict[str, Any] = {"default_value": default_value} 
            if element_type is not None:
                getter_kwargs["list_item_name"] = list_item_name

            typed_getter = getattr(sys.modules[__name__], f"_get_{getter_name}_property")
            if len(inspect.signature(typed_getter).parameters) != (len(getter_args) + len(getter_kwargs)):
                if element_type is not None:
                    getter_args.append(element_type)
                else:
                    getter_args.append(property_type)

            new_val = typed_getter(*getter_args, **getter_kwargs)

            # For compound types, set up a change callback to update the XML when modified
            if hasattr(new_val, '_on_change_callback'):
                def setter_wrapper(new_value: PropertyTypeT) -> None:
                    self.__setattr__(prop_name, new_value)
                new_val._on_change_callback = setter_wrapper

            return new_val

        def setter(self, value: PropertyTypeT) -> None:
            setter_name = _find_getter_setter_by_type(property_type, func="setter")
            setter_args = [prop_name, value]
            setter_kwargs = {} if list_item_name is None else {"list_item_name": list_item_name}

            # TODO: Break out into seperate function
            def validate_input_value(value: PropertyTypeT) -> bool:
                if element_type is not None and isinstance(value, Sequence):
                    if all(isinstance(i, element_type) for i in value):
                        return True
                    raise TypeError(f"Property {prop_name} must be set to be a list with elements of type {get_args(property_type)[0].__name__}!")
                elif property_type is ObservableDict:
                    if not isinstance(value, Mapping):
                        raise TypeError(f"Property {prop_name} must be a dict-like type, got {type(value).__name__}!")
                    return True
                elif property_type is float and isinstance(value, int):
                    return True
                elif not isinstance(value, property_type):
                    raise TypeError(f"Property {prop_name} must be of type {property_type.__name__}, got {type(value).__name__}!")
                return True

            validation_function = validate_input_value
            if hasattr(sys.modules[__name__], f"_validate_{property_type.__name__.lower()}_value"):
                validation_function = getattr(sys.modules[__name__], f"_validate_{property_type.__name__.lower()}_value")

            assert validation_function(value)

            # Remove existing property element if found
            if self.root.find(prop_name) is not None:
                self.root.remove(self.root.find(prop_name))

            new_elem = getattr(sys.modules[__name__], f"_set_{setter_name}_property")(*setter_args, **setter_kwargs)
            self.root.append(new_elem)

        setattr(cls, prop_name, property(getter, setter))
        if not hasattr(cls, "_all_properties"):
            setattr(cls, "_all_properties", {})
        cls._all_properties[cls] = PropertyInfo(prop_name, property_type)


        return cls
    return decorator


class PropertyTypeTracker(type):
    def __new__(cls, name, bases, attrs):
        # Collect property names and types from base classes
        property_types = {}
        for base in bases:
            if hasattr(base, "_all_properties"):
                property_types.update(base._all_properties)

        # Add property names and types from the current class
        if "_all_properties" in attrs:
            property_types.update(attrs["_all_properties"])

        attrs["_all_properties"] = property_types
        return super().__new__(cls, name, bases, attrs)


class PropertyBase(metaclass=PropertyTypeTracker):
    root: Element
    _all_properties: dict[type['PropertyBase'], PropertyInfo] = {}

    @classmethod
    def get_property_name(cls, property_cls: type['PropertyBase'] | None = None) -> str:
        if property_cls is None:
            property_cls = cls

        if property_cls not in cls._all_properties:
            raise ValueError(f"Class {cls.__name__} is not a property!")

        return cls._all_properties[property_cls].name

    @classmethod
    def get_property_type(cls, property_cls: type['PropertyBase'] | None = None) -> type[PropertyType]:
        if property_cls is None:
            property_cls = cls

        if property_cls not in cls._all_properties:
            raise ValueError(f"Class {cls.__name__} is not a property!")

        return cls._all_properties[property_cls].type

    @classmethod
    def get_property_type_by_name(cls, property_name: str) -> type[PropertyType]:

        for prop_name, prop_type in cls._all_properties.values():
            if prop_name == property_name:
                return prop_type
        raise ValueError(f"Class {cls.__name__} does not have a property named {property_name}!")
