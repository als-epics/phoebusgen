from typing import Type, TypeVar
from xml.dom import minidom
from xml.etree.ElementTree import Element, fromstring, tostring


def prettify_xml(elem):
    """Return a pretty-printed XML string for the Element.
        From: https://pymotw.com/3/xml.etree.ElementTree/create.html
    """
    rough_string = tostring(elem, 'utf-8')
    reparse_xml = minidom.parseString(rough_string)
    return reparse_xml.toprettyxml(indent='  ', newl='\n')


def _elements_equal(e1: Element, e2: Element) -> bool:
    """Recursively compare two XML elements, ignoring attribute order."""
    if e1.tag != e2.tag:
        return False
    if (e1.text or '').strip() != (e2.text or '').strip():
        return False
    if (e1.tail or '').strip() != (e2.tail or '').strip():
        return False
    if e1.attrib != e2.attrib:
        return False
    if len(e1) != len(e2):
        return False
    return all(_elements_equal(c1, c2) for c1, c2 in zip(e1, e2))


PhoebusElementT = TypeVar('PhoebusElementT', bound='PhoebusElement')

class PhoebusElement:
    """Base class for all Phoebus elements, including screens, widgets, and properties.

    Attributes
    ----------
    root : Element
        The XML element that represents this PhoebusElement object.
    """

    root: Element

    def __init__(self, root: Element) -> None:
        self.root = root

    def __str__(self):
        return prettify_xml(self.root)

    def __repr__(self):
        return prettify_xml(self.root)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, PhoebusElement):
            return _elements_equal(self.root, other.root)
        if isinstance(other, str):
            xml_str = other.strip()
            if xml_str.startswith('<?xml'):
                xml_str = xml_str.split('?>', 1)[1].strip()
            return _elements_equal(self.root, fromstring(xml_str))
        return NotImplemented

    @classmethod
    def from_element(cls: Type[PhoebusElementT], element: Element) -> PhoebusElementT:
        """Create a PhoebusElement from an XML Element.

        :param element: XML Element to create from
        :return: PhoebusElement instance
        """
        return cls(element)
