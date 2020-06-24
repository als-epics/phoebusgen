from phoebusgen.widget._widget import Widget
from phoebusgen.widget._property_stubs import *

# Displays

class Label(Widget, Text, Macro, Font, ForegroundColor, BackgroundColor, Transparent, HorizontalAlignment,
            VerticalAlignment, RotationStep, WrapWords, AutoSize, Border):
    """ Label widget, req: text """
    def __init__(self, name, text, x, y, width, height):
        Widget.__init__(self, 'label', name, x, y, width, height)

        self.text(text)

# Monitors

class TextUpdate(Widget, PVName, Font, ForegroundColor, BackgroundColor, Transparent,
                 Format, Precision, ShowUnits, HorizontalAlignment, VerticalAlignment, WrapWords,
                 RotationStep, Border):
    """ Text Update widget, req: pv name """
    def __init__(self, name, pv_name, x, y, width, height):
        Widget.__init__(self, 'textupdate', name, x, y, width, height)
        self.pv_name(pv_name)

# Class, Bit, Off Label, Off Color, On Label, On Color, Line Color, Square, Labels from PV,
# Alarm border
class LED(Widget, PVName, Bit, Off, On, Font, ForegroundColor, LineColor,
          Square, LabelsFromPV, AlarmBorder):
    """ LED widget, req: None """
    pass

# Controls
# Actions, Rotation, Enabled, Confirmation Dialog, Confirmation Message, Password
class ActionButton(Widget, PVName, Text, Font, ForegroundColor, BackgroundColor,
                   Transparent, Rotation, Enabled, Confirmation):
    """ Action button widget, req: None """
    pass


class TextEntry(Widget, PVName, Font, ForegroundColor, BackgroundColor, Format,
                Precision, ShowUnits, WrapWords, MultiLine, AlarmBorder, Enabled,
                Border):
    """ Text Entry widget, req: pv name """
    def __init__(self, name, pv_name, x, y, width, height):
        Widget.__init__(self, 'textentry', name, x, y, width, height)
        self.pv_name(pv_name)


if __name__ == '__main__':
    pass

