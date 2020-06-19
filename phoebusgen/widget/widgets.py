from xml.etree.ElementTree import Element, SubElement, tostring
from widget import Widget
from _property_stubs import *


class Label(Widget, Text, Font, ForegroundColor, BackgroundColor, Transparent, HorizontalAlignment,
            RotationStep, WrapWords, AutoSize, Border):
    def __init__(self, name, x, y, width, height, text):
        super().__init__('label', name, x, y, width, height)

        self.add_text(text)


class TextUpdate(Widget, PVName, Font, ForegroundColor, BackgroundColor, Transparent,
                 Format, Precision, ShowUnits, HorizontalAlignment, VerticalAlignment, WrapWords,
                 RotationStep, Border):
    def __init__(self, name, pv_name, x, y, width, height):
        Widget.__init__(self, 'textupdate', name, x, y, width, height)
        self.add_pv_name(pv_name)


if __name__ == '__main__':
    pass
