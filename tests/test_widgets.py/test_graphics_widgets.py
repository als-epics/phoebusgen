import pytest
from phoebusgen.widgets import Label

def test_label_widget_properties(widget_factory, check_xml_element):
    widget = widget_factory(Label)
    assert hasattr(widget, "text")
    assert widget.text == ""
    widget.text = "Hello, World!"
    assert widget.text == "Hello, World!"
    check_xml_element(widget.root, "text", "Hello, World!")