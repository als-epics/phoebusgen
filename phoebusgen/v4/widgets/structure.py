from pathlib import Path
from typing import List, Optional, Union
from xml.etree.ElementTree import Element, SubElement

from phoebusgen.v4.properties.behavior import HasAlarmBorder
from phoebusgen.v4.properties.display import (
    HasBackgroundColor,
    HasDeselectedColor,
    HasFont,
    HasForegroundColor,
    HasGap,
    HasGroupName,
    HasGroupStyle,
    HasHorizontal,
    HasLineColor,
    HasResizeBehavior,
    HasSelectedColor,
    HasTabActiveHeightDirection,
    HasTransparent,
    HasWrapCount,
)
from phoebusgen.v4.properties.misc import HasBorder
from phoebusgen.v4.properties.property_helpers import PropertyBase
from phoebusgen.v4.properties.types import Color
from phoebusgen.v4.properties.widget import (
    HasFile,
    HasInstances,
    HasMacros,
    HasName,
    HasNavTabs,
    HasPVName
)

from .widget import HasWidgets, Widget, STANDARD_TOOLTIP


class Array(Widget, HasPVName, HasMacros, HasForegroundColor, HasBackgroundColor, HasAlarmBorder):
    """Array Phoebus Widget"""

    tooltip: str = STANDARD_TOOLTIP
    height: int = 300

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 100, height: int = 300) -> None:
        """
        Create Array Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class EmbeddedDisplay(Widget, HasMacros, HasFile, HasResizeBehavior, HasGroupName, HasTransparent, HasBorder):
    """EmbeddedDisplay Phoebus Widget"""

    width: int = 400
    height: int = 300

    def __init__(self, name: str = '', file: Optional[Union[Path, str]] = '', x: int = 0, y: int = 0, width: int = 400, height: int = 300) -> None:
        """
        Create EmbeddedDisplay Widget

        :param name: Widget name
        :param file: File path
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.file = file

class Group(Widget, HasWidgets, HasMacros, HasGroupStyle, HasFont, HasForegroundColor, HasBackgroundColor, HasTransparent, HasLineColor):
    """Group Phoebus Widget"""

    width: int = 300
    height: int = 200

    def __init__(self, name: str = '', x: int = 0, y: int = 0, width: int = 300, height: int = 200) -> None:
        """
        Create Group Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)

# Group widgets store child <widget> elements directly under the group root,
# not inside a <widgets> wrapper. Set this at class level so it works even
# when instances are created via from_element (which bypasses __init__).
Group._override_property_tag_name('widgets', None)


class NavigationTabs(Widget, HasNavTabs, HasSelectedColor, HasDeselectedColor, HasFont):
    """NavigationTabs Phoebus Widget"""

    selected_color: Color = Color((236, 236, 236))
    deselected_color: Color = Color((200, 200, 200))
    width: int = 500
    height: int = 300

    def __init__(self, name: str = '', x: int = 0, y: int = 0, width: int = 500, height: int = 300) -> None:
        """
        Create NavigationTabs Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)


class Tab(HasWidgets, HasName):
    """Tab object for tabs widget"""
    def __init__(self, name: str, root: Optional[Element] = None) -> None:
        """
        Create Tab object for tabs widget

        :param name: Tab name
        :param root: Optional XML element to initialize the tab from
        """
        if root is None:
            self.root = Element('tab')
        else:
            self.root = root
        self.name = name

        children_elem = self.root.find('children')
        if children_elem is None:
            children_elem = SubElement(self.root, 'children')

        HasTabs.__init__(self)
        HasWidgets.__init__(self, widgets_tag_name='children')

    @classmethod
    def from_element(cls, element: Element) -> 'Tab':
        """Convert an XML element into a Tab instance.

        :param cls: The Tab class
        :param element: The XML element to convert
        :type element: Element
        :return: A Tab instance
        :rtype: Tab
        """

        if element.tag != 'tab':
            raise ValueError(f"Expected 'tab' element, got '{element.tag}'")

        name_element = element.find('name')
        if name_element is None or name_element.text is None:
            raise ValueError("Tab element missing 'name' subelement or name text!")

        tab = cls(name_element.text, root=element)

        return tab


class HasTabs(PropertyBase):
    """Interface for widgets that contain tabs that contain other widgets"""

    tabs: List[Tab]


class Tabs(Widget, HasTabs, HasMacros, HasTabActiveHeightDirection, HasFont, HasBackgroundColor):
    """Tabs Phoebus Widget"""

    width: int = 400
    height: int = 300

    def __init__(self, name: str = '', x: int = 0, y: int = 0, width: int = 400, height: int = 300) -> None:
        """
        Create Tabs Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)


class TemplateInstance(Widget, HasWidgets, HasMacros, HasFile, HasInstances, HasTransparent, HasHorizontal, HasWrapCount, HasGap):
    """TemplateInstance Phoebus Widget"""

    horizontal: bool = False
    width: int = 400
    height: int = 300

    def __init__(self, name: str = '', file: Optional[Union[Path, str]] = '', x: int = 0, y: int = 0, width: int = 400, height: int = 300) -> None:
        """
        Create TemplateInstance Widget

        :param name: Widget name
        :param file: File path
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.file = file
