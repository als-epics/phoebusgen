from xml.etree.ElementTree import Element, SubElement
from enum import Enum

class _SharedPropertyFunctions(object):
    def __init__(self, root_element):
        self.root = root_element
        from phoebusgen import colors, _predefined_colors, fonts, _predefined_fonts
        self.predefined_colors = _predefined_colors
        self.predefined_fonts = _predefined_fonts
        self.colors = colors
        self.fonts = fonts

    def add_macro(self, name, val):
        root_macro = self.root.find('macros')
        if root_macro is None:
            root_macro = SubElement(self.root, 'macros')
        macro = SubElement(root_macro, name)
        macro.text = str(val)

    def generic_property(self, prop_type, val=None):
        self.root.append(self.create_element(prop_type, val))

    def integer_property(self, prop_type, val=None):
        if type(val) == int or type(val) == float:
            self.generic_property(prop_type, int(val))
        else:
            print('Property {} must be an integer! Not: {}'.format(prop_type, val))

    def number_property(self, prop_type, val):
        if type(val) == int or type(val) == float:
            self.generic_property(prop_type, val)
        else:
            print('Property {} must be a number! Not: {}'.format(prop_type, val))

    def boolean_property(self, prop_type, val):
        if type(val) == bool:
            self.generic_property(prop_type, str(val).lower())
        elif type(val) == int:
            self.generic_property(prop_type, str(bool(val)).lower())
        elif val.lower() == 'true' or val.lower() == 'false':
            self.generic_property(prop_type, val.lower())
        else:
            print('Property {} must be a boolean value! Not: {}'.format(prop_type, val))

    def create_element(self, prop_type, val=None):
        element = self.root.find(prop_type)
        if element is not None:
            self.root.remove(element)
        element = Element(prop_type)
        if val is not None:
            if type(val) == bool:
                element.text = str(val).lower()
            else:
                element.text = str(val)
        return element

    def valid_rgb_value(self, val):
        try:
            val = int(val)
        except ValueError:
            print('Color RGB value must be a number! Not: {}'.format(val))
            return False
        if 0 <= val <= 255:
            return True
        else:
            print('Color RGB must be between 0 and 255')
            return False

    def create_color_element(self, root_color_elem, name, red, green, blue, alpha):
        sub_e = self.create_element('color')
        if name is None:
            for color in [red, green, blue, alpha]:
                if not self.valid_rgb_value(color):
                    return
            sub_e.attrib = {'red': str(red), 'blue': str(blue), 'green': str(green), 'alpha': str(alpha)}
        else:
            if isinstance(name, Enum):
                sub_e.attrib['name'] = name.name
                sub_e.attrib = name.value
            elif isinstance(name, dict):
                sub_e.attrib = name
            elif isinstance(name, str):
                color_attrib = self.predefined_colors.get(name)
                if color_attrib is None:
                    print('Color name is undefined')
                    return
                sub_e.attrib = color_attrib
                sub_e.attrib['name'] = name
            else:
                print('Predefined color input must be phoebusgen.colors.<named-color>, not: {} of type: {}'.format(name, type(name)))
                return
        root_color_elem.append(sub_e)
        self.root.append(root_color_elem)

    def create_named_font_elemet(self, name):
        root_font_elem = self.create_element('font')
        child_font_elem = self.create_element('font')
        if isinstance(name, Enum):
            font_attrib = name.value
        elif isinstance(name, dict):
            font_attrib = name
        elif isinstance(name, str):
            font_attrib = self.predefined_fonts.get(name.lower())
            if font_attrib is None:
                print('Font name is undefined')
                return
            font_attrib['style'] = font_attrib['style'].upper()
        else:
            print('Predefined font input must be phoebusgen.fonts.<named-color>, not: {} of type: {}'.format(name, type(name)))
            return
        child_font_elem.attrib = font_attrib
        root_font_elem.append(child_font_elem)
        self.root.append(root_font_elem)

if __name__ == '__main__':
    pass
