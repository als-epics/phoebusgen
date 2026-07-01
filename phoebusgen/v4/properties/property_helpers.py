import copy
import inspect
import sys
from collections.abc import Mapping
from dataclasses import dataclass, is_dataclass
from enum import Enum
from pathlib import Path
from types import NoneType
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Type, TypeVar, Union
from xml.etree.ElementTree import Element

from phoebusgen.v4.utils import PhoebusElement

# get_origin / get_args were added in Python 3.8; provide a shim for 3.6/3.7
try:
    from typing import get_args, get_origin  # novermin
except ImportError:
    def get_origin(tp):
        return getattr(tp, '__origin__', None)

    def get_args(tp):
        return getattr(tp, '__args__', ())

from .types import (
    Action,
    Color,
    Font,
    ObservableDataclass,
    ObservableDict,
    ObservableList,
    Rule,
    RuleExpression,
    ValidListTypeT,
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
    Rule,
    RuleExpression,
]
PropertyTypeT = TypeVar('PropertyTypeT', bound=PropertyType)

@dataclass
class PropertyInfo:
    type: Type[PropertyTypeT]
    default_value: PropertyTypeT


def _create_element(prop_name: str, value: Optional[str] = None) -> Element:
    """Create an XML element with the given property name and optional value.

    :param prop_name: The name of the property
    :param value: The optional value of the property
    :return: An XML element with the given property name and value
    """

    element = Element(prop_name)
    if value is not None:
        element.text = str(value)
    return element


def _unpack_union_type(union_type: Type[PropertyType]) -> Type[PropertyType]:
    """Given a Union type, return the first non-None type in the union.

    For example, given Union[int, None], this function will return int.
    If there are multiple non-None types, the first one is returned.
    If there are no non-None types, None is returned.

    :param union_type: The Union type to unpack
    :return: The first non-None type in the union, or None if there are no non-None types
    """
    if get_origin(union_type) is not Union:
        raise ValueError(f"Type {union_type} is not a Union type!")

    args = get_args(union_type)
    non_none_args = [arg for arg in args if arg is not NoneType]
    if len(non_none_args) == 0:
        raise ValueError(f"Union type {union_type} has no non-None types!")
    return non_none_args[0]


def _normalize_property_type(property_type: Type[PropertyType]) -> Type[PropertyType]:
    """Given a property type, normalize it to a single type for use in the _all_properties dictionary.

    :param property_type: The property type to normalize
    :return: The normalized property type
    """

    if get_origin(property_type) is Union:
        return _normalize_property_type(_unpack_union_type(property_type))
    args = get_args(property_type)
    if args:
        origin = get_origin(property_type)
        # On Python < 3.9, builtin types (list, dict, tuple) don't support
        # subscripting directly; use their typing module equivalents instead.
        _builtin_to_typing = {list: List, dict: Dict, tuple: Tuple}
        subscriptable = _builtin_to_typing.get(origin, origin)
        normalized_args = tuple(_normalize_property_type(arg) for arg in args)
        if len(normalized_args) == 1:
            return subscriptable[normalized_args[0]]
        return subscriptable[normalized_args]
    return property_type


def _make_default_prop_val(property_type: Type[PropertyType]) -> PropertyType:
    """Given a property type, return a default value for it.

    For example, for int return 0, for str return '', for ObservableList return an empty list, etc.

    :param property_type: The type of the property to create a default value for
    :return: A default value for the property type
    """

    if get_origin(property_type) is list:
        return ObservableList()
    elif get_origin(property_type) is dict:
        return ObservableDict()
    elif isinstance(property_type, type) and issubclass(property_type, Enum):
        return list(property_type)[0]
    else:
        return property_type()  # Call the type to get a default value (e.g. int() -> 0, str() -> '', etc.)


class PropertyMetaclass(type):
    def __new__(mcs, name: str, bases: List[Type], attrs: Dict[str, object]) -> Type:

        # Keep a running dictionary of all properties defined by all property mixin classes,
        # so that we can look up property types and default values by name at runtime for any
        # class that inherits from those mixins, even indirectly.
        all_properties: Dict[Type, Dict[str, PropertyInfo]] = {}

        # Create the new class
        cls = super().__new__(mcs, name, bases, attrs)

        def getter(self: 'PropertyBase', prop_name: str, property_type: Type[PropertyType]) -> PropertyType:
            tag_name = self._get_property_tag_name(prop_name)
            element = self.root.find(tag_name) if tag_name is not None else self.root
            if element is not None:
                # Get the appropriate getter function for the property type
                typed_getter = self._find_getter_by_type(property_type)

                # For lists, we pass the item type instead
                if get_origin(property_type) is list:
                    property_type = get_args(property_type)[0]

                # Based on the function signature, dynamically create a list of arguments
                # from the local variables in the current scope
                getter_args = []
                for param_name in inspect.signature(typed_getter).parameters.keys():
                    getter_args.append(locals().get(param_name))

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

        def setter(self: 'PropertyBase', prop_name: str, property_type: Type[PropertyType], value: PropertyType) -> None:

            tag_name = self._get_property_tag_name(prop_name)
            typed_setter = self._find_setter_by_type(property_type)

            if not self._is_set_value_valid(value, property_type):
                raise TypeError(f"Value {value} is of invalid type for property '{prop_name}': must be of type {property_type}")

            # Remove existing property element if found
            if tag_name is not None and self.root.find(tag_name) is not None:
                self.root.remove(self.root.find(tag_name))
            elif tag_name is None and get_origin(property_type) is list:
                # For list properties stored as direct children (tag_name=None),
                # remove all existing child elements with the item tag name
                item_tag = self._get_list_item_tag_name(prop_name)
                for existing in self.root.findall(item_tag):
                    self.root.remove(existing)

            setter_args = []
            for param_name in inspect.signature(typed_setter).parameters.keys():
                setter_args.append(locals().get(param_name))

            # Setter funtions always take property name and a new value
            new_elem = typed_setter(*setter_args)
            self.root.extend(new_elem if isinstance(new_elem, Sequence) else [new_elem])

        # Only create dynamic properties for classes that directly inherit from PropertyBase, not for subclasses of those classes.
        # This way we can have property classes that inherit from other property classes without overwriting the propertiesdefined in the parent class.
        if name not in ['PropertyBase', 'Widget', 'Screen'] and not any(base.__name__ in ['Widget', 'Screen'] for base in bases):
            all_properties[cls] = {}
            for prop_name, annotation in cls.__annotations__.items():

                # Unwrap Optional[X] (Union[X, None]) to X for property type resolution
                property_type = _normalize_property_type(annotation)
                default_value = attrs.get(prop_name, _make_default_prop_val(property_type))

                def prop_getter(self, prop_name=prop_name, prop_type=property_type):
                    return getter(self, prop_name, prop_type)
                def prop_setter(self, value, prop_name=prop_name, prop_type=property_type):
                    return setter(self, prop_name, prop_type, value)

                setattr(cls, prop_name, property(prop_getter, prop_setter))
                all_properties[cls][prop_name] = PropertyInfo(type=property_type, default_value=default_value)


        # Collect property names and types from base classes to keep a running dictionary
        # of all property classes and the individual properties they define
        for base in bases:
            if hasattr(base, '_all_properties'):
                all_properties.update(base._all_properties)

        if '_all_properties' in attrs:
            all_properties.update(attrs['_all_properties'])

        # Allow subclasses (e.g. Screen, Widget) to override default values for inherited
        # properties by declaring class-level annotations with a value. For example:
        #   class Screen(...):
        #       width: int = 800
        # This keeps type checker support while customizing defaults per class.
        # Only applies to classes that don't define their own properties (i.e. Widget/Screen and their subclasses).
        is_property_mixin = name not in ['PropertyBase', 'Widget', 'Screen'] and not any(base.__name__ in ['Widget', 'Screen'] for base in bases)
        if not is_property_mixin:
            for prop_name, default_val in attrs.items():
                if prop_name.startswith('_') or callable(default_val) or isinstance(default_val, (classmethod, staticmethod, property)):
                    continue
                # Check if this attribute matches a property defined in a parent mixin
                for prop_cls, props in all_properties.items():
                    if prop_name in props:
                        # Make a per-class copy of the mixin's property dict so we don't mutate the shared one
                        all_properties[prop_cls] = copy.deepcopy(all_properties[prop_cls])
                        all_properties[prop_cls][prop_name].default_value = default_val
                        # Remove the class attribute so the property descriptor from the mixin is used
                        if prop_name in cls.__dict__:
                            delattr(cls, prop_name)
                        break

        setattr(cls, '_all_properties', all_properties)

        return cls


class PropertyBase(metaclass=PropertyMetaclass):
    root: Element
    _all_properties: Dict[Type['PropertyBase'], Dict[str, PropertyInfo]] = {}
    _property_tag_names: Dict[str, Optional[str]] = {}

    @classmethod
    def _get_property_tag_name(cls, property_name: str) -> Optional[str]:
        """Get the XML tag name used for a given property.

        :param property_name: The name of the property to get the tag name for
        :return: The XML tag name used for the property, or None if the property is configured to add its XML directly to the root element
        """
        if property_name not in cls.get_property_names():
            raise ValueError(f"Property '{property_name}' is not a valid property of class '{cls.__name__}'!")

        if property_name in cls._property_tag_names:
            return cls._property_tag_names[property_name]
        else:
            return property_name

    @classmethod
    def _override_property_tag_name(cls, property_name: str, tag_name: Optional[str]) -> None:
        """Override the default XML tag name used for a property.

        By default, the tag name for the XML element for a property is the same as the property name.
        For example, a property named 'background_color' would be represented in XML as <background_color>...</background_color>.
        In some cases, such as for the widgets property, we want to use a different tag name (e.g. 'children')
        or no tag at all and instead add the child elements directly to the root element.

        If None is given for tag_name, the property must be a list or dictionary - and
        the generated tags will be instead added to the root element instead.

        :param property_name: The name of the property to override the tag for
        :param tag_name: The XML tag name to use for the property, or None to use the default (same as property name)
        """

        property_type = cls.get_property_type_by_name(property_name)
        if tag_name is None and get_origin(property_type) not in (list, dict):
            raise ValueError(f"Only list or dict properties can have tag_name set to None, but property '{property_name}' is of type '{property_type}'!")

        # Ensure we have a per-class dict rather than mutating a parent class's dict
        if '_property_tag_names' not in cls.__dict__:
            cls._property_tag_names = dict(cls._property_tag_names)

        cls._property_tag_names[property_name] = tag_name

    @classmethod
    def _set_default_value(cls, property_name: str, default_value: PropertyType) -> None:
        """Set the default value for a property, which is used when the property is accessed but not found in the XML.

        :param property_name: The name of the property to set the default value for
        :param default_value: The default value to use for the property when it is not found in the XML
        """

        if property_name not in cls.get_property_names():
            raise ValueError(f"Property '{property_name}' is not a valid property of class '{cls.__name__}'!")

        # Find which class in _all_properties defines this property
        owner_cls = None
        for prop_cls, props in cls._all_properties.items():
            if property_name in props:
                owner_cls = prop_cls
                break

        if owner_cls is None:
            raise ValueError(f"Property '{property_name}' is not defined in any property class for '{cls.__name__}'!")

        # Ensure we have a per-class copy so we don't mutate the shared parent dict.
        # Track which inner dicts have been copied via a set on the class.
        if not hasattr(cls, '_copied_property_classes'):
            cls._copied_property_classes = set()
        if owner_cls not in cls._copied_property_classes:
            cls._all_properties = dict(cls._all_properties)
            cls._all_properties[owner_cls] = copy.deepcopy(cls._all_properties[owner_cls])
            cls._copied_property_classes.add(owner_cls)

        cls._all_properties[owner_cls][property_name].default_value = default_value

    @classmethod
    def get_property_classes(cls) -> List[Type['PropertyBase']]:
        """Return a list of all property mixins this class inheritys, including itself if it is a property mixin.

        :return: List of property mixin classes
        """

        return list(cls._all_properties.keys())


    @classmethod
    def get_property_names(cls, property_cls: Optional[Type['PropertyBase']] = None) -> List[str]:

        """Return a list of property names for a given property class or all property classes if none is specified.

        :param property_cls: The property class to get names for, or None to get names for all property classes
        :return: List of property names
        """

        if property_cls is not None:
            if property_cls not in cls._all_properties:
                raise ValueError(f"Class '{property_cls.__name__}' is not a property mixin class that '{cls.__name__}' inherits from!")
            return list(cls._all_properties[property_cls].keys())
        else:
            property_names = []
            for property_cls in cls._all_properties:
                property_names.extend(cls._all_properties[property_cls].keys())
            return property_names


    @classmethod
    def get_property_type_by_name(cls, property_name: str) -> Type[PropertyType]:
        """Given a property name, return the type of that property by looking it up in the _all_properties dictionary.

        :param property_name: The name of the property to get the type for
        :return: The type of the property
        """

        for property_cls in cls._all_properties:
            if property_name in cls._all_properties[property_cls]:
                return cls._all_properties[property_cls][property_name].type
        raise ValueError(f"Widget '{cls.__name__}' has no property '{property_name}'!")


    @classmethod
    def _get_property_type_from_prop_id(cls, prop_id: str) -> Type:
        """Given a property ID string, get the type of the innermost property.

        For example, given the prop_id 'y_axes[0].title_font.style', this function will return FontStyle,
        because y_axes is a list of `Axis` dataclass objects, and the title_font field is a Font dataclass,
        which has a style field that is of type FontStyle.

        :param prop_id: The property ID string to get the type for
        :return: The type of the property specified by the prop_id
        """

        names_to_types = {prop_name: prop_info.type for cls_props in cls._all_properties.values() for prop_name, prop_info in cls_props.items()}
        base_prop_name = prop_id
        if '.' in base_prop_name:
            base_prop_name = base_prop_name.split('.')[0]
        if '[' in base_prop_name:
            base_prop_name = base_prop_name.split('[')[0]

        base_prop_type = names_to_types.get(base_prop_name, None)
        if base_prop_type is None:
            raise ValueError(f"Property type for prop_id '{prop_id}' not found in all_properties dictionary!")

        base_prop_type = _normalize_property_type(base_prop_type)

        def get_nested_property_type(prop_id: str, base_type: type):
            if get_origin(base_type) is list:
                return get_nested_property_type(prop_id.split(']', 1)[1], get_args(base_type)[0])
            elif get_origin(base_type) is dict:
                return get_nested_property_type(prop_id.split('.', 1)[1], get_args(base_type)[1])
            elif is_dataclass(base_type):
                dataclass_field_name = prop_id.split('.')[1]
                if '[' in dataclass_field_name:
                    dataclass_field_name = dataclass_field_name.split('[')[0]
                dataclass_fields = base_type.fields()
                if dataclass_field_name in dataclass_fields:
                    field_type = _normalize_property_type(dataclass_fields[dataclass_field_name].type)
                    return get_nested_property_type(prop_id.split('.', 1)[1], field_type)
            else:
                return base_type

        return get_nested_property_type(prop_id, base_prop_type)


    @classmethod
    def _find_getter_by_type(cls, property_type: Type[PropertyType]) -> Callable:
        """Given a property type, find the appropriate low-level getter function for it.

        For example, if the property type is Color, this function will return the _get_color_property function,
        which knows how to parse a Color from XML.

        :param property_type: The type of the property to find a getter for
        :return: The getter function for the property type
        """
        return cls._find_getter_setter_by_type(property_type, 'get')


    @classmethod
    def _find_setter_by_type(cls, property_type: Type[PropertyType]) -> Callable:
        """Given a property type, find the appropriate low-level setter function for it.

        For example, if the property type is Color, this function will return the _set_color_property function,
        which knows how to convert a Color to XML.

        :param property_type: The type of the property to find a setter for
        :return: The setter function for the property type
        """
        return cls._find_getter_setter_by_type(property_type, 'set')


    @classmethod
    def _find_getter_setter_by_type(cls, property_type: Type[PropertyType], prefix: str) -> Callable:
        """Given a property type and whether we are looking for a getter or setter, find the appropriate low-level function for it.

        :param property_type: The type of the property to find a function for
        :param prefix: 'get' to find a getter, 'set' to find a setter
        :return: The getter or setter function for the property type
        """

        base_property_type = property_type
        if hasattr(property_type, '__origin__'):
            base_property_type = property_type.__origin__

        property_type_str = ''.join(['_' + c.lower() if c.isupper() and i != 0 else c.lower() for i, c in enumerate(base_property_type.__name__)]).lstrip('_')

        method_name = f'_{prefix}_{property_type_str}_property'
        if hasattr(cls, method_name):
            return getattr(cls, method_name)
        elif issubclass(property_type, Action):
            return getattr(cls, f'_{prefix}_action_property')
        elif property_type is RuleExpression:
            return getattr(cls, f'_{prefix}_rule_expression_property')
        elif issubclass(property_type, PhoebusElement):
            return getattr(cls, f'_{prefix}_element_property')
        elif isinstance(property_type, type) and issubclass(property_type, Enum):
            return getattr(cls, f'_{prefix}_enum_property')
        elif is_dataclass(property_type):
            return getattr(cls, f'_{prefix}_dataclass_property')
        elif property_type in (int, float, str, bool):
            return getattr(cls, f'_{prefix}_primitive_property')

        raise TypeError(f"No getter/setter function found for property type '{property_type}'!")


    @classmethod
    def _get_primitive_property(cls, element: Element, property_type: Type[Primitive]) -> Primitive:
        """Given an XML element with a primitive type (int, float, str, bool), parse the value from the element text and return it.

        :param element: The XML element to parse the property value from
        :param property_type: The primitive type to parse (int, float, str, bool)
        :return: The parsed primitive value
        """

        if element.text is None and property_type is not str:
            raise ValueError(f"XML element for primitive property '{element.tag}' has no text value!")

        if property_type is bool:
            return element.text.lower() == 'true'
        elif property_type is str and element.text is None:
            return ''
        else:
            return property_type(element.text)


    @classmethod
    def _set_primitive_property(cls, prop_name: str, value: Primitive) -> Element:
        """Given a primitive value (int, float, str, bool), create an XML element with the value as text.

        :param prop_name: The name of the property
        :param value: The primitive value to set
        :return: The XML element representing the primitive property
        """
        if isinstance(value, bool):
            return _create_element(prop_name, str(value).lower())
        return _create_element(prop_name, str(value))


    @classmethod
    def _get_path_property(cls, element: Element) -> Path:
        """Given an XML element representing a file path property, parse the value and return a Path object.

        :param element: The XML element to parse the file path from
        :return: A Path object representing the file path
        """

        return Path(cls._get_primitive_property(element, str))

    @classmethod
    def _set_path_property(cls, prop_name: str, value: Union[Path, str, None]) -> Element:
        """Given a Path, string, or None, create an XML element representing the file path property.

        :param prop_name: The name of the property
        :param value: The Path object, string, or None to set
        :return: The XML element representing the file path property
        """

        if value is None:
            return _create_element(prop_name)
        return cls._set_primitive_property(prop_name, str(value))


    @classmethod
    def _get_element_property(cls, element: Element, property_type: Type[PhoebusElement]) -> PhoebusElement:
        """Given an XML element representing a property that is itself a PhoebusElement, parse the value and return an instance of the PhoebusElement."""

        return property_type.from_element(element)


    @classmethod
    def _set_element_property(cls, prop_name: str, value: PhoebusElement) -> Element:
        """Given a PhoebusElement, create an XML element representing the property, using the XML from the PhoebusElement."""

        return value.root


    @classmethod
    def _get_enum_property(cls, element: Element, property_type: Type[Enum]) -> Enum:
        """Given an XML element representing an enum property, parse the value and return the corresponding Enum member.

        :param element: The XML element to parse the enum value from
        :param property_type: The Enum type to parse
        :return: The corresponding Enum member
        """
        if element.text is None:
            raise ValueError('Enum property element has no text value!')

        actual_value = element.text
        if issubclass(property_type, int):
            actual_value = int(actual_value)

        return property_type(actual_value)


    @classmethod
    def _set_enum_property(cls, prop_name: str, value: Enum) -> Element:
        """Given an Enum member, create an XML element with the enum value as text.

        :param prop_name: The name of the property
        :param value: The Enum member to set
        :return: The XML element representing the enum property
        """
        return _create_element(prop_name, value.value)


    @classmethod
    def _get_color_property(cls, element: Element) -> Color:
        """Given an XML element representing a color property, parse the value and return a Color object.

        :param element: The XML element to parse the color value from
        :return: The corresponding Color object
        """

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


    @classmethod
    def _set_color_property(cls, prop_name: str, value: Union[Color, Tuple[int, int, int], Tuple[int, int, int, int], str]) -> Element:
        """Given a Color object or a tuple representing RGB or RGBA values, create an XML element representing the color property.

        :param prop_name: The name of the property
        :param value: The Color object or tuple to set
        :return: The XML element representing the color property
        """

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


    @classmethod
    def _get_font_property(cls, element: Element, property_type: Type[Font] = Font) -> Font:
        """Given an XML element representing a font property, parse the inner <font> element and return a Font instance.

        Phoebus uses a nested structure: <font><font family="..." size="..." style="..." /></font>

        :param element: The outer XML element (e.g. <font>)
        :param property_type: The Font type (default: Font)
        :return: A Font instance with fields populated from the inner <font> element attributes
        """
        font_elem = element.find('font')
        if font_elem is None:
            raise ValueError('Font property element has no inner font child element!')
        return cls._get_dataclass_property(font_elem, Font)


    @classmethod
    def _set_font_property(cls, prop_name: str, value: Font) -> Element:
        """Given a Font instance, create an XML element with nested <font> structure.

        Phoebus uses: <prop_name><font family="..." size="..." style="..." /></prop_name>

        :param prop_name: The name of the property
        :param value: The Font instance to set
        :return: The XML element representing the font property
        """
        element = _create_element(prop_name)
        inner = cls._set_dataclass_property('font', value)
        element.append(inner)
        return element


    @classmethod
    def _get_dataclass_property(cls, element: Element, property_type: Type[ObservableDataclass]) -> ObservableDataclass:
        """Given an XML element representing a dataclass property, parse the value and return an instance of the dataclass.

        :param element: The XML element to parse the dataclass value from
        :param property_type: The type of the dataclass to parse
        :return: An instance of the dataclass with fields populated from the XML
        """

        field_values = {}
        for field in property_type.fields():
            field_elem = element.find(field)
            field_type = _normalize_property_type(property_type.fields()[field].type)

            if field_elem is None and field in element.attrib:
                field_values[field] = field_type(element.attrib[field])
            elif field_elem is not None and (field_elem.text is not None or field_type not in (int, float, str, bool, Path)):
                typed_getter = cls._find_getter_by_type(field_type)
                getter_args = [field_elem]
                if len(inspect.signature(typed_getter).parameters) > 1:
                    getter_args.append(field_type)
                field_values[field] = typed_getter(*getter_args)

        return property_type(**field_values)


    @classmethod
    def _set_dataclass_property(cls, prop_name: str, value: ObservableDataclass) -> Element:
        """Given an instance of a dataclass, create an XML element representing the dataclass property, with child elements or attributes for each field.

        :param prop_name: The name of the property
        :param value: The dataclass instance to set
        :return: The XML element representing the dataclass property
        """

        element = _create_element(prop_name)

        property_cls = type(value)

        for field in value.fields():
            field_value = getattr(value, field)
            field_type = _normalize_property_type(property_cls.fields()[field].type)
            valid = cls._is_set_value_valid(field_value, field_type)

            if valid:
                if field in value._attrib_fields:
                    if field_type in (int, float, str, bool):
                        element.attrib[field] = str(field_value)
                    elif isinstance(field_value, Enum):
                        element.attrib[field] = field_value.value
                    else:
                        raise TypeError('Only primitive types or enums can be set as attributes!')
                else:
                    typed_setter = cls._find_setter_by_type(field_type)
                    sub_elem = typed_setter(field, field_value)
                    element.append(sub_elem)
            else:
                raise TypeError(f"Value {field_value} is of invalid type for field '{field}' of dataclass '{property_cls.__name__}': must be of type {field_type}")
        return element


    @classmethod
    def _get_action_property(cls, element: Element) -> Action:
        """Given an XML element representing an action property, parse the value and return an instance of the appropriate Action subclass.

        :param element: The XML element to parse the action value from
        :return: An instance of the appropriate Action subclass with fields populated from the XML
        """
        action_type = ''.join([word.capitalize() for word in element.attrib.get('type', '').split('_')])
        action_cls_name = f'{action_type}Action'
        action_cls = getattr(sys.modules['phoebusgen.v4.properties.types'], action_cls_name, None)

        if action_cls is None or not issubclass(action_cls, Action):
            raise ValueError(f'Action type {action_type} is not recognized.')

        action = cls._get_dataclass_property(element, action_cls)
        if not isinstance(action, Action):
            raise ValueError(f'Failed to create action of type {action_type}.')

        return action


    @classmethod
    def _set_action_property(cls, prop_name: str, value: Action) -> Element:
        """Given an instance of an Action subclass, create an XML element representing the action property, with child elements or attributes for each field.

        :param prop_name: The name of the property (unused, actions always use 'action' as tag)
        :param value: The Action subclass instance to set
        :return: The XML element representing the action property
        """
        element = cls._set_dataclass_property('action', value)
        action_type = ''.join(['_' + c.lower() if c.isupper() and i != 0 else c.lower() for i, c in enumerate(type(value).__name__[:-6])])
        element.attrib['type'] = action_type
        return element


    @classmethod
    def _get_rule_expression_property(cls, element: Element, property_type: ValidListTypeT) -> RuleExpression:
        """Given an XML element representing a rule expression property, parse the value and return an instance of RuleExpression.

        :param element: The XML element to parse the rule expression value from
        :param property_type: The type of the property
        :return: An instance of RuleExpression with fields populated from the XML
        """

        # bool_exp attribute is required
        bool_exp = element.attrib.get('bool_exp', None)
        if bool_exp is None:
            raise ValueError("Rule expression element is missing required 'bool_exp' attribute!")

        # There are two ways to structure a RuleExpression, with value as an expression or as a literal.
        # With value_as_expression=True, the value is stored as text in an <expression> child element,
        # and the expression is evaluated at runtime to get the value, so we just return it as a string.
        expression_elem = element.find('expression')
        if expression_elem is not None:
            value_as_expression = True
            value = expression_elem.text
        else:
            value_as_expression = False
            value_get_func = cls._find_getter_by_type(property_type)
            getter_args = [element.find('value')]  # type: List[Any]
            if len(inspect.signature(value_get_func).parameters) > 1:
                getter_args.append(property_type)
            value = value_get_func(*getter_args) if element.find('value') is not None else None

        expression = RuleExpression(bool_exp=bool_exp, value=value, value_as_expression=value_as_expression)
        expression._on_change_callback = lambda new_value: cls._set_rule_expression_property(element.tag, new_value)
        return expression


    @classmethod
    def _set_rule_expression_property(cls, prop_name: str, value: RuleExpression) -> Element:
        """Given an instance of RuleExpression, create an XML element representing the rule expression property, with child elements or attributes for each field.

        :param prop_name: The name of the property
        :param value: The RuleExpression instance to set
        :return: The XML element representing the rule expression property
        """

        element = _create_element(prop_name)
        element.attrib['bool_exp'] = value.bool_exp
        if value.value_as_expression:
            expression_elem = _create_element('expression', str(value.value))
            element.append(expression_elem)
        else:
            value_set_func = cls._find_setter_by_type(type(value.value))
            value_elem = value_set_func('value', value.value)
            element.append(value_elem)

        return element


    @classmethod
    def _get_rule_property(cls, element: Element, property_type: ValidListTypeT) -> Rule:
        """Given an XML element representing a rule property, parse the value and return an instance of Rule.

        :param prop_name: The name of the property
        :param element: The XML element to parse the rule property value from
        :param property_type: The type of the property
        :return: An instance of Rule with fields populated from the XML
        """

        name = element.attrib.get('name', 'None')
        out_exp = element.attrib.get('out_exp', 'false') == 'true'
        prop_id = element.attrib.get('prop_id', None)

        expressions: ObservableList[RuleExpression] = ObservableList()
        pv_names: ObservableDict[str, bool] = ObservableDict()

        for expr_elem in element.findall('exp'):
            expressions.append(cls._get_rule_expression_property(expr_elem, property_type))
        for pv_elem in element.findall('pv_name'):
            pv_names[pv_elem.text] = pv_elem.attrib.get('trigger', 'true') == 'true'

        # Add on change callbacks to children to update the XML when they are modified.
        expressions._on_change_callback = lambda _: cls._set_rule_property(element.tag, Rule(name=name, expressions=expressions, pv_names=pv_names, out_exp=out_exp, prop_id=prop_id))
        pv_names._on_change_callback = lambda _: cls._set_rule_property(element.tag, Rule(name=name, expressions=expressions, pv_names=pv_names, out_exp=out_exp, prop_id=prop_id))

        return Rule(name=name, expressions=expressions, pv_names=pv_names, out_exp=out_exp, prop_id=prop_id)


    @classmethod
    def _set_rule_property(cls, prop_name: str, value: Rule) -> Element:
        """Given an instance of Rule, create an XML element representing the rule property, with child elements or attributes for each field.

        :param prop_name: The name of the property
        :param value: The Rule instance to set
        :return: The XML element representing the rule property
        """

        # Validate that all expressions in the rule have values of the correct type for the property
        # id of the rule. For example if the prop_id is 'y_axes[0].title_font.style',
        # then the expression values must be of type FontStyle, which is the type of the title_font.style property.
        property_type = cls._get_property_type_from_prop_id(value.prop_id)
        for exp in value.expressions:
            if exp.value_as_expression:
                continue
            if not cls._is_set_value_valid(exp.value, property_type):
                raise TypeError(f"Rule {value.name} has expression with value {exp.value} that is of invalid type for property '{value.prop_id}'. Is {type(exp.value)} must be of type {property_type}")

        # Disallow mix-and-match of value_as_expression True and False within the same rule
        if set(exp.value_as_expression for exp in value.expressions) == {False, True}:
            raise ValueError(f'All expressions in a rule must either be value_as_expression=True or value_as_expression=False. Rule {value.name} has mixed expressions.')


        element = _create_element(prop_name)
        element.attrib['name'] = value.name
        element.attrib['out_exp'] = str(value.out_exp).lower()
        element.attrib['prop_id'] = value.prop_id


        for expr in value.expressions:
            expr_elem = cls._set_rule_expression_property('exp', expr)
            element.append(expr_elem)

        for pv_name, trigger in value.pv_names.items():
            pv_elem = _create_element('pv_name', pv_name)
            pv_elem.attrib['trigger'] = str(trigger).lower()
            element.append(pv_elem)

        return element


    @classmethod
    def _get_dict_property(cls, element: Element) -> ObservableDict:
        """Given an XML element representing a dictionary property, parse the value and return an ObservableDict.

        :param element: The XML element to parse the dictionary value from
        :return: An ObservableDict with key-value pairs populated from the XML
        """

        result = ObservableDict()

        for item in element:
            result[item.tag] = item.text

        return result


    @classmethod
    def _set_dict_property(cls, tag_name: str, value: Mapping) -> Union[Element, Sequence[Element]]:
        """Given a dictionary, create an XML element representing the dictionary property, with child elements for each key-value pair.

        :param tag_name: The XML tag name to use for the dictionary property
        :param value: The dictionary to set
        :return: The XML element representing the dictionary property
        """

        dict_elem = []
        if tag_name is not None:
            dict_elem = _create_element(tag_name)
        for k, v in value.items():
            item_elem = _create_element(str(k), str(v))
            dict_elem.append(item_elem)
        return dict_elem


    @classmethod
    def _get_list_item_tag_name(cls, prop_name: str) -> str:
        """Given a list property name, return the XML tag name to use for items in the list.

        By default, this is the singular form of the property name (e.g. 'widgets' -> 'widget'), but there are some exceptions
        such as properties ending in 'axes', which use 'axis' as the item tag name.

        :param prop_name: The name of the list property
        :return: The XML tag name to use for items in the list
        """

        if prop_name.endswith('axes'):
            return prop_name.replace('axes', 'axis')
        else:
            return prop_name[:-1]


    @classmethod
    def _get_list_property(cls, prop_name: str, element: Element, property_type: Type[ValidListTypeT]) -> ObservableList[ValidListTypeT]:
        """Given an XML element representing a list property, parse the value and return an ObservableList of the appropriate type.

        :param prop_name: The name of the property
        :param element: The XML element to parse the list value from
        :param property_type: The type of the items in the list
        :return: An ObservableList with items parsed from the XML
        """

        result = ObservableList[ValidListTypeT]()
        if element is not None:
            for item_elem in element.findall(cls._get_list_item_tag_name(prop_name)):
                typed_getter = cls._find_getter_by_type(property_type)
                getter_args = [item_elem]  # type: List[Any]
                if len(inspect.signature(typed_getter).parameters) > 1:
                    if property_type is Rule:
                        rule_prop_id = item_elem.attrib.get('prop_id', None)
                        if rule_prop_id is None:
                            raise ValueError("Rule element is missing required 'prop_id' attribute!")
                        rule_prop_type = cls._get_property_type_from_prop_id(rule_prop_id)
                        getter_args.append(rule_prop_type)
                    else:
                        getter_args.append(property_type)
                result.append(typed_getter(*getter_args))
        return result


    @classmethod
    def _set_list_property(cls, prop_name: str, tag_name: str, value: Sequence[ValidListTypeT]) -> Union[Element, Sequence[Element]]:
        """Given a sequence of values, create an XML element representing the list property, with child elements for each item in the list.

        :param prop_name: The name of the property
        :param tag_name: The XML tag name to use for the list property
        :param value: The sequence of values to set
        :return: The XML element representing the list property
        """

        items = []
        for item in value:

            list_item_name = cls._get_list_item_tag_name(prop_name)
            typed_setter = cls._find_setter_by_type(type(item))
            items.append(typed_setter(list_item_name, item))

        if tag_name is not None:
            list_elem = _create_element(tag_name)
            list_elem.extend(items)
            return list_elem
        else:
            return items


    @classmethod
    def _is_set_value_valid(cls, value: PropertyType, expected_type: Type[PropertyType]) -> bool:
        """Given a value being set for a property and the expected type of that property, validate that the value is of the correct type.

        :param value: The value being set for the property
        :param expected_type: The expected type of the property
        :return: True if the value is valid for the expected type, False otherwise
        """

        def _validate_element(value: PropertyType, expected_type: Type[PropertyType]) -> bool:
            if expected_type is Color:
                return Color.is_color(value)
            elif expected_type is float:
                return isinstance(value, (float, int))
            elif expected_type is Path:
                return isinstance(value, (Path, str, type(None)))
            else:
                return isinstance(value, expected_type)

        if get_origin(expected_type) is list:
            expected_type = get_args(expected_type)[0]
            if not isinstance(value, Sequence):
                return False
            else:
                return all(_validate_element(v, expected_type) for v in value)

        if get_origin(expected_type) is dict:
            key_type, val_type = get_args(expected_type)
            if not isinstance(value, Mapping):
                return False
            else:
                return all(isinstance(k, key_type) and _validate_element(v, val_type) for k, v in value.items())

        return _validate_element(value, expected_type)
