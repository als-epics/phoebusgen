from typing import List, Tuple, Type

import pytest

from phoebusgen.v4.properties.display import HasVisible
from phoebusgen.v4.properties.position import HasPosition
from phoebusgen.v4.properties.types import (
    Axis,
    Color,
    Font,
    FontStyle,
    ObservableDict,
    ObservableList,
    PointType,
    Trace,
    TraceType,
)
from phoebusgen.v4.properties.widget import HasName
from phoebusgen.v4.widgets import Label, Rectangle, TextUpdate, Widget
from phoebusgen.v4.widgets.structure import Group
from phoebusgen.v4.widgets.widget import WidgetType, _widget_type_from_class_name

WIDGET_CLASSES = Widget.__subclasses__()


@pytest.mark.parametrize('widget_class', WIDGET_CLASSES, ids=lambda cls: cls.__name__)
def test_widget_type_from_class_name(widget_class):
    """Verify that every Widget subclass resolves to a valid WidgetType enum member."""
    wt = _widget_type_from_class_name(widget_class.__name__)
    assert isinstance(wt, WidgetType), f'{widget_class.__name__} did not resolve to a WidgetType'
    assert wt.value, f'{widget_class.__name__} resolved to an enum member with an empty value'


def _filter_widget_classes_by_property_type(property_type: type) -> List[Tuple[Type[Widget], str]]:
    """
    Helper function that generates a list of tuples of widget classes and property classes that match the given property type.

    :param property_type: Type of property to filter by
    :return: List of tuples of widget classes and matching property classes
    :rtype: List[Tuple[Type[Widget], str]]
    """

    widgets_and_matching_props = [
        (w, [p for p in w.get_property_names() if w.get_property_type_by_name(p) == property_type]) for w in WIDGET_CLASSES
    ]
    parametrized_product = [
        (widget_cls, prop)
        for widget_cls, props in widgets_and_matching_props
        for prop in props
    ]
    return parametrized_product

def test_init_widget_base_cls_raises_value_error():
    with pytest.raises(ValueError, match='Widget is an abstract base class and cannot be instantiated directly!'):
        Widget(name='BaseWidget', x_pos=0, y_pos=0, width=100, height=100)

@pytest.mark.parametrize('widget_class', WIDGET_CLASSES)
def test_base_widget_properties(widget_class, widget_factory, base_widget_prop_validator, check_xml_element):
    widget = widget_factory(widget_class)
    base_widget_prop_validator(widget)
    assert widget.x == 0
    assert widget.y == 0
    assert widget.width == 100
    assert widget.height == 100
    assert widget.visible

    check_xml_element(widget.root, 'x', '0')
    check_xml_element(widget.root, 'y', '0')
    check_xml_element(widget.root, 'width', '100')
    check_xml_element(widget.root, 'height', '100')

    widget.x = 50
    widget.y = 75
    widget.width = 200
    widget.height = 150
    widget.visible = False
    assert widget.x == 50
    assert widget.y == 75
    assert widget.width == 200
    assert widget.height == 150
    assert not widget.visible

    check_xml_element(widget.root, 'x', '50')
    check_xml_element(widget.root, 'y', '75')
    check_xml_element(widget.root, 'width', '200')
    check_xml_element(widget.root, 'height', '150')
    check_xml_element(widget.root, 'visible', 'false')

    # Visible defaults to true when no element is present,
    # so it wasn't checked above. Set it back to true and make sure the XML updates.
    widget.visible = True
    assert widget.visible
    check_xml_element(widget.root, 'visible', 'true')


@pytest.mark.parametrize('widget_class', WIDGET_CLASSES)
def test_widget_is_subclass_of_base_widget_properties(widget_class, widget_factory):
    widget = widget_factory(widget_class)
    assert isinstance(widget, Widget)
    for prop_cls in [HasName, HasPosition, HasVisible]:
        assert isinstance(widget, prop_cls)
        assert widget.has_property_class(prop_cls)


@pytest.mark.parametrize('widget_class', WIDGET_CLASSES)
def test_widget_from_element(widget_class, widget_xml_factory):
    widget_xml = widget_xml_factory(widget_class)
    widget = widget_class.from_element(widget_xml)
    assert isinstance(widget, widget_class)
    assert widget.name == widget_xml.find('name').text
    assert widget.x == int(widget_xml.find('x').text)
    assert widget.y == int(widget_xml.find('y').text)
    assert widget.width == int(widget_xml.find('width').text)
    assert widget.height == int(widget_xml.find('height').text)
    assert widget.visible


@pytest.mark.parametrize('widget_class, prop_name', _filter_widget_classes_by_property_type(Color))
def test_widget_color_properties(widget_class, widget_factory, prop_name, check_color_xml):
    widget = widget_factory(widget_class)

    # Make sure the property attr is set with correct type and default value
    assert hasattr(widget, prop_name)
    assert isinstance(getattr(widget, prop_name), Color)

    # Set color property as tuple with three elements
    setattr(widget, prop_name, (255, 128, 64))
    assert getattr(widget, prop_name) == (255, 128, 64)
    prop_elem = widget.root.find(prop_name)
    check_color_xml(prop_elem.find('color'), (255, 128, 64))

    # Set color property as tuple with four elements (including alpha)
    setattr(widget, prop_name, (0, 128, 255, 200))
    assert getattr(widget, prop_name) == (0, 128, 255, 200)
    prop_elem = widget.root.find(prop_name)
    check_color_xml(prop_elem.find('color'), (0, 128, 255, 200))

    # Set color property using Color type
    setattr(widget, prop_name, Color((100, 150, 200, 255)))
    assert getattr(widget, prop_name) == (100, 150, 200)
    prop_elem = widget.root.find(prop_name)
    check_color_xml(prop_elem.find('color'), (100, 150, 200))

    # Set color property using hex string
    setattr(widget, prop_name, '#FF00FF')
    assert getattr(widget, prop_name) == (255, 0, 255)
    prop_elem = widget.root.find(prop_name)
    check_color_xml(prop_elem.find('color'), (255, 0, 255))


@pytest.mark.parametrize('widget_class, prop_name', _filter_widget_classes_by_property_type(Font))
def test_widget_font_properties(widget_class, widget_factory, prop_name, check_font_xml):
    widget = widget_factory(widget_class)

    # Make sure the property attr is set with correct type and default value
    assert hasattr(widget, prop_name)
    assert isinstance(getattr(widget, prop_name), Font)
    assert getattr(widget, prop_name) == Font() # Default font value

    # Set font property to a new Font value
    new_font = Font(family='Times New Roman', size=16, style=FontStyle.ITALIC)
    setattr(widget, prop_name, new_font)
    assert getattr(widget, prop_name) == new_font
    prop_elem = widget.root.find(prop_name)
    check_font_xml(prop_elem, new_font)

    # Make sure setting individual font attributes updates the property and XML correctly
    font_prop = getattr(widget, prop_name)
    font_prop.size = 18
    assert getattr(widget, prop_name).size == 18
    prop_elem = widget.root.find(prop_name)
    assert prop_elem is not None and prop_elem.find('font').attrib.get('size') == '18'


@pytest.mark.parametrize('widget_class, prop_name', _filter_widget_classes_by_property_type(ObservableDict))
def test_widget_dict_properties(widget_class, widget_factory, prop_name):
    widget = widget_factory(widget_class)

    # Make sure the property attribute is set with correct type and default value
    assert hasattr(widget, prop_name)
    dict_prop = getattr(widget, prop_name)
    assert isinstance(dict_prop, ObservableDict)
    assert dict_prop == ObservableDict() # Default value is empty dict

    # Set some key-value pairs in the dict property
    dict_prop['Key1'] = 'Value1'
    dict_prop['Key2'] = 'Value2'
    assert dict_prop['Key1'] == 'Value1'
    assert dict_prop['Key2'] == 'Value2'

    # Check that the XML reflects the changes
    prop_elem = widget.root.find(prop_name)
    assert prop_elem is not None
    assert len(prop_elem) == 2
    for i in range(2):
        assert prop_elem[i].tag == f'Key{i+1}'
        assert prop_elem[i].text == f'Value{i+1}'

    # Delete a key and check updates
    del dict_prop['Key1']
    assert 'Key1' not in dict_prop
    prop_elem = widget.root.find(prop_name)
    assert len(prop_elem) == 1
    assert prop_elem.find('Key2') is not None
    assert prop_elem.find('Key1') is None


@pytest.mark.parametrize('widget_class, prop_name', _filter_widget_classes_by_property_type(Axis))
def test_widget_axis_properties(widget_class, widget_factory, prop_name, check_color_xml):
    widget = widget_factory(widget_class)

    # Make sure the property attr is set with correct type and default value
    assert hasattr(widget, prop_name)
    axis_prop = getattr(widget, prop_name)
    assert isinstance(axis_prop, Axis)
    assert axis_prop == Axis() # Default axis value

    # Set some attributes on the Axis property
    axis_prop.title = 'Test Axis'
    axis_prop.autoscale = False
    axis_prop.log_scale = True
    axis_prop.minimum = 0.0
    axis_prop.maximum = 100.0
    axis_prop.show_grid = True
    axis_prop.visible = False
    axis_prop.color = '#FF0000'

    # Check that the XML reflects the changes
    axis_elem = widget.root.find(prop_name)
    assert axis_elem is not None
    assert axis_elem.find('title').text == 'Test Axis'
    assert axis_elem.find('autoscale').text == 'false'
    assert axis_elem.find('log_scale').text == 'true'
    assert axis_elem.find('minimum').text == '0.0'
    assert axis_elem.find('maximum').text == '100.0'
    assert axis_elem.find('show_grid').text == 'true'
    assert axis_elem.find('visible').text == 'false'
    color_elem = axis_elem.find('color')
    check_color_xml(color_elem.find('color'), (255, 0, 0))

@pytest.mark.parametrize('widget_class, prop_name', _filter_widget_classes_by_property_type(ObservableList[Axis]))
def test_widget_axis_list_properties(widget_class, widget_factory, prop_name, check_color_xml):
    widget = widget_factory(widget_class)

    # Make sure the property attr is set with correct type and default value
    assert hasattr(widget, prop_name)
    axis_list_prop = getattr(widget, prop_name)
    assert isinstance(axis_list_prop, ObservableList)
    assert len(axis_list_prop) == 0  # Default value is empty list

    # Create and add Axis instances to the list
    axis1 = Axis(title='Axis 1', minimum=0.0, maximum=50.0, color='#00FF00')
    axis2 = Axis(title='Axis 2', minimum=50.0, maximum=100.0, color='#0000FF')
    axis_list_prop.append(axis1)
    axis_list_prop.append(axis2)
    assert len(axis_list_prop) == 2
    assert axis_list_prop[0] == axis1
    assert axis_list_prop[1] == axis2

    # Check that the XML reflects the changes
    prop_elem = widget.root.find(prop_name)
    assert prop_elem is not None
    assert len(prop_elem) == 2

    axis_elem1 = prop_elem[0]
    assert axis_elem1.tag.endswith('axis')
    assert axis_elem1.find('title').text == 'Axis 1'
    assert axis_elem1.find('minimum').text == '0.0'
    assert axis_elem1.find('maximum').text == '50.0'
    color_elem1 = axis_elem1.find('color')
    check_color_xml(color_elem1.find('color'), (0, 255, 0))

    axis_elem2 = prop_elem[1]
    assert axis_elem2.find('title').text == 'Axis 2'
    assert axis_elem2.find('minimum').text == '50.0'
    assert axis_elem2.find('maximum').text == '100.0'
    color_elem2 = axis_elem2.find('color')
    check_color_xml(color_elem2.find('color'), (0, 0, 255))

    del axis_list_prop[0]
    assert len(axis_list_prop) == 1
    prop_elem = widget.root.find(prop_name)
    assert len(prop_elem) == 1
    axis_elem_remaining = prop_elem[0]
    assert axis_elem_remaining.find('title').text == 'Axis 2'


@pytest.mark.parametrize('widget_class, prop_name', _filter_widget_classes_by_property_type(ObservableList[Trace]))
def test_widget_trace_list_properties(widget_class, widget_factory, prop_name, check_color_xml):
    widget = widget_factory(widget_class)

    # Make sure the property attr is set with correct type and default value
    assert hasattr(widget, prop_name)
    trace_list_prop = getattr(widget, prop_name)
    assert isinstance(trace_list_prop, ObservableList)
    assert len(trace_list_prop) == 0  # Default value is empty list

    # Create and add Trace instances to the list
    trace1 = Trace(name='Trace 1', trace_type=TraceType.STEP)
    trace2 = Trace(name='Trace 2', trace_type=TraceType.LINE, x_pv='pv1', y_pv='pv2', y_axis=0, color='#FF00FF', line_width=2, visible=False, point_size=10, point_type=PointType.TRIANGLES)
    trace_list_prop.extend([trace1, trace2])
    assert len(trace_list_prop) == 2
    assert trace_list_prop[0] == trace1
    assert trace_list_prop[1] == trace2

    del trace_list_prop[0]
    assert len(trace_list_prop) == 1
    assert trace_list_prop[0] == trace2
    prop_elem = widget.root.find(prop_name)
    assert len(prop_elem) == 1
    trace_elem_remaining = prop_elem[0]
    assert trace_elem_remaining.find('name').text == 'Trace 2'
    assert trace_elem_remaining.find('trace_type').text == '1'
    assert trace_elem_remaining.find('x_pv').text == 'pv1'
    assert trace_elem_remaining.find('y_pv').text == 'pv2'
    assert trace_elem_remaining.find('y_axis').text == '0'
    assert trace_elem_remaining.find('visible').text == 'false'
    assert trace_elem_remaining.find('line_width').text == '2'
    color_elem = trace_elem_remaining.find('color')
    check_color_xml(color_elem.find('color'), (255, 0, 255))


def test_widget_from_element_error_conditions(widget_xml_factory):
    # Create an XML element with missing 'type' attribute
    xml_element = widget_xml_factory(TextUpdate)
    xml_element.tag = 'not-a-widget'
    del xml_element.attrib['type']

    with pytest.raises(ValueError, match="Expected 'widget' element, got 'not-a-widget'"):
        TextUpdate.from_element(xml_element)

    xml_element.tag = 'widget'  # Change tag back to 'widget' but it's still missing 'type' attribute

    with pytest.raises(ValueError, match='Widget type attribute missing!'):
        TextUpdate.from_element(xml_element)

    xml_element.attrib['type'] = 'nonexistent_widget_type'

    with pytest.raises(ValueError, match="Widget type 'nonexistent_widget_type' is not a valid widget type!"):
        TextUpdate.from_element(xml_element)

    xml_element.attrib['type'] = 'label'

    with pytest.raises(ValueError, match="Expected widget type 'textupdate', got 'label'"):
        TextUpdate.from_element(xml_element)


# --- Ordering tests (bring_to_front, bring_forward, send_backward, send_to_back) ---

def test_bring_to_front():
    grp = Group(name='G', x=0, y=0, width=300, height=300)
    l1 = Label(name='L1', text='A', x=0, y=0, width=50, height=20)
    l2 = Label(name='L2', text='B', x=0, y=0, width=50, height=20)
    l3 = Label(name='L3', text='C', x=0, y=0, width=50, height=20)
    grp.add_widget([l1, l2, l3])

    # Bring L1 (index 0) to front (last position)
    grp.bring_to_front(l1)
    assert grp.widgets[0].name == 'L2'
    assert grp.widgets[1].name == 'L3'
    assert grp.widgets[2].name == 'L1'


def test_bring_to_front_already_at_front():
    grp = Group(name='G', x=0, y=0, width=300, height=300)
    l1 = Label(name='L1', text='A', x=0, y=0, width=50, height=20)
    l2 = Label(name='L2', text='B', x=0, y=0, width=50, height=20)
    grp.add_widget([l1, l2])

    grp.bring_to_front(l2)
    assert grp.widgets[0].name == 'L1'
    assert grp.widgets[1].name == 'L2'


def test_send_to_back():
    grp = Group(name='G', x=0, y=0, width=300, height=300)
    l1 = Label(name='L1', text='A', x=0, y=0, width=50, height=20)
    l2 = Label(name='L2', text='B', x=0, y=0, width=50, height=20)
    l3 = Label(name='L3', text='C', x=0, y=0, width=50, height=20)
    grp.add_widget([l1, l2, l3])

    # Send L3 (index 2) to back (first position)
    grp.send_to_back(l3)
    assert grp.widgets[0].name == 'L3'
    assert grp.widgets[1].name == 'L1'
    assert grp.widgets[2].name == 'L2'


def test_send_to_back_already_at_back():
    grp = Group(name='G', x=0, y=0, width=300, height=300)
    l1 = Label(name='L1', text='A', x=0, y=0, width=50, height=20)
    l2 = Label(name='L2', text='B', x=0, y=0, width=50, height=20)
    grp.add_widget([l1, l2])

    grp.send_to_back(l1)
    assert grp.widgets[0].name == 'L1'
    assert grp.widgets[1].name == 'L2'


def test_bring_forward():
    grp = Group(name='G', x=0, y=0, width=300, height=300)
    l1 = Label(name='L1', text='A', x=0, y=0, width=50, height=20)
    l2 = Label(name='L2', text='B', x=0, y=0, width=50, height=20)
    l3 = Label(name='L3', text='C', x=0, y=0, width=50, height=20)
    grp.add_widget([l1, l2, l3])

    # Bring L1 (index 0) forward one step -> index 1
    grp.bring_forward(l1)
    assert grp.widgets[0].name == 'L2'
    assert grp.widgets[1].name == 'L1'
    assert grp.widgets[2].name == 'L3'


def test_bring_forward_already_at_front():
    grp = Group(name='G', x=0, y=0, width=300, height=300)
    l1 = Label(name='L1', text='A', x=0, y=0, width=50, height=20)
    l2 = Label(name='L2', text='B', x=0, y=0, width=50, height=20)
    grp.add_widget([l1, l2])

    # L2 is already at the front (last index), should be no-op
    grp.bring_forward(l2)
    assert grp.widgets[0].name == 'L1'
    assert grp.widgets[1].name == 'L2'


def test_send_backward():
    grp = Group(name='G', x=0, y=0, width=300, height=300)
    l1 = Label(name='L1', text='A', x=0, y=0, width=50, height=20)
    l2 = Label(name='L2', text='B', x=0, y=0, width=50, height=20)
    l3 = Label(name='L3', text='C', x=0, y=0, width=50, height=20)
    grp.add_widget([l1, l2, l3])

    # Send L3 (index 2) backward one step -> index 1
    grp.send_backward(l3)
    assert grp.widgets[0].name == 'L1'
    assert grp.widgets[1].name == 'L3'
    assert grp.widgets[2].name == 'L2'


def test_send_backward_already_at_back():
    grp = Group(name='G', x=0, y=0, width=300, height=300)
    l1 = Label(name='L1', text='A', x=0, y=0, width=50, height=20)
    l2 = Label(name='L2', text='B', x=0, y=0, width=50, height=20)
    grp.add_widget([l1, l2])

    # L1 is already at the back (index 0), should be no-op
    grp.send_backward(l1)
    assert grp.widgets[0].name == 'L1'
    assert grp.widgets[1].name == 'L2'


# --- Duplicate name suffix tests ---

def test_add_widget_duplicate_name_gets_suffix():
    grp = Group(name='G', x=0, y=0, width=300, height=300)
    l1 = Label(name='MyLabel', text='A', x=0, y=0, width=50, height=20)
    l2 = Label(name='MyLabel', text='B', x=0, y=0, width=50, height=20)
    grp.add_widget(l1)
    grp.add_widget(l2)

    assert grp.widgets[0].name == 'MyLabel'
    assert grp.widgets[1].name == 'MyLabel_1'


def test_add_widget_three_duplicates_suffix():
    grp = Group(name='G', x=0, y=0, width=300, height=300)
    l1 = Label(name='MyLabel', text='A', x=0, y=0, width=50, height=20)
    l2 = Label(name='MyLabel', text='B', x=0, y=0, width=50, height=20)
    l3 = Label(name='MyLabel', text='C', x=0, y=0, width=50, height=20)
    grp.add_widget(l1)
    grp.add_widget(l2)
    grp.add_widget(l3)

    assert grp.widgets[0].name == 'MyLabel'
    assert grp.widgets[1].name == 'MyLabel_1'
    assert grp.widgets[2].name == 'MyLabel_2'


def test_add_widget_batch_duplicates_suffix():
    grp = Group(name='G', x=0, y=0, width=300, height=300)
    labels = [Label(name='W', text=str(i), x=0, y=0, width=50, height=20) for i in range(4)]
    grp.add_widget(labels)

    assert grp.widgets[0].name == 'W'
    assert grp.widgets[1].name == 'W_1'
    assert grp.widgets[2].name == 'W_2'
    assert grp.widgets[3].name == 'W_3'


def test_add_widget_no_rename_when_unique():
    grp = Group(name='G', x=0, y=0, width=300, height=300)
    l1 = Label(name='A', text='A', x=0, y=0, width=50, height=20)
    l2 = Label(name='B', text='B', x=0, y=0, width=50, height=20)
    l3 = Label(name='C', text='C', x=0, y=0, width=50, height=20)
    grp.add_widget([l1, l2, l3])

    assert grp.widgets[0].name == 'A'
    assert grp.widgets[1].name == 'B'
    assert grp.widgets[2].name == 'C'
