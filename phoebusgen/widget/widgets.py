from phoebusgen.widget.widget import _Widget
from phoebusgen.widget import properties as _p

# Displays
class Arc(_Widget, _p._Macro, _p._Angle, _p._LineWidth, _p._LineColor, _p._BackgroundColor, _p._Transparent):
    """ Arc Phoebus Widget """
    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Arc Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'arc', name, x, y, width, height)

class Ellipse(_Widget, _p._Macro, _p._LineWidth, _p._LineColor, _p._BackgroundColor, _p._Transparent):
    """ Ellipse Phoebus Widget """
    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Ellipse Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'ellipse', name, x, y, width, height)

class Label(_Widget, _p._Text, _p._Macro, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._Transparent, _p._HorizontalAlignment,
            _p._VerticalAlignment, _p._RotationStep, _p._WrapWords, _p._AutoSize, _p._Border):
    """ Label Phoebus Widget """
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
        _Widget.__init__(self, 'label', name, x, y, width, height)
        self.text(text)

class Picture(_Widget, _p._Macro, _p._File, _p._StretchToFit, _p._Rotation):
    """ Picture Phoebus Widget """
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
        _Widget.__init__(self, 'picture', name, x, y, width, height)
        self.file(file)

class Polygon(_Widget, _p._Macro, _p._LineWidth, _p._LineColor, _p._BackgroundColor, _p._Points):
    """ Polygon Phoebus Widget """
    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Polygon Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'polygon', name, x, y, width, height)

class Polyline(_Widget, _p._Macro, _p._LineWidth, _p._LineColor, _p._LineStyle, _p._Arrow, _p._Points):
    """ Polyline Phoebus Widget """
    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Polyline Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'polyline', name, x, y, width, height)

class Rectangle(_Widget, _p._Macro, _p._LineWidth, _p._LineColor, _p._BackgroundColor, _p._Transparent, _p._Corner):
    """ Rectangle Phoebus Widget """
    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Rectangle Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'rectangle', name, x, y, width, height)

# Monitors
class ByteMonitor(_Widget, _p._PVName, _p._StartBit, _p._NumBits, _p._ReverseBits, _p._Horizontal, _p._Square,
                  _p._OffColor, _p._OnColor, _p._ForegroundColor, _p._Font, _p._Labels, _p._AlarmBorder):
    """ ByteMonitor Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create ByteMonitor Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'byte_monitor', name, x, y, width, height)
        self.pv_name(pv_name)

class LED(_Widget, _p._PVName, _p._Bit, _p._Off, _p._On, _p._Font, _p._ForegroundColor, _p._LineColor,
          _p._Square, _p._LabelsFromPV, _p._AlarmBorder):
    """ LED Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create LED Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'led', name, x, y, width, height)
        self.pv_name(pv_name)

class LEDMultiState(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._LineColor, _p._Square,
                    _p._AlarmBorder, _p._States, _p._Fallback):
    """ LEDMultiState Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create LEDMultiState Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'multi_state_led', name, x, y, width, height)
        self.pv_name(pv_name)

class Meter(_Widget, _p._PVName, _p._ForegroundColor, _p._BackgroundColor, _p._Font, _p._Format,
            _p._Precision, _p._ShowValue, _p._ShowUnits, _p._ShowLimits, _p._AlarmBorder,
            _p._LimitsFromPV, _p._MinMax, _p._NeedleColor, _p._KnobColor):
    """ Meter Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Meter Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'meter', name, x, y, width, height)
        self.pv_name(pv_name)

class ProgressBar(_Widget, _p._PVName, _p._FillColor, _p._BackgroundColor, _p._Horizontal,
                  _p._AlarmBorder, _p._LimitsFromPV, _p._MinMax):
    """ ProgressBar Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create ProgressBar Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'progressbar', name, x, y, width, height)
        self.pv_name(pv_name)

class Symbol(_Widget, _p._Symbols, _p._PVName, _p._BackgroundColor, _p._InitialIndex,
             _p._Rotation, _p._ShowIndex, _p._Transparent, _p._AlarmBorder, _p._ArrayIndex,
             _p._AutoSize, _p._Enabled, _p._PreserveRatio):
    """ Symbol Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Symbol Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'symbol', name, x, y, width, height)
        self.pv_name(pv_name)

class Table(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._ShowToolbar,
            _p._AlarmBorder, _p._Editable, _p._SelectRows, _p._SelectionPV, _p._Columns):
    """ Table Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Table Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'table', name, x, y, width, height)
        self.pv_name(pv_name)

class Tank(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._BackgroundColor,
           _p._FillColor, _p._EmptyColor, _p._ScaleVisible, _p._AlarmBorder, _p._LimitsFromPV,
           _p._MinMax):
    """ Tank Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Tank Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height:
        """
        _Widget.__init__(self, 'tank', name, x, y, width, height)
        self.pv_name(pv_name)

class TextSymbol(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._Transparent,
                 _p._HorizontalAlignment, _p._VerticalAlignment, _p._Rotation, _p._WrapWords,
                 _p._AlarmBorder, _p._Enabled, _p._ArrayIndex, _p._Symbols):
    """ TextSymbol Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create TextSymbol Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'text-symbol', name, x, y, width, height)
        self.pv_name(pv_name)

class TextUpdate(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._Transparent,
                 _p._Format, _p._Precision, _p._ShowUnits, _p._HorizontalAlignment, _p._VerticalAlignment, _p._WrapWords,
                 _p._RotationStep, _p._Border):
    """ TextUpdate Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create TextUpdate Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'textupdate', name, x, y, width, height)
        self.pv_name(pv_name)

class Thermometer(_Widget, _p._PVName, _p._FillColor, _p._AlarmBorder, _p._LimitsFromPV, _p._MinMax):
    """ Thermometer Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Thermometer Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'thermometer', name, x, y, width, height)
        self.pv_name(pv_name)

# Controls
class ActionButton(_Widget, _p._PVName, _p._Actions, _p._Text, _p._Font, _p._ForegroundColor, _p._BackgroundColor,
                   _p._Transparent, _p._RotationStep, _p._Enabled, _p._Confirmation):
    """ ActionButton Phoebus Widget """
    def __init__(self, name: str, text: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create ActionButton Widget

        :param name: Widget name
        :param text: Button text
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'action_button', name, x, y, width, height)
        self.pv_name(pv_name)
        self.text(text)

class BooleanButton(_Widget, _p._PVName, _p._Bit, _p._OffImage, _p._OnImage, _p._ShowLED, _p._Font, _p._ForegroundColor, _p._BackgroundColor,
                    _p._LabelsFromPV, _p._AlarmBorder, _p._Enabled, _p._Mode, _p._Confirmation):
    """ BooleanButton Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create BooleanButton Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'bool_button', name, x, y, width, height)
        self.pv_name(pv_name)

class CheckBox(_Widget, _p._PVName, _p._Bit, _p._Label, _p._Font, _p._ForegroundColor, _p._AutoSize,
               _p._AlarmBorder, _p._Confirmation):
    """ CheckBox Phoebus Widget """
    def __init__(self, name: str, label: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create CheckBox Widget

        :param name: Widget name
        :param label: Label text
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'checkbox', name, x, y, width, height)
        self.pv_name(pv_name)
        self.label(label)

class ChoiceButton(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._SelectedColor, _p._Horizontal,
                   _p._AlarmBorder, _p._Items, _p._ItemsFromPV, _p._Confirmation):
    """ ChoiceButton Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create ChoiceButton Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'choice', name, x, y, width, height)
        self.pv_name(pv_name)

class ComboBox(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._AlarmBorder, _p._Items,
               _p._ItemsFromPV, _p._Editable, _p._Enabled, _p._Confirmation):
    """ ComboBox Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create ComboBox Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'combo', name, x, y, width, height)
        self.pv_name(pv_name)


class FileSelector(_Widget, _p._PVName, _p._FileComponent, _p._AlarmBorder, _p._Enabled):
    """ FileSelector Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create FileSelector Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'fileselector', name, x, y, width, height)
        self.pv_name(pv_name)

class RadioButton(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._Horizontal, _p._AlarmBorder,
                  _p._Items, _p._ItemsFromPV, _p._Enabled, _p._Confirmation):
    """ RadioButton Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create RadioButton Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'radio', name, x, y, width, height)
        self.pv_name(pv_name)

class ScaledSlider(_Widget, _p._PVName, _p._Horizontal, _p._ForegroundColor, _p._BackgroundColor, _p._Transparent, _p._Font,
                   _p._ShowScale, _p._ShowMinorTicks, _p._MajorTicksPixelDist, _p._ScaleFormat, _p._LevelsAndShow, _p._AlarmBorder,
                   _p._Increment, _p._MinMax, _p._LimitsFromPV, _p._Enabled):
    """ ScaledSlider Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create ScaledSlider Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'scaledslider', name, x, y, width, height)
        self.pv_name(pv_name)

class Scrollbar(_Widget, _p._PVName, _p._Horizontal, _p._ShowValueTip, _p._AlarmBorder, _p._MinMax,
                _p._LimitsFromPV, _p._BarLength, _p._Increment, _p._Enabled):
    """ Scrollbar Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Scrollbar Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'scrollbar', name, x, y, width, height)
        self.pv_name(pv_name)

class SlideButton(_Widget, _p._PVName, _p._Bit, _p._Label, _p._OffColor, _p._OnColor, _p._Font, _p._ForegroundColor,
                  _p._AutoSize, _p._AlarmBorder, _p._Enabled, _p._Confirmation):
    """ SlideButton Phoebus Widget """
    def __init__(self, name: str, label: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create SlideButton Widget

        :param name: Widget name
        :param label: Label text
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'slide_button', name, x, y, width, height)
        self.pv_name(pv_name)
        self.label(label)

class Spinner(_Widget, _p._PVName, _p._Format, _p._Precision, _p._ShowUnits, _p._ForegroundColor, _p._BackgroundColor,
              _p._ButtonsOnLeft, _p._AlarmBorder, _p._MinMax, _p._LimitsFromPV, _p._Increment, _p._Enabled):
    """ Spinner Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Spinner Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'spinner', name, x, y, width, height)
        self.pv_name(pv_name)

class TextEntry(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._Format,
                _p._Precision, _p._ShowUnits, _p._WrapWords, _p._MultiLine, _p._AlarmBorder, _p._Enabled,
                _p._Border):
    """ TextEntry Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create TextEntry Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'textentry', name, x, y, width, height)
        self.pv_name(pv_name)

# Plots

class DataBrowser(_Widget, _p._Macro, _p._File, _p._ShowToolbar, _p._SelectionValuePV):
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
        _Widget.__init__(self, 'databrowser', name, x, y, width, height)
        self.file(file)

# colormap, colorbar, xaxis, yaxis, datawidth, dataheight, interpolation, colormode, unsigneddata, autoscale,
# logscale, cursor, roi
#class Image(_Widget, _p._PVName, _p._ForegroundColor, _p._BackgroundColor, _p._ShowToolbar, _p._ColorMap, _p._ColorBar,
#            _p._XAxis, _p._YAxis, _p._AlarmBorder, _p._DataWidth, _p._Interpolation, _p._ColorMode, _p._UnsignedData,
#            _p._AutoScale, _p._LogScale, _p._MinMax, _p._Cursor, _p._RegionsOfInterest):
#    pass
class Image(_Widget, _p._PVName, _p._ForegroundColor, _p._BackgroundColor, _p._ShowToolbar,
            _p._AlarmBorder, _p._MinMax, _p._AutoScale, _p._DataHeightAndWidth, _p._UnsignedData,
            _p._LogScale):
    """ Image - Incomplete Widget """
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
        _Widget.__init__(self, 'image', name, x, y, width, height)
        self.pv_name(pv_name)

# showgrid, labelfont, scalefont, timerange, yaxes, traces
#class StripChart(_Widget, _p._ForegroundColor, _p._BackgroundColor, _p._ShowGrid, _p._Title, _p._LabelFont, _p._ScaleFont,
#                 _p._ShowToolbar, _p._TimeRange, _p._YAxes, _p._Traces):
#    pass
class StripChart(_Widget, _p._ForegroundColor, _p._BackgroundColor, _p._ShowToolbar, _p._Title,
                 _p._ShowLegend, _p._ShowGrid):
    """ StripChart - Incomplete Widget """
    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create StripChart Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'stripchart', name, x, y, width, height)

# gridcolor, title, showlegend, xaxis, yaxes, traces, markers
#class XYPlot(_Widget, _p._ForegroundColor, _p._BackgroundColor, _p._GridColor, _p._Title, _p._ShowToolbar, _p._ShowLegend,
#             _p._XAxis, _p._YAxes, _p._Traces, _p._Markers):
#    pass
class XYPlot(_Widget, _p._ForegroundColor, _p._BackgroundColor, _p._ShowToolbar, _p._Title):
    """ XYPlot - Incomplete Widget """
    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create XYPlot Widget

        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'xyplot', name, x, y, width, height)

# Structure
class Array(_Widget, _p._PVName, _p._Macro, _p._ForegroundColor, _p._BackgroundColor, _p._AlarmBorder):
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
        _Widget.__init__(self, 'array', name, x, y, width, height)
        self.pv_name(pv_name)

class EmbeddedDisplay(_Widget, _p._Macro, _p._File, _p._ResizeBehavior, _p._GroupName, _p._Transparent, _p._Border):
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
        _Widget.__init__(self, 'embedded', name, x, y, width, height)
        self.file(file)

class Group(_Widget, _p._Structure, _p._Macro, _p._Style, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._Transparent):
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
        _Widget.__init__(self, 'group', name, x, y, width, height)

class NavigationTabs(_Widget, _p._NavTabs, _p._ActiveTab, _p._TabWidth, _p._TabSpacing, _p._TabHeight,
                     _p._SelectedColor, _p._DeselectedColor, _p._Direction, _p._Font):
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
        _Widget.__init__(self, 'navtabs', name, x, y, width, height)

class Tabs(_Widget, _p._Macro, _p._Tabs, _p._ActiveTab, _p._TabHeight, _p._Font, _p._BackgroundColor, _p._Direction):
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
        _Widget.__init__(self, 'tabs', name, x, y, width, height)

# Miscellaneous

class ThreeDViewer(_Widget, _p._File):
    """ ThreeDViewer Phoebus Widget """
    def __init__(self, name: str, file: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create ThreeDViewer Widget

        :param name: Widget name
        :param file: File path
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, '3dviewer', name, x, y, width, height)
        self.file(file)

class WebBrowser(_Widget, _p._URL, _p._ShowToolbar):
    """ WebBrowser Phoebus Widget """
    def __init__(self, name: str, url: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create WebBrowser Widget

        :param name: Widget name
        :param url: URL
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        _Widget.__init__(self, 'webbrowser', name, x, y, width, height)
        self.url(url)

