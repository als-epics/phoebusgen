from .widget import Widget
from phoebusgen.properties import (
    HasMacros,
    HasFile,
    HasShowToolbar,
    HasName,
    HasBackgroundColor,
    HasForegroundColor,
    HasAlarmBorder,
)


# # Plots
# class StripChartTrace(_Generic, _Name, _YPV, _Axis, _TraceType, _Color, HasLineWidth,
#                       intType, intSize):
#     def __init__(self) -> None:
#         _Generic.__init__(self, 'trace')

# class XYPlotTrace(StripChartTrace, _XPV, _ErrPV, _LineStyle):
#     def __init__(self) -> None:
#         super().__init__()

# class StripChartYAxis(_Generic, _Title, _AutoScale, _LogScale, _MinMax, _ShowGrid,
#                       _Color):
#     def __init__(self) -> None:
#         _Generic.__init__(self, 'y_axis')

# class XYPlotYAxis(StripChartYAxis, _TitleFont, _ScaleFont, _OnRight, _Color):
#     def __init__(self) -> None:
#         super().__init__()

# class ImageYAxis(_Generic, _Title, _MinMax, _TitleFont, _ScaleFont):
#     def __init__(self) -> None:
#         _Generic.__init__(self, 'y_axis')

# class XYPlotXAxis(_Generic, _Title, _AutoScale, _LogScale, _MinMax, _ShowGrid, _TitleFont,
#             _ScaleFont):
#     def __init__(self) -> None:
#         _Generic.__init__(self, 'x_axis')

# class ImageXAxis(_Generic, _Title, _MinMax, _TitleFont, _ScaleFont):
#     def __init__(self) -> None:
#         _Generic.__init__(self, 'x_axis')

# class Marker(_Generic, _Color, Name, _Interactive):
#     def __init__(self) -> None:
#         _Generic.__init__(self, 'marker')

# class RegionOfInterest(_Generic, _Name, _Color, _Interactive, _XPV, _YPV, _WidthPV, _HeightPV, HasFile):
#     def __init__(self) -> None:
#         _Generic.__init__(self, 'roi')

# class ColorBar(_Generic, _ScaleFont, _ColorBarSize):
#     def __init__(self) -> None:
#         _Generic.__init__(self, 'color_bar')

# class ColorMapColor(_Generic):
#     def __init__(self, value, red, green, blue):
#         _Generic.__init__(self, 'section')
#         self.root.attrib['value'] = str(value)
#         self.root.attrib['red'] = str(red)
#         self.root.attrib['green'] = str(green)
#         self.root.attrib['blue'] = str(blue)

class DataBrowser(Widget, HasMacros, HasFile, _ShowToolbar, _SelectionValuePV):
    """ DataBrowser Phoebus Widget """
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
        Widget.__init__(self, 'databrowser', name, x, y, width, height)
        self.file(file)

# colormap, colorbar, xaxis, yaxis, datawidth, dataheight, interpolation, colormode, unsigneddata, autoscale,
# logscale, cursor, roi
#class Image(Widget, HasName, _ForegroundColor, HasBackgroundColor, _ShowToolbar, _ColorMap, _ColorBar,
#            _XAxis, _YAxis, _AlarmBorder, _DataWidth, _Interpolation, _ColorMode, _UnsignedData,
#            _AutoScale, _LogScale, _MinMax, _Cursor, _RegionsOfInterest):
#    pass
class Image(Widget, HasName, _ForegroundColor, HasBackgroundColor, _ShowToolbar,
            _AlarmBorder, _MinMax, _AutoScale, _DataHeightAndWidth, _UnsignedData,
            _LogScale, _Cursor, _Interpolation, _XAxis, _YAxis, _ColorMode,
            _RegionsOfInterest, _ColorBar, _ColorMap):
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
        Widget.__init__(self, 'image', name, x, y, width, height)
        self.pv_name(pv_name)

# showgrid, labelfont, scalefont, yaxes, traces
#class StripChart(Widget, _ForegroundColor, HasBackgroundColor, _ShowGrid, _Title, _LabelFont, _ScaleFont,
#                 _ShowToolbar, _TimeRange, _YAxes, _Traces):
#    pass
class StripChart(Widget, _ForegroundColor, HasBackgroundColor, _ShowToolbar, _Title,
                 _TitleFont, _ShowLegend, _ShowGrid, _TimeRange, _LabelFont,
                 _ScaleFont, _YAxes, _Traces):
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
        Widget.__init__(self, 'stripchart', name, x, y, width, height)

# title, showlegend, xaxis, yaxes, traces, markers
#class XYPlot(Widget, _ForegroundColor, HasBackgroundColor, _GridColor, _Title, _ShowToolbar, _ShowLegend,
#             _XAxis, _YAxes, _Traces, _Markers):
#    pass
class XYPlot(Widget, _ForegroundColor, HasBackgroundColor, _ShowToolbar, _Title,
             _TitleFont, _GridColor, _XAxis, _YAxes, _Traces, _Markers):
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
        Widget.__init__(self, 'xyplot', name, x, y, width, height)
