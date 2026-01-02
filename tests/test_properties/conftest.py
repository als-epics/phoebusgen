import pytest
from xml.etree.ElementTree import Element
from phoebusgen.properties.property_helpers import PropertyBase
from phoebusgen.properties.types import Color
from typing import Any, Callable
from enum import Enum

@pytest.fixture
def property_factory() -> Callable[[type[PropertyBase]], PropertyBase]:
    def _factory(property_type: type[PropertyBase]) -> PropertyBase:
        prop = property_type()
        prop.root = Element('widget')
        return prop
    return _factory


@pytest.fixture
def validate_primitive_property(property_factory) -> Callable[[type[PropertyBase], str, Any], None]:
    def _validator(property_cls: type[PropertyBase], property_name: str, value: Any) -> None:
        prop = property_factory(property_cls)
        assert hasattr(prop, property_name)
        setattr(prop, property_name, value)
        assert getattr(prop, property_name) == value

        assert prop.root.find(property_name) is not None
        expected_text = str(value)
        if isinstance(value, Enum):
            expected_text = str(value.value)
        elif isinstance(value, bool):
            expected_text = str(value).lower()

        assert prop.root.find(property_name).text == expected_text
    return _validator


@pytest.fixture
def validate_color_property(property_factory, check_color_xml) -> Callable[[type[PropertyBase], str, Color], None]:
    def _validator(property_cls: type[PropertyBase], property_name: str, value: Color) -> None:
        prop = property_factory(property_cls)
        assert hasattr(prop, property_name)
        setattr(prop, property_name, value)
        assert getattr(prop, property_name) == value

        elem = prop.root.find(property_name)
        assert elem is not None
        color_elem = elem.find("color")
        check_color_xml(color_elem, value)
    return _validator