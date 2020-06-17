from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
from _property import Property


# TO DO : move macros out of widget class
# TO DO : Add rest of global properties - class, tool tip, actions, rules, scripts
class Widget(object):
    def __init__(self, w_type, name, x_pos, y_pos, width, height, macro_list=None):
        self.root = Element('widget', type=w_type, version='2.0.0')
        name_child = SubElement(self.root, 'name')
        name_child.text = name

        x_child = SubElement(self.root, 'x')
        x_child.text = str(x_pos)

        y_child = SubElement(self.root, 'y')
        y_child.text = str(y_pos)

        width_child = SubElement(self.root, 'width')
        width_child.text = str(width)

        height_child = SubElement(self.root, 'height')
        height_child.text = str(height)

        self.prop_factory = Property(self.root)

        if macro_list is None:
            self.macro_elem = None
        else:
            for m in macro_list:
                self.add_macro(m['name'], m['val'])

    def set_visible(self, visible):
        child = SubElement(self.root, 'visible')
        child.text = str(visible)

    def add_macro(self, name, val):
        if self.macro_elem is None:
            self.macro_elem = SubElement(self.root, 'macros')
        macro = SubElement(self.macro_elem, name)
        macro.text = val

    def find_element(self, tag):
        element = self.root.find(tag)
        return element

    def remove_element(self, tag):
        element = self.find_element(tag)
        if element is not None:
            self.root.remove(element)

    # From: https://pymotw.com/3/xml.etree.ElementTree/create.html
    def prettify(self, elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = tostring(elem, 'utf-8')
        reparse_xml = minidom.parseString(rough_string)
        return reparse_xml.toprettyxml(indent="  ", newl="\n")

    def print_widget(self):
        print(self.prettify(self.root))


if __name__ == '__main__':
    pass
