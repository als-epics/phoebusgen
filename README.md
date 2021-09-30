Python Module to Generate Phoebus Control Screens
===

[![Python unittest Status](https://github.com/tynanford/phoebusgen/workflows/Python%20unittest/badge.svg)](https://github.com/tynanford/phoebusgen/actions)
[![codecov](https://codecov.io/gh/tynanford/phoebusgen/branch/master/graph/badge.svg)](https://codecov.io/gh/tynanford/phoebusgen)

Phoebus is the next generation of Control System Studio, a graphical platform for EPICS control systems.
https://github.com/ControlSystemStudio/phoebus

This module aims to provide a way to generate Phoebus xml through Python. See examples [here](examples).

# Requirements

- Python >= 3.5

# Install
Pip Package: [phoebusgen](https://pypi.org/project/phoebusgen/)
```
pip install phoebusgen
```

# Intro

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

Low Level Python API to directly create Phoebus widgets. All standard Phoebus widgets are available, but some are not fully feature complete.

### Incomplete Widgets
- Image
- Strip Chart
- X/Y Plot

See [here](docs/html) for more details on the available methods for each widget.

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

# Site specific color and font definitions

Place a custon color.def or font.def in ~/.phoebusgen/ to force phoebusgen.colors or phoebusgen.fonts to reflect your site's custom definitions. 


```my_widget.predefined_font(phoebusgen.fonts.Header1)```
```my_widget.predefined_color(phoebusgen.colors.OK)```
