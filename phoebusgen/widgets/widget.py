from xml.etree.ElementTree import Element, SubElement
import phoebusgen
from phoebusgen.properties import HasName, HasX, HasY, HasWidth, HasHeight, HasVisible
from phoebusgen.properties.property_helpers import PropertyBase
from phoebusgen.utils import prettify_xml

from enum import Enum

class WidgetType(str, Enum):
    """ Enum of Phoebus Widget Types """

    # Base class
    BASE = "base"

    # Graphics
    ARC = "arc"
    ELLIPSE = "ellipse"
    LABEL = "label"
    # Graphics
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
    TEMPLATE = "template"

    # Miscellaneous
    THREED_VIEWER = "3dviewer"
    WEBBROWSER = "webbrowser"


class Widget(HasVisible, HasName, HasX, HasY, HasWidth, HasHeight):
    """ Base Class for all Phoebus widgets """

    _widget_type: WidgetType = WidgetType.BASE

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
            raise ValueError("Widget type not defined in subclass!")
        
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
    def supported_properties(cls) -> list[type[PropertyBase]]:
        """
        Get list of supported properties for this widget

        :return: List of supported property classes
        """
        return list(cls._all_properties.keys())

    @classmethod
    def supported_property_names(cls) -> list[str]:
        return [name for name, _ in cls._all_properties.values()]

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
        elif cls._widget_type is WidgetType.BASE:
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


    def rule(self, name: str, widget_property: str, pv_dict: dict,
             expression_dict: dict, value_as_expression: bool = False) -> None:
        """
        Add a rule to the widget to control a property based on some logic

        :param name: Name of the rule
        :param widget_property: Property for rule to control, i.e. name, foreground_color, etc.
        :param pv_dict: Dictionary of PVs for the rule, format - { pvName: triggerOnPV }
        :param expression_dict: Dictionary of expressions for the rules, format - { boolean expression : value }
        :param value_as_expression: Defaults to False. If True, use value as expression
        """
        root_rules = self.root.find('rules')
        if root_rules is None:
            root_rules = SubElement(self.root, 'rules')
        root_rule = SubElement(root_rules, 'rule')
        root_rule.attrib['name'] = name
        root_rule.attrib['prop_id'] = widget_property
        if value_as_expression is True:
            root_rule.attrib['out_exp'] = 'true'
        else:
            root_rule.attrib['out_exp'] = 'false'
        if expression_dict is not None:
            for expression, value in expression_dict.items():
                expression_element = SubElement(root_rule, 'exp', {'bool_exp': expression})
                if value_as_expression is True:
                    val_as_exp_element = SubElement(expression_element, 'expression')
                    val_as_exp_element.text = str(value)
                else:
                    val_element = SubElement(expression_element, 'value')
                    if 'color' in widget_property:
                        name = None
                        red = None
                        green = None
                        blue = None
                        alpha = None

                        # red, green, blue, alpha entered in a tuple (R,G,B,A)
                        # alpha optional (defaults to 255)
                        if str(type(value)) == "<class 'tuple'>":
                            red = value[0]
                            green = value[1]
                            blue = value[2]
                            alpha = '255'

                            if len(value) == 4:
                                alpha = value[3]

                        else: # predefined colors
                            name = str(value)
                        self._shared.create_color_element(val_element, name, red, green, blue, alpha, False)
                    else:
                        val_element.text = str(value)
        if pv_dict is not None:
            for pv, trigger in pv_dict.items():
                pv_element = SubElement(root_rule, 'pv_name', {'trigger': str(trigger).lower()})
                pv_element.text = pv

    def _script(self, file_name, script_contents, pv_dict, only_trigger_if_connected):
        root_scripts = self.root.find('scripts')
        if root_scripts is None:
            root_scripts = SubElement(self.root, 'scripts')
        root_script = SubElement(root_scripts, 'script')
        root_script.attrib['file'] = file_name
        if only_trigger_if_connected is False:
            root_script.attrib['check_connections'] = 'false'
        if script_contents is not None:
            # self._shared.generic_property(root_script, 'text', "<![CDATA[" + python_script + "]]>")
            # from what I can tell, Phoebus will automatically add <![CDATA[ ... ]]> after saving in editor
            self._shared.generic_property(root_script, 'text', script_contents)
        if pv_dict is not None:
            for pv, trigger in pv_dict.items():
                pv_element = SubElement(root_script, 'pv_name', {'trigger': str(trigger).lower()})
                pv_element.text = pv

    def embedded_python_script(self, python_script: str, pv_dict: dict, only_trigger_if_connected: bool = True) -> None:
        """
        Add an embedded Jython (Python) script to the widget

        :param python_script: Usually multi-line string representing the actual python code to attach to widget
        :param pv_dict: Dictionary of PVs for the script, format - { pvName: triggerOnPV }
        :param only_trigger_if_connected: Defaults to True. If False, script will run even if PVs are not connected
        """
        file_name = 'EmbeddedPy'
        self._script(file_name, python_script, pv_dict, only_trigger_if_connected)

    def embedded_javascript_script(self, js_script: str, pv_dict: dict, only_trigger_if_connected: bool = True) -> None:
        """
        Add an embedded JS script to the widget

        :param js_script: Usually multi-line string representing the actual JS code to attach to widget
        :param pv_dict: Dictionary of PVs for the script, format - { pvName: triggerOnPV }
        :param only_trigger_if_connected: Defaults to True. If False, script will run even if PVs are not connected
        """
        file_name = 'EmbeddedJs'
        self._script(file_name, js_script, pv_dict, only_trigger_if_connected)

    def external_script(self, file_name: str, pv_dict: dict, only_trigger_if_connected: bool = True) -> None:
        """
        Add an external script to the widget, either jython (.py) or javascript (.js)

        :param file_name: Path and file name of the external script to attach to widget
        :param pv_dict: Dictionary of PVs for the script, format - { pvName: triggerOnPV }
        :param only_trigger_if_connected: Defaults to True. If False, script will run even if PVs are not connected
        """
        self._script(file_name, None, pv_dict, only_trigger_if_connected)

    def has_property(self, prop_cls: type) -> bool:
        """
        Check if widget has a property

        :param prop_cls: Property class to check for
        :return: True if property exists, False if not
        """
        if isinstance(self, prop_cls):
            return True
        return False

    def __str__(self):
        return prettify_xml(self.root)

    def __repr__(self):
        return prettify_xml(self.root)
