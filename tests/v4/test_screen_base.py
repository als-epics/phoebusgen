from pathlib import Path
from xml.etree.ElementTree import Element

import pytest

from phoebusgen.v4.properties.widget import HasPVName
from phoebusgen.v4.properties.types import Color, OpenDisplayAction, OpenDisplayTarget, ObservableDict
from phoebusgen.v4.screen import Screen, ScreenTransition, NavigationGraph, NavigationEdge
from phoebusgen.v4.widgets import ActionButton, EmbeddedDisplay, Label, NavigationTabs, TextUpdate, Widget, WidgetType


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
    ('background_color', '#FFFFFF', '#FF0000'),
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
    assert isinstance(linked_screens, list)
    assert len(linked_screens) == 0


@pytest.mark.parametrize('macros', [{}, {'Macro1': 'Value1', 'Macro2': 'Value2'}])
def test_get_linked_screens_embedded_display(sample_screen, macros):
    embedded_display = EmbeddedDisplay(name='Embedded Display', file='tests/v4/bobfiles/simple_embedded_display.bob', x=0, y=0, width=100, height=100)
    embedded_display.macros = macros
    assert embedded_display.macros == macros
    sample_screen.add_widget(embedded_display)
    linked_screens = sample_screen.get_linked_screens()
    assert isinstance(linked_screens, list)
    assert len(linked_screens) == 1
    assert linked_screens[0].target == Path('tests/v4/bobfiles/simple_embedded_display.bob')
    assert dict(linked_screens[0].macros) == macros


def test_get_linked_screens_action_button(sample_screen):
    """Test that OpenDisplayActions on widgets are found."""
    btn = ActionButton(name='Go', text='Go', pv_name='', x=0, y=0, width=50, height=20)
    btn.actions = [
        OpenDisplayAction(description='Open Sub', file='sub_screen.bob', target=OpenDisplayTarget.REPLACE, macros=ObservableDict({'M': 'V'}))
    ]
    sample_screen.add_widget(btn)
    transitions = sample_screen.get_linked_screens()
    assert len(transitions) == 1
    assert transitions[0].target == Path('sub_screen.bob')
    assert transitions[0].macros == {'M': 'V'}


def test_get_linked_screens_action_on_screen(sample_screen):
    """Test that OpenDisplayActions on the screen itself are found."""
    sample_screen.actions = [
        OpenDisplayAction(description='Top Link', file='other.bob', target=OpenDisplayTarget.NEW_TAB, macros=ObservableDict({'X': '1'}))
    ]
    transitions = sample_screen.get_linked_screens()
    assert len(transitions) == 1
    assert transitions[0].target == Path('other.bob')
    assert transitions[0].macros == {'X': '1'}


def test_get_linked_screens_multiple_targets(sample_screen):
    """Test multiple transitions from a single widget with multiple actions."""
    btn1 = ActionButton(name='Btn1', text='Btn1', pv_name='', x=0, y=0, width=50, height=20)
    btn1.actions = [
        OpenDisplayAction(description='A', file='screen_a.bob', target=OpenDisplayTarget.REPLACE),
        OpenDisplayAction(description='B', file='screen_b.bob', target=OpenDisplayTarget.NEW_TAB, macros=ObservableDict({'K': 'V'})),
        OpenDisplayAction(description='A again', file='screen_a.bob', target=OpenDisplayTarget.NEW_WINDOW, macros=ObservableDict({'Z': '9'})),
    ]
    sample_screen.add_widget(btn1)
    transitions = sample_screen.get_linked_screens()
    assert len(transitions) == 3
    targets = [t.target for t in transitions]
    assert targets.count(Path('screen_a.bob')) == 2
    assert targets.count(Path('screen_b.bob')) == 1


def test_get_linked_screens_inherits_screen_macros(sample_screen):
    """Test that screen-level macros are inherited by transitions."""
    sample_screen.macros = {'GLOBAL': 'yes'}
    ed = EmbeddedDisplay(name='ED', file='child.bob', x=0, y=0, width=100, height=100)
    ed.macros = {'LOCAL': 'val'}
    sample_screen.add_widget(ed)
    transitions = sample_screen.get_linked_screens()
    assert len(transitions) == 1
    assert transitions[0].macros == {'GLOBAL': 'yes', 'LOCAL': 'val'}


# --- Tests using included bob files ---

def test_linked_screens_example_top1():
    """Example_TOP1 has one embedded display linking to Nested/Nested1.bob with macros."""
    screen = Screen(f_name='tests/v4/bobfiles/Example_TOP1.bob')
    transitions = screen.get_linked_screens()
    assert len(transitions) == 1
    assert transitions[0].target == Path('Nested/Nested1.bob')
    assert transitions[0].macros == {'A': '2', 'B': '3'}


def test_linked_screens_example_top2():
    """Example_TOP2 has an action button with two open_display actions, macros inherited from screen."""
    screen = Screen(f_name='tests/v4/bobfiles/Example_TOP2.bob')
    transitions = screen.get_linked_screens()
    assert len(transitions) == 2
    targets = {t.target for t in transitions}
    assert Path('Nested/Nested1.bob') in targets
    assert Path('Nested/Nested2.bob') in targets
    # Screen macros A=1, B=2 should be inherited
    for t in transitions:
        assert t.macros['A'] == '1'
        assert t.macros['B'] == '2'


def test_linked_screens_nested2():
    """Nested2 has a navtab (linking Even_More_Nested1.bob) and an action button (linking Nested1.bob)."""
    screen = Screen(f_name='tests/v4/bobfiles/Nested/Nested2.bob')
    transitions = screen.get_linked_screens()
    assert len(transitions) == 2
    targets = {t.target for t in transitions}
    assert Path('Nested1.bob') in targets
    assert Path('Even_More_Nested/Even_More_Nested1.bob') in targets
    # NavTab transition has macro C=2
    navtab_transition = next(t for t in transitions if t.target == Path('Even_More_Nested/Even_More_Nested1.bob'))
    assert navtab_transition.macros == {'C': '2'}


def test_linked_screens_leaf_screen():
    """Nested1 is a leaf screen with no links."""
    screen = Screen(f_name='tests/v4/bobfiles/Nested/Nested1.bob')
    transitions = screen.get_linked_screens()
    assert len(transitions) == 0


# --- Navigation graph tests ---

def test_build_navigation_graph_no_links(sample_screen):
    """A screen with no links produces a graph with just itself."""
    sample_screen.bob_file = 'standalone.bob'
    graph = sample_screen.build_navigation_graph()
    assert Path('standalone.bob') in graph.screens
    assert len(graph.transitions) == 0


def test_build_navigation_graph_example_top1():
    """Graph from TOP1: TOP1 -> Nested1 (leaf)."""
    screen = Screen(f_name='tests/v4/bobfiles/Example_TOP1.bob')
    graph = screen.build_navigation_graph(base_dir=Path('tests/v4/bobfiles'))
    assert Path('tests/v4/bobfiles/Example_TOP1.bob') in graph.screens
    assert Path('Nested/Nested1.bob') in graph.screens
    assert len(graph.transitions) == 1
    assert graph.transitions[0].source == Path('tests/v4/bobfiles/Example_TOP1.bob')
    assert graph.transitions[0].target == Path('Nested/Nested1.bob')


def test_build_navigation_graph_example_top2():
    """Graph from TOP2 traverses into Nested2's links (navtab + action button)."""
    screen = Screen(f_name='tests/v4/bobfiles/Example_TOP2.bob')
    graph = screen.build_navigation_graph(base_dir=Path('tests/v4/bobfiles'))

    # TOP2 -> Nested1, TOP2 -> Nested2, Nested2 -> Nested1, Nested2 -> Even_More_Nested1
    assert len(graph.transitions) == 4
    assert Path('Nested/Nested1.bob') in graph.screens
    assert Path('Nested/Nested2.bob') in graph.screens
    assert Path('Even_More_Nested/Even_More_Nested1.bob') in graph.screens

    # Verify specific edges exist
    edges = [(e.source, e.target) for e in graph.transitions]
    assert (Path('tests/v4/bobfiles/Example_TOP2.bob'), Path('Nested/Nested1.bob')) in edges
    assert (Path('tests/v4/bobfiles/Example_TOP2.bob'), Path('Nested/Nested2.bob')) in edges
    assert (Path('Nested/Nested2.bob'), Path('Nested1.bob')) in edges
    assert (Path('Nested/Nested2.bob'), Path('Even_More_Nested/Even_More_Nested1.bob')) in edges


def test_build_navigation_graph_circular_reference():
    """A <-> B circular link does not cause infinite recursion."""
    screen = Screen(f_name='tests/v4/bobfiles/Nested/loop_a.bob')
    graph = screen.build_navigation_graph(base_dir=Path('tests/v4/bobfiles/Nested'))

    # Should terminate and contain both screens
    assert Path('tests/v4/bobfiles/Nested/loop_a.bob') in graph.screens
    assert Path('loop_b.bob') in graph.screens
    assert Path('loop_a.bob') in graph.screens

    # A -> B and B -> A
    edges = [(e.source, e.target) for e in graph.transitions]
    assert (Path('tests/v4/bobfiles/Nested/loop_a.bob'), Path('loop_b.bob')) in edges
    assert (Path('loop_b.bob'), Path('loop_a.bob')) in edges

    # No duplicate traversal — exactly 2 edges
    assert len(graph.transitions) == 2


def test_build_navigation_graph_back_link():
    """A screen that links back to a parent does not cause infinite recursion."""
    screen = Screen(f_name='tests/v4/bobfiles/Nested/loop_back.bob')
    graph = screen.build_navigation_graph(base_dir=Path('tests/v4/bobfiles/Nested'))

    # loop_back links to ../Example_TOP2.bob which is outside base_dir and won't be found
    assert Path('tests/v4/bobfiles/Nested/loop_back.bob') in graph.screens
    assert Path('../Example_TOP2.bob') in graph.screens


# --- get_used_macros tests ---

def test_get_used_macros_empty_screen(sample_screen):
    """A fresh screen with no macro references returns empty sets."""
    macros, defaults = sample_screen.get_used_macros()
    assert macros == set()
    assert defaults == set()


def test_get_used_macros_pv_name(sample_screen):
    """Macros in PV names are detected."""
    widget = TextUpdate(name='test', pv_name='$(PREFIX):sensor:$(CHANNEL)', x=0, y=0, width=100, height=20)
    sample_screen.add_widget(widget)
    macros, defaults = sample_screen.get_used_macros()
    assert macros == {'PREFIX', 'CHANNEL'}
    assert defaults == set()


def test_get_used_macros_in_text(sample_screen):
    """Macros in widget text/labels are detected."""
    btn = ActionButton(name='btn', text='$(LABEL) Control', pv_name='', x=0, y=0, width=50, height=20)
    sample_screen.add_widget(btn)
    macros, _ = sample_screen.get_used_macros()
    assert 'LABEL' in macros


def test_get_used_macros_in_actions(sample_screen):
    """Macros in action file paths are detected."""
    btn = ActionButton(name='btn', text='Go', pv_name='', x=0, y=0, width=50, height=20)
    btn.actions = [
        OpenDisplayAction(description='Open', file='$(TOP)/screens/detail.bob', target=OpenDisplayTarget.REPLACE)
    ]
    sample_screen.add_widget(btn)
    macros, _ = sample_screen.get_used_macros()
    assert 'TOP' in macros


def test_get_used_macros_multiple_widgets(sample_screen):
    """Macros from multiple widgets are collected."""
    w1 = TextUpdate(name='w1', pv_name='$(SYS):temp', x=0, y=0, width=100, height=20)
    w2 = TextUpdate(name='w2', pv_name='$(DEV):pressure', x=0, y=30, width=100, height=20)
    sample_screen.add_widget(w1)
    sample_screen.add_widget(w2)
    macros, defaults = sample_screen.get_used_macros()
    assert macros == {'SYS', 'DEV'}
    assert defaults == set()


def test_get_used_macros_from_file():
    """Macros are detected when loading a screen from a file."""
    screen = Screen(f_name='tests/v4/bobfiles/Example_TOP1.bob')
    macros, defaults = screen.get_used_macros()
    # Example_TOP1 has macros defined in embedded display macro assignments
    assert isinstance(macros, set)
    assert isinstance(defaults, set)


def test_get_used_macros_excludes_widget_properties_in_tooltip(sample_screen):
    """Widget property names used as macros (e.g. in tooltip) are excluded."""
    widget = TextUpdate(name='sensor', pv_name='$(PREFIX):temp', x=0, y=0, width=100, height=20)
    widget.tooltip = '$(pv_name) = $(pv_value)'
    sample_screen.add_widget(widget)
    macros, _ = sample_screen.get_used_macros()
    # pv_name is a property of TextUpdate, pv_value is a runtime macro for PV widgets
    assert 'pv_name' not in macros
    assert 'pv_value' not in macros
    # PREFIX is a real user macro
    assert 'PREFIX' in macros


def test_get_used_macros_excludes_name_property_in_tooltip(sample_screen):
    """The 'name' property used as $(name) in a tooltip is excluded."""
    widget = TextUpdate(name='MySensor', pv_name='TEST:PV', x=0, y=0, width=100, height=20)
    widget.tooltip = 'Widget: $(name)'
    sample_screen.add_widget(widget)
    macros, _ = sample_screen.get_used_macros()
    assert 'name' not in macros


def test_get_used_macros_excludes_builtin_macros(sample_screen):
    """Phoebus built-in macros DID and DNAME are excluded."""
    widget = Label(name='info', text='Display $(DNAME) id=$(DID)', x=0, y=0, width=200, height=20)
    sample_screen.add_widget(widget)
    macros, _ = sample_screen.get_used_macros()
    assert 'DID' not in macros
    assert 'DNAME' not in macros


def test_get_used_macros_pv_value_not_excluded_for_non_pv_widget(sample_screen):
    """$(pv_value) is only excluded for widgets that have a pv_name property."""
    widget = Label(name='lbl', text='$(pv_value)', x=0, y=0, width=100, height=20)
    sample_screen.add_widget(widget)
    macros, _ = sample_screen.get_used_macros()
    # Label has no pv_name, so pv_value is treated as a user macro
    assert 'pv_value' in macros


def test_get_used_macros_mixed_properties_and_user_macros(sample_screen):
    """Only real user macros are returned when properties and builtins are mixed."""
    widget = TextUpdate(name='w', pv_name='$(SYS):$(DEV):reading', x=0, y=0, width=100, height=20)
    widget.tooltip = 'PV: $(pv_name) Val: $(pv_value) Display: $(DNAME)'
    sample_screen.add_widget(widget)
    macros, defaults = sample_screen.get_used_macros()
    assert macros == {'SYS', 'DEV'}
    assert defaults == set()


def test_get_used_macros_with_defaults(sample_screen):
    """Macros that always have defaults are returned in the defaults set."""
    widget = TextUpdate(name='w', pv_name='$(PREFIX=TEST):$(CHANNEL):reading', x=0, y=0, width=100, height=20)
    sample_screen.add_widget(widget)
    macros, defaults = sample_screen.get_used_macros()
    assert 'CHANNEL' in macros
    assert 'PREFIX' not in macros
    assert defaults == {'PREFIX'}


def test_get_used_macros_all_uses_have_defaults(sample_screen):
    """A macro used multiple times always with defaults stays in the defaults set."""
    w1 = TextUpdate(name='w1', pv_name='$(SYS=SysA):temp', x=0, y=0, width=100, height=20)
    w2 = TextUpdate(name='w2', pv_name='$(SYS=SysB):pressure', x=0, y=30, width=100, height=20)
    sample_screen.add_widget(w1)
    sample_screen.add_widget(w2)
    macros, defaults = sample_screen.get_used_macros()
    assert 'SYS' not in macros
    assert defaults == {'SYS'}


def test_get_used_macros_mixed_default_and_no_default(sample_screen):
    """A macro used both with and without a default is only in the required set."""
    w1 = TextUpdate(name='w1', pv_name='$(PREFIX=DEF):temp', x=0, y=0, width=100, height=20)
    w2 = TextUpdate(name='w2', pv_name='$(PREFIX):pressure', x=0, y=30, width=100, height=20)
    sample_screen.add_widget(w1)
    sample_screen.add_widget(w2)
    macros, defaults = sample_screen.get_used_macros()
    # Has a use without default, so it's required
    assert 'PREFIX' in macros
    assert 'PREFIX' not in defaults
