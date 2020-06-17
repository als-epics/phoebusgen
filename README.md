Python Module to Generate Phoebus Control Screens
===

Phoebus is the next generation of Control System Studio, a graphical platform for EPICS control systems.
https://github.com/ControlSystemStudio/phoebus

This module aims to provide a way to generate Phoebus xml through Python.

# Requirements

- Python >= 3.5
- [pyyaml](https://pypi.org/project/PyYAML/)

# Basics

## phoebusgen.widget

Low Level Python API to directly create Phoebus widgets

Example
- ```text_update_xml = phoebusgen.widget.TextUpdate(widget_name, pv_name, x, y, height, width)```


## phoebusgen.screen 



