from phoebusgen.widget._widget import Widget
from phoebusgen.widget._property_stubs import *

# Displays
class Arc(Widget, Macro, Angle, LineWidth, LineColor, BackgroundColor, Transparent):
    """ Arc widget, req: none """
    def __init__(self, name, x, y, width, height):
        Widget.__init__(self, 'arc', name, x, y, width, height)

class Ellipse(Widget, Macro, LineWidth, LineColor, BackgroundColor, Transparent):
    """ Ellipse widget, req: none """
    def __init__(self, name, x, y, width, height):
        Widget.__init__(self, 'ellipse', name, x, y, width, height)

class Label(Widget, Text, Macro, Font, ForegroundColor, BackgroundColor, Transparent, HorizontalAlignment,
            VerticalAlignment, RotationStep, WrapWords, AutoSize, Border):
    """ Label widget, req: text """
    def __init__(self, name, text, x, y, width, height):
        Widget.__init__(self, 'label', name, x, y, width, height)

        self.text(text)

# TODO: File, Stretch to Fit, Rotation
class Picture(Widget, Macro, File, StretchToFit, Rotation):
    pass

class Rectangle(Widget, Macro, LineWidth, LineColor, BackgroundColor, Transparent, Corner):
    """ Rectangle widget, req: none """
    def __init__(self, name, x, y, width, height):
        Widget.__init__(self, 'rectangle', name, x, y, width, height)

# Monitors
# Start bit, number of bits, reverse bits, horizontal, labels
class ByteMonitor(Widget, PVName, StartBit, NumBits, ReverseBits, Horizontal, Square, OffColor, OnColor,
                  ForegroundColor, Font, Labels, AlarmBorder):
    pass

class LED(Widget, PVName, Bit, Off, On, Font, ForegroundColor, LineColor,
          Square, LabelsFromPV, AlarmBorder):
    """ LED widget, req: None """
    def __init__(self, name, pv_name, x, y, width, height):
        Widget.__init__(self, 'led', name, x, y, width, height)
        self.pv_name(pv_name)

# States, Fallback
class LEDMultiState(Widget, PVName, Font, ForegroundColor, LineColor, Square, AlarmBorder, States, Fallback):
    pass


# ShowValue, ShowLimits, LimitsFromPV, Minimum, Maximum, NeedleColor, KnobColor
class Meter(Widget, PVName, ForegroundColor, BackgroundColor, Font, Format, Precision, ShowValue,
            ShowUnits, ShowLimits, AlarmBorder, LimitsFromPV, Minimum, Maximum, NeedleColor, KnobColor):
    pass

# FillColor
class ProgressBar(Widget, PVName, FillColor, BackgroundColor, Horizontal, AlarmBorder, LimitsFromPV,
                  Minimum, Maximum):
    pass

class Tank(Widget, PVName, Font, ForegroundColor, BackgroundColor, FillColor, EmptyColor, ScaleVisible,
           AlarmBorder, LimitsFromPV, Minimum, Maximum):
    pass

class TextUpdate(Widget, PVName, Font, ForegroundColor, BackgroundColor, Transparent,
                 Format, Precision, ShowUnits, HorizontalAlignment, VerticalAlignment, WrapWords,
                 RotationStep, Border):
    """ Text Update widget, req: pv name """
    def __init__(self, name, pv_name, x, y, width, height):
        Widget.__init__(self, 'textupdate', name, x, y, width, height)
        self.pv_name(pv_name)

class Thermometer(Widget, PVName, FillColor, AlarmBorder, LimitsFromPV, Minimum, Maximum):
    pass

# Controls
class ActionButton(Widget, PVName, Text, Font, ForegroundColor, BackgroundColor,
                   Transparent, RotationStep, Enabled, Confirmation):
    """ Action button widget, req: text, pv name """
    def __init__(self, name, text, pv_name, x, y, width, height):
        Widget.__init__(self, 'action_button', name, x, y, width, height)
        self.pv_name(pv_name)
        self.text(text)

class BooleanButton(Widget, PVName, Bit, OffImage, OnImage, ShowLED, Font, ForegroundColor, BackgroundColor,
                    LabelsFromPV, AlarmBorder, Enabled, Mode, Confirmation):
    pass

class CheckBox():
    pass

class ChoiceButton():
    pass

class ComboBox():
    pass

class FileSelector():
    pass

class RadioButton():
    pass

class ScaledSlider():
    pass

class TextEntry(Widget, PVName, Font, ForegroundColor, BackgroundColor, Format,
                Precision, ShowUnits, WrapWords, MultiLine, AlarmBorder, Enabled,
                Border):
    """ Text Entry widget, req: pv name """
    def __init__(self, name, pv_name, x, y, width, height):
        Widget.__init__(self, 'textentry', name, x, y, width, height)
        self.pv_name(pv_name)

# Structure
class EmbeddedDisplay(Macro, File, ResizeBehavior, GroupName, Transparent, Border):
    pass

class Group(Widget, Macro, Style, Font, ForegroundColor, BackgroundColor, Transparent):
    pass

class Tabs():
    pass


if __name__ == '__main__':
    pass

