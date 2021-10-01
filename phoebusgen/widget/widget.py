from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
from phoebusgen._shared_property_helpers import _SharedPropertyFunctions

class _Widget(object):
    """ Base Class for all Phoebus widgets """
    def __init__(self, w_type: str, name: str, x_pos: int, y_pos: int, width: int, height: int) -> None:
        """
        Base Class for all Phoebus widgets

        :param w_type: Widget type to be written into XML
        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height:
        """
        self.root = Element('widget', type=w_type, version='2.0.0')
        name_child = SubElement(self.root, 'name')
        name_child.text = name

        self._shared = _SharedPropertyFunctions(self.root)
        self._shared.integer_property(self.root, 'x', x_pos)
        self._shared.integer_property(self.root, 'y', y_pos)
        self._shared.integer_property(self.root, 'width', width)
        self._shared.integer_property(self.root, 'height', height)

    def visible(self, visible: bool) -> None:
        """
        Change visible property for widget

        :param visible: Is widget visible?
        """
        self._shared.boolean_property(self.root, 'visible', visible)

    def version(self, version: str) -> None:
        """
        Change widget version in root widget. i.e. <widget type="textupdate" version="2.0.0">

        :param version: Version string
        """
        self.root.attrib['version'] = version

    def name(self, name: str) -> None:
        """
        Change widget name

        :param name: Widget name
        """
        self._shared.generic_property(self.root, 'name', name)

    def width(self, width: int) -> None:
        """
        Change widget width

        :param width: Width
        """
        self._shared.integer_property(self.root, 'width', width)

    def height(self, height: int) -> None:
        """
        Change widget height

        :param height: height
        """
        self._shared.integer_property(self.root, 'height', height)

    def x(self, val: int) -> None:
        """
        Change widget x position

        :param val: x
        """
        self._shared.integer_property(self.root, 'x', val)

    def y(self, val: int) -> None:
        """
        Change widget y position

        :param val: y
        """
        self._shared.integer_property(self.root, 'y', val)

    #def class_name(self, name):
    #    pass

    #def rule(self, rule):
    #    pass

    #def scripts(self, script):
    #    pass

    def tool_tip(self, tool_tip: str) -> None:
        """
        Add tool tip string to widget

        :param tool_tip: Tool tip string
        """
        child = SubElement(self.root, 'tooltip')
        child.text = tool_tip

    def find_element(self, tag: str) -> Element:
        """
        Find first XML element in widget by tag name

        :param tag: Tag name to search for
        :return: Return XML element or None if not found
        """
        elements = self.root.findall(tag)
        # check to make sure there are not more than 1 elements
        # we don't want duplicate tags
        if len(elements) > 1:
            print('Warning, more than one element of the same tag! Returning a list')
            return elements
        elif len(elements) == 0:
            return None
        else:
            return elements[0]

    def remove_element(self, tag: str) -> None:
        """
        Delete XML element in widget by tag name

        :param tag: Tag name to delete
        """
        element = self.find_element(tag)
        if element is not None:
            self.root.remove(element)

    def get_element_value(self, tag: str) -> str:
        """
        Get value of an XML element by tag name

        :param tag: Tag name to get value from
        :return: Value of XML tag
        """
        return self.find_element(tag).text

    # From: https://pymotw.com/3/xml.etree.ElementTree/create.html
    def _prettify(self, elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = tostring(elem, 'utf-8')
        reparse_xml = minidom.parseString(rough_string)
        return reparse_xml.toprettyxml(indent="  ", newl="\n")

    def __str__(self):
        return self._prettify(self.root)

    def __repr__(self):
        return self._prettify(self.root)

