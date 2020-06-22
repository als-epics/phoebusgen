from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
from phoebusgen.widget._property import Property


class Widget(object):
    def __init__(self, w_type, name, x_pos, y_pos, width, height):
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

    def visible(self, visible):
        child = SubElement(self.root, 'visible')
        child.text = str(visible)

    def class_name(self, name):
        pass

    def rule(self, rule):
        pass

    def scripts(self, script):
        pass

    def tool_tip(self, tool_tip):
        child = SubElement(self.root, 'tooltip')
        child.text = tool_tip

    def find_element(self, tag):
        element = self.root.find(tag)
        return element

    def remove_element(self, tag):
        element = self.find_element(tag)
        if element is not None:
            self.root.remove(element)

    def get_element_value(self, tag):
        return self.find_element(tag).text

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
    pass
