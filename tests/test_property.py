import sys
sys.path.insert(1, '../phoebusgen/widget/')
sys.path.insert(1, './phoebusgen/widget/')
sys.path.insert(1, '../phoebusgen/')
sys.path.insert(1, './phoebusgen/')
import unittest
from xml.etree.ElementTree import Element, SubElement

class TestGenericPropertyElements(unittest.TestCase):
    def setUp(self):
        self.element = Element('test_root')


class TestColorPropertyElements(unittest.TestCase):
    def setUp(self):
        self.element = Element('test_root')
        self.color_dict = {'activetext': {'red': '255', 'green': '255', 'blue': '0', 'alpha': '255'},
                           'attention': {'red': '255', 'green': '160', 'blue': '0', 'alpha': '255'},
                           'background': {'red': '255', 'green': '255', 'blue': '255', 'alpha': '255'},
                           'button_background': {'red': '210', 'green': '210', 'blue': 210, 'alpha': '255'},
                           'disconnected': {'red': '200', 'green': '0', 'blue': '200', 'alpha': '200'},
                           'grid': {'red': '128', 'green': '128', 'blue': '128', 'alpha': '255'},
                           'header_background': {'red': '77', 'green': '77', 'blue': '77', 'alpha': '255'},
                           'header_foreground': {'red': '255', 'green': '255', 'blue': '255', 'alpha': '255'},
                           'invalid': {'red': '255', 'green': '0', 'blue': '255', 'alpha': '255'},
                           'major': {'red': '255', 'green': '0', 'blue': '0', 'alpha': '255'},
                           'minor': {'red': '255', 'green': '128', 'blue': '0', 'alpha': '255'},
                           'off': {'red': '60', 'green': '100', 'blue': '60', 'alpha': '255'},
                           'ok': {'red': '0', 'green': '255', 'blue': '0', 'alpha': '255'},
                           'on': {'red': '0', 'green': '255', 'blue': '0', 'alpha': '255'},
                           'read_background': {'red': '240', 'green': '240', 'blue': '240', 'alpha': '255'},
                           'stop': {'red': '255', 'green': '0', 'blue': '0', 'alpha': '255'},
                           'text': {'red': '0', 'green': '0', 'blue': '0', 'alpha': '255'},
                           'transparent': {'red': '255', 'green': '255', 'blue': '255', 'alpha': '0'},
                           'write_background': {'red': '128', 'green': '255', 'blue': '255', 'alpha': '255'}}


class TestFontPropertyElements(unittest.TestCase):
    def setUp(self):
        self.element = Element('test_ROOT_tag test')
        self.font_dict = {'comment': {'family': 'Liberation Sans', 'size': '14', 'style': 'Italic'},
                          'default': {'family': 'Liberation Sans', 'size': '14', 'style': 'Regular'},
                          'default bold': {'family': 'Liberation Sans', 'size': '14', 'style': 'Bold'},
                          'fine print': {'family': 'Liberation Sans', 'size': '12', 'style': 'Regular'},
                          'header 1': {'family': 'Liberation Sans', 'size': '22', 'style': 'Bold'},
                          'header 2': {'family': 'Liberation Sans', 'size': '18', 'style': 'Bold'},
                          'header 3': {'family': 'Liberation Sans', 'size': '16', 'style': 'Bold'},
                          'oddball': {'family': 'Liberation Sans', 'size': '40', 'style': 'Regular'}}


if __name__ == '__main__':
    unittest.main()
