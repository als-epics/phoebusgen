from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
from phoebusgen._shared_property_helpers import _SharedPropertyFunctions
from typing import Union


class Screen(object):
    """ Phoebus Screen object that holds widgets and can be written to .bob file """
    def __init__(self, name: str, f_name: str = None) -> None:
        """
        Create Phoebus screen object. File name is optional and can be specified later

        :param name: Screen Name
        :param f_name: File name for Phoebus screen
        """
        self.bob_file = f_name
        self.root = Element('display', version='2.0.0')
        name_child = SubElement(self.root, 'name')
        name_child.text = name
        self._shared = _SharedPropertyFunctions(self.root)

    def write_screen(self, file_name: str = None) -> bool:
        """
        Writes screen XML to file. File name parameter is optional, if not given Screen bob_file member will be used

        :param file_name: File name to write to
        :return: True is successful write, False otherwise
        """
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

    def find_widget(self, widget_tag_name: str) -> Element:
        """
        Find widget in the screen

        :param widget_tag_name: Tag name of widget to find
        :return: None if not found or widget that was found
        """
        elements = self.root.findall(widget_tag_name)
        if len(elements) > 1:
            print('Warning, more than one element of the same tag! Returning a list')
            return elements
        elif len(elements) == 0:
            return None
        else:
            return elements[0]

    def add_widget(self, elem: Union[list, object]) -> None:
        """
        Add widget or list of widgets to screen

        :param elem: <list/Phoebusgen.widget> List of Phoebusgen.widget's or a single widget to add
        """
        if type(elem) == list:
            for e in elem:
                self.root.append(e.root)
        else:
            self.root.append(elem.root)

    def width(self, val: int) -> None:
        """
        Change width of screen

        :param val: Screen width
        """
        self._shared.number_property(self.root, 'width', val)

    def height(self, val: int) -> None:
        """
        Change height of screen

        :param val: Screen height
        """
        self._shared.number_property(self.root, 'height', val)

    def macro(self, name: str, val: Union[str, int, float]) -> None:
        """
        Add macro to screen

        :param name: Macro name
        :param val: Macro value
        """
        self._shared.add_macro(name, val)

    def background_color(self, red: int, green: int, blue: int, alpha: int = 255) -> None:
        """
        Add background color to screen RGB values

        :param red: 0-255
        :param green: 0-255
        :param blue: 0-255
        :param alpha: 0-255. Default is 255
        """
        e = self._shared.create_element(self.root, 'background_color')
        self._shared.create_color_element(e, None, red, green, blue, alpha)

    def predefined_background_color(self, name: object) -> None:
        """
        Add named background color to screen

        :param name: <Phoebusgen.colors> Predefined color name
        """
        e = self._shared.create_element(self.root, 'background_color')
        self._shared.create_color_element(e, name, None, None, None, None)

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
