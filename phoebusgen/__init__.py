""" phoebusgen Module
This module contains a Python class representation of a Phoebus screen and all widgets.
With the module, you can create Python scripts to write Phoebus screens to a .bob file.
Almost all possible functionality should exist in Phoebusgen that you can do in the Display
Builder Editor.

In addition, phoebusgen.colors and phoebusgen.fonts are Enum objects that are available
to use to add predefined colors/fonts to widgets.
    Example: text_update_widget.predefined_foreground_color(phoebusgen.colors.OK)
A custom site specific color.def or font.def in ~/.phoebusgen/ to force phoebusgen.colors or phoebusgen.fonts
to reflect your site's custom definitions.
"""

# Copyright (c) 2021 Lawrence Berkeley National Laboratory,
# Advanced Light Source, Engineering Division

import phoebusgen.widget
import phoebusgen.screen

from os import path as _path
from sys import platform as _platform
import re as _re
from enum import Enum as _enum

_curr_path = _path.dirname(__file__)
_color_def = _curr_path + '/config/color.def'
_font_def = _curr_path + '/config/font.def'
_classes_bcf = _curr_path + '/config/classes.bcf'
_local_color_def = _path.expanduser('~/.phoebusgen/color.def')
_local_font_def = _path.expanduser('~/.phoebusgen/font.def')
if _path.isfile(_local_color_def):
    _color_def = _local_color_def
if _path.isfile(_local_font_def):
    _font_def = _local_font_def

def _update_color_def(file_path):
    #print('Using color.def file at: {}'.format(file_path))
    predefined_colors = {}
    if not _path.isfile(file_path):
        print('File at this path does not exist: {}'.format(file_path))
    with open(file_path, 'r') as color_file:
        for line in color_file:
            line = line.partition('#')[0].rstrip()
            if line != "":
                color, value = line.split('=')
                color = color.strip()
                vals = [v.strip() for v in value.split(',')]
                if len(vals) == 1:
                    predefined_colors[color] = predefined_colors[vals[0]]
                else:
                    if len(vals) == 4:
                        alpha = vals[3]
                    else:
                        alpha = 255
                    predefined_colors[color] = {'name': color, 'red': str(vals[0]), 'green': str(vals[1]),
                                                'blue': str(vals[2]), 'alpha': str(alpha)}
    return predefined_colors

def _update_font_def(file_path):
    if not _path.isfile(file_path):
        print('File at this path does not exist: {}'.format(file_path))
    with open(file_path, 'r') as font_file:
        predefined_fonts = {}
        os = _platform.lower()
        if 'linux' in os:
            os = 'linux'
        elif 'darwin' in os:
            os = 'macosx'
        elif 'win' in os:
            os = 'windows'
        for line in font_file:
            line = line.partition('//')[0].rstrip()
            if line != "":
                font, value = line.split('=')
                font = font.strip()
                os_name = _re.search('\(([^)]+)', font)
                if os_name:
                    os_name = os_name.group(1)
                    if os_name != os:
                        continue
                    else:
                        font = font.replace('(', '')
                        font = font.replace(')', '')
                        font = font.replace(os, '')
                vals = [v.strip() for v in value.split('-')]
                if len(vals) == 1:
                    predefined_fonts[font] = predefined_fonts[vals[0].strip('@')]
                else:
                    family = vals[0]
                    style = vals[1]
                    size = vals[2]
                    if style.lower() == 'regular':
                        style = 'REGULAR'
                    elif style.lower() == 'bold':
                        style = 'BOLD'
                    elif style.lower() == 'italic':
                        style = 'ITALIC'
                    elif style.lower() == 'bold italic':
                        style = 'BOLD_ITALIC'
                    predefined_fonts[font.replace(' ', '')] = {'name': font, 'family': family, 'style': style, 'size': size}
        return predefined_fonts



_predefined_colors = _update_color_def(_color_def)
colors = _enum('colors', _predefined_colors)
_predefined_fonts = _update_font_def(_font_def)
fonts = _enum('fonts', _predefined_fonts)
