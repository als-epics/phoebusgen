""" phoebusgen.screen Module

This module contains a Python class representation of a Phoebus screen. A screen
can be created via the Screen class and then widgets from Phoebusgen.widget can be
added to the Python screen object. At the end, the screen object can write the XML
to a .bob file which can be opened immeditaely into Phoebus

Example:
    >>> import phoebusgen.screen
    >>> import phoebusgen.widget
    >>> my_screen = phoebusgen.screen.Screen("my screen")
    >>> print(my_screen)
    <?xml version="1.0" ?>
    <display version="2.0.0">
      <name>my screen</name>
    </display>

    >>> my_widget = phoebusgen.widget.TextUpdate("test", "test:PV", 10, 10 ,10 ,10)
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


import copy
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
from phoebusgen.v4.properties import HasPosition, HasBackgroundColor, HasMacros, HasName, HasGrid, HasActionsRulesAndScripts, PropertyBase
from phoebusgen.v4.properties.types import OpenDisplayAction
from phoebusgen.v4.widgets import Widget, WidgetContainer
from phoebusgen.v4.utils import prettify_xml
from collections.abc import Sequence
from pathlib import Path
from typing import TypeVar

from phoebusgen.v4.widgets.structure import EmbeddedDisplay




class Screen(WidgetContainer, HasPosition, HasBackgroundColor, HasMacros, HasName, HasGrid, HasActionsRulesAndScripts):
    """ Phoebus Screen object that holds widgets and can be written to .bob file """
    def __init__(self, name: str | None = None, f_name: str | None = None) -> None:
        """
        Create Phoebus screen object. File name is optional and can be specified later

        :param name: Screen Name
        :param f_name: File name for Phoebus screen
        """
        self.bob_file = f_name
        if f_name is not None and os.path.exists(f_name):
            with open(f_name, 'r') as f:
                rough_string = ''.join([line.strip() for line in f.readlines()])
            self.root = ET.fromstring(rough_string)
        else:
            self.root = ET.Element('display', attrib={'version': '2.0.0'})

            # Default screen size for new screens
            self.width = 800
            self.height = 600

        name_elem = self.root.find('name')
        if name_elem is None or name_elem.text is None:
            self.name = 'Display' if not name else name
        else:
            self.name = name_elem.text if not name else name

    def write_screen(self, file_name: str | None = None) -> bool:
        """
        Writes screen XML to file. File name parameter is optional, if not given Screen bob_file member will be used

        :param file_name: File name to write to
        :return: True is successful write, False otherwise
        """
        rough_string = ET.tostring(self.root, encoding = 'utf-8')
        reparse_xml = minidom.parseString(rough_string)
        if file_name is None:
            if self.bob_file is None:
                raise ValueError('Outptut file name not specified. Set bob_file member or provide file_name parameter')

            file_name = self.bob_file
        with open(file_name, 'w') as f:
            reparse_xml.writexml(f, indent='  ', addindent='  ', newl='\n', encoding='UTF-8')
        return True

    def get_linked_screens(self) -> dict[Path, dict[str, str]]:
        linked_screens = {}

        # Add any actions that open displays from the screen
        for action in self.actions:
            if isinstance(action, OpenDisplayAction):
                linked_screens[Path(action.file)] = copy.deepcopy(action.macros).update(self.macros)

        # Add any actions that open displays from the widgets
        def _get_actions_from_widgets(widget: Widget) -> Sequence[PropertyBase]:
            for widget in self.get_widgets():
                for action in widget.actions:
                    if isinstance(action, OpenDisplayAction):
                        linked_screens[Path(action.file)] = copy.deepcopy(action.macros).update(self.macros)
                        if isinstance(widget, HasMacros):
                            linked_screens[Path(action.file)].update(widget.macros)

        for widget_container in [self, *self.get_widgets_by_type(WidgetContainer)]:
            _get_actions_from_widgets(widget_container)

        # Add any embedded displays from the widgets
        for widget in self.get_widgets_by_type(EmbeddedDisplay):
            linked_screens[Path(widget.file)] = copy.deepcopy(widget.macros).update(self.macros)

        return linked_screens

    # def predefined_background_color(self, name: object) -> None:
    #     """
    #     Add named background color to screen

    #     :param name: <Phoebusgen.colors> Predefined color name
    #     """
    #     e = self._shared.create_element(self.root, 'background_color')
    #     self._shared.create_color_element(e, name, None, None, None, None)

    def __str__(self):
        return prettify_xml(self.root)

    def __repr__(self):
        return prettify_xml(self.root)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Screen):
            return False
        return prettify_xml(self.root) == prettify_xml(other.root)
