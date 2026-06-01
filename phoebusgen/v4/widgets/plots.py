from pathlib import Path
from typing import Union

from phoebusgen.v4.properties.behavior import (
    HasAlarmBorder,
    HasAutoScale,
    HasColorMode,
    HasDataWidthAndHeight,
    HasInterpolation,
    HasLimitsFromPV,
    HasLogScale,
    HasMinMax,
    HasTraces,
    HasUnisignedData,
    HasXAxis,
    HasYAxes,
    HasYAxis,
)
from phoebusgen.v4.properties.display import (
    HasBackgroundColor,
    HasColorBar,
    HasColorMap,
    HasForegroundColor,
    HasLabelFont,
    HasScaleFont,
    HasSelectionValuePV,
    HasShowGrid,
    HasShowLegend,
    HasShowToolbar,
    HasTimeRange,
    HasTitle,
    HasTitleFont,
)
from phoebusgen.v4.properties.misc import HasCursor, HasMarkers, HasROIs
from phoebusgen.v4.properties.types import Color
from phoebusgen.v4.properties.widget import HasFile, HasMacros, HasPVName

from .widget import Widget


class DataBrowser(Widget, HasMacros, HasFile, HasShowToolbar, HasSelectionValuePV):
    """DataBrowser Phoebus Widget"""

    show_toolbar: bool = False
    width: int = 400
    height: int = 300

    def __init__(self, name: str, file: Union[Path, str], x: int, y: int, width: int, height: int) -> None:
        """
        Create DataBrowser Widget

        :param name: Widget name
        :param file: File path
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.file = file

class Image(Widget, HasPVName, HasBackgroundColor, HasForegroundColor, HasShowToolbar, HasColorMap, HasColorBar, HasXAxis, HasYAxis,
            HasAlarmBorder, HasLimitsFromPV, HasDataWidthAndHeight, HasInterpolation, HasColorMode, HasUnisignedData, HasAutoScale, HasLogScale,
            HasMinMax, HasCursor, HasROIs):
    """Image Phoebus Widget"""

    width: int = 400
    height: int = 300

    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Image Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class StripChart(Widget, HasForegroundColor, HasBackgroundColor, HasShowGrid, HasTitle,
                 HasTitleFont, HasLabelFont, HasScaleFont, HasShowToolbar, HasShowLegend, HasTimeRange,
                 HasYAxes, HasTraces):
    """StripChart Phoebus Widget"""

    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create StripChart Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)

class XYPlot(Widget, HasForegroundColor, HasBackgroundColor, HasTitle,
             HasTitleFont, HasShowToolbar, HasShowLegend, HasXAxis, HasYAxes, HasTraces, HasMarkers):
    """XYPlot Phoebus Widget"""

    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create XYPlot Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
