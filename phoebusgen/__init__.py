"phoebusgen package -- test_widget"

import phoebusgen.widget
import phoebusgen.screen

from os import path as _path
from enum import Enum as _enum

_curr_path = _path.dirname(__file__)
_color_def = _curr_path + '/config/color.def'
_font_def = _curr_path + '/config/font.def'
_classes_bcf = _curr_path + '/config/classes.bcf'
_local_color_def = _path.expanduser('~/.phoebusgen/color.def')
if _path.isfile(_local_color_def):
    _color_def = _local_color_def

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
    pass


_predefined_colors = _update_color_def(_color_def)
colors = _enum('colors', _predefined_colors)
