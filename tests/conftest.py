import pytest
from xml.etree.ElementTree import Element
from phoebusgen.properties.property_helpers import PropertyBase
from phoebusgen.properties.types import Color
from typing import Callable
from enum import Enum
from phoebusgen.utils import prettify_xml

@pytest.fixture
def property_factory() -> Callable[[type[PropertyBase]], PropertyBase]:
    def _factory(property_type: type[PropertyBase]) -> PropertyBase:
        prop = property_type()
        prop.root = Element('widget')
        return prop
    return _factory


@pytest.fixture
def validate_primitive_property(property_factory) -> Callable[[PropertyBase, str, str], None]:
    def _validator(property_cls: type[PropertyBase], property_name: str, value) -> None:
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
def check_xml_element() -> Callable[[Element, str, str], None]:
    def _checker(root: Element, property_name: str, expected_text: str) -> None:
        elem = root.find(property_name)
        assert elem is not None
        assert elem.text == expected_text
    return _checker

@pytest.fixture
def check_color_xml() -> Callable[[Element, str, Color], None]:
    def _checker(color_elem: Element, expected_color: Color) -> None:
        assert color_elem is not None
        assert int(color_elem.attrib.get("red", -1)) == expected_color[0]
        assert int(color_elem.attrib.get("green", -1)) == expected_color[1]
        assert int(color_elem.attrib.get("blue", -1)) == expected_color[2]
        if len(expected_color) == 4:
            assert int(color_elem.attrib.get("alpha", -1)) == expected_color[3]
    return _checker

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