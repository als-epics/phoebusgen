import pytest
from phoebusgen.widgets import Widget
from typing import Callable
import inspect
from xml.etree.ElementTree import Element, SubElement


@pytest.fixture
def widget_factory() -> Callable[..., Widget]:
    def _factory(widget_cls: type[Widget], num = 1, **kwargs) -> Widget:
        
        base_params = {
            "name": f"{widget_cls.__name__}_{num}",
            "x": 0,
            "y": 0,
            "width": 100,
            "height": 100,
        }

        params = []
        for param_name in inspect.signature(widget_cls.__init__).parameters:
            if param_name != "self":
                if param_name in base_params:
                    params.append(base_params[param_name])
                elif param_name in kwargs:
                    params.append(kwargs[param_name])
                else:
                    params.append("")
        return widget_cls(*params)
    return _factory

@pytest.fixture
def widget_xml_factory():
    def _factory(widget_cls: type[Widget], num = 1, **kwargs) -> Element:
        root = Element('widget')
        root.attrib['type'] = widget_cls._widget_type.value
        root.attrib['version'] = '2.0.0'
        SubElement(root, 'name').text = f"{widget_cls.__name__}_{num}"
        SubElement(root, 'x').text = str(10)
        SubElement(root, 'y').text = str(10)
        SubElement(root, 'width').text = str(100)
        SubElement(root, 'height').text = str(100)
        for key, value in kwargs.items():
            SubElement(root, key).text = str(value)
        return root

    return _factory


def verify_widget_has_props(widget: Widget, property_names_and_types: list[tuple[str, type]]) -> None:

    for property_name, property_type in property_names_and_types:
        assert hasattr(widget, property_name)
        prop = getattr(widget, property_name)
        assert isinstance(prop, property_type)

@pytest.fixture
def base_widget_prop_validator():
    def _validator(widget: Widget) -> None:
        base_props = [
            ("name", str),
            ("x", int),
            ("y", int),
            ("width", int),
            ("height", int),
            ("visible", bool),
        ]
        for prop_name, prop_type in base_props:
            assert hasattr(widget, prop_name)
            prop = getattr(widget, prop_name)
            assert isinstance(prop, prop_type)
    return _validator



