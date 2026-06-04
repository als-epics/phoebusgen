""" phoebusgen.screen Module

This module contains a Python class representation of a Phoebus screen. A screen
can be created via the Screen class and then widgets from Phoebusgen.widget can be
added to the Python screen object. At the end, the screen object can write the XML
to a .bob file which can be opened immeditaely into Phoebus

Example:
    >>> import phoebusgen.v4.screen
    >>> import phoebusgen.v4.widgets
    >>> my_screen = phoebusgen.v4.screen.Screen("my screen")
    >>> print(my_screen)
    <?xml version="1.0" ?>
    <display version="2.0.0">
      <name>my screen</name>
    </display>

    >>> my_widget = phoebusgen.v4.widgets.TextUpdate("test", "test:PV", 10, 10 ,10 ,10)
    >>> my_screen.add_widget(my_widget)
    >>> print(my_screen)
    <?xml version="1.0" ?>
    <display version="2.0.0">
      <name>my screen</name>
      <widget type="textupdate" version="2.0.0">
        <name>test</name>
        <x>10</x>
        <y>10</y>
        <width>10</width>
        <height>10</height>
        <pv_name>test:PV</pv_name>
      </widget>
    </display>

"""


import os
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from xml.dom import minidom

from phoebusgen.v4.properties.behavior import HasActionsRulesAndScripts
from phoebusgen.v4.properties.display import HasBackgroundColor
from phoebusgen.v4.properties.misc import HasGrid
from phoebusgen.v4.properties.position import HasPosition
from phoebusgen.v4.properties.types import OpenDisplayAction
from phoebusgen.v4.properties.widget import HasMacros, HasName, HasNavTabs
from phoebusgen.v4.widgets import HasWidgets, Widget
from phoebusgen.v4.widgets.structure import EmbeddedDisplay, TemplateInstance


class Screen(HasWidgets, HasPosition, HasBackgroundColor, HasMacros, HasName, HasGrid, HasActionsRulesAndScripts):
    """ Phoebus Screen object that holds widgets and can be written to .bob file """

    width: int = 800
    height: int = 600

    def __init__(self, name: Optional[str] = None, f_name: Optional[str] = None) -> None:
        """
        Create Phoebus screen object. File name is optional and can be specified later

        :param name: Screen Name
        :param f_name: File name for Phoebus screen
        """

        self.bob_file = f_name
        if f_name is not None and os.path.exists(f_name):
            with open(f_name, 'r') as f:
                rough_string = ''.join([line.strip() for line in f.readlines()])
            root = ET.fromstring(rough_string)
        else:
            root = ET.Element('display', attrib={'version': '2.0.0'})

        self.root = root
        HasWidgets.__init__(self, None)

        if f_name is None or not os.path.exists(f_name):
            # Default screen size for new screens
            self.width = 800
            self.height = 600

        name_elem = root.find('name')
        if name_elem is None or name_elem.text is None:
            self.name = 'Display' if not name else name
        else:
            self.name = name_elem.text if not name else name

    def write_screen(self, file_name: Optional[str] = None) -> bool:
        """
        Writes screen XML to file. File name parameter is optional, if not given Screen bob_file member will be used

        :param file_name: File name to write to
        :return: True is successful write, False otherwise
        """
        rough_string = ET.tostring(self.root, encoding = 'utf-8')
        reparse_xml = minidom.parseString(rough_string)
        if file_name is None:
            if self.bob_file is None:
                raise ValueError('Output file name not specified. Set bob_file member or provide file_name parameter')

            file_name = self.bob_file
        with open(file_name, 'w') as f:
            reparse_xml.writexml(f, indent='', addindent='  ', newl='\n', encoding='UTF-8')
        return True

    def get_linked_screens(self) -> List['ScreenTransition']:
        """Get all screens linked from this screen via actions, embedded displays, nav tabs, etc.

        :return: List of ScreenTransition objects describing each link
        """
        transitions = []  # type: List[ScreenTransition]
        screen_macros = dict(self.macros)

        def _collect_actions(container):
            """Collect OpenDisplayAction transitions from a widget or screen."""
            if not isinstance(container, HasActionsRulesAndScripts):
                return
            container_macros = dict(container.macros) if isinstance(container, HasMacros) else {}
            for action in container.actions:
                if isinstance(action, OpenDisplayAction) and action.file is not None:
                    macros = {}
                    macros.update(screen_macros)
                    macros.update(container_macros)
                    macros.update(action.macros)
                    transitions.append(ScreenTransition(
                        target=Path(action.file),
                        macros=macros,
                    ))

        # Collect from the screen itself
        _collect_actions(self)

        # Collect from all widgets (including nested ones in groups/tabs)
        all_widgets = self.get_all_widgets()

        for widget in all_widgets:
            _collect_actions(widget)

        # Collect from EmbeddedDisplay widgets
        for widget in all_widgets:
            if isinstance(widget, EmbeddedDisplay) and widget.file is not None:
                macros = {}
                macros.update(screen_macros)
                macros.update(widget.macros)
                transitions.append(ScreenTransition(
                    target=Path(widget.file),
                    macros=macros,
                ))

        # Collect from TemplateInstance widgets
        for widget in all_widgets:
            if isinstance(widget, TemplateInstance) and widget.file is not None:
                macros = {}
                macros.update(screen_macros)
                macros.update(widget.macros)
                transitions.append(ScreenTransition(
                    target=Path(widget.file),
                    macros=macros,
                ))

        # Collect from NavigationTabs widgets
        for widget in all_widgets:
            if isinstance(widget, HasNavTabs):
                for tab in widget.tabs:
                    if tab.file is not None:
                        macros = {}
                        macros.update(screen_macros)
                        macros.update(tab.macros)
                        transitions.append(ScreenTransition(
                            target=Path(tab.file),
                            macros=macros,
                        ))

        return transitions

    def predefined_background_color(self, name: object) -> None:
        """
        Add named background color to screen

        :param name: <Phoebusgen.colors> Predefined color name
        """
        e = self._shared.create_element(self.root, 'background_color')
        self._shared.create_color_element(e, name, None, None, None, None)

    # Phoebus built-in macros that are always available at runtime
    # and should not be reported as user-defined macros.
    # See: MacroOrPropertyProvider.java in Phoebus source
    BUILTIN_MACROS = frozenset({'DID', 'DNAME'})

    # Macros conditionally available for widgets that have a pv_name property.
    # $(pv_value) resolves to the current PV value at runtime.
    PV_WIDGET_MACROS = frozenset({'pv_value'})

    def get_used_macros(self) -> Tuple[Set[str], Set[str]]:
        """Get all macro names referenced in this screen via the $(MACRO) pattern.

        Scans all text content and attribute values in the screen's XML tree
        for macro references like $(PV_PREFIX), $(DEVICE), etc.

        Macros that always specify a default via ``$(NAME=DEFAULT)`` are returned
        in a separate set. If a macro appears both with and without a default,
        it is included only in the required (no-default) set.

        Excludes references that match property names of the widget they appear in,
        since Phoebus resolves those from the widget's own properties rather than macros.
        Also excludes Phoebus built-in macros (DID, DNAME) that are always available at runtime.

        :return: Tuple of (set of macros without defaults, set of macros that always have defaults)
        """
        macro_pattern = re.compile(r'\$\(([^)]+)\)')
        macros = set()  # type: Set[str]
        macros_with_defaults = set()  # type: Set[str]

        def _scan_element(elem, widget_property_names: Set[str]):
            raw_matches = []  # type: list
            if elem.text:
                raw_matches.extend(macro_pattern.findall(elem.text))
            if elem.tail:
                raw_matches.extend(macro_pattern.findall(elem.tail))
            for value in elem.attrib.values():
                raw_matches.extend(macro_pattern.findall(value))

            for match in raw_matches:
                if '=' in match:
                    name = match.split('=', 1)[0]
                    has_default = True
                else:
                    name = match
                    has_default = False
                # Exclude widget property references and built-in macros
                if name in widget_property_names or name in self.BUILTIN_MACROS:
                    continue
                if has_default:
                    macros_with_defaults.add(name)
                else:
                    macros.add(name)

            for child in elem:
                # When entering a widget element, resolve its property names
                if child.tag == 'widget':
                    child_prop_names = set()  # type: Set[str]
                    try:
                        w = Widget.from_element(child)
                        child_prop_names = set(w.get_property_names())
                        # Widgets with a pv_name also have pv_value available at runtime
                        if 'pv_name' in child_prop_names:
                            child_prop_names |= self.PV_WIDGET_MACROS
                    except (ValueError, KeyError):
                        pass
                    _scan_element(child, child_prop_names)
                else:
                    _scan_element(child, widget_property_names)

        # Screen-level properties
        screen_prop_names = set(self.get_property_names())
        _scan_element(self.root, screen_prop_names)
        # If a macro appears both with and without a default, it's required
        macros_with_defaults -= macros
        return macros, macros_with_defaults

    def build_navigation_graph(self, base_dir: Optional[Path] = None) -> 'NavigationGraph':
        """Build a navigation graph starting from this screen, recursively following all linked screens.

        :param base_dir: Base directory to resolve relative file paths. If None, uses bob_file's parent or cwd.
        :return: NavigationGraph with all reachable screens and transitions
        """
        if base_dir is None:
            if self.bob_file is not None:
                base_dir = Path(self.bob_file).resolve().parent
            else:
                base_dir = Path.cwd()
        else:
            base_dir = base_dir.resolve()

        graph = NavigationGraph()
        start_path = Path(self.bob_file) if self.bob_file else Path(self.name + '.bob')
        visited = set()  # type: Set[Path]

        def _visit(screen_path: Path, screen: 'Screen', screen_dir: Path = None):
            if screen_dir is None:
                screen_dir = Path(screen_path).resolve().parent

            resolved = screen_dir / screen_path.name
            resolved = resolved.resolve()
            if resolved in visited:
                return
            visited.add(resolved)
            graph.screens.add(screen_path)

            for transition in screen.get_linked_screens():
                graph.transitions.append(NavigationEdge(
                    source=screen_path,
                    target=transition.target,
                    macros=transition.macros,
                ))
                graph.screens.add(transition.target)

                # Resolve the target relative to the current screen's directory
                target_resolved = (screen_dir / transition.target).resolve()
                if target_resolved not in visited and target_resolved.exists():
                    try:
                        linked_screen = Screen(f_name=str(target_resolved))
                        _visit(transition.target, linked_screen, target_resolved.parent)
                    except Exception:
                        pass  # Skip screens that can't be parsed

        _visit(start_path, self, Path(self.bob_file).resolve().parent if self.bob_file else base_dir)
        return graph


@dataclass
class ScreenTransition:
    """A transition from one screen to another, with the macros that are passed."""
    target: Path
    macros: Dict[str, str] = field(default_factory=dict)


@dataclass
class NavigationGraph:
    """A graph of screen navigation paths.

    Nodes are screen file paths. Edges are transitions between screens,
    each carrying the macros passed during that transition.
    """
    screens: Set[Path] = field(default_factory=set)
    transitions: List['NavigationEdge'] = field(default_factory=list)


@dataclass
class NavigationEdge:
    """A directed edge in the navigation graph."""
    source: Path
    target: Path
    macros: Dict[str, str] = field(default_factory=dict)
