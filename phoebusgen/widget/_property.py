from xml.etree.ElementTree import Element, SubElement
import yaml
import os


# TO DO : Add check if property is already available
# TO DO : Add way to specify defaults in a config file
# TO DO : Default property value should delete element (can use remove element with self.root)
class Property(object):
    def __init__(self, root_element):
        self.root = root_element
        curr_path = os.path.dirname(__file__)
        with open(curr_path + '/colors.yaml') as f:
            self.predefined_colors = yaml.safe_load(f)
        with open(curr_path + '/fonts.yaml') as f:
            self.predefined_fonts = yaml.safe_load(f)

    def generic_property(self, prop_type, val=None):
        self.root.append(self.create_element(prop_type, val))

    def create_element(self, prop_type, val=None):
        element = Element(prop_type)
        if val is not None:
            element.text = str(val)
        return element

    def add_pv_name(self, name):
        self.generic_property('pv_name', name)

    def add_precision(self, val):
        self.generic_property('precision', val)

    def add_show_units(self, show):
        self.generic_property('show_units', show)

    def add_wrap_words(self, wrap):
        self.generic_property('wrap_words', wrap)

    def add_transparent(self, transparent):
        self.generic_property('transparent', transparent)

    def add_horizontal_alignment(self, val):
        if val.lower() == 'left':
            v = 0
        elif val.lower() == 'center':
            v = 1
        elif val.lower() == 'right':
            v = 2
        else:
            print('Wrong input to horizontal alignment: {}. Must be Left, Center, or Right'.format(val))
            return
        self.generic_property('horizontal_alignment', v)

    def add_vertical_alignment(self, val):
        if val.lower() == 'top':
            v = 0
        elif val.lower() == 'middle':
            v = 1
        elif val.lower() == 'bottom':
            v = 2
        else:
            print('Wrong input to vertical alignment: {}. Must be Top, Middle, or Bottom'.format(val))
            return
        self.generic_property('vertical_alignment', v)

    def create_color_element(self, root_color_elem, name, red, green, blue, alpha):
        sub_e = self.create_element('color')
        if name is None:
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

    def add_background_color(self, name, red, green, blue, alpha):
        e = self.create_element('background_color')
        self.create_color_element(e, name, red, green, blue, alpha)

    def add_foreground_color(self, name, red, green, blue, alpha):
        e = self.create_element('foreground_color')
        self.create_color_element(e, name, red, green, blue, alpha)

    def add_font(self, family, style, size, name):
        e = self.create_element('font')
        if name is not None:
            font_attrib = self.predefined_fonts.get(name.lower())
            if font_attrib is None:
                print('Font name is wrong')
                return
        else:
            font_attrib = {}
            font_attrib['family'] = 'Liberation Sans' if family is None else family
            font_attrib['style'] = 'Regular' if style is None else style
            font_attrib['size'] = '14' if size is None else str(size)
        SubElement(e, 'font', attrib=font_attrib)
        self.root.append(e)


