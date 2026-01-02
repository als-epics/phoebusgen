from xml.etree.ElementTree import Element
import pytest
from typing import Any, Callable
from phoebusgen.utils import prettify_xml
from phoebusgen.properties import Color




@pytest.fixture
def check_xml_element() -> Callable[[Element, str, str], None]:
    def _checker(root: Element, property_name: str, expected_text: str) -> None:
        print(f"Checking XML Element: {property_name} expecting text: {expected_text}")
        print(prettify_xml(root))
        elem = root.find(property_name)
        print(elem)
        print("--------------")
        assert elem is not None
        assert elem.text == expected_text
    return _checker

@pytest.fixture
def check_color_xml() -> Callable[[Element, Color], None]:
    def _checker(color_elem: Element, expected_color: Color) -> None:
        assert color_elem is not None
        assert int(color_elem.attrib.get("red", -1)) == expected_color[0]
        assert int(color_elem.attrib.get("green", -1)) == expected_color[1]
        assert int(color_elem.attrib.get("blue", -1)) == expected_color[2]
        if len(expected_color) == 4:
            assert int(color_elem.attrib.get("alpha", -1)) == expected_color[3]
    return _checker

@pytest.fixture
def check_font_xml() -> Callable[[Element, Any], None]:
    def _checker(font_elem: Element, expected_font: Any) -> None:
        assert font_elem is not None
        assert font_elem.attrib.get("family", "") == expected_font.family
        assert int(font_elem.attrib.get("size", -1)) == expected_font.size
        assert font_elem.attrib.get("style", "") == expected_font.style.value
    return _checker
