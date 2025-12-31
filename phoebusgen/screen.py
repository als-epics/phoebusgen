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


import xml.etree.ElementTree as ET
from xml.dom import minidom
from typing import Union
import os
from phoebusgen.properties import HasHeight, HasWidth, HasBackgroundColor, HasX, HasY, HasMacros, HasName, HasGridVisible, HasGridColor, HasGridStepX, HasGridStepY, HasActions, HasRules, HasScripts, PropertyBase
from phoebusgen.widgets import Widget
from phoebusgen.utils import prettify_xml
from collections.abc import Sequence, Mapping

class Screen(HasHeight, HasWidth, HasBackgroundColor, HasX, HasY, HasMacros, HasName, HasGridVisible, HasGridColor, HasGridStepX, HasGridStepY, HasActions, HasRules, HasScripts):
    """ Phoebus Screen object that holds widgets and can be written to .bob file """
    def __init__(self, name: str, f_name: str | None = None) -> None:
        """
        Create Phoebus screen object. File name is optional and can be specified later

        :param name: Screen Name
        :param f_name: File name for Phoebus screen
        """
        self.bob_file = f_name
        self.root = ET.Element('display', version='2.0.0')
        if f_name is not None and os.path.exists(f_name):
            with open(f_name, 'r') as f:
                rough_string = f.read()
            self.root = ET.fromstring(rough_string)

        self.name = name

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
                print('Output Phoebus file name is not set! First set bob_file or use file_name parameter')
                return False
            file_name = self.bob_file
        with open(file_name, 'w') as f:
            reparse_xml.writexml(f, indent='  ', addindent='  ', newl='\n', encoding='UTF-8')
        return True

    def find_widget(self, widget_tag_name: str) -> ET.Element | list[ET.Element] | None:
        """
        Find widget in the screen

        :param widget_tag_name: Tag name of widget to find
        :return: None if not found or widget that was found
        """
        elements = self.root.findall(widget_tag_name)
        if len(elements) > 1:
            print('Warning, more than one element of the same tag! Returning a list')
            return elements
        elif len(elements) == 0:
            return None
        else:
            return elements[0]
        
    def get_widgets(self) -> list[Widget]:
        return [Widget(elem) for elem in self.root.findall('widget')]

    def get_widgets_by_type(self, widget_type: type[Widget]) -> list[Widget]:
        return [w for w in self.get_widgets() if isinstance(w, widget_type)]

    def get_widgets_by_property(self, prop_type: type[PropertyBase]) -> list[Widget]:
        return [w for w in self.get_widgets() if isinstance(w, prop_type)]

    def add_widget(self, elem: Widget | Sequence[Widget]) -> None:
        """
        Add widget or list of widgets to screen

        :param elem: <list/Phoebusgen.widget> List of Phoebusgen.widget's or a single widget to add
        """
        if isinstance(elem, Sequence):
            for e in elem:
                self.root.append(e.root)
        else:
            self.root.append(elem.root)

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