from .widget import Widget, WidgetContainer
from phoebusgen.v4.properties.display import (
    HasPVName,
    HasBackgroundColor,
    HasAlarmBorder,
    HasForegroundColor,
    HasResizeBehavior,
    HasGroupName,
    HasGroupStyle,
    HasSelectedColor,
    HasDeselectedColor,
    HasTransparent,
    HasFont,
    HasLineColor,
    HasHorizontal,
    HasWrapCount,
    HasGap,
)
from phoebusgen.v4.properties.widget import HasMacros, HasFile, HasTabs, HasInstances
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

class Group(Widget, WidgetContainer, HasMacros, HasGroupStyle, HasFont, HasForegroundColor, HasBackgroundColor, HasTransparent, HasLineColor):
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

class NavigationTabs(Widget, WidgetContainer, HasTabs, HasSelectedColor, HasDeselectedColor, HasFont):
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

class Tabs(Widget, WidgetContainer, HasMacros, HasTabs, HasFont, HasBackgroundColor):
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


class TemplateInstance(Widget, WidgetContainer, HasFile, HasInstances, HasTransparent, HasHorizontal, HasWrapCount, HasGap):
    """ TemplateInstance Phoebus Widget """

    def __init__(self, name: str, file: str, x: int, y: int, width: int, height: int) -> None:
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
