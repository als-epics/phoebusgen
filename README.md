Python Module to Generate Phoebus Control Screens
===

Phoebus is the next generation of Control System Studio, a graphical platform for EPICS control systems.
https://github.com/ControlSystemStudio/phoebus

This module aims to provide a way to generate Phoebus xml through Python.

# Requirements

- Python >= 3.5
  - Python 2.7 currently is [passing tests](https://travis-ci.org/github/tynanford/phoebusgen) but has not been throughly tested
- [pyyaml](https://pypi.org/project/PyYAML/)

# Install
Pip Package: [phoebusgen](https://pypi.org/project/phoebusgen/)
```
pip install phoebusgen
```

# Intro

```
>>> import phoebusgen.widget as w
>>> text_update_widget = w.TextUpdate('test widget', 'TEST:PV', 10, 20, 20, 50)
>>> text_update_widget.predefined_foreground_color('OK')
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
    <color red="0" green="255" blue="0" alpha="255" name="OK"/>
  </foreground_color>
</widget>
```


# Modules 

## phoebusgen.widget

Low Level Python API to directly create Phoebus widgets

Widgets Finished:
- Label
- Text Update
- Text Entry

Example
- ```text_update_xml = phoebusgen.widget.TextUpdate(widget_name, pv_name, x, y, height, width)```


## phoebusgen.screen 

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



