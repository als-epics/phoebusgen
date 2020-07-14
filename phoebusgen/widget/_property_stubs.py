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


class File(object):
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
    def bit(self, val=-1):
        self.prop_factory.add_bit(val)


class Off(object):
    def predefined_off_color(self, name):
        self.prop_factory.add_off_color(name, None, None, None, None)

    def off_color(self, red, green, blue, alpha=255):
        self.prop_factory.add_off_color(None, red, green, blue, alpha)

    def off_label(self, label):
        self.prop_factory.add_off_label(label)


class On(object):
    def predefined_on_color(self, name):
        self.prop_factory.add_on_color(name, None, None, None, None)

    def on_color(self, red, green, blue, alpha=255):
        self.prop_factory.add_on_color(None, red, green, blue, alpha)

    def on_label(self, label):
        self.prop_factory.add_on_label(label)


# Arc, Ellipse, Polygon, Polyline, Rectangle, LED, LED Multi State
class LineColor(object):
    def predefined_line_color(self, name):
        self.prop_factory.add_line_color(name, None, None, None, None)

    def line_color(self, red, green, blue, alpha=255):
        self.prop_factory.add_line_color(None, red, green, blue, alpha)


# Arc, Ellipse, Polygon, Polyline, Rectangle
class LineWidth(object):
    def line_width(self, width):
        self.prop_factory.add_line_width(width)


# Rectangle
class Corner(object):
    def corner_width(self, width):
        self.prop_factory.add_corner_width(width)

    def corner_height(self, height):
        self.prop_factory.add_corner_height(height)


class Square(object):
    def square(self, val):
        self.prop_factory.add_square(val)


class LabelsFromPV(object):
    def labels_from_pv(self, val):
        self.prop_factory.add_labels_from_pv(val)


class AlarmBorder(object):
    def alarm_border(self, val):
        self.prop_factory.add_alarm_border(val)


class Enabled(object):
    def enabled(self, val):
        self.prop_factory.add_enabled(val)


class Confirmation(object):
    def confirmation_dialog(self, message, password=None):
        self.prop_factory.add_confirmation_dialog(True)
        self.prop_factory.add_confirmation_message(message)
        if password is not None:
            self.prop_factory.add_password(password)


class MultiLine(object):
    def multi_line(self, val):
        self.prop_factory.add_multi_line(val)


class Angle(object):
    def angle_start(self, val):
        self.prop_factory.add_angle_start(val)

    def angle_size(self, val):
        self.prop_factory.add_angle_size(val)