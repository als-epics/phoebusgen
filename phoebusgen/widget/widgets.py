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

class Rectangle(_Widget, _p._Macro, _p._LineWidth, _p._LineColor, _p._BackgroundColor, _p._Transparent, _p._Corner):
    """ Rectangle widget, req: none """
    def __init__(self, name, x, y, width, height):
        _Widget.__init__(self, 'rectangle', name, x, y, width, height)

# Monitors
# Start bit, number of bits, reverse bits, horizontal, labels
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
#class LEDMultiState(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._LineColor, _p._Square, _p._AlarmBorder, _p._States, _p._Fallback):
#    pass


# ShowValue, ShowLimits, LimitsFromPV, Minimum, Maximum, NeedleColor, KnobColor
#class Meter(_Widget, _p._PVName, _p._ForegroundColor, _p._BackgroundColor, _p._Font, _p._Format, _p._Precision, _p._ShowValue,
#            _p._ShowUnits, _p._ShowLimits, _p._AlarmBorder, _p._LimitsFromPV, _p._Minimum, _p._Maximum, _p._NeedleColor, _p._KnobColor):
#    pass

# FillColor, minimum, maximum, limitsfrompv
#class ProgressBar(_Widget, _p._PVName, _p._FillColor, _p._BackgroundColor, _p._Horizontal, _p._AlarmBorder, _p._LimitsFromPV,
#                  _p._Minimum, _p._Maximum):
#    pass

# fillcolor, min, max, limits, scalevisible, emptycolor
#class Tank(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._FillColor, _p._EmptyColor, _p._ScaleVisible,
#           _p._AlarmBorder, _p._LimitsFromPV, _p._Minimum, _p._Maximum):
#    pass

class TextUpdate(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._Transparent,
                 _p._Format, _p._Precision, _p._ShowUnits, _p._HorizontalAlignment, _p._VerticalAlignment, _p._WrapWords,
                 _p._RotationStep, _p._Border):
    """ Text Update widget, req: pv name """
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'textupdate', name, x, y, width, height)
        self.pv_name(pv_name)

#class Thermometer(_Widget, _p._PVName, _p._FillColor, _p._AlarmBorder, _p._LimitsFromPV, _p._Minimum, _p._Maximum):
#    pass

# Controls
class ActionButton(_Widget, _p._PVName, _p._Actions, _p._Text, _p._Font, _p._ForegroundColor, _p._BackgroundColor,
                   _p._Transparent, _p._RotationStep, _p._Enabled, _p._Confirmation):
    """ Action button widget, req: text, pv name """
    def __init__(self, name, text, pv_name, x, y, width, height):
        _Widget.__init__(self, 'action_button', name, x, y, width, height)
        self.pv_name(pv_name)
        self.text(text)

#class BooleanButton(_Widget, _p._PVName, _p._Bit, _p._OffImage, _p._OnImage, _p._ShowLED, _p._Font, _p._ForegroundColor, _p._BackgroundColor,
#                    _p._LabelsFromPV, _p._AlarmBorder, _p._Enabled, _p._Mode, _p._Confirmation):
#    pass

# Bit, PVname, label, font, foreground color, auto-size, alarm border, enabled, confirm
class CheckBox(_Widget, _p._PVName, _p._Bit, _p._Label, _p._Font, _p._ForegroundColor, _p._AutoSize,
               _p._AlarmBorder, _p._Confirmation):
    def __init__(self, name, label, pv_name, x, y, width, height):
        _Widget.__init__(self, 'checkbox', name, x, y, width, height)
        self.pv_name(pv_name)
        self.label(label)

#class ChoiceButton():
#    pass

#class ComboBox():
#    pass

#class FileSelector():
#    pass

# horizontal, items, itemsfrompv
class RadioButton(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._Horizontal, _p._AlarmBorder,
                  _p._Items, _p._ItemsFromPV, _p._Enabled, _p._Confirmation):
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'radio', name, x, y, width, height)
        self.pv_name(pv_name)
        self.horizontal(True)
        self.items_from_pv(True)

#class ScaledSlider():
#    pass

class TextEntry(_Widget, _p._PVName, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._Format,
                _p._Precision, _p._ShowUnits, _p._WrapWords, _p._MultiLine, _p._AlarmBorder, _p._Enabled,
                _p._Border):
    """ Text Entry widget, req: pv name """
    def __init__(self, name, pv_name, x, y, width, height):
        _Widget.__init__(self, 'textentry', name, x, y, width, height)
        self.pv_name(pv_name)

# Structure

# ResizeBehavior, Group Name
class EmbeddedDisplay(_Widget, _p._Macro, _p._File, _p._ResizeBehavior, _p._GroupName, _p._Transparent, _p._Border):
    def __init__(self, name, file, x, y, width, height):
        _Widget.__init__(self, 'embedded', name, x, y, width, height)
        self.file(file)
        self.no_resize()


class Group(_Widget, _p._Macro, _p._Style, _p._Font, _p._ForegroundColor, _p._BackgroundColor, _p._Transparent):
    def __init__(self, name, x, y, width, height):
        _Widget.__init__(self, 'group', name, x, y, width, height)
        self.group_box()


#class Tabs():
#    pass


if __name__ == '__main__':
    pass

