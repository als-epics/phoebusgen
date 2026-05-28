from pathlib import Path
from typing import Union

from .widget import Widget
from phoebusgen.v4.properties.display import (
    HasShowToolbar,
    HasBackgroundColor,
    HasForegroundColor,
    HasAlarmBorder,
    HasSelectionValuePV,
    HasColorBar,
    HasTitle,
    HasLabelFont,
    HasScaleFont,
    HasShowGrid,
    HasShowLegend,
    HasTimeRange,
    HasTitleFont,
    HasPVName,
)
from phoebusgen.v4.properties.behavior import (
    HasXAxis,
    HasDataWidthAndHeight,
    HasYAxis,
    HasColorMap,
    HasInterpolation,
    HasColorMode,
    HasUnisignedData,
    HasAutoScale,
    HasYAxes,
    HasLogScale,
    HasTraces,
    HasMinMax,
    HasLimitsFromPV,
)
from phoebusgen.v4.properties.widget import HasMacros, HasFile
from phoebusgen.v4.properties.misc import HasCursor, HasROIs, HasMarkers

class DataBrowser(Widget, HasMacros, HasFile, HasShowToolbar, HasSelectionValuePV):
    """ DataBrowser Phoebus Widget """

    def __init__(self, name: str, file: Union[Path, str], x: int, y: int, width: int, height: int) -> None:
        """
        Create DataBrowser Widget

        :param name: Widget name
        :param pv_name: Widget PV
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
    """ Image Phoebus Widget """

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
    """ StripChart Phoebus Widget """

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
    """ XYPlot Phoebus Widget """

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
