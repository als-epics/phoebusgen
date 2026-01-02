from .widget import WidgetType, Widget
from phoebusgen.properties import (
    HasMacros,
    HasFile,
    HasShowToolbar,
    HasBackgroundColor,
    HasForegroundColor,
    HasAlarmBorder,
    HasXAxis,
    HasDataWidthAndHeight,
    HasSelectionValuePV,
    HasYAxis,
    HasColorMap,
    HasColorBar,
    HasCursor,
    HasTitle,
    HasROIs,
    HasInterpolation,
    HasLabelFont,
    HasScaleFont,
    HasShowGrid,
    HasShowLegend,
    HasTimeRange,
    HasColorMode,
    HasUnisignedData,
    HasAutoScale,
    HasYAxes,
    HasLogScale,
    HasTraces,
    HasMinMax,
    HasTitleFont,
    HasMarkers,
    HasLimitsFromPV,
    HasPVName
)

class DataBrowser(Widget, HasMacros, HasFile, HasShowToolbar, HasSelectionValuePV):
    """ DataBrowser Phoebus Widget """
    _widget_type: WidgetType | None = WidgetType.DATABROWSER
    def __init__(self, name: str, file: str, x: int, y: int, width: int, height: int) -> None:
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

    _widget_type: WidgetType | None = WidgetType.IMAGE
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
    _widget_type: WidgetType | None = WidgetType.STRIPCHART
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
    _widget_type: WidgetType | None = WidgetType.XYPLOT
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
