class PVName(object):
    def add_pv_name(self, name):
        self.prop_factory.add_pv_name(name)


class Font(object):
    def add_predefined_font(self, name):
        self.prop_factory.add_font(None, None, None, name)

    def add_font(self, family=None, style=None, size=None):
        self.prop_factory.add_font(family, style, size, None)


class ForegroundColor(object):
    def add_predefined_foreground_color(self, name):
        self.prop_factory.add_foreground_color(name, None, None, None, None)

    def add_foreground_color(self, red, green, blue, alpha=255):
        self.prop_factory.add_foreground_color(None, red, green, blue, alpha)


class BackgroundColor(object):
    def add_predefined_background_color(self, name):
        self.prop_factory.add_background_color(name, None, None, None, None)

    def add_background_color(self, red, green, blue, alpha=255):
        self.prop_factory.add_background_color(None, red, green, blue, alpha)


class Transparent(object):
    def add_transparent(self, transparent=False):
        self.prop_factory.add_transparent(transparent)


class Format(object):
    def add_format(self, format):
        self.prop_factory.add_format(format)


class Precision(object):
    def add_precision(self, val):
        self.prop_factory.add_precision(val)

class ShowUnits(object):
    def add_show_units(self, show=True):
        self.prop_factory.add_show_units(show)


class HorizontalAlignment(object):
    def add_horizontal_alignment(self, val):
        self.prop_factory.add_horizontal_alignment(val)


class VerticalAlignment(object):
    def add_vertical_alignment(self, val):
        self.prop_factory.add_vertical_alignment(val)


class WrapWords(object):
    def add_wrap_words(self, wrap=True):
        self.prop_factory.add_wrap_words(wrap)


class Text(object):
    def add_text(self, text):
        self.prop_factory.add_text(text)


class AutoSize(object):
    def add_auto_size(self, auto=True):
        self.prop_factory.add_auto_size(auto)


# 0, 90, 180, -90
# text update, label, action button
class RotationStep(object):
    def add_rotation_step(self, rotation):
        self.prop_factory.add_rotation_step(rotation)


# picture, symbol
class Rotation(object):
    pass


class Border(object):
    def add_border_width(self, width):
        self.prop_factory.add_border_width(width)

    def add_predefined_border_color(self, name):
        self.prop_factory.add_border_color(name, None, None, None, None)

    def add_border_color(self, red, green, blue, alpha=255):
        self.prop_factory.add_border_color(None, red, green, blue, alpha)
