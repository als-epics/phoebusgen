from .widget import Widget
from phoebusgen.properties import (
    HasName,
    HasMacros,
    HasBackgroundColor,
    HasAlarmBorder,
    HasForegroundColor,
    HasFile,
    HasBorder,
    HasResizeBehavior,
    HasGroupName,
    HasStructure,
    HasStyle,
    HasTabs,
    HasActiveTab,
    HasTabWidth,
    HasTabSpacing,
    HasTabHeight,
    HasSelectedColor,
    HasDeselectedColor,
    HasTransparent,
    HasFont,
    HasLineColor,
    HasDirection,
)

class Array(Widget, HasName, HasMacros, HasForegroundColor, HasBackgroundColor, HasAlarmBorder):
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
        Widget.__init__(self, 'array', name, x, y, width, height)
        self.pv_name = pv_name

class EmbeddedDisplay(Widget, HasMacros, HasFile, HasResizeBehavior, HasGroupName, HasTransparent, HasBorder):
    """ EmbeddedDisplay Phoebus Widget """
    def __init__(self, name: str, file: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create EmbeddedDisplay Widget

        :param name: Widget name
        :param file: File path
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, 'embedded', name, x, y, width, height)
        self.file = file

class Group(Widget, HasStructure, HasMacros, HasStyle, HasFont, HasForegroundColor, HasBackgroundColor, HasTransparent,
            HasLineColor):
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
        Widget.__init__(self, 'group', name, x, y, width, height)

class NavigationTabs(Widget, HasTabs, HasActiveTab, HasTabWidth, HasTabSpacing, HasTabHeight,
                     HasSelectedColor, HasDeselectedColor, HasDirection, HasFont):
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
        Widget.__init__(self, 'navtabs', name, x, y, width, height)

class Tabs(Widget, HasMacros, HasTabs, HasActiveTab, HasTabHeight, HasFont, HasBackgroundColor, HasDirection):
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
        Widget.__init__(self, 'tabs', name, x, y, width, height)
