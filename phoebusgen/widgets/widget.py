from xml.etree.ElementTree import Element
import phoebusgen
from phoebusgen.properties import HasName, HasVisible, HasPosition, HasActionsRulesAndScripts, HasToolTip
from phoebusgen.utils import prettify_xml

from enum import Enum

class WidgetType(str, Enum):
    """ Enum of Phoebus Widget Types """

    # Graphics
    ARC = "arc"
    ELLIPSE = "ellipse"
    LABEL = "label"
    PICTURE = "picture"
    POLYGON = "polygon"
    POLYLINE = "polyline"
    RECTANGLE = "rectangle"

    # Monitors
    BYTE_MONITOR = "byte_monitor"
    LED = "led"
    MULTI_STATE_LED = "multi_state_led"
    METER = "meter"
    PROGRESS_BAR = "progressbar"
    LINEAR_METER = "linearmeter"
    SYMBOL = "symbol"
    TABLE = "table"
    TANK = "tank"
    TEXT_SYMBOL = "text-symbol"
    TEXT_UPDATE = "textupdate"
    THERMOMETER = "thermometer"

    # Controls
    ACTION_BUTTON = "action_button"
    BOOL_BUTTON = "bool_button"
    CHECKBOX = "checkbox"
    CHOICE = "choice"
    COMBO = "combo"
    FILE_SELECTOR = "fileselector"
    RADIO = "radio"
    SCALED_SLIDER = "scaledslider"
    SCROLLBAR = "scrollbar"
    SLIDE_BUTTON = "slide_button"
    SPINNER = "spinner"
    TEXT_ENTRY = "textentry"
    THUMBWHEEL = "thumbwheel"

    # Plots
    DATABROWSER = "databrowser"
    IMAGE = "image"
    STRIPCHART = "stripchart"
    XYPLOT = "xyplot"

    # Structure
    ARRAY = "array"
    TABS = "tabs"
    EMBEDDED = "embedded"
    GROUP = "group"
    NAVTABS = "navtabs"
    TEMPLATE_INSTANCE = "template"

    # Miscellaneous
    THREED_VIEWER = "3dviewer"
    WEBBROWSER = "webbrowser"


class Widget(HasVisible, HasName, HasPosition, HasActionsRulesAndScripts, HasToolTip):
    """ Base Class for all Phoebus widgets """

    _widget_type: WidgetType | None = None

    def __init__(self, name: str, x_pos: int, y_pos: int, width: int, height: int) -> None:
        """
        Base Class for all Phoebus widgets

        :param w_type: Widget type to be written into XML
        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height:
        """

        if self._widget_type is None:
            raise ValueError("Widget type must be defined in subclass!")
        
        self.root = Element('widget')
        self.root.attrib['type'] = self._widget_type.value
        if self._widget_type in phoebusgen.widget_versions:
            self.root.attrib['version'] = phoebusgen.widget_versions[self._widget_type.value]
        else:
            self.root.attrib['version'] = '2.0.0'

        self.name = name
        self.x = x_pos
        self.y = y_pos
        self.width = width
        self.height = height

    @classmethod
    def from_element(cls, element: Element) -> 'Widget':
        """
        Docstring for from_element
        
        :param cls: Description
        :param element: Description
        :type element: Element
        :return: Description
        :rtype: Widget
        """

        if element.tag != 'widget':
            raise ValueError(f"Expected 'widget' element, got '{element.tag}'")

        w_type = element.attrib.get('type', None)
        if w_type is None:
            raise ValueError("Widget type attribute missing!")
        elif cls._widget_type is None:
            raise ValueError("Instantiating widget base class from XML element is not allowed!")
        if w_type != cls._widget_type.value:
            raise ValueError(f"Expected widget type '{cls._widget_type.value}', got '{w_type}'")

        cls_instance = cls.__new__(cls)
        cls_instance.root = element
        return cls_instance


    def version(self, version: str) -> None:
        """
        Change widget version in root widget. i.e. <widget type="textupdate" version="2.0.0">

        :param version: Version string
        """
        self.root.attrib['version'] = version

    def has_property(self, prop_name: str) -> bool:
        """
        Check if widget has a prop_name

        :param prop_name: Property name to check for
        :return: True if property exists, False if not
        """
        return hasattr(self, prop_name)
    

    def has_property_class(self, prop_class: type) -> bool:
        """
        Check if widget has a property of type prop_class

        :param prop_class: Property class to check for
        :return: True if property class exists, False if not
        """
        return isinstance(self, prop_class)

    def __str__(self):
        return prettify_xml(self.root)

    def __repr__(self):
        return prettify_xml(self.root)
