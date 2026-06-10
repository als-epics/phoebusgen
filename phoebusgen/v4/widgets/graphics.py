from pathlib import Path
from typing import Union

from phoebusgen.v4.properties.behavior import HasWrapWords
from phoebusgen.v4.properties.display import (
    HasAngle,
    HasArrows,
    HasAutoSize,
    HasBackgroundColor,
    HasCorners,
    HasFont,
    HasForegroundColor,
    HasHorizontalAlignment,
    HasLineColor,
    HasLineStyle,
    HasLineWidth,
    HasOpacity,
    HasPoints,
    HasRotation,
    HasRotationStep,
    HasStretchToFit,
    HasText,
    HasTransparent,
    HasVerticalAlignment,
)
from phoebusgen.v4.properties.misc import HasBorder
from phoebusgen.v4.properties.types import Color, VerticalAlignment
from phoebusgen.v4.properties.widget import HasFile, HasMacros

from .widget import Widget

BLUE = Color((0, 0, 255)) # Full blue used for default line color
POLY_BLUE = Color((50, 50, 255)) # Slightly lighter blue used for polygon bg color
LIGHT_BLUE = Color((30, 144, 255)) # Light blue used for shape bg color

# Graphics
class Arc(Widget, HasMacros, HasAngle, HasLineWidth, HasLineColor, HasLineStyle, HasBackgroundColor, HasTransparent):
    """Arc Phoebus Widget"""

    height: int = 100
    line_color: Color = BLUE
    background_color: Color = LIGHT_BLUE

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

class Ellipse(Widget, HasMacros, HasLineWidth, HasLineColor, HasLineStyle, HasBackgroundColor, HasTransparent):
    """Ellipse Phoebus Widget"""

    height: int = 50
    line_color: Color = BLUE
    background_color: Color = LIGHT_BLUE

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
    """Label Phoebus Widget"""

    background_color: Color = Color((255, 255, 255))
    width: int = 100
    height: int = 20
    text: str = 'Label text'
    vertical_alignment: VerticalAlignment = VerticalAlignment.TOP

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

class Picture(Widget, HasMacros, HasFile, HasStretchToFit, HasRotation, HasOpacity):
    """Picture Phoebus Widget"""

    def __init__(self, name: str, file: Union[Path, str], x: int, y: int, width: int, height: int) -> None:
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

class Polygon(Widget, HasMacros, HasLineWidth, HasLineColor, HasLineStyle, HasTransparent, HasPoints, HasBackgroundColor):
    """Polygon Phoebus Widget"""

    line_color: Color = BLUE
    background_color: Color = POLY_BLUE

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

class Polyline(Widget, HasMacros, HasLineWidth, HasLineColor, HasLineStyle, HasArrows, HasPoints):
    """Polyline Phoebus Widget"""

    line_color: Color = BLUE

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

class Rectangle(Widget, HasMacros, HasLineWidth, HasLineColor, HasLineStyle, HasBackgroundColor, HasTransparent, HasCorners):
    """Rectangle Phoebus Widget"""

    line_color: Color = BLUE
    background_color: Color = LIGHT_BLUE

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
