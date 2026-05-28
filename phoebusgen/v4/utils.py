from typing import Type, TypeVar
from xml.dom import minidom
from xml.etree.ElementTree import Element, tostring


def prettify_xml(elem):
    """Return a pretty-printed XML string for the Element.
        From: https://pymotw.com/3/xml.etree.ElementTree/create.html
    """
    rough_string = tostring(elem, 'utf-8')
    reparse_xml = minidom.parseString(rough_string)
    return reparse_xml.toprettyxml(indent='  ', newl='\n')


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
        if not isinstance(other, PhoebusElement):
            return False
        return prettify_xml(self.root) == prettify_xml(other.root)

    @classmethod
    def from_element(cls: Type[PhoebusElementT], element: Element) -> PhoebusElementT:
        """Create a PhoebusElement from an XML Element.

        :param element: XML Element to create from
        :return: PhoebusElement instance
        """
        return cls(element)
