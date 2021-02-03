from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
from phoebusgen._shared_property_helpers import _SharedPropertyFunctions


class Screen(object):
    def __init__(self, name, f_name=None):
        self.bob_file = f_name
        self.root = Element('display', version='2.0.0')
        name_child = SubElement(self.root, 'name')
        name_child.text = name
        self.shared_functions = _SharedPropertyFunctions(self.root)

    def write_screen(self, file_name=None):
        rough_string = tostring(self.root, 'utf-8')
        reparse_xml = minidom.parseString(rough_string)
        if file_name is None:
            file_name = self.bob_file
        if file_name is None:
            print('Output Phoebus file name is not set! First set bob_file or use file_name parameter')
            return False
        else:
            with open(file_name, 'w') as f:
                reparse_xml.writexml(f, indent="  ", addindent="  ", newl="\n", encoding="UTF-8")
            return True

    def find_widget(self, widget_tag_name):
        elements = self.root.findall(widget_tag_name)
        if len(elements) > 1:
            print('Warning, more than one element of the same tag! Returning a list')
            return elements
        elif len(elements) == 0:
            return None
        else:
            return elements[0]

    def add_widget(self, elem):
        if type(elem) == list:
            for e in elem:
                self.root.append(e.root)
        else:
            self.root.append(elem.root)

    def width(self, val):
        self.shared_functions.number_property('width', val)

    def height(self, val):
        self.shared_functions.number_property('height', val)

    def macro(self, name, val):
        self.shared_functions.add_macro(name, val)

    def background_color(self, red, green, blue, alpha=255):
        e = self.shared_functions.create_element('background_color')
        self.shared_functions.create_color_element(e, None, red, green, blue, alpha)

    def predefined_background_color(self, name):
        e = self.shared_functions.create_element('background_color')
        self.shared_functions.create_color_element(e, name, None, None, None, None)

    # From: https://pymotw.com/3/xml.etree.ElementTree/create.html
    def prettify(self, elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = tostring(elem, 'utf-8')
        reparse_xml = minidom.parseString(rough_string)
        return reparse_xml.toprettyxml(indent="  ", newl="\n")

    def __str__(self):
        return self.prettify(self.root)

    def __repr__(self):
        return self.prettify(self.root)


if __name__ == '__main__':
    s = Screen('DisplayTest')
