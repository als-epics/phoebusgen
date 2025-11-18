from .properties import _StringProperty, PropertyTypeT, _GenericProperty
from typing import Union
from enum import Enum


def dynamic_property(prop_name: str, property_type: PropertyTypeT):
    def decorator(cls):

        def getter(self) -> PropertyTypeT:
            property_type_name = property_type.__name__
            if isinstance(property_type, Enum):
                property_type_name = "enum"
            typed_getter = getattr(self, f"_get_{property_type_name.lower()}_property")
            if isinstance(property_type, Enum):
                return typed_getter(prop_name, property_type)
            else:
                return typed_getter(prop_name)
        
        def setter(self, value: PropertyTypeT) -> None:
            property_type_name = property_type.__name__

            if not isinstance(value, property_type):
                raise TypeError(f"Expected value of type {property_type.__name__} for property '{prop_name}', got {type(value).__name__}")
            elif hasattr(cls, f"validate"):
                self.validate(value)
            elif isinstance(property_type, Enum):
                property_type_name = "enum"

            typed_setter = getattr(self, f"_set_{property_type_name.lower()}_property")
            typed_setter(prop_name, value)

        setattr(cls, prop_name, property(getter, setter))
        return cls
    return decorator

class PropertyBase:

    def _get_bool_property(self, prop_name: str) -> bool:
        element = self.root.find(prop_name)
        if element is not None and element.text is not None:
            return element.text.lower() == 'true'
        return False

    def _set_bool_property(self, prop_name: str, value: bool) -> None:
        self._shared.boolean_property(self.root, prop_name, str(value).lower())

    def _get_str_property(self, prop_name: str) -> str:
        element = self.root.find(prop_name)
        if element is not None and element.text is not None:
            return element.text
        return ""

    def _set_str_property(self, prop_name: str, value: str) -> None:
        self._shared.generic_property(self.root, prop_name, value)

    def _get_int_property(self, prop_name: str) -> int:
        element = self.root.find(prop_name)
        if element is not None and element.text is not None:
            try:
                return int(element.text)
            except ValueError:
                print(f'Property {prop_name} value is not an integer: {element.text}')
        return 0

    def _set_int_property(self, prop_name: str, value: int) -> None:
        self._shared.integer_property(self.root, prop_name, value)

    def _get_float_property(self, prop_name: str) -> float:
        element = self.root.find(prop_name)
        if element is not None and element.text is not None:
            try:
                return float(element.text)
            except ValueError:
                print(f'Property {prop_name} value is not a number: {element.text}')
        return 0.0
    
    def _set_float_property(self, prop_name: str, value: float) -> None:
        self._shared.number_property(self.root, prop_name, value)

    def _get_enum_property(self, prop_name: str, enum_type: PropertyEnumT) -> PropertyEnumT:
        element = self.root.find(prop_name)
        if element is not None and element.text is not None:
            actual_value = element.text
            try:
                actual_value = int(actual_value)
            except ValueError:
                pass

            try:
                return PropertyEnumT[actual_value]
            except KeyError:
                print(f'Property {prop_name} value is not a valid enum member: {element.text}')
        return list(enum_type)[0]

    def _set_enum_property(self, prop_name: str, value: Enum) -> None:
        actual_value = value.value
        if isinstance(value, int):
            self._shared.integer_property(self.root, prop_name, actual_value)
        elif isinstance(value, float):
            self._shared.number_property(self.root, prop_name, actual_value)
        else:
            self._shared.generic_property(self.root, prop_name, value.name)


@dynamic_property('text', str)
class HasText(PropertyBase):
    ...

@dynamic_property('wrap_words', bool)
class HasWrapWords(PropertyBase):
    ...

@dynamic_property('font_size', int)
class HasFontSize(PropertyBase):
    ...

@dynamic_property("auto_size", bool)
class HasAutoSize(PropertyBase):
    ...

@dynamic_property("border_width", int)
class HasBorderWidth(PropertyBase):
    ...

class HasBorder(HasBorderWidth):
    ...

@dynamic_property("point_size", int)
class HasPointSize(PropertyBase):
    ...

@dynamic_property("name", str)
class HasName(PropertyBase):
    ...

@dynamic_property("axis", int)
class HasAxis(PropertyBase):
    ...


@dynamic_property("x_pv", str)
class HasXPV(PropertyBase):
    ...

