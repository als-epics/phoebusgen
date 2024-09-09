# Python Module to Generate Phoebus Control Screens

[![PyPI](https://img.shields.io/pypi/v/phoebusgen)](https://pypi.org/project/phoebusgen/)
[![Python unittest Status](https://github.com/als-epics/phoebusgen/workflows/Python%20unittest/badge.svg)](https://github.com/als-epics/phoebusgen/actions)
[![codecov](https://codecov.io/gh/als-epics/phoebusgen/branch/master/graph/badge.svg?token=Ue2BauI8IW)](https://codecov.io/gh/als-epics/phoebusgen)
[![Build Docs](https://github.com/als-epics/phoebusgen/actions/workflows/build-docs.yml/badge.svg)](https://github.com/als-epics/phoebusgen/actions/workflows/build-docs.yml)
[![Upload Python Package](https://github.com/als-epics/phoebusgen/actions/workflows/python-publish.yml/badge.svg)](https://github.com/als-epics/phoebusgen/actions/workflows/python-publish.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/e16f9c35657f47fcb31347fbd4f92367)](https://www.codacy.com/gh/als-epics/phoebusgen/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=als-epics/phoebusgen&amp;utm_campaign=Badge_Grade)

Phoebus is the next generation of Control System Studio, a graphical platform for EPICS control systems.
https://github.com/ControlSystemStudio/phoebus

This module provides a way through Python to generate the Display Builder XML format used by Phoebus (and other tools like DBWR). See examples [here](examples).

API docs here: [https://als-epics.github.io/phoebusgen](https://als-epics.github.io/phoebusgen/)

Suggestions, comments, and pull requests are welcome.

## Requirements

-   Python >= 3.5

## Install
Pip Package: [phoebusgen](https://pypi.org/project/phoebusgen/)
```shell
pip install phoebusgen
```

## Intro

Phoebus widgets and a Phoebus screen are all Python objects. Widgets can be added to a screen or even to other widgets (for things like Group or Tab widgets).

```pycon
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

## Modules

### phoebusgen.widget

Python API to directly create Phoebus widgets. All standard Phoebus widgets are available, but some (3) are not fully feature complete.

[Widgets Docs](https://als-epics.github.io/phoebusgen/source/phoebusgen.widget.html#module-phoebusgen.widget.widgets)

#### Incomplete Widgets
-   Image
-   Strip Chart
-   X/Y Plot

Example
-   ```text_update_xml = phoebusgen.widget.TextUpdate(widget_name, pv_name, x, y, width, height)```

### phoebusgen.screen

Python object to represent a Phoebus screen. Widgets can be added to the screen object and the screen object can be written to a .bob file to be opened in Phoebus.

[Screen Docs](https://als-epics.github.io/phoebusgen/source/phoebusgen.screen.html#module-phoebusgen.screen.screen)

Example
```pycon
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

## Phoebus Version Support

In some cases, the XML definitions for a widget can differ between CS Studio Phoebus versions. With phoebusgen 3.0.0 and above,
versioning is supported via several methods.

phoebusgen will default to use the latest Phoebus released version. At this time for example:

```python
>>> import phoebusgen
>>> phoebusgen.phoebus_version
'4.7.3'
>>> phoebusgen.widget_versions
{'arc': '2.0.0', 'ellipse': '2.0.0', 'label': '2.0.0', 'picture': '2.0.0', 'polygon': '2.0.0', 'polyline': '2.0.0',
 'rectangle': '2.0.0', 'byte_monitor': '2.0.0', 'led': '2.0.0', 'multi_state_led': '2.0.0', 'meter': '3.0.0',
 'progressbar': '2.0.0', 'symbol': '2.0.0', 'table': '2.0.0', 'tank': '2.0.0', 'text-symbol': '2.0.0',
 'textupdate': '2.0.0', 'thermometer': '2.0.0', 'action_button': '2.0.0', 'bool_button': '2.0.0', 'checkbox': '2.0.0',
 'choice': '2.0.0', 'combo': '2.0.0', 'fileselector': '2.0.0', 'radio': '2.0.0', 'scaledslider': '2.0.0',
 'scrollbar': '2.0.0', 'slide_button': '2.0.0', 'spinner': '2.0.0', 'textentry': '2.0.0', 'thumbwheel': '2.0.0',
 'databrowser': '2.0.0', 'image': '2.0.0', 'stripchart': '2.1.0', 'xyplot': '3.0.0', 'array': '2.0.0', 'tabs': '2.0.0',
 'embedded': '2.0.0', 'group': '3.0.0', 'navtabs': '2.0.0', 'template': '2.0.0', '3dviewer': '2.0.0',
 'webbrowser': '2.0.0'}
```

Here are several ways to change the widget versioning:

- Call the change_phoebus_version method. Currently version 4.7, 4.7.1, 4.7.2, and 4.7.3 are supported. This will update
  all the widget version to what they were in that specific release of phoebus.
  - `phoebusgen.change_phoebus_version("4.7.2")`
- Add your own version definition file (overrides any other def files in ~/.phoebusgen)
  - `~/.phoebusgen/widgets.def`
- Add your own version definition file that matches `phoebusgen.phoebus_version`
  - `~/.phoebusgen/4.7.2_widgets.def`
- Change the version on an individual widget object
  - `my_group = phoebusgen.widget.Group("test", 2,2,2,2); my_group.version("2.0.0")`

See the available versions supported in phoebusgen here: [config directory](./phoebusgen/config)

```python
>>> import phoebusgen
>>> phoebusgen.phoebus_version
'4.7.3'
>>> phoebusgen.change_phoebus_version("4.7.2")
Phoebus version manually changed to 4.7.2.
>>> b = phoebusgen.widget.Group("test", 2,2,2,2)
>>> b
<?xml version="1.0" ?>
<widget type="group" version="2.0.0">
  <name>test</name>
  <x>2</x>
  <y>2</y>
  <width>2</width>
  <height>2</height>
</widget>
>>> b.predefined_line_color("OK")
Line color not compatible with group widget version less than 3.0.0.
```

## Site specific color and font definitions

Place a custom `color.def` or `font.def` in `~/.phoebusgen/` to force phoebusgen.colors or phoebusgen.fonts to reflect your site's custom definitions.

```python
my_widget.predefined_font(phoebusgen.fonts.Header1)
```
```python
my_widget.predefined_color(phoebusgen.colors.OK)
```
