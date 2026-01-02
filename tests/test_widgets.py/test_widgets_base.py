import pytest
from phoebusgen.widgets import (
    Widget,
)
from phoebusgen.properties import (
    Font,
    FontStyle,
    ObservableDict,
    ObservableList,
    Trace,
    TraceType,
    PointType,
    HasName,
    HasPosition,
    HasVisible,
    Color,
    Axis
)

WIDGET_CLASSES = Widget.__subclasses__()


def _filter_widget_classes_by_property_type(property_type: type) -> list[tuple[type[Widget], str]]:
    """
    Helper function that generates a list of tuples of widget classes and property classes that match the given property type.
    
    :param property_type: Type of property to filter by
    :return: List of tuples of widget classes and matching property classes
    :rtype: list[tuple[type[Widget], str]]
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

@pytest.mark.parametrize("widget_class", WIDGET_CLASSES)
def test_base_widget_properties(widget_class, widget_factory, base_widget_prop_validator, check_xml_element):
    widget = widget_factory(widget_class)
    base_widget_prop_validator(widget)
    assert widget.x == 0
    assert widget.y == 0
    assert widget.width == 100
    assert widget.height == 100
    assert widget.visible

    check_xml_element(widget.root, "x", "0")
    check_xml_element(widget.root, "y", "0")
    check_xml_element(widget.root, "width", "100")
    check_xml_element(widget.root, "height", "100")

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

    check_xml_element(widget.root, "x", "50")
    check_xml_element(widget.root, "y", "75")
    check_xml_element(widget.root, "width", "200")
    check_xml_element(widget.root, "height", "150")
    check_xml_element(widget.root, "visible", "false")

    # Visible defaults to true when no element is present,
    # so it wasn't checked above. Set it back to true and make sure the XML updates.
    widget.visible = True
    assert widget.visible
    check_xml_element(widget.root, "visible", "true")


@pytest.mark.parametrize("widget_class", WIDGET_CLASSES)
def test_widget_is_subclass_of_base_widget_properties(widget_class, widget_factory):
    widget = widget_factory(widget_class)
    assert isinstance(widget, Widget)
    for prop_cls in [HasName, HasPosition, HasVisible]:
        assert isinstance(widget, prop_cls)
        assert widget.has_property_class(prop_cls)


@pytest.mark.parametrize("widget_class", WIDGET_CLASSES)
def test_widget_from_element(widget_class, widget_xml_factory):
    widget_xml = widget_xml_factory(widget_class)
    widget = widget_class.from_element(widget_xml)
    assert isinstance(widget, widget_class)
    assert widget.name == widget_xml.find("name").text
    assert widget.x == int(widget_xml.find("x").text)
    assert widget.y == int(widget_xml.find("y").text)
    assert widget.width == int(widget_xml.find("width").text)
    assert widget.height == int(widget_xml.find("height").text)
    assert widget.visible


@pytest.mark.parametrize("widget_class, prop_name", _filter_widget_classes_by_property_type(Color))
def test_widget_color_properties(widget_class, widget_factory, prop_name, check_color_xml):
    widget = widget_factory(widget_class)

    # Make sure the property attr is set with correct type and default value
    assert hasattr(widget, prop_name)
    assert isinstance(getattr(widget, prop_name), Color)
    assert getattr(widget, prop_name) == (0, 0, 0) # Default color value is 0,0,0 (black)

    # Set color property as tuple with three elements
    setattr(widget, prop_name, (255, 128, 64))
    assert getattr(widget, prop_name) == (255, 128, 64)
    prop_elem = widget.root.find(prop_name)
    check_color_xml(prop_elem.find("color"), (255, 128, 64))

    # Set color property as tuple with four elements (including alpha)
    setattr(widget, prop_name, (0, 128, 255, 200))
    assert getattr(widget, prop_name) == (0, 128, 255, 200)
    prop_elem = widget.root.find(prop_name)
    check_color_xml(prop_elem.find("color"), (0, 128, 255, 200))

    # Set color property using Color type
    setattr(widget, prop_name, Color((100, 150, 200, 255)))
    assert getattr(widget, prop_name) == (100, 150, 200)
    prop_elem = widget.root.find(prop_name)
    check_color_xml(prop_elem.find("color"), (100, 150, 200))

    # Set color property using hex string
    setattr(widget, prop_name, "#FF00FF")
    assert getattr(widget, prop_name) == (255, 0, 255)
    prop_elem = widget.root.find(prop_name)
    check_color_xml(prop_elem.find("color"), (255, 0, 255))


@pytest.mark.parametrize("widget_class, prop_name", _filter_widget_classes_by_property_type(Font))
def test_widget_font_properties(widget_class, widget_factory, prop_name, check_font_xml):
    widget = widget_factory(widget_class)

    # Make sure the property attr is set with correct type and default value
    assert hasattr(widget, prop_name)
    assert isinstance(getattr(widget, prop_name), Font)
    assert getattr(widget, prop_name) == Font() # Default font value

    # Set font property to a new Font value
    new_font = Font(family="Times New Roman", size=16, style=FontStyle.ITALIC)
    setattr(widget, prop_name, new_font)
    assert getattr(widget, prop_name) == new_font
    prop_elem = widget.root.find(prop_name)
    check_font_xml(prop_elem, new_font)

    # Make sure setting individual font attributes updates the property and XML correctly
    font_prop = getattr(widget, prop_name)
    font_prop.size = 18
    assert getattr(widget, prop_name).size == 18
    prop_elem = widget.root.find(prop_name)
    assert prop_elem is not None and prop_elem.attrib.get("size") == "18"


@pytest.mark.parametrize("widget_class, prop_name", _filter_widget_classes_by_property_type(ObservableDict))
def test_widget_dict_properties(widget_class, widget_factory, prop_name):
    widget = widget_factory(widget_class)

    print(widget)

    # Make sure the property attribute is set with correct type and default value
    assert hasattr(widget, prop_name)
    dict_prop = getattr(widget, prop_name)
    assert isinstance(dict_prop, ObservableDict)
    assert dict_prop == ObservableDict() # Default value is empty dict

    # Set some key-value pairs in the dict property
    dict_prop["Key1"] = "Value1"
    dict_prop["Key2"] = "Value2"
    assert dict_prop["Key1"] == "Value1"
    assert dict_prop["Key2"] == "Value2"

    # Check that the XML reflects the changes
    prop_elem = widget.root.find(prop_name)
    assert prop_elem is not None
    assert len(prop_elem) == 2
    for i in range(2):
        assert prop_elem[i].tag == f"Key{i+1}"
        assert prop_elem[i].text == f"Value{i+1}"

    # Delete a key and check updates
    del dict_prop["Key1"]
    assert "Key1" not in dict_prop
    prop_elem = widget.root.find(prop_name)
    assert len(prop_elem) == 1
    assert prop_elem.find("Key2") is not None
    assert prop_elem.find("Key1") is None


@pytest.mark.parametrize("widget_class, prop_name", _filter_widget_classes_by_property_type(Axis))
def test_widget_axis_properties(widget_class, widget_factory, prop_name, check_color_xml):
    widget = widget_factory(widget_class)

    # Make sure the property attr is set with correct type and default value
    assert hasattr(widget, prop_name)
    axis_prop = getattr(widget, prop_name)
    assert isinstance(axis_prop, Axis)
    assert axis_prop == Axis() # Default axis value

    # Set some attributes on the Axis property
    axis_prop.title = "Test Axis"
    axis_prop.autoscale = False
    axis_prop.log_scale = True
    axis_prop.minimum = 0.0
    axis_prop.maximum = 100.0
    axis_prop.show_grid = True
    axis_prop.visible = False
    axis_prop.color = "#FF0000"

    # Check that the XML reflects the changes
    axis_elem = widget.root.find(prop_name)
    assert axis_elem is not None
    assert axis_elem.find("title").text == "Test Axis"
    assert axis_elem.find("autoscale").text == "false"
    assert axis_elem.find("log_scale").text == "true"
    assert axis_elem.find("minimum").text == "0.0"
    assert axis_elem.find("maximum").text == "100.0"
    assert axis_elem.find("show_grid").text == "true"
    assert axis_elem.find("visible").text == "false"
    color_elem = axis_elem.find("color")
    check_color_xml(color_elem.find("color"), (255, 0, 0))

@pytest.mark.parametrize("widget_class, prop_name", _filter_widget_classes_by_property_type(ObservableList[Axis]))
def test_widget_axis_list_properties(widget_class, widget_factory, prop_name, check_color_xml):
    widget = widget_factory(widget_class)

    # Make sure the property attr is set with correct type and default value
    assert hasattr(widget, prop_name)
    axis_list_prop = getattr(widget, prop_name)
    assert isinstance(axis_list_prop, ObservableList)
    assert len(axis_list_prop) == 0  # Default value is empty list

    # Create and add Axis instances to the list
    axis1 = Axis(title="Axis 1", minimum=0.0, maximum=50.0, color="#00FF00")
    axis2 = Axis(title="Axis 2", minimum=50.0, maximum=100.0, color="#0000FF")
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
    assert axis_elem1.tag.endswith("axis")
    assert axis_elem1.find("title").text == "Axis 1"
    assert axis_elem1.find("minimum").text == "0.0"
    assert axis_elem1.find("maximum").text == "50.0"
    color_elem1 = axis_elem1.find("color")
    check_color_xml(color_elem1.find("color"), (0, 255, 0))

    axis_elem2 = prop_elem[1]
    assert axis_elem2.find("title").text == "Axis 2"
    assert axis_elem2.find("minimum").text == "50.0"
    assert axis_elem2.find("maximum").text == "100.0"
    color_elem2 = axis_elem2.find("color")
    check_color_xml(color_elem2.find("color"), (0, 0, 255))

    del axis_list_prop[0]
    assert len(axis_list_prop) == 1
    prop_elem = widget.root.find(prop_name)
    assert len(prop_elem) == 1
    axis_elem_remaining = prop_elem[0]
    assert axis_elem_remaining.find("title").text == "Axis 2"


@pytest.mark.parametrize("widget_class, prop_name", _filter_widget_classes_by_property_type(ObservableList[Trace]))
def test_widget_trace_list_properties(widget_class, widget_factory, prop_name, check_color_xml):
    widget = widget_factory(widget_class)

    # Make sure the property attr is set with correct type and default value
    assert hasattr(widget, prop_name)
    trace_list_prop = getattr(widget, prop_name)
    assert isinstance(trace_list_prop, ObservableList)
    assert len(trace_list_prop) == 0  # Default value is empty list

    # Create and add Trace instances to the list
    trace1 = Trace(name="Trace 1", trace_type=TraceType.STEP)
    trace2 = Trace(name="Trace 2", trace_type=TraceType.LINE, x_pv="pv1", y_pv="pv2", y_axis=0, color="#FF00FF", line_width=2, visible=False, point_size=10, point_type=PointType.TRIANGLES)
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
    assert trace_elem_remaining.find("name").text == "Trace 2"
    assert trace_elem_remaining.find("trace_type").text == "1"
    assert trace_elem_remaining.find("x_pv").text == "pv1"
    assert trace_elem_remaining.find("y_pv").text == "pv2"
    assert trace_elem_remaining.find("y_axis").text == "0"
    assert trace_elem_remaining.find("visible").text == "false"
    assert trace_elem_remaining.find("line_width").text == "2"
    color_elem = trace_elem_remaining.find("color")
    check_color_xml(color_elem.find("color"), (255, 0, 255))