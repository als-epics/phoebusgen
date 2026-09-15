from pathlib import Path
from typing import Optional, Union

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
from phoebusgen.v4.properties.types import Axis, Font, FontStyle
from phoebusgen.v4.properties.widget import HasFile, HasMacros, HasPVName

from .widget import Widget


class DataBrowser(Widget, HasMacros, HasFile, HasShowToolbar, HasSelectionValuePV):
    """DataBrowser Phoebus Widget"""

    show_toolbar: bool = False
    width: int = 400
    height: int = 300

    def __init__(self, name: str = '', file: Optional[Union[Path, str]] = '', x: int = 0, y: int = 0, width: int = 400, height: int = 300) -> None:
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

    limits_from_pv: bool = False
    maximum: float = 255.0
    tooltip: str = '$(pv_name)'
    x_axis: Axis = Axis(title='X', maximum=100.0, title_font=Font(style=FontStyle.BOLD))
    y_axis: Axis = Axis(title='Y', maximum=100.0, title_font=Font(style=FontStyle.BOLD))
    width: int = 400
    height: int = 300

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 400, height: int = 300) -> None:
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

    show_toolbar: bool = True
    tooltip: str = '$(traces[0].y_pv)'
    title_font: Font = Font(size=18, style=FontStyle.BOLD)
    label_font: Font = Font(style=FontStyle.BOLD)
    width: int = 400
    height: int = 300

    def __init__(self, name: str = '', x: int = 0, y: int = 0, width: int = 400, height: int = 300) -> None:
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

    show_legend: bool = True
    tooltip: str = '$(traces[0].y_pv)'
    title_font: Font = Font(size=18, style=FontStyle.BOLD)
    x_axis: Axis = Axis(title='X', maximum=100.0, autoscale=False, show_grid=False, title_font=Font(style=FontStyle.BOLD))
    width: int = 400
    height: int = 300

    def __init__(self, name: str = '', x: int = 0, y: int = 0, width: int = 400, height: int = 300) -> None:
        """
        Create XYPlot Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
