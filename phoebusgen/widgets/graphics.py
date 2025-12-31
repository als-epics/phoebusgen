from .widget import WidgetType, Widget
from phoebusgen.properties import (
    HasMacros,
    HasAngle,
    HasLineWidth,
    HasLineColor,
    HasBackgroundColor,
    HasTransparent,
    HasText,
    HasFont,
    HasForegroundColor,
    HasHorizontalAlignment,
    HasVerticalAlignment,
    HasRotationStep,
    HasWrapWords,
    HasAutoSize,
    HasBorder,
    HasFile,
    HasStretchToFit,
    HasRotation,
    HasLineStyle,
    HasArrows,
    HasCorner,
)

# Graphics
class Arc(Widget, HasMacros, HasAngle, HasLineWidth, HasLineColor, HasLineStyle, HasBackgroundColor, HasTransparent):
    """ Arc Phoebus Widget """

    _widget_type: WidgetType = WidgetType.ARC

    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Arc Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)

class Ellipse(Widget, HasMacros, HasLineWidth, HasLineColor, HasBackgroundColor, HasTransparent):
    """ Ellipse Phoebus Widget """

    _widget_type: WidgetType = WidgetType.ELLIPSE

    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Ellipse Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)

class Label(Widget, HasText, HasMacros, HasFont, HasForegroundColor, HasBackgroundColor, HasTransparent, HasHorizontalAlignment,
            HasVerticalAlignment, HasRotationStep, HasWrapWords, HasAutoSize, HasBorder):
    """ Label Phoebus Widget """

    _widget_type: WidgetType = WidgetType.LABEL

    def __init__(self, name: str, text: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Label Widget

        :param name: Widget name
        :param text: Text of label
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.text = text

class Picture(Widget, HasMacros, HasFile, HasStretchToFit, HasRotation):
    """ Picture Phoebus Widget """

    _widget_type: WidgetType = WidgetType.PICTURE

    def __init__(self, name: str, file: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Picture Widget

        :param name: Widget name
        :param file: File path to image
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.file = file

class Polygon(Widget, HasMacros, HasLineWidth, HasLineColor, HasBackgroundColor):
    """ Polygon Phoebus Widget """

    _widget_type: WidgetType = WidgetType.POLYGON

    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Polygon Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)

class Polyline(Widget, HasMacros, HasLineWidth, HasLineColor, HasLineStyle, HasArrows):
    """ Polyline Phoebus Widget """

    _widget_type: WidgetType = WidgetType.POLYLINE

    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Polyline Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)

class Rectangle(Widget, HasMacros, HasLineWidth, HasLineColor, HasBackgroundColor, HasTransparent, HasCorner):
    """ Rectangle Phoebus Widget """

    _widget_type: WidgetType = WidgetType.RECTANGLE

    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Rectangle Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
