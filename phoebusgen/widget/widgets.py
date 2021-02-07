from phoebusgen.widget.widget import _Widget
from phoebusgen.widget import property_stubs as _p

# Displays
class Arc(_Widget, _p._Macro, _p._Angle, _p._LineWidth, _p._LineColor, _p._BackgroundColor, _p._Transparent):
    """ Arc widget, req: none """
    def __init__(self, name, x, y, width, height):
        _Widget.__init__(self, 'arc', name, x, y, width, height)

class Ellipse(_Widget, _p._Macro, _p._LineWidth, _p._LineColor, _p._BackgroundColor, _p._Transparent):
    """ Ellipse widget, req: none """
    def __init__(self, name, x, y, width, height):
        _Widget.__init__(self, 'ellipse', name, x, y, width, height)

class Label(_Widget, _p._Text, _p._Macro, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._Transparent, _p._HorizontalAlignment,
            _p._VerticalAlignment, _p._RotationStep, _p._WrapWords, _p._AutoSize, _p._Border):
    """ Label widget, req: text """
    def __init__(self, name, text, x, y, width, height):
        _Widget.__init__(self, 'label', name, x, y, width, height)
        self.text(text)

class Picture(_Widget, _p._Macro, _p._File, _p._StretchToFit, _p._Rotation):
    def __init__(self, name, file, x, y, width, height):
        _Widget.__init__(self, 'picture', name, x, y, width, height)
        self.file(file)

# points
#class Polygon(_Widget, _p._Macro, _p._LineWidth, _p._LineColor, _p._BackgroundColor, _p._Points):
#    pass

# line style, arrows, arrow length, points
#class Polyline(_Widget, _p._Macro, _p._LineWidth, _p._LineColor, _p._LineStyle, _p._Arrow, _p.Points):
#    pass

class Rectangle(_Widget, _p._Macro, _p._LineWidth, _p._LineColor, _p._BackgroundColor, _p._Transparent, _p._Corner):
    """ Rectangle widget, req: none """
    def __init__(self, name, x, y, width, height):
        _Widget.__init__(self, 'rectangle', name, x, y, width, height)

# Monitors
# Start bit, number of bits, reverse bits, labels
#class ByteMonitor(_Widget, _p._PVName, _p._StartBit, _p._NumBits, _p._ReverseBits, _p._Horizontal, _p._Square, _p._OffColor, _p._OnColor,
#                  _p._ForegroundColor, _p._Font, _p._Labels, _p._AlarmBorder):
#    pass

class LED(_Widget, _p._PVName, _p._Bit, _p._Off, _p._On, _p._Font, _p._ForegroundColor, _p._LineColor,
          _p._Square, _p._LabelsFromPV, _p._AlarmBorder):
    """ LED widget, req: None """
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'led', name, x, y, width, height)
        self.pv_name(pv_name)

# States, Fallback
#class LEDMultiState(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._LineColor, _p._Square,
#                    _p._AlarmBorder, _p._States, _p._Fallback):
#    pass

class Meter(_Widget, _p._PVName, _p._ForegroundColor, _p._BackgroundColor, _p._Font, _p._Format,
            _p._Precision, _p._ShowValue, _p._ShowUnits, _p._ShowLimits, _p._AlarmBorder,
            _p._LimitsFromPV, _p._MinMax, _p._NeedleColor, _p._KnobColor):
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'meter', name, x, y, width, height)
        self.pv_name(pv_name)

class ProgressBar(_Widget, _p._PVName, _p._FillColor, _p._BackgroundColor, _p._Horizontal,
                  _p._AlarmBorder, _p._LimitsFromPV, _p._MinMax):
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'progressbar', name, x, y, width, height)
        self.pv_name(pv_name)

# Symbols, InitialIndex, showindex, arrayindex, preserve ratio
#class Symbol(_Widget, _p._Symbols, _p._PVName, _p._BackgroundColor, _p._InitialIndex,
#             _p._Rotation, _p._ShowIndex, _p._Transparent, _p._AlarmBorder, _p._ArrayIndex,
#             _p._AutoSize, _p._Enabled, _p._PreserveRatio):

# columns, selectrows, selectionpv
#class Table(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._ShowToolbar,
#            _p._Columns, _p._AlarmBorder, _p._Editable, _p._SelectRows, _p._SelectionPV):

class Tank(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._BackgroundColor,
           _p._FillColor, _p._EmptyColor, _p._ScaleVisible, _p._AlarmBorder, _p._LimitsFromPV,
           _p._MinMax):
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'tank', name, x, y, width, height)
        self.pv_name(pv_name)

# Symbols, arrayindex
#class TextSymbol(_Widget, _p._PVName, _p._Symbols, _p._Font, _p._ForegroundColor, _p._BackgroundColor,
#                 _p._Transparent, _p._HorizontalAlignment, _p._VerticalAlignment, _p._Rotation,
#                 _p._WrapWords, _p._AlarmBorder, _p._ArrayIndex, _p._Enabled):
#    pass

class TextUpdate(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._Transparent,
                 _p._Format, _p._Precision, _p._ShowUnits, _p._HorizontalAlignment, _p._VerticalAlignment, _p._WrapWords,
                 _p._RotationStep, _p._Border):
    """ Text Update widget, req: pv name """
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'textupdate', name, x, y, width, height)
        self.pv_name(pv_name)

class Thermometer(_Widget, _p._PVName, _p._FillColor, _p._AlarmBorder, _p._LimitsFromPV, _p._MinMax):
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'thermometer', name, x, y, width, height)
        self.pv_name(pv_name)

# Controls
class ActionButton(_Widget, _p._PVName, _p._Actions, _p._Text, _p._Font, _p._ForegroundColor, _p._BackgroundColor,
                   _p._Transparent, _p._RotationStep, _p._Enabled, _p._Confirmation):
    """ Action button widget, req: text, pv name """
    def __init__(self, name, text, pv_name, x, y, width, height):
        _Widget.__init__(self, 'action_button', name, x, y, width, height)
        self.pv_name(pv_name)
        self.text(text)

class BooleanButton(_Widget, _p._PVName, _p._Bit, _p._OffImage, _p._OnImage, _p._ShowLED, _p._Font, _p._ForegroundColor, _p._BackgroundColor,
                    _p._LabelsFromPV, _p._AlarmBorder, _p._Enabled, _p._Mode, _p._Confirmation):
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'bool_button', name, x, y, width, height)
        self.pv_name(pv_name)

class CheckBox(_Widget, _p._PVName, _p._Bit, _p._Label, _p._Font, _p._ForegroundColor, _p._AutoSize,
               _p._AlarmBorder, _p._Confirmation):
    def __init__(self, name, label, pv_name, x, y, width, height):
        _Widget.__init__(self, 'checkbox', name, x, y, width, height)
        self.pv_name(pv_name)
        self.label(label)

class ChoiceButton(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._SelectedColor, _p._Horizontal,
                   _p._AlarmBorder, _p._Items, _p._ItemsFromPV, _p._Confirmation):
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'choice', name, x, y, width, height)
        self.pv_name(pv_name)

class ComboBox(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._AlarmBorder, _p._Items,
               _p._ItemsFromPV, _p._Editable, _p._Enabled, _p._Confirmation):
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'combo', name, x, y, width, height)
        self.pv_name(pv_name)


class FileSelector(_Widget, _p._PVName, _p._FileComponent, _p._AlarmBorder, _p._Enabled):
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'fileselector', name, x, y, width, height)
        self.pv_name(pv_name)

class RadioButton(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._Horizontal, _p._AlarmBorder,
                  _p._Items, _p._ItemsFromPV, _p._Enabled, _p._Confirmation):
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'radio', name, x, y, width, height)
        self.pv_name(pv_name)

# showscale, showminorticks, majortickspixeldist, scaleformat, levelhihi, levelhigh, levellow, levellolo, showhihi, showhigh
# showlow, showlolo
#class ScaledSlider(_Widget, _p._PVName, _p._Horizontal, _p._ForegroundColor, _p._BackgroundColor, _p._Transparent, _p._Font,
#                   _p._ShowScale, _p._ShowMinorTicks, _p._MajorTicksPixelDist, _p._ScaleFormat, _p._LevelsandShow, _p._AlarmBorder,
#                   _p._Increment, _p._MinMax, _p._LimitsFromPV, _p._Enabled):
#    pass

class Scrollbar(_Widget, _p._PVName, _p._Horizontal, _p._ShowValueTip, _p._AlarmBorder, _p._MinMax,
                _p._LimitsFromPV, _p._BarLength, _p._Increment, _p._Enabled):
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'scrollbar', name, x, y, width, height)
        self.pv_name(pv_name)

class SlideButton(_Widget, _p._PVName, _p._Bit, _p._Label, _p._OffColor, _p._OnColor, _p._Font, _p._ForegroundColor,
                  _p._AutoSize, _p._AlarmBorder, _p._Enabled, _p._Confirmation):
    def __init__(self, name, label, pv_name, x, y, width, height):
        _Widget.__init__(self, 'slide_button', name, x, y, width, height)
        self.pv_name(pv_name)
        self.label(label)

class Spinner(_Widget, _p._PVName, _p._Format, _p._Precision, _p._ShowUnits, _p._ForegroundColor, _p._BackgroundColor,
              _p._ButtonsOnLeft, _p._AlarmBorder, _p._MinMax, _p._LimitsFromPV, _p._Increment, _p._Enabled):
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'spinner', name, x, y, width, height)
        self.pv_name(pv_name)

class TextEntry(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._Format,
                _p._Precision, _p._ShowUnits, _p._WrapWords, _p._MultiLine, _p._AlarmBorder, _p._Enabled,
                _p._Border):
    """ Text Entry widget, req: pv name """
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'textentry', name, x, y, width, height)
        self.pv_name(pv_name)

# Plots

class DataBrowser(_Widget, _p._Macro, _p._File, _p._ShowToolbar, _p._SelectionValuePV):
    def __init__(self, name, file, x, y, width, height):
        _Widget.__init__(self, 'databrowser', name, x, y, width, height)
        self.file(file)

# showtoolbar, colormap, colorbar, xaxis, yaxis, datawidth, interpolation, colormode, unsigneddata, autoscale,
# logscale, cursor, roi
#class Image(_Widget, _p._PVName, _p._ForegroundColor, _p._BackgroundColor, _p._ShowToolbar, _p._ColorMap, _p._ColorBar,
#            _p._XAxis, _p._YAxis, _p._AlarmBorder, _p._DataWidth, _p._Interpolation, _p._ColorMode, _p._UnsignedData,
#            _p._AutoScale, _p._LogScale, _p._MinMax, _p._Cursor, _p._RegionsOfInterest):
#    pass

# showgrid, title, labelfont, scalefont, showtoolbar, tooltip, timerange, yaxes, traces
#class StripChart(_Widget, _p._ForegroundColor, _p._BackgroundColor, _p._ShowGrid, _p._Title, _p._LabelFont, _p._ScaleFont,
#                 _p._ShowToolbar, _p._ToolTip, _p._TimeRange, _p._YAxes, _p._Traces):
#    pass


# gridcolor, title, showtoolbar, showlegend, xaxis, yaxes, traces, markers
#class XYPlot(_Widget, _p._ForegroundColor, _p._BackgroundColor, _p._GridColor, _p._Title, _p._ShowToolbar, _p._ShowLegend,
#             _p._XAxis, _p._YAxes, _p._Traces, _p._Markers):
#    pass

# Structure
class Array(_Widget, _p._PVName, _p._Macro, _p._ForegroundColor, _p._BackgroundColor, _p._AlarmBorder):
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'array', name, x, y, width, height)
        self.pv_name(pv_name)

class EmbeddedDisplay(_Widget, _p._Macro, _p._File, _p._ResizeBehavior, _p._GroupName, _p._Transparent, _p._Border):
    def __init__(self, name, file, x, y, width, height):
        _Widget.__init__(self, 'embedded', name, x, y, width, height)
        self.file(file)

class Group(_Widget, _p._Structure, _p._Macro, _p._Style, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._Transparent):
    def __init__(self, name, x, y, width, height):
        _Widget.__init__(self, 'group', name, x, y, width, height)

# tab width, tab height, tab spacing, selected color, deselected color, active tab
#class NavigationTabs(_Widget, _p._Tabs, _p._Direction, _p._TabWidth, _p._TabHeight, _p._TabSpacing, _p._SelectColor, _p._Font, _p._ActiveTab):
#    pass


# tabs, active tab, direction, tab height
#class Tabs(_Widget, _p._Macro, _p._Tabs, _p._Font, _p._BackgroundColor, _p._ActiveTab, _p._Direction, _p._TabHeight):
#    pass

# Miscellaneous

class ThreeDViewer(_Widget, _p._File):
    def __init__(self, name, file, x, y, width, height):
        _Widget.__init__(self, '3dviewer', name, x, y, width, height)
        self.file(file)

class WebBrowser(_Widget, _p._URL, _p._ShowToolbar):
    def __init__(self, name, url, x, y, width, height):
        _Widget.__init__(self, 'webbrowser', name, x, y, width, height)
        self.url(url)


if __name__ == '__main__':
    pass

