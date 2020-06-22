import phoebusgen.widget._widget as _w
import phoebusgen.widget._property_stubs as _p

# Displays

class Label(_w.Widget, _p.Text, _p.Macro, _p.Font, _p.ForegroundColor, _p.BackgroundColor, _p.Transparent, _p.HorizontalAlignment,
            _p.VerticalAlignment, _p.RotationStep, _p.WrapWords, _p.AutoSize, _p.Border):
    """ Label widget, req: text """
    def __init__(self, name, text, x, y, width, height):
        _w.Widget.__init__(self, 'label', name, x, y, width, height)

        self.text(text)

# Monitors

class TextUpdate(_w.Widget, _p.PVName, _p.Font, _p.ForegroundColor, _p.BackgroundColor, _p.Transparent,
                 _p.Format, _p.Precision, _p.ShowUnits, _p.HorizontalAlignment, _p.VerticalAlignment, _p.WrapWords,
                 _p.RotationStep, _p.Border):
    """ Text Update widget, req: pv name """
    def __init__(self, name, pv_name, x, y, width, height):
        _w.Widget.__init__(self, 'textupdate', name, x, y, width, height)
        self.pv_name(pv_name)

# Class, Bit, Off Label, Off Color, On Label, On Color, Line Color, Square, Labels from PV,
# Alarm border
class LED(_w.Widget, _p.PVName, _p.Bit, _p.Off, _p.On, _p.Font, _p.ForegroundColor, _p.LineColor,
          _p.Square, _p.LabelsFromPV, _p.AlarmBorder):
    """ LED widget, req: None """
    pass

# Controls
# Actions, Rotation, Enabled, Confirmation Dialog, Confirmation Message, Password
class ActionButton(_w.Widget, _p.PVName, _p.Text, _p.Font, _p.ForegroundColor, _p.BackgroundColor,
                   _p.Transparent, _p.Rotation, _p.Enabled, _p.Confirmation):
    """ Action button widget, req: None """
    pass

# Multi-Line
class TextEntry(_w.Widget, _p.PVName, _p.Font, _p.ForegroundColor, _p.BackgroundColor, _p.Format,
                _p.Precision, _p.ShowUnits, _p.WrapWords, _p.MultiLine, _p.AlarmBorder, _p.Enabled,
                _p.Border):
    """ Text Entry widget, req: pv name """
    pass


if __name__ == '__main__':
    pass
