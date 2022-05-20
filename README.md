Python Module to Generate Phoebus Control Screens
===

[![Python unittest Status](https://github.com/als-epics/phoebusgen/workflows/Python%20unittest/badge.svg)](https://github.com/als-epics/phoebusgen/actions)
[![codecov](https://codecov.io/gh/als-epics/phoebusgen/branch/master/graph/badge.svg?token=Ue2BauI8IW)](https://codecov.io/gh/als-epics/phoebusgen)
[![Build Docs](https://github.com/als-epics/phoebusgen/actions/workflows/build-docs.yml/badge.svg)](https://github.com/als-epics/phoebusgen/actions/workflows/build-docs.yml)
[![Upload Python Package](https://github.com/als-epics/phoebusgen/actions/workflows/python-publish.yml/badge.svg)](https://github.com/als-epics/phoebusgen/actions/workflows/python-publish.yml)

Phoebus is the next generation of Control System Studio, a graphical platform for EPICS control systems.
https://github.com/ControlSystemStudio/phoebus

This module aims to provide a way to generate Phoebus xml through Python. See examples [here](examples).

API docs here: [https://als-epics.github.io/phoebusgen](https://als-epics.github.io/phoebusgen/)

Suggestions, comments, and pull requests are welcome.

# Requirements

- Python >= 3.5

# Install
Pip Package: [phoebusgen](https://pypi.org/project/phoebusgen/)
```
pip install phoebusgen
```

# Intro

Phoebus widgets and a Phoebus screen are all Python objects. Widgets can be added to a screen or even to other widgets (for things like Group or Tab widgets).

```
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

```

# Modules 

## phoebusgen.widget

Python API to directly create Phoebus widgets. All standard Phoebus widgets are available, but some (3) are not fully feature complete.

[Widgets Docs](https://als-epics.github.io/phoebusgen/source/phoebusgen.widget.html#module-phoebusgen.widget.widgets)

### Incomplete Widgets
- Image
- Strip Chart
- X/Y Plot

Example
- ```text_update_xml = phoebusgen.widget.TextUpdate(widget_name, pv_name, x, y, width, height)```


## phoebusgen.screen 

Python object to represent a Phoebus screen. Widgets can be added to the screen object and the screen object can be written to a .bob file to be opened in Phoebus.

[Screen Docs](https://als-epics.github.io/phoebusgen/source/phoebusgen.screen.html#module-phoebusgen.screen.screen)

Example
```
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
```

# Site specific color and font definitions

Place a custon color.def or font.def in ~/.phoebusgen/ to force phoebusgen.colors or phoebusgen.fonts to reflect your site's custom definitions. 


```my_widget.predefined_font(phoebusgen.fonts.Header1)```
```my_widget.predefined_color(phoebusgen.colors.OK)```
