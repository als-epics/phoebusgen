from pathlib import Path
from typing import Union
from xml.etree.ElementTree import Element, SubElement

from phoebusgen.v4.properties.property_helpers import PropertyBase
from phoebusgen.v4.properties.types import ObservableList

from .widget import Widget, HasWidgets
from phoebusgen.v4.properties.display import (
    HasPVName,
    HasBackgroundColor,
    HasForegroundColor,
    HasResizeBehavior,
    HasGroupName,
    HasGroupStyle,
    HasSelectedColor,
    HasDeselectedColor,
    HasTabActiveHeightDirection,
    HasTransparent,
    HasFont,
    HasLineColor,
    HasHorizontal,
    HasWrapCount,
    HasGap,
)
from phoebusgen.v4.properties.behavior import HasAlarmBorder
from phoebusgen.v4.properties.widget import HasMacros, HasFile, HasName, HasNavTabs, HasInstances
from phoebusgen.v4.properties.misc import HasBorder

class Array(Widget, HasPVName, HasMacros, HasForegroundColor, HasBackgroundColor, HasAlarmBorder):
    """ Array Phoebus Widget """

    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
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
    """ EmbeddedDisplay Phoebus Widget """

    def __init__(self, name: str, file: Union[Path, str], x: int, y: int, width: int, height: int) -> None:
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
    """ Group Phoebus Widget """

    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Group Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self._override_property_tag_name('widgets', None)

class NavigationTabs(Widget, HasNavTabs, HasSelectedColor, HasDeselectedColor, HasFont):
    """ NavigationTabs Phoebus Widget """

    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
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
    def __init__(self, name: str, root: Element | None = None) -> None:
        """
        Create Tab object for tabs widget

        :param name: Tab name
        :param root: Optional XML element to initialize the tab from
        """
        self.root = root
        if root is None:
            self.root = Element('tab')
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

    tabs: ObservableList[Tab]


class Tabs(Widget, HasTabs, HasMacros, HasTabActiveHeightDirection, HasFont, HasBackgroundColor):
    """ Tabs Phoebus Widget """

    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Tabs Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)


class TemplateInstance(Widget, HasWidgets, HasFile, HasInstances, HasTransparent, HasHorizontal, HasWrapCount, HasGap):
    """ TemplateInstance Phoebus Widget """

    def __init__(self, name: str, file: Union[Path, str], x: int, y: int, width: int, height: int) -> None:
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
