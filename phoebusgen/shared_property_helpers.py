from xml.etree.ElementTree import Element, SubElement
import os
import yaml

class SharedPropertyFunctions(object):
    def __init__(self, root_element):
        self.root = root_element
        curr_path = os.path.dirname(__file__)
        with open(curr_path + '/widget/colors.yaml') as f:
            self.predefined_colors = yaml.safe_load(f)
        with open(curr_path + '/widget/fonts.yaml') as f:
            self.predefined_fonts = yaml.safe_load(f)

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
            color_list = self.predefined_colors.get(name.lower())
            if color_list is None:
                print('Color name is undefined')
                return
            else:
                sub_e.attrib = color_list
                sub_e.attrib['name'] = name
        root_color_elem.append(sub_e)
        self.root.append(root_color_elem)



if __name__ == '__main__':
    pass