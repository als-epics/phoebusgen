from .widget import WidgetType, Widget
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
    HasGroupStyle,
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
    HasTabDirection,
)

class Array(Widget, HasName, HasMacros, HasForegroundColor, HasBackgroundColor, HasAlarmBorder):
    """ Array Phoebus Widget """

    _widget_type: WidgetType = WidgetType.ARRAY

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

    _widget_type: WidgetType = WidgetType.EMBEDDED

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
        Widget.__init__(self, name, x, y, width, height)
        self.file = file

class Group(Widget, HasMacros, HasGroupStyle, HasFont, HasForegroundColor, HasBackgroundColor, HasTransparent,
            HasLineColor):
    """ Group Phoebus Widget """

    _widget_type: WidgetType = WidgetType.GROUP

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

class NavigationTabs(Widget, HasTabs, HasActiveTab, HasTabWidth, HasTabSpacing, HasTabHeight,
                     HasSelectedColor, HasDeselectedColor, HasTabDirection, HasFont):
    """ NavigationTabs Phoebus Widget """

    _widget_type: WidgetType = WidgetType.NAVTABS

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

class Tabs(Widget, HasMacros, HasTabs, HasActiveTab, HasTabHeight, HasFont, HasBackgroundColor, HasTabDirection):
    """ Tabs Phoebus Widget """

    _widget_type: WidgetType = WidgetType.TABS

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
