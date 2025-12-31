from phoebusgen.properties.behavior import HasDataWidth, HasToolTip
from phoebusgen.properties.display import HasLimitsFromPV, HasSelectionValuePV
from .widget import WidgetType, Widget
from phoebusgen.properties import (
    HasMacros,
    HasFile,
    HasShowToolbar,
    HasName,
    HasBackgroundColor,
    HasForegroundColor,
    HasAlarmBorder,
    HasXAxis,
    HasYAxis,
    HasColorMap,
    HasColorBar,
    HasCursor,
    HasROIs,
    HasDataHeight,
    HasInterpolation,
    HasTitle,
    HasTitleFont,
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
    HasGridColor,
    HasMarkers,
    HasLimitsFromPV,
    HasToolTip,
    HasPVName
)

class DataBrowser(Widget, HasToolTip, HasMacros, HasFile, HasShowToolbar, HasSelectionValuePV):
    """ DataBrowser Phoebus Widget """
    _widget_type: WidgetType = WidgetType.DATABROWSER
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

# colormap, colorbar, xaxis, yaxis, datawidth, dataheight, interpolation, colormode, unsigneddata, autoscale,
# logscale, cursor, roi
#class Image(Widget, HasName, _ForegroundColor, HasBackgroundColor, _ShowToolbar, _ColorMap, _ColorBar,
#            _XAxis, _YAxis, _AlarmBorder, _DataWidth, _Interpolation, _ColorMode, _UnsignedData,
#            _AutoScale, _LogScale, _MinMax, _Cursor, _RegionsOfInterest):
#    pass
class Image(Widget, HasPVName, HasBackgroundColor, HasForegroundColor, HasShowToolbar, HasColorMap, HasColorBar, HasXAxis, HasYAxis, HasToolTip, HasAlarmBorder, HasLimitsFromPV, HasDataWidth, HasDataHeight, HasInterpolation, HasColorMode, HasUnisignedData, HasAutoScale, HasLogScale, HasMinMax, HasCursor, HasROIs):
    """ Image Phoebus Widget """

    _widget_type: WidgetType = WidgetType.IMAGE
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

# showgrid, labelfont, scalefont, yaxes, traces
#class StripChart(Widget, _ForegroundColor, HasBackgroundColor, _ShowGrid, _Title, _LabelFont, _ScaleFont,
#                 _ShowToolbar, _TimeRange, _YAxes, _Traces):
#    pass
class StripChart(Widget, HasForegroundColor, HasBackgroundColor, HasShowToolbar, HasTitle,
                 HasTitleFont, HasShowLegend, HasShowGrid, HasTimeRange, HasLabelFont,
                 HasScaleFont, HasYAxes, HasTraces):
    """ StripChart Phoebus Widget """
    _widget_type: WidgetType = WidgetType.STRIPCHART
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

# title, showlegend, xaxis, yaxes, traces, markers
#class XYPlot(Widget, _ForegroundColor, HasBackgroundColor, _GridColor, _Title, _ShowToolbar, _ShowLegend,
#             _XAxis, _YAxes, _Traces, _Markers):
#    pass
class XYPlot(Widget, HasForegroundColor, HasBackgroundColor, HasShowToolbar, HasTitle,
             HasTitleFont, HasGridColor, HasXAxis, HasYAxes, HasTraces, HasMarkers):
    """ XYPlot Phoebus Widget """
    _widget_type: WidgetType = WidgetType.XYPLOT
    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create XYPlot Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, 'xyplot', name, x, y, width, height)
