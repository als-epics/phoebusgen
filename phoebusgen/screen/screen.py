from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

# macros, width, height, backgroundcolor, gridvisible, gridcolor, hortizontalstepsize, vertstepsize
class Screen(object):
    def __init__(self, name, f_name=None):
        self.f_name = f_name
        self.root = Element('display', version='2.0.0')
        name_child = SubElement(self.root, 'name')
        name_child.text = name

    def write_screen(self):
        rough_string = tostring(self.root, 'utf-8')
        reparse_xml = minidom.parseString(rough_string)
        if self.f_name == None:
            return False
        else:
            with open(self.f_name, 'w') as f:
                reparse_xml.writexml(f, indent="  ", addindent="  ", newl="\n", encoding="UTF-8")
            return True

    def add_widget(self, elem):
        if type(elem) == list:
            for e in elem:
                self.root.append(e.root)
        else:
            self.root.append(elem.root)

    def _number_property(self, prop_type, val):
        if type(val) == int or type(val) == float:
            child = SubElement(self.root, prop_type)
            child.text = str(int(val))
        else:
            print('Property {} must be a number! Not: {}'.format(prop_type, val))

    def width(self, val):
        self._number_property('width', val)

    def height(self, val):
        self._number_property('height', val)

    def macro(self, name, val):
        root_macro = self.root.find('macros')
        if root_macro is None:
            root_macro = SubElement(self.root, 'macros')
        macro = SubElement(root_macro, name)
        macro.text = str(val)

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

    def _color_element(self, elem, name, red, green, blue, alpha):
        sub_e = Element('color')
        if name is None:
            for color in [red, green, blue, alpha]:
                if not self.valid_rgb_value(color):
                    return
            sub_e.attrib = {'red': str(red), 'blue': str(blue), 'green': str(green), 'alpha': str(alpha)}
        elem.append(sub_e)
        self.root.append(elem)

    def background_color(self, red, green, blue, alpha=255):
        root_elem = Element('background_color')
        self._color_element(root_elem, None, red, green, blue, alpha)

    # this is all duplicated. Should pull out dup code in widget/property.py into shared file
    #def predefined_background_color(self, name):
    #    e = self.root.append('background_color')
    #    self._color_element(e, name, None, None, None, None)

    # From: https://pymotw.com/3/xml.etree.ElementTree/create.html
    def prettify(self, elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = tostring(elem, 'utf-8')
        reparse_xml = minidom.parseString(rough_string)
        return reparse_xml.toprettyxml(indent="  ", newl="\n")

    def __str__(self):
        return self.prettify(self.root)




if __name__ == '__main__':
    s = Screen('DisplayTest')
