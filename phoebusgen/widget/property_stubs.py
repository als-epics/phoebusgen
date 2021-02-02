class _PVName(object):
    def pv_name(self, name):
        self._prop_factory.add_pv_name(name)


class _Font(object):
    def predefined_font(self, name):
        self._prop_factory.add_font(None, None, None, name)

    def font(self, family=None, style=None, size=None):
        self._prop_factory.add_font(family, style, size, None)


class _ForegroundColor(object):
    def predefined_foreground_color(self, name):
        self._prop_factory.add_foreground_color(name, None, None, None, None)

    def foreground_color(self, red, green, blue, alpha=255):
        self._prop_factory.add_foreground_color(None, red, green, blue, alpha)


class _BackgroundColor(object):
    def predefined_background_color(self, name):
        self._prop_factory.add_background_color(name, None, None, None, None)

    def background_color(self, red, green, blue, alpha=255):
        self._prop_factory.add_background_color(None, red, green, blue, alpha)


class _Transparent(object):
    def transparent(self, transparent=False):
        self._prop_factory.add_transparent(transparent)


class _Format(object):
    def format(self, format):
        self._prop_factory.add_format(format)


class _Precision(object):
    def precision(self, val):
        self._prop_factory.add_precision(val)

class _ShowUnits(object):
    def show_units(self, show=True):
        self._prop_factory.add_show_units(show)


class _HorizontalAlignment(object):
    def horizontal_alignment(self, val):
        self._prop_factory.add_horizontal_alignment(val)


class _VerticalAlignment(object):
    def vertical_alignment(self, val):
        self._prop_factory.add_vertical_alignment(val)


class _WrapWords(object):
    def wrap_words(self, wrap=True):
        self._prop_factory.add_wrap_words(wrap)


class _Text(object):
    def text(self, text):
        self._prop_factory.add_text(text)


class _AutoSize(object):
    def auto_size(self, auto=True):
        self._prop_factory.add_auto_size(auto)


# 0, 90, 180, -90
# text update, label, action button
class _RotationStep(object):
    def rotation_step(self, rotation):
        self._prop_factory.add_rotation_step(rotation)


class _Border(object):
    def border_width(self, width):
        self._prop_factory.add_border_width(width)

    def predefined_border_color(self, name):
        self._prop_factory.add_border_color(name, None, None, None, None)

    def border_color(self, red, green, blue, alpha=255):
        self._prop_factory.add_border_color(None, red, green, blue, alpha)


class _Macro(object):
    def macro(self, name, val):
        self._prop_factory.add_macro(name, val)


class _Bit(object):
    def bit(self, val=-1):
        self._prop_factory.add_bit(val)


class _OffColor(object):
    def predefined_off_color(self, name):
        self._prop_factory.add_off_color(name, None, None, None, None)

    def off_color(self, red, green, blue, alpha=255):
        self._prop_factory.add_off_color(None, red, green, blue, alpha)

class _Off(_OffColor):
    def off_label(self, label):
        self._prop_factory.add_off_label(label)

class _OffImage(_Off):
    def off_image(self):
        pass

class _OnColor(object):
    def predefined_on_color(self, name):
        self._prop_factory.add_on_color(name, None, None, None, None)

    def on_color(self, red, green, blue, alpha=255):
        self._prop_factory.add_on_color(None, red, green, blue, alpha)

class _On(_OnColor):
    def on_label(self, label):
        self._prop_factory.add_on_label(label)

class _OnImage(_On):
    def on_image(self):
        pass


# Arc, Ellipse, Polygon, Polyline, Rectangle, LED, LED Multi State
class _LineColor(object):
    def predefined_line_color(self, name):
        self._prop_factory.add_line_color(name, None, None, None, None)

    def line_color(self, red, green, blue, alpha=255):
        self._prop_factory.add_line_color(None, red, green, blue, alpha)


# Arc, Ellipse, Polygon, Polyline, Rectangle
class _LineWidth(object):
    def line_width(self, width):
        self._prop_factory.add_line_width(width)


# Rectangle
class _Corner(object):
    def corner_width(self, width):
        self._prop_factory.add_corner_width(width)

    def corner_height(self, height):
        self._prop_factory.add_corner_height(height)


class _Square(object):
    def square(self, val):
        self._prop_factory.add_square(val)


class _LabelsFromPV(object):
    def labels_from_pv(self, val):
        self._prop_factory.add_labels_from_pv(val)


class _AlarmBorder(object):
    def alarm_border(self, val):
        self._prop_factory.add_alarm_border(val)


class _Enabled(object):
    def enabled(self, val):
        self._prop_factory.add_enabled(val)


class _Confirmation(object):
    def confirmation_dialog(self, message, password=None):
        self._prop_factory.add_confirmation_dialog(True)
        self._prop_factory.add_confirmation_message(message)
        if password is not None:
            self._prop_factory.add_password(password)

    def disable_confirmation_dialog(self):
        self._prop_factory.add_confirmation_dialog(False)


class _MultiLine(object):
    def multi_line(self, val):
        self._prop_factory.add_multi_line(val)


class _Angle(object):
    def angle_start(self, val):
        self._prop_factory.add_angle_start(val)

    def angle_size(self, val):
        self._prop_factory.add_angle_size(val)

# picture, symbol
class _Rotation(object):
    def rotation(self, val):
        self._prop_factory.add_rotation(val)


class _File(object):
    def file(self, val):
        self._prop_factory.add_file(val)

class _StretchToFit(object):
    def stretch_to_fit(self, val):
        self._prop_factory.add_stretch_to_fit(val)

class _Actions(object):
    def action_execute_as_one(self, val):
        self._prop_factory.add_action_execute_as_one(val)

    def action_open_display(self, file, target, description=None):
        # still needs macros
        if description is None:
            description = 'Open Display'
        possible_targets = ['tab', 'replace', 'window']
        if target.lower() not in possible_targets:
            print('Target must be one of {}, not: {}'.format(possible_targets, target))
            return
        args = {'file': file, 'target': target.lower()}
        self._prop_factory.add_action('open_display', description, args)

    def action_write_pv(self, pv_name, value, description=None):
        if description is None:
            description = 'Write PV'
        args = {'pv_name': pv_name, 'value': value}
        self._prop_factory.add_action('write_pv', description, args)

    def action_execute_command(self, command, description=None):
        if description is None:
            description = 'Execute Command'
        args = {'command': command}
        self._prop_factory.add_action('command', description, args)

    def action_open_file(self, file, description=None):
        if description is None:
            description = 'Open File'
        args = {'file': file}
        self._prop_factory.add_action('open_file', description, args)

    def action_open_webpage(self, url, description=None):
        if description is None:
            description = 'Open Webpage'
        args = {'url': url}
        self._prop_factory.add_action('open_webpage', description, args)

class _Label(object):
    def label(self, val):
        self._prop_factory.add_label(val)

class _Horizontal(object):
    def horizontal(self, val):
        self._prop_factory.add_horizontal(val)

class _Items(object):
    def item(self, val):
        self._prop_factory.add_item(val)

class _ItemsFromPV(object):
    def items_from_pv(self, val):
        self._prop_factory.add_items_from_pv(val)

class _StartBit(object):
    pass

class _NumBits(object):
    pass

class _ReverseBits(object):
    pass

class _States(object):
    pass

class _Fallback(object):
    pass

class _ShowValue(object):
    pass

class _ShowLimits(object):
    pass

class _LimitsFromPV(object):
    def limits_from_pv(self, val):
        self._prop_factory.add_limits_from_pv(val)

class _MinMax(object):
    def minimum(self, val):
        self._prop_factory.add_minimum(val)

    def maximum(self, val):
        self._prop_factory.add_maximum(val)

class _NeedleColor(object):
    pass

class _KnobColor(object):
    pass

class _FillColor(object):
    def fill_color(self, red, green, blue, alpha=255):
        self._prop_factory.add_fill_color(None, red, green, blue, alpha)

    def predefined_fill_color(self, name):
        self._prop_factory.add_fill_color(name, None, None, None, None)

class _EmptyColor(object):
    def empty_color(self, red, green, blue, alpha=255):
        self._prop_factory.add_empty_color(None, red, green, blue, alpha)

    def predefined_empty_color(self, name):
        self._prop_factory.add_empty_color(name, None, None, None, None)

class _ScaleVisible(object):
    def scale_visible(self, val):
        self._prop_factory.add_scale_visible(val)

class _ShowLED(object):
    pass

class _Mode(object):
    pass

class _Style(object):
    def group_box(self):
        self._prop_factory.add_style('group box')

    def title_bar(self):
        self._prop_factory.add_style('title bar')

    def line(self):
        self._prop_factory.add_style('line')

    def no_style(self):
        self._prop_factory.add_style('none')


class _ResizeBehavior(object):
    def no_resize(self):
        self._prop_factory.add_resize_behavior('no resize')

    def size_content_to_fit_widget(self):
        self._prop_factory.add_resize_behavior('size content to fit widget')

    def size_widget_to_match_content(self):
        self._prop_factory.add_resize_behavior('size widget to match content')

    def stretch_content_to_fit_widget(self):
        self._prop_factory.add_resize_behavior('stretch content to fit widget')

    def crop_content(self):
        self._prop_factory.add_resize_behavior('crop content')


class _GroupName(object):
    def group_name(self, val):
        self._prop_factory.add_group_name(val)


class _Structure(object):
    def add_widget(self, elem):
        if type(elem) == list:
            for e in elem:
                self._prop_factory.root.append(e.root)
        else:
            self._prop_factory.root.append(elem.root)
