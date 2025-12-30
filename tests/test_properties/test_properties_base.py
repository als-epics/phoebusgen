import pytest


from xml.etree.ElementTree import Element, SubElement

from phoebusgen.properties.property_helpers import dynamic_property, _create_element, _find_getter_setter_by_type, _get_color_property, _get_dataclass_property, _get_enum_property, _get_list_property, _get_primitive_property, _get_dict_property, _set_action_property, _set_color_property, _set_dataclass_property, _set_enum_property, _set_list_property, _set_primitive_property, _set_dict_property, _validate_color_value, _get_action_property
from phoebusgen.properties.types import ObservableDataclass, ObservableDict, FileComponent, Action, ObservableList, Color, Font, State, Trace, FontStyle, HorizontalAlignment, VerticalAlignment, RotationStep, InterpolationType, ButtonMode, ColorMode, GroupStyle, ResizeSetting, LineStyle, PointType, ColorMap, ArrowTypes, TabDirection, OpenDisplayTarget, TraceType, OpenDisplayAction
from phoebusgen.utils import prettify_xml
from enum import Enum

def _get_elem(root_elem: Element, tag_name: str) -> Element:
    elem = root_elem.find(tag_name)
    assert elem is not None
    return elem

def _check_elem_val(root_elem: Element, tag_name: str, value: str) -> None:
    elem = _get_elem(root_elem, tag_name)
    assert elem.text == value


def test_create_element():
    elem = _create_element('testProp', 'testValue')
    assert elem.tag == 'testProp'
    assert elem.text == 'testValue'
    assert prettify_xml(elem) == """<?xml version="1.0" ?>
<testProp>testValue</testProp>
"""


@pytest.mark.parametrize("prop_type, expected_getter, expected_setter", 
                         [
                                (int, "primitive", "primitive"),
                                (str, "primitive", "primitive"),
                                (float, "primitive", "primitive"),
                                (bool, "primitive", "primitive"),
                                (ObservableDict, "dict", "dict"),
                                (ObservableList[int], "list", "list"),
                                (FileComponent, "enum", "enum"),
                                (Color, "color", "color"),
                                (Font, "dataclass", "dataclass"),
                                (Enum, "enum", "enum"),
                                (Trace, "dataclass", "dataclass"),
                                (Action, "action", "action"),
                         ])
def test_find_getter_setter_by_type(prop_type, expected_getter, expected_setter):
    getter = _find_getter_setter_by_type(prop_type, func = "getter")
    setter = _find_getter_setter_by_type(prop_type, func = "setter")
    assert getter == expected_getter
    assert setter == expected_setter


@pytest.mark.parametrize("text, prop_type, expected_value",
                         [
                             ("255", int, 255),
                             ("3.14", float, 3.14),
                             ("true", bool, True),
                             ("false", bool, False),
                             ("some string", str, "some string"),
                         ])
def test_get_primitive_property(text, prop_type, expected_value):
    elem = Element('widget')
    elem.text = text
    value = _get_primitive_property(elem, prop_type)
    assert value == expected_value


@pytest.mark.parametrize("value, prop_type, expected_text",
                            [
                                (255, int, "255"),
                                (3.14, float, "3.14"),
                                (True, bool, "true"),
                                (False, bool, "false"),
                                ("some string", str, "some string"),
                            ])
def test_set_primitive_property(value, prop_type, expected_text):
    elem = _set_primitive_property("widget", value)
    assert elem.tag == 'widget'
    assert elem.text == expected_text
    assert _get_primitive_property(elem, prop_type) == value


@pytest.mark.parametrize("text, prop_type, expected_value",
                         [("0", TraceType, TraceType.NONE),
                          ("1", TraceType, TraceType.LINE),
                          ("2", TraceType, TraceType.STEP),
                          ("Both", ArrowTypes, ArrowTypes.BOTH),
                          ("replace", OpenDisplayTarget, OpenDisplayTarget.REPLACE)
                         ])
def test_get_enum_property(text, prop_type, expected_value):
    elem = Element("test")
    elem.text = text
    value = _get_enum_property(elem, prop_type)
    assert value == expected_value

@pytest.mark.parametrize("value, prop_type, expected_text",
                            [(TraceType.NONE, TraceType, "0"),
                                (TraceType.LINE, TraceType, "1"),
                                (TraceType.STEP, TraceType, "2"),
                                (ArrowTypes.BOTH, ArrowTypes, "Both"),
                                (OpenDisplayTarget.REPLACE, OpenDisplayTarget, "replace")
                                ]) 
def test_set_enum_property(value, prop_type, expected_text):
    elem = _set_enum_property("test", value)
    assert elem.tag == "test"
    assert elem.text == expected_text
    assert _get_enum_property(elem, prop_type) == value


def test_get_color_property():
    elem = Element("top")
    color_elem = SubElement(elem, "color")
    
    color_elem.attrib["red"] = "255"
    color_elem.attrib["green"] = "0"
    color_elem.attrib["blue"] = "0"
    color_elem.attrib["alpha"] = "255"
    color = _get_color_property(elem)
    assert color == Color((255, 0, 0, 255))


@pytest.mark.parametrize("color_input, expected_attrs, color_output",
                         [
                             (Color((0, 255, 0, 128)), {"red": "0", "green": "255", "blue": "0", "alpha": "128"}, Color((0, 255, 0, 128))),
                                (Color((0, 0, 255)), {"red": "0", "green": "0", "blue": "255", "alpha": "255"}, Color((0, 0, 255, 255))),
                                ((255, 255, 0, 200), {"red": "255", "green": "255", "blue": "0", "alpha": "200"}, Color((255, 255, 0, 200))),
                                ((255, 0, 255), {"red": "255", "green": "0", "blue": "255", "alpha": "255"}, Color((255, 0, 255, 255))),
                                ("#123456", {"red": "18", "green": "52", "blue": "86", "alpha": "255"}, Color((18, 52, 86, 255))),
                         ])
def test_set_color_property_various_inputs(color_input, expected_attrs, color_output):
    elem = _set_color_property("test", color_input)
    assert elem.tag == "test"
    color_elem = elem.find("color")
    assert color_elem is not None

    for attr, expected_value in expected_attrs.items():
        assert color_elem.attrib[attr] == expected_value
    retrieved_color = _get_color_property(elem)
    assert retrieved_color == color_output


@pytest.mark.parametrize("color, expected_valid",
                            [
                                (Color((0, 0, 0)), True),
                                (Color((255, 255, 255, 128)), True),
                                ((0, 0, 0), True),
                                ("#FFAABB", True),
                                ("not-a-color", False),
                            ])
def test_validate_color_value(color, expected_valid):
    assert _validate_color_value(color) == expected_valid


def test_get_font_property():
    elem = Element("widget")
    font_elem = SubElement(elem, "font")
    font_elem.attrib["family"] = "Arial"
    font_elem.attrib["size"] = "12"
    font_elem.attrib["style"] = "BOLD"

    font = _get_dataclass_property(font_elem, Font)
    assert isinstance(font, Font)
    assert font.family == "Arial"
    assert font.size == 12
    assert font.style == FontStyle.BOLD


def test_set_font_property():
    font = Font(family="Times New Roman", size=16, style=FontStyle.ITALIC)
    elem = _set_dataclass_property("font", font)
    assert elem.tag == "font"
    assert elem.attrib["family"] == "Times New Roman"
    assert elem.attrib["size"] == "16"
    assert elem.attrib["style"] == "ITALIC"
    assert font == _get_dataclass_property(elem, Font)


@pytest.fixture
def sample_state_element():
    elem = Element("widget")
    state_elem = SubElement(elem, "state")
    SubElement(state_elem, "label").text = "Test state"
    SubElement(state_elem, "value").text = "1"
    color = SubElement(state_elem, "color")
    SubElement(color, "color").attrib = {"red": "0", "green": "0", "blue": "255", "alpha": "255"}
    return elem


def test_get_state_property(sample_state_element):
    state = _get_dataclass_property(sample_state_element.find("state"), State)
    assert isinstance(state, State)
    assert state.label == "Test state"
    assert state.value == 1
    assert state.color == Color((0, 0, 255, 255))


def test_set_state_property():
    color = Color((255, 0, 0, 255))
    state = State(label="Active", value=1, color=color)
    elem = _set_dataclass_property("state", state)
    assert elem is not None
    assert elem.tag == "state"
    _check_elem_val(elem, "label", "Active")
    _check_elem_val(elem, "value", "1")
    color_elem = _get_elem(elem, "color")
    inner_color_elem = _get_elem(color_elem, "color")
    assert inner_color_elem.attrib["red"] == "255"
    assert inner_color_elem.attrib["green"] == "0"
    assert inner_color_elem.attrib["blue"] == "0"
    assert inner_color_elem.attrib["alpha"] == "255"
    retrieved_state = _get_dataclass_property(elem, State)
    assert retrieved_state == state

def test_get_action_property():
    elem = Element("action")
    elem.attrib["type"] = "open_display"
    SubElement(elem, "target").text = "window"
    SubElement(elem, "description").text = "test"
    SubElement(elem, "file").text = "test.bob"
    macros_elem = SubElement(elem, "macros")
    SubElement(macros_elem, "test").text = "value"

    action = _get_action_property(elem)
    assert isinstance(action, OpenDisplayAction)
    assert action.description == "test"
    assert action.file == "test.bob"
    assert action.target == OpenDisplayTarget.NEW_WINDOW
    assert action.macros["test"] == "value"


def test_set_action_property():
    action = OpenDisplayAction("test", "test.bob", OpenDisplayTarget.NEW_WINDOW, ObservableDict({"test": "value"}))
    elem = _set_action_property("action", action)
    print(prettify_xml(elem))
    assert elem.tag == "action"
    assert elem.attrib["type"] == "open_display"
    _check_elem_val(elem, "target", "window")
    _check_elem_val(elem, "description", "test")
    _check_elem_val(elem, "file", "test.bob")
    macros_elem = elem.find("macros")
    assert macros_elem is not None
    _check_elem_val(macros_elem, "test", "value")


def test_get_list_property_primitive():
    elem = Element("numbers")
    for i in range(3):
        item_elem = SubElement(elem, "item")
        item_elem.text = str(i + 1)
    values = _get_list_property(elem, int, list_item_name="item")
    assert values == [1, 2, 3]

def test_set_list_property_primitive():
    values = [1, 2, 3]
    elem = _set_list_property("numbers", values, list_item_name="item")
    assert elem.tag == "numbers"
    items = elem.findall("item")
    assert len(items) == 3
    for i, item_elem in enumerate(items):
        assert item_elem.text == str(values[i])
    retrieved_values = _get_list_property(elem, int, list_item_name="item")
    assert retrieved_values == values

def test_get_list_property_dataclass():
    elem = Element("states")
    for i in range(2):
        state_elem = SubElement(elem, "state")
        SubElement(state_elem, "label").text = f"State {i+1}"
        SubElement(state_elem, "value").text = str(i)
        color_elem = SubElement(state_elem, "color")
        SubElement(color_elem, "color").attrib = {"red": str(i * 100), "green": "0", "blue": "255", "alpha": "255"}
    values = _get_list_property(elem, State)
    assert len(values) == 2
    assert values[0] == State(label="State 1", value=0, color=Color((0, 0, 255)))
    assert values[1] == State(label="State 2", value=1, color=Color((100, 0, 255)))

def test_set_list_property_dataclass():
    states = [
        State(label="State 1", value=0, color=Color((0, 0, 255))),
        State(label="State 2", value=1, color=Color((100, 0, 255)))
    ]
    elem = _set_list_property("states", states)
    assert elem.tag == "states"
    state_elems = elem.findall("state")
    assert len(state_elems) == 2
    for i, state_elem in enumerate(state_elems):
        _check_elem_val(state_elem, "label", states[i].label)
        _check_elem_val(state_elem, "value", str(states[i].value))
        color_elem = _get_elem(state_elem, "color")
        inner_color_elem = _get_elem(color_elem, "color")
        expected_color = states[i].color
        assert inner_color_elem.attrib["red"] == str(expected_color[0])
        assert inner_color_elem.attrib["green"] == str(expected_color[1])
        assert inner_color_elem.attrib["blue"] == str(expected_color[2])
        assert inner_color_elem.attrib["alpha"] == "255"
    retrieved_states = _get_list_property(elem, State)
    assert retrieved_states == states

def test_get_dict_property():
    elem = Element("macros")
    for key, value in [("key1", "value1"), ("key2", "value2")]:
        item_elem = SubElement(elem, key)
        item_elem.text = value
    result = _get_dict_property(elem)
    assert result == {"key1": "value1", "key2": "value2"}

def test_set_dict_property():
    data = {"key1": "value1", "key2": "value2"}
    elem = _set_dict_property("macros", ObservableDict(data))
    assert elem.tag == "macros"
    for key, value in data.items():
        item_elem = _get_elem(elem, key)
        assert item_elem.text == value
    retrieved_data = _get_dict_property(elem)
    assert retrieved_data == data
