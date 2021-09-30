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

# Copyright (c) 2021 Lawrence Berkeley National Laboratory,
# Advanced Light Source, Engineering Division

from phoebusgen.screen.screen import *

__all__ = ["screen"]
