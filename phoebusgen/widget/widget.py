from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
from phoebusgen._shared_property_helpers import _SharedPropertyFunctions


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
        From: https://pymotw.com/3/xml.etree.ElementTree/create.html
    """
    rough_string = tostring(elem, 'utf-8')
    reparse_xml = minidom.parseString(rough_string)
    return reparse_xml.toprettyxml(indent="  ", newl="\n")


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
            root_rule.attrib['out_exp'] = "true"
        else:
            root_rule.attrib['out_exp'] = "false"
        if expression_dict is not None:
            for expression, value in expression_dict.items():
                print(expression, value)
                expression_element = SubElement(root_rule, 'exp', {'bool_exp': expression})
                if value_as_expression is True:
                    val_as_exp_element = SubElement(expression_element, 'expression')
                    val_as_exp_element.text = value
                else:
                    val_element = SubElement(expression_element, 'value')
                    val_element.text = value
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
        file_name = "EmbeddedPy"
        self._script(file_name, python_script, pv_dict, only_trigger_if_connected)

    def embedded_javascript_script(self, js_script: str, pv_dict: dict, only_trigger_if_connected: bool = True) -> None:
        """
        Add an embedded JS script to the widget

        :param js_script: Usually multi-line string representing the actual JS code to attach to widget
        :param pv_dict: Dictionary of PVs for the script, format - { pvName: triggerOnPV }
        :param only_trigger_if_connected: Defaults to True. If False, script will run even if PVs are not connected
        """
        file_name = "EmbeddedJs"
        self._script(file_name, js_script, pv_dict, only_trigger_if_connected)

    def external_script(self, file_name: str, pv_dict: dict, only_trigger_if_connected: bool = True) -> None:
        """
        Add an external script to the widget, either jython (.py) or javascript (.js)

        :param file_name: Path and file name of the external script to attach to widget
        :param pv_dict: Dictionary of PVs for the script, format - { pvName: triggerOnPV }
        :param only_trigger_if_connected: Defaults to True. If False, script will run even if PVs are not connected
        """
        self._script(file_name, None, pv_dict, only_trigger_if_connected)

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


    def __str__(self):
        return prettify(self.root)

    def __repr__(self):
        return prettify(self.root)

