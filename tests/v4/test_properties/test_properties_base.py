import pytest


from xml.etree.ElementTree import Element, SubElement

from phoebusgen.v4.properties.behavior import HasActionsRulesAndScripts, HasToolTip, HasTraces, HasTraces, HasXAxis, HasYAxes, HasYAxis
from phoebusgen.v4.properties.display import HasBackgroundColor, HasForegroundColor, HasShowLegend, HasShowLegend, HasShowToolbar, HasShowToolbar, HasTitle, HasTitleFont, HasVisible
from phoebusgen.v4.properties.display import HasTitleFont
from phoebusgen.v4.properties.misc import HasMarkers
from phoebusgen.v4.properties.position import HasPosition
from phoebusgen.v4.properties.property_helpers import PropertyBase, _create_element

from phoebusgen.v4.properties.widget import HasName
from phoebusgen.v4.widgets import XYPlot
from phoebusgen.v4.properties.types import Axis, ObservableDict, FileComponent, Action, ObservableList, Color, Font, Rule, RuleExpression, State, Trace, FontStyle, ArrowTypes, OpenDisplayTarget, TraceType, OpenDisplayAction
from phoebusgen.v4.utils import prettify_xml
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


@pytest.mark.parametrize('prop_type, expected_getter, expected_setter',
[
    (int, PropertyBase._get_primitive_property, PropertyBase._set_primitive_property),
    (str, PropertyBase._get_primitive_property, PropertyBase._set_primitive_property),
    (float, PropertyBase._get_primitive_property, PropertyBase._set_primitive_property),
    (bool, PropertyBase._get_primitive_property, PropertyBase._set_primitive_property),
    (ObservableDict, PropertyBase._get_dict_property, PropertyBase._set_dict_property),
    (ObservableList[int], PropertyBase._get_list_property, PropertyBase._set_list_property),
    (FileComponent, PropertyBase._get_enum_property, PropertyBase._set_enum_property),
    (Color, PropertyBase._get_color_property, PropertyBase._set_color_property),
    (Font, PropertyBase._get_dataclass_property, PropertyBase._set_dataclass_property),
    (Enum, PropertyBase._get_enum_property, PropertyBase._set_enum_property),
    (Trace, PropertyBase._get_dataclass_property, PropertyBase._set_dataclass_property),
    (Action, PropertyBase._get_action_property, PropertyBase._set_action_property),
    (RuleExpression, PropertyBase._get_rule_expression_property, PropertyBase._set_rule_expression_property),
    (Rule, PropertyBase._get_rule_property, PropertyBase._set_rule_property),
])
def test_find_getter_setter_by_type(prop_type, expected_getter, expected_setter):
    getter = PropertyBase._find_getter_by_type(prop_type)
    setter = PropertyBase._find_setter_by_type(prop_type)
    assert getter == expected_getter
    assert setter == expected_setter


@pytest.mark.parametrize('value, expected_type, expected_valid',[
    (255, int, True),
    (3.14, float, True),
    (True, bool, True),
    ('some string', str, True),
    (Color((0, 0, 0)), Color, True),
    ((255, 255, 255), Color, True),
    ('#FFAABB', Color, True),
    (Font(), Font, True),
    (ObservableDict(), ObservableDict, True),
    ({}, ObservableDict, True),
    (ObservableList[int](), ObservableList[int], True),
    ([], ObservableList[str], True),
    ([1, 'str'], ObservableList[int], False),
    (FileComponent.DIRECTORY, FileComponent, True),
    ('not-a-color', Color, False),
    (123, str, False),
    ([], ObservableDict, False),
    (['item1', 'item2', 'item3'], ObservableList[str], True),
])
def test_is_set_value_valid(value, expected_type, expected_valid):
    is_valid = PropertyBase._is_set_value_valid(value, expected_type)
    assert is_valid == expected_valid


@pytest.mark.parametrize('text, prop_type, expected_value',
[
    ('255', int, 255),
    ('3.14', float, 3.14),
    ('true', bool, True),
    ('false', bool, False),
    ('some string', str, 'some string'),
])
def test_get_primitive_property(text, prop_type, expected_value):
    elem = Element('widget')
    elem.text = text
    value = PropertyBase._get_primitive_property(elem, prop_type)
    assert value == expected_value


@pytest.mark.parametrize('value, prop_type, expected_text',
[
    (255, int, '255'),
    (3.14, float, '3.14'),
    (True, bool, 'true'),
    (False, bool, 'false'),
    ('some string', str, 'some string'),
])
def test_set_primitive_property(value, prop_type, expected_text):
    elem = PropertyBase._set_primitive_property('widget', value)
    assert elem.tag == 'widget'
    assert elem.text == expected_text
    assert PropertyBase._get_primitive_property(elem, prop_type) == value


@pytest.mark.parametrize('text, prop_type, expected_value',
[
    ('0', TraceType, TraceType.NONE),
    ('1', TraceType, TraceType.LINE),
    ('2', TraceType, TraceType.STEP),
    ('Both', ArrowTypes, ArrowTypes.BOTH),
    ('replace', OpenDisplayTarget, OpenDisplayTarget.REPLACE)
])
def test_get_enum_property(text, prop_type, expected_value):
    elem = Element('test')
    elem.text = text
    value = PropertyBase._get_enum_property(elem, prop_type)
    assert value == expected_value

@pytest.mark.parametrize('value, prop_type, expected_text',
                            [(TraceType.NONE, TraceType, '0'),
                                (TraceType.LINE, TraceType, '1'),
                                (TraceType.STEP, TraceType, '2'),
                                (ArrowTypes.BOTH, ArrowTypes, 'Both'),
                                (OpenDisplayTarget.REPLACE, OpenDisplayTarget, 'replace')
                                ])
def test_set_enum_property(value, prop_type, expected_text):
    elem = PropertyBase._set_enum_property('test', value)
    assert elem.tag == 'test'
    assert elem.text == expected_text
    assert PropertyBase._get_enum_property(elem, prop_type) == value


def test_get_color_property():
    elem = Element('top')
    color_elem = SubElement(elem, 'color')

    color_elem.attrib['red'] = '255'
    color_elem.attrib['green'] = '0'
    color_elem.attrib['blue'] = '0'
    color_elem.attrib['alpha'] = '255'
    color = PropertyBase._get_color_property(elem)
    assert color == Color((255, 0, 0, 255))


@pytest.mark.parametrize('color_input, expected_attrs, color_output',
[
    (Color((0, 255, 0, 128)), {'red': '0', 'green': '255', 'blue': '0', 'alpha': '128'}, Color((0, 255, 0, 128))),
    (Color((0, 0, 255)), {'red': '0', 'green': '0', 'blue': '255', 'alpha': '255'}, Color((0, 0, 255, 255))),
    ((255, 255, 0, 200), {'red': '255', 'green': '255', 'blue': '0', 'alpha': '200'}, Color((255, 255, 0, 200))),
    ((255, 0, 255), {'red': '255', 'green': '0', 'blue': '255', 'alpha': '255'}, Color((255, 0, 255, 255))),
    ('#123456', {'red': '18', 'green': '52', 'blue': '86', 'alpha': '255'}, Color((18, 52, 86, 255))),
])
def test_set_color_property_various_inputs(color_input, expected_attrs, color_output):
    elem = PropertyBase._set_color_property('test', color_input)
    assert elem.tag == 'test'
    color_elem = elem.find('color')
    assert color_elem is not None

    for attr, expected_value in expected_attrs.items():
        assert color_elem.attrib[attr] == expected_value
    retrieved_color = PropertyBase._get_color_property(elem)
    assert retrieved_color == color_output


@pytest.mark.parametrize('color, expected_valid',
[
    (Color((0, 0, 0)), True),
    (Color((255, 255, 255, 128)), True),
    ((0, 0, 0), True),
    ('#FFAABB', True),
    ('not-a-color', False),
])
def test_validate_color_value(color, expected_valid):
    assert Color.is_color(color) == expected_valid


def test_get_font_property():
    elem = Element('widget')
    font_elem = SubElement(elem, 'font')
    font_elem.attrib['family'] = 'Arial'
    font_elem.attrib['size'] = '12'
    font_elem.attrib['style'] = 'BOLD'

    font = PropertyBase._get_dataclass_property(font_elem, Font)
    assert isinstance(font, Font)
    assert font.family == 'Arial'
    assert font.size == 12
    assert font.style == FontStyle.BOLD


def test_set_font_property():
    font = Font(family='Times New Roman', size=16, style=FontStyle.ITALIC)
    elem = PropertyBase._set_dataclass_property('font', font)
    assert elem.tag == 'font'
    assert elem.attrib['family'] == 'Times New Roman'
    assert elem.attrib['size'] == '16'
    assert elem.attrib['style'] == 'ITALIC'
    assert font == PropertyBase._get_dataclass_property(elem, Font)


@pytest.fixture
def sample_state_element():
    elem = Element('widget')
    state_elem = SubElement(elem, 'state')
    SubElement(state_elem, 'label').text = 'Test state'
    SubElement(state_elem, 'value').text = '1'
    color = SubElement(state_elem, 'color')
    SubElement(color, 'color').attrib = {'red': '0', 'green': '0', 'blue': '255', 'alpha': '255'}
    return elem


def test_get_state_property(sample_state_element):
    state = PropertyBase._get_dataclass_property(sample_state_element.find('state'), State)
    assert isinstance(state, State)
    assert state.label == 'Test state'
    assert state.value == 1
    assert state.color == Color((0, 0, 255, 255))


def test_set_state_property():
    color = Color((255, 0, 0, 255))
    state = State(label='Active', value=1, color=color)
    elem = PropertyBase._set_dataclass_property('state', state)
    assert elem is not None
    assert elem.tag == 'state'
    _check_elem_val(elem, 'label', 'Active')
    _check_elem_val(elem, 'value', '1')
    color_elem = _get_elem(elem, 'color')
    inner_color_elem = _get_elem(color_elem, 'color')
    assert inner_color_elem.attrib['red'] == '255'
    assert inner_color_elem.attrib['green'] == '0'
    assert inner_color_elem.attrib['blue'] == '0'
    assert inner_color_elem.attrib['alpha'] == '255'
    retrieved_state = PropertyBase._get_dataclass_property(elem, State)
    assert retrieved_state == state


def test_get_action_property():
    elem = Element('action')
    elem.attrib['type'] = 'open_display'
    SubElement(elem, 'target').text = 'window'
    SubElement(elem, 'description').text = 'test'
    SubElement(elem, 'file').text = 'test.bob'
    macros_elem = SubElement(elem, 'macros')
    SubElement(macros_elem, 'test').text = 'value'

    action = PropertyBase._get_action_property(elem)
    assert isinstance(action, OpenDisplayAction)
    assert action.description == 'test'
    assert action.file == 'test.bob'
    assert action.target == OpenDisplayTarget.NEW_WINDOW
    assert action.macros['test'] == 'value'


def test_set_action_property():
    action = OpenDisplayAction('test', 'test.bob', OpenDisplayTarget.NEW_WINDOW, ObservableDict({'test': 'value'}))
    elem = PropertyBase._set_action_property('action', action)
    print(prettify_xml(elem))
    assert elem.tag == 'action'
    assert elem.attrib['type'] == 'open_display'
    _check_elem_val(elem, 'target', 'window')
    _check_elem_val(elem, 'description', 'test')
    _check_elem_val(elem, 'file', 'test.bob')
    macros_elem = elem.find('macros')
    assert macros_elem is not None
    _check_elem_val(macros_elem, 'test', 'value')


def test_get_list_property_primitive():
    elem = Element('items')
    for i in range(3):
        item_elem = SubElement(elem, 'item')
        item_elem.text = str(i + 1)
    values = PropertyBase._get_list_property(elem, int)
    assert values == [1, 2, 3]


def test_set_list_property_primitive():
    values = [1, 2, 3]
    elem = PropertyBase._set_list_property('items', values)
    assert elem.tag == 'items'
    items = elem.findall('item')
    assert len(items) == 3
    for i, item_elem in enumerate(items):
        assert item_elem.text == str(values[i])
    retrieved_values = PropertyBase._get_list_property(elem, int)
    assert retrieved_values == values


def test_get_list_property_dataclass():
    elem = Element('states')
    for i in range(2):
        state_elem = SubElement(elem, 'state')
        SubElement(state_elem, 'label').text = f"State {i+1}"
        SubElement(state_elem, 'value').text = str(i)
        color_elem = SubElement(state_elem, 'color')
        SubElement(color_elem, 'color').attrib = {'red': str(i * 100), 'green': '0', 'blue': '255', 'alpha': '255'}
    values = PropertyBase._get_list_property(elem, State)
    assert len(values) == 2
    assert values[0] == State(label='State 1', value=0, color=Color((0, 0, 255)))
    assert values[1] == State(label='State 2', value=1, color=Color((100, 0, 255)))


def test_set_list_property_dataclass():
    states = [
        State(label='State 1', value=0, color=Color((0, 0, 255))),
        State(label='State 2', value=1, color=Color((100, 0, 255)))
    ]
    elem = PropertyBase._set_list_property('states', states)
    assert elem.tag == 'states'
    state_elems = elem.findall('state')
    assert len(state_elems) == 2
    for i, state_elem in enumerate(state_elems):
        _check_elem_val(state_elem, 'label', states[i].label)
        _check_elem_val(state_elem, 'value', str(states[i].value))
        color_elem = _get_elem(state_elem, 'color')
        inner_color_elem = _get_elem(color_elem, 'color')
        expected_color = states[i].color
        assert inner_color_elem.attrib['red'] == str(expected_color[0])
        assert inner_color_elem.attrib['green'] == str(expected_color[1])
        assert inner_color_elem.attrib['blue'] == str(expected_color[2])
        assert inner_color_elem.attrib['alpha'] == '255'
    retrieved_states = PropertyBase._get_list_property(elem, State)
    assert retrieved_states == states


def test_get_dict_property():
    elem = Element('macros')
    for key, value in [('key1', 'value1'), ('key2', 'value2')]:
        item_elem = SubElement(elem, key)
        item_elem.text = value
    result = PropertyBase._get_dict_property(elem)
    assert result == {'key1': 'value1', 'key2': 'value2'}


def test_set_dict_property():
    data = {'key1': 'value1', 'key2': 'value2'}
    elem = PropertyBase._set_dict_property('macros', ObservableDict(data))
    assert elem.tag == 'macros'
    for key, value in data.items():
        item_elem = _get_elem(elem, key)
        assert item_elem.text == value
    retrieved_data = PropertyBase._get_dict_property(elem)
    assert retrieved_data == data


def test_get_rule_expression_property():
    elem = Element('exp')
    elem.attrib["bool_exp"] = 'true'
    SubElement(elem, 'expression').text = 'pvStr0'
    rule_expr = PropertyBase._get_rule_expression_property(elem, str)
    assert isinstance(rule_expr, RuleExpression)
    assert rule_expr.bool_exp == 'true'
    assert rule_expr.value_as_expression
    assert rule_expr.value == 'pvStr0'

    elem = Element('exp')
    elem.attrib['bool_exp'] = 'pv0 == 0'
    value_elem = SubElement(elem, 'value')
    SubElement(value_elem, 'color').attrib = {'red': '255', 'green': '0', 'blue': '0', 'alpha': '255'}

    rule_expr = PropertyBase._get_rule_expression_property(elem, Color)
    assert isinstance(rule_expr, RuleExpression)
    assert rule_expr.bool_exp == 'pv0 == 0'
    assert not rule_expr.value_as_expression
    assert rule_expr.value == Color((255, 0, 0, 255))


# TODO: Currently this doesn't raise an error, but it should.
# def test_get_rule_expression_incorrect_type():
#     elem = Element('exp')
#     elem.attrib['bool_exp'] = 'pv0 == 0'
#     value_elem = SubElement(elem, 'value')
#     SubElement(value_elem, 'color').attrib = {'red': '255', 'green': '0', 'blue': '0', 'alpha': '255'}
#     PropertyBase._get_rule_expression_property(elem, Font) # Should raise an error


def test_set_rule_expression_property():
    rule_expr = RuleExpression(bool_exp='pv0 == 0', value=Color((255, 0, 0, 255)), value_as_expression=False)
    elem = PropertyBase._set_rule_expression_property('exp', rule_expr)
    assert elem.tag == 'exp'
    assert elem.attrib['bool_exp'] == 'pv0 == 0'
    value_elem = _get_elem(elem, 'value')
    color_elem = _get_elem(value_elem, 'color')
    assert color_elem.attrib['red'] == '255'
    assert color_elem.attrib['green'] == '0'
    assert color_elem.attrib['blue'] == '0'
    assert color_elem.attrib['alpha'] == '255'
    retrieved_rule_expr = PropertyBase._get_rule_expression_property(elem, Color)
    assert retrieved_rule_expr == rule_expr

    rule_expr2 = RuleExpression(bool_exp='true', value='pvStr0', value_as_expression=True)
    elem2 = PropertyBase._set_rule_expression_property('exp', rule_expr2)
    assert elem2.tag == 'exp'
    assert elem2.attrib['bool_exp'] == 'true'
    expression_elem = _get_elem(elem2, 'expression')
    assert expression_elem.text == 'pvStr0'
    retrieved_rule_expr2 = PropertyBase._get_rule_expression_property(elem2, str)
    assert retrieved_rule_expr2 == rule_expr2


def test_get_rule_property():
    elem = Element('rule')
    elem.attrib['name'] = 'Test Rule'
    elem.attrib['prop_id'] = 'background_color'
    elem.attrib['out_exp'] = 'true'
    exp_elem = SubElement(elem, 'exp')
    exp_elem.attrib['bool_exp'] = 'pv0 == 0'
    value_elem = SubElement(exp_elem, 'value')
    SubElement(value_elem, 'color').attrib = {'red': '255', 'green': '0', 'blue': '0', 'alpha': '255'}
    pv_name_elem = SubElement(elem, 'pv_name')
    pv_name_elem.text = 'test_pv1'
    pv_name_elem2 = SubElement(elem, 'pv_name')
    pv_name_elem2.text = 'test_pv2'
    pv_name_elem2.attrib['trigger'] = 'false'

    rule = PropertyBase._get_rule_property(elem, Color)
    assert isinstance(rule, Rule)
    assert rule.name == 'Test Rule'
    assert len(rule.expressions) == 1
    assert type(rule.expressions[0]) == RuleExpression
    assert rule.expressions[0].bool_exp == 'pv0 == 0'
    assert rule.out_exp == True
    assert not rule.expressions[0].value_as_expression
    assert rule.expressions[0].value == Color((255, 0, 0, 255))
    assert rule.pv_names == {"test_pv1": True, "test_pv2": False}


@pytest.mark.parametrize('prop_id, expected_type', [
    ('name', str),
    ('x', int),
    ('y', int),
    ('width', int),
    ('height', int),
    ('background_color', Color),
    ('show_legend', bool),
    ('x_axis.title', str),
    ('x_axis.title_font.family', str),
    ('y_axes[0].title', str),
    ('y_axes[0].color', Color),
    ('y_axes[0].title_font.style', FontStyle),
])
def test_get_property_type_from_prop_id(prop_id, expected_type):
    xy_plot = XYPlot(name='Test Plot', x=10, y=20, width=400, height=300)
    prop_type = xy_plot._get_property_type_from_prop_id(prop_id)
    assert prop_type == expected_type


def test_set_prop_with_incorrect_type_raises_typerror():
    xy_plot = XYPlot(name='Test Plot', x=10, y=20, width=400, height=300)
    with pytest.raises(TypeError, match="invalid type for property 'x': must be of type <class 'int'>"):
        xy_plot.x = 'Hello Phoebusgen'


def test_get_property_classes():
    prop_classes = XYPlot.get_property_classes()
    assert XYPlot.get_property_classes() == [
        HasVisible,
        HasName,
        HasPosition,
        HasActionsRulesAndScripts,
        HasToolTip,
        HasForegroundColor,
        HasBackgroundColor,
        HasTitle,
        HasTitleFont,
        HasShowToolbar,
        HasShowLegend,
        HasXAxis,
        HasYAxes,
        HasTraces,
        HasMarkers
    ]

def test_get_property_names():
    xy_plot = XYPlot(name='Test Plot', x=10, y=20, width=400, height=300)
    assert xy_plot.get_property_names() == [
        'visible',
        'name',
        'x',
        'y',
        'width',
        'height',
        'actions',
        'rules',
        'scripts',
        'tooltip',
        'foreground_color',
        'background_color',
        'title',
        'title_font',
        'show_toolbar',
        'show_legend',
        'x_axis',
        'y_axes',
        'traces',
        'markers'
    ]

    assert xy_plot.get_property_names(property_cls = HasVisible) == ['visible']

    with pytest.raises(ValueError, match="Class 'str' is not a property mixin class that 'XYPlot' inherits from!"):
        xy_plot.get_property_names(property_cls=str)


def test_get_property_type_by_name():
    xy_plot = XYPlot(name='Test Plot', x=10, y=20, width=400, height=300)
    assert xy_plot.get_property_type_by_name('x') == int
    assert xy_plot.get_property_type_by_name('background_color') == Color
    assert xy_plot.get_property_type_by_name('y_axes') == ObservableList[Axis]
    assert xy_plot.get_property_type_by_name('x_axis') == Axis

    with pytest.raises(ValueError, match="Widget 'XYPlot' has no property 'nonexistent'!"):
        xy_plot.get_property_type_by_name('nonexistent')