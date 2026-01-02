from phoebusgen.properties.types import Font, FontStyle, ObservableDict
from phoebusgen.utils import prettify_xml
import pytest
from phoebusgen.widgets import (
    Widget,
)
from phoebusgen.properties import (
    HasName,
    HasPosition,
    HasVisible,
    Color
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
        assert widget.has_property(prop_cls)


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