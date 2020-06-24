class PVName(object):
    def pv_name(self, name):
        self.prop_factory.add_pv_name(name)


class Font(object):
    def predefined_font(self, name):
        self.prop_factory.add_font(None, None, None, name)

    def font(self, family=None, style=None, size=None):
        self.prop_factory.add_font(family, style, size, None)


class ForegroundColor(object):
    def predefined_foreground_color(self, name):
        self.prop_factory.add_foreground_color(name, None, None, None, None)

    def foreground_color(self, red, green, blue, alpha=255):
        self.prop_factory.add_foreground_color(None, red, green, blue, alpha)


class BackgroundColor(object):
    def predefined_background_color(self, name):
        self.prop_factory.add_background_color(name, None, None, None, None)

    def background_color(self, red, green, blue, alpha=255):
        self.prop_factory.add_background_color(None, red, green, blue, alpha)


class Transparent(object):
    def transparent(self, transparent=False):
        self.prop_factory.add_transparent(transparent)


class Format(object):
    def format(self, format):
        self.prop_factory.add_format(format)


class Precision(object):
    def precision(self, val):
        self.prop_factory.add_precision(val)

class ShowUnits(object):
    def show_units(self, show=True):
        self.prop_factory.add_show_units(show)


class HorizontalAlignment(object):
    def horizontal_alignment(self, val):
        self.prop_factory.add_horizontal_alignment(val)


class VerticalAlignment(object):
    def vertical_alignment(self, val):
        self.prop_factory.add_vertical_alignment(val)


class WrapWords(object):
    def wrap_words(self, wrap=True):
        self.prop_factory.add_wrap_words(wrap)


class Text(object):
    def text(self, text):
        self.prop_factory.add_text(text)


class AutoSize(object):
    def auto_size(self, auto=True):
        self.prop_factory.add_auto_size(auto)


# 0, 90, 180, -90
# text update, label, action button
class RotationStep(object):
    def rotation_step(self, rotation):
        self.prop_factory.add_rotation_step(rotation)


# picture, symbol
class Rotation(object):
    pass


class Border(object):
    def border_width(self, width):
        self.prop_factory.add_border_width(width)

    def predefined_border_color(self, name):
        self.prop_factory.add_border_color(name, None, None, None, None)

    def border_color(self, red, green, blue, alpha=255):
        self.prop_factory.add_border_color(None, red, green, blue, alpha)


class Macro(object):
    def macro(self, name, val):
        self.prop_factory.add_macro(name, val)


class Bit(object):
    pass


class Off(object):
    pass


class On(object):
    pass


class LineColor(object):
    pass


class Square(object):
    pass


class LabelsFromPV(object):
    pass


class AlarmBorder(object):
    pass


class Enabled(object):
    pass


# dialog, message, password
class Confirmation(object):
    pass


class MultiLine(object):
    def multi_line(self, val):
        self.prop_factory.add_multi_line(val)
