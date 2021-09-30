""" phoebusgen.widget Module
This module contains Python class representations of each widget. Widgets can be created
by calling the widget class constructor, i.e. phoebusgen.widget.TextUpdate(...) or
phoebusgen.widget.ScaledSlider(...). Once the class is created and assigned to a Python
variable, additional methods to change widget properties are available.

Example:
    >>> import phoebusgen
    >>> text_update_widget = phoebusgen.widget.TextUpdate('test widget', 'TEST:PV', 10, 20, 20, 50)
    >>> text_update_widget.predefined_foreground_color(phoebusgen.colors.OK)
    >>> text_update_widget.font_style_bold()
    >>> print(text_update_widget)
    <?xml version="1.0" ?>
    <widget type="textupdate" version="2.0.0">
      <name>test widget</name>
      <x>10</x>
      <y>20</y>
      <width>20</width>
      <height>50</height>
      <pv_name>TEST:PV</pv_name>
      <foreground_color>
        <color name="OK" red="0" green="255" blue="0" alpha="255"/>
      </foreground_color>
      <font>
        <font family="Liberation Sans" size="14" style="BOLD"/>
      </font>
    </widget>
"""

# Copyright (c) 2021 Lawrence Berkeley National Laboratory,
# Advanced Light Source, Engineering Division

from phoebusgen.widget.widgets import *

__all__ = ["widgets"]
