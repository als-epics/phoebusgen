from pathlib import Path
from xml.etree.ElementTree import Element

import pytest

from phoebusgen.v4.properties.display import HasPVName
from phoebusgen.v4.properties.types import Color
from phoebusgen.v4.screen import Screen
from phoebusgen.v4.widgets import EmbeddedDisplay, Widget, WidgetType


@pytest.fixture
def sample_screen():
    screen = Screen(name='Sample Screen')
    return screen

@pytest.fixture
def one_of_every_widget_screen():
    screen = Screen(f_name='tests/v4/bobfiles/one_of_every_widget.bob')
    return screen

@pytest.mark.parametrize('screen_name', [None, 'My Test Screen'])
def test_create_fresh_screen(screen_name):
    screen = Screen(name=screen_name)
    assert screen is not None
    assert isinstance(screen.root, Element)
    assert screen.root.tag == 'display'
    if screen_name is None:
        assert screen.name == 'Display'
    else:
        assert screen.name == screen_name


@pytest.mark.parametrize('property_name, initial_value, new_value', [
    ('width', 800, 1280),
    ('height', 600, 720),
    ('grid_visible', True, False),
    ('grid_color', Color((128, 128, 128)), Color((100, 100, 100))),
    ('background_color', '#000000', '#FF0000'),
    ('macros', {}, {'TestA': 'ValueA', 'TestB': 'ValueB'}),
])
def test_screen_properties(sample_screen, property_name, initial_value, new_value):
    assert hasattr(sample_screen, property_name)
    assert getattr(sample_screen, property_name) == initial_value
    setattr(sample_screen, property_name, new_value)
    assert getattr(sample_screen, property_name) == new_value


def test_parse_screen_from_file(one_of_every_widget_screen):
    screen = one_of_every_widget_screen
    assert screen is not None
    assert isinstance(screen.root, Element)
    assert screen.name == 'OneOfEveryWidget'
    assert screen.width == 2000
    assert screen.height == 1200
    assert screen.background_color == Color('#F0F0F0')
    assert screen.grid_visible
    assert screen.grid_step_x == 10
    assert screen.grid_step_y == 10
    for widget in Widget.__subclasses__():
        assert len(screen.get_widgets_by_type(widget)) == 1
    assert len(screen.get_widgets()) == len(list(WidgetType))


def test_get_widgets_by_property(one_of_every_widget_screen):
    screen = one_of_every_widget_screen
    widgets_with_pv_name = screen.get_widgets_by_property_class(HasPVName)
    assert len(widgets_with_pv_name) == 27  # 27 of the 44 widgets have the PV Name property
    widgets_with_tabs = screen.get_widgets_by_property('tabs')
    assert len(widgets_with_tabs) == 2 # There are 2 widgets with tabs property in the test file


def test_get_linked_screens_no_links(sample_screen):
    linked_screens = sample_screen.get_linked_screens()
    assert isinstance(linked_screens, dict)
    assert len(linked_screens) == 0


@pytest.mark.parametrize('macros', [{}, {'Macro1': 'Value1', 'Macro2': 'Value2'}])
def test_get_linked_screens_embedded_display(sample_screen, macros):
    embedded_display = EmbeddedDisplay(name='Embedded Display', file='tests/v4/bobfiles/simple_embedded_display.bob', x=0, y=0, width=100, height=100)
    embedded_display.macros = macros
    assert embedded_display.macros == macros
    sample_screen.add_widget(embedded_display)
    linked_screens = sample_screen.get_linked_screens()
    assert isinstance(linked_screens, dict)
    assert len(linked_screens) == 1
    assert Path('tests/v4/bobfiles/simple_embedded_display.bob') in linked_screens
    assert linked_screens[Path('tests/v4/bobfiles/simple_embedded_display.bob')] == macros
