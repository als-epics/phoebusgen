from phoebusgen.properties.behavior import HasDataWidthAndHeight
import pytest
from phoebusgen.properties import (
    HasActionsRulesAndScripts, OpenDisplayAction, HasStates, HasSymbols, OpenFileAction, ExecuteAction, CommandAction, 
OpenWebpageAction, HasToolTip, HasShowLimits, HasLevelsAndShow, HasEnabled, HasConfirmation, HasButtonMode, ButtonMode, HasBarLength, HasIncrement, HasMinMax, HasWrapWords, HasLimitsFromPV, HasEditable, HasFallbackSymbol, HasPreserveRatio, HasRunActionsOnMouseClick, HasArrayIndex, HasFallback, HasLogScale, HasSelectionValuePV, 
InterpolationType, ColorMode, ColorMap, HasInterpolation, HasColorMode, HasColorMap, HasItems, State)
from phoebusgen.utils import prettify_xml
from enum import Enum


@pytest.mark.parametrize("property_cls, property_name, value", [
    (HasToolTip, "tooltip", "This is a tooltip"),
    (HasShowLimits, "show_limits", True),
    (HasLevelsAndShow, "level_hihi", 90.0),
    (HasLevelsAndShow, "level_high", 80.0),
    (HasLevelsAndShow, "level_low", 20.0),
    (HasLevelsAndShow, "level_lolo", 10.0),
    (HasLevelsAndShow, "show_hihi", True),
    (HasLevelsAndShow, "show_high", True),
    (HasLevelsAndShow, "show_low", True),
    (HasLevelsAndShow, "show_lolo", True),
    (HasEnabled, "enabled", False),
    (HasConfirmation, "show_confirm_dialog", True),
    (HasConfirmation, "confirm_message", "Are you sure?"),
    (HasConfirmation, "password", "secret"),
    (HasButtonMode, "mode", ButtonMode.TOGGLE),
    (HasBarLength, "bar_length", 150),
    (HasIncrement, "increment", 5),
    (HasMinMax, "minimum", 0.0),
    (HasMinMax, "maximum", 100.0),
    (HasWrapWords, "wrap_words", True),
    (HasLimitsFromPV, "limits_from_pv", False),
    (HasEditable, "editable", True),
    (HasFallbackSymbol, "fallback_symbol", "N/A"),
    (HasPreserveRatio, "preserve_ratio", True),
    (HasRunActionsOnMouseClick, "run_actions_on_mouse_click", False),
    (HasArrayIndex, "array_index", 2),
    (HasFallback, "fallback_label", "No Data"),
    (HasLogScale, "log_scale", True),
    (HasSelectionValuePV, "selection_value_pv", "PV:SELECT"),
    (HasDataWidthAndHeight, "data_width", 512),
    (HasDataWidthAndHeight, "data_height", 384),
    (HasInterpolation, "interpolation", InterpolationType.AUTOMATIC),
    (HasColorMode, "color_mode", ColorMode.TYPE_MONO),
    (HasColorMap, "color_map", ColorMap.VIRIDIS),

])
def test_primitive_behavior_properties(validate_primitive_property, property_cls, property_name, value):
    validate_primitive_property(property_cls, property_name, value)

@pytest.mark.parametrize("property_cls, property_name, property_item_name", [
    (HasItems, "items", "item"),
    (HasSymbols, "symbols", "symbol"),
])
def test_string_list_properties(property_factory, property_cls, property_name, property_item_name):
    prop = property_factory(property_cls)
    assert hasattr(prop, property_name)
    assert getattr(prop, property_name) == []
    setattr(prop, property_name, ["Item1", "Item2", "Item3"])
    assert getattr(prop, property_name) == ["Item1", "Item2", "Item3"]
    del getattr(prop, property_name)[1]
    assert getattr(prop, property_name) == ["Item1", "Item3"]
    getattr(prop, property_name).append("Item4")
    assert getattr(prop, property_name) == ["Item1", "Item3", "Item4"]
    assert prop.root.find(property_name) is not None
    item_elems = prop.root.find(property_name).findall(property_item_name)
    assert len(item_elems) == 3
    assert item_elems[0].text == "Item1"
    assert item_elems[1].text == "Item3"
    assert item_elems[2].text == "Item4"


@pytest.mark.parametrize("action, expected_type, expected_field_vals", [
    (OpenDisplayAction(file="display.bob"), "open_display", {"file": "display.bob"}),
    (OpenFileAction(file="file.txt"), "open_file", {"file": "file.txt"}),
    (CommandAction(command="ls -l"), "command", {"command": "ls -l"}),
    (OpenWebpageAction(url="http://example.com"), "open_webpage", {"url": "http://example.com"}),
])
def test_actions_property(property_factory, action, expected_type, expected_field_vals):
    prop = property_factory(HasActionsRulesAndScripts)
    assert prop.actions == []
    prop.actions = [action]
    assert len(prop.actions) == 1
    actions_elem = prop.root.find("actions")
    assert actions_elem is not None
    action_elems = actions_elem.findall("action")
    assert len(action_elems) == 1
    for action_elem, expected_type, expected_fields in zip(action_elems, [expected_type], [expected_field_vals]):
        assert action_elem.attrib["type"] == expected_type
        for field_name, expected_value in expected_fields.items():
            field_elem = action_elem.find(field_name)
            assert field_elem is not None
            assert field_elem.text == expected_value

def test_can_del_action(property_factory):
    prop = property_factory(HasActionsRulesAndScripts)
    assert prop.actions == []
    prop.actions = [OpenDisplayAction(file="display.bob"), CommandAction(command="script.py")]
    print(prettify_xml(prop.root))
    assert len(prop.actions) == 2
    print(prop.actions)
    assert isinstance(prop.actions[0], OpenDisplayAction)
    del prop.actions[0]
    assert len(prop.actions) == 1
    assert isinstance(prop.actions[0], CommandAction)


def test_can_append_action(property_factory):
    prop = property_factory(HasActionsRulesAndScripts)
    prop.actions.append(OpenFileAction(file="file.txt"))
    assert len(prop.actions) == 1
    assert isinstance(prop.actions[0], OpenFileAction)
    prop.actions.append(CommandAction(command="ls -l"))
    assert len(prop.actions) == 2
    assert isinstance(prop.actions[1], CommandAction)


def test_states_property(property_factory):
    prop = property_factory(HasStates)
    assert hasattr(prop, "states")
    assert prop.states == []
    prop.states = [State(value=4, label="State1"), State(value=7, label="State2")]
    assert len(prop.states) == 2
    assert prop.states[0].value == 4
    assert prop.states[0].label == "State1"
    assert prop.states[1].value == 7
    assert prop.states[1].label == "State2"
    del prop.states[0]
    assert len(prop.states) == 1
    assert prop.states[0].value == 7
    assert prop.states[0].label == "State2"
    prop.states.append(State(value=10, label="State3"))
    assert len(prop.states) == 2
    assert prop.states[1].value == 10
    assert prop.states[1].label == "State3"
    assert prop.root.find("states") is not None
    state_elems = prop.root.find("states").findall("state")
    assert len(state_elems) == 2
    assert state_elems[0].find("value").text == "7"
    assert state_elems[0].find("label").text == "State2"
    assert state_elems[1].find("value").text == "10"
    assert state_elems[1].find("label").text == "State3"