class _PVName(object):
    def pv_name(self, name):
        self._prop_factory.add_pv_name(name)


class _Font(object):
    def predefined_font(self, name):
        self._prop_factory.add_named_font(name)

    def font_family(self, family):
        self._prop_factory.add_font_family(family)

    def font_size(self, size):
        self._prop_factory.add_font_size(size)

    def font_style_bold(self):
        self._prop_factory.add_font_style(self._prop_factory.FontStyle.bold)

    def font_style_italic(self):
        self._prop_factory.add_font_style(self._prop_factory.FontStyle.italic)

    def font_style_bold_italic(self):
        self._prop_factory.add_font_style(self._prop_factory.FontStyle.bold_and_italic)

    def font_style_regular(self):
        self._prop_factory.add_font_style(self._prop_factory.FontStyle.regular)

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
    def horizontal_alignment_left(self):
        self._prop_factory.add_horizontal_alignment(self._prop_factory.HorizontalAlignment.left)

    def horizontal_alignment_center(self):
        self._prop_factory.add_horizontal_alignment(self._prop_factory.HorizontalAlignment.center)

    def horizontal_alignment_right(self):
        self._prop_factory.add_horizontal_alignment(self._prop_factory.HorizontalAlignment.right)

class _VerticalAlignment(object):
    def vertical_alignment_top(self):
        self._prop_factory.add_vertical_alignment(self._prop_factory.VerticalAlignment.top)

    def vertical_alignment_middle(self):
        self._prop_factory.add_vertical_alignment(self._prop_factory.VerticalAlignment.middle)

    def vertical_alignment_bottom(self):
        self._prop_factory.add_vertical_alignment(self._prop_factory.VerticalAlignment.bottom)


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
    def rotation_step_0(self):
        self._prop_factory.add_rotation_step(self._prop_factory.RotationStep.zero)

    def rotation_step_90(self):
        self._prop_factory.add_rotation_step(self._prop_factory.RotationStep.ninety)

    def rotation_step_180(self):
        self._prop_factory.add_rotation_step(self._prop_factory.RotationStep.one_hundred_eighty)

    def rotation_step_negative_90(self):
        self._prop_factory.add_rotation_step(self._prop_factory.RotationStep.negative_ninety)

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
    def off_image(self, val):
        self._prop_factory.add_off_image(val)

class _OnColor(object):
    def predefined_on_color(self, name):
        self._prop_factory.add_on_color(name, None, None, None, None)

    def on_color(self, red, green, blue, alpha=255):
        self._prop_factory.add_on_color(None, red, green, blue, alpha)

class _On(_OnColor):
    def on_label(self, label):
        self._prop_factory.add_on_label(label)

class _OnImage(_On):
    def on_image(self, val):
        self._prop_factory.add_on_image(val)


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

class _ShowValueTip(object):
    def show_value_tip(self, val):
        self._prop_factory.add_show_value_tip(val)

class _BarLength(object):
    def bar_length(self, val):
        self._prop_factory.add_bar_length(val)

class _ShowValue(object):
    def show_value(self, val):
        self._prop_factory.add_show_value(val)

class _ShowLimits(object):
    def show_limits(self, val):
        self._prop_factory.add_show_limits(val)

class _LimitsFromPV(object):
    def limits_from_pv(self, val):
        self._prop_factory.add_limits_from_pv(val)

class _MinMax(object):
    def minimum(self, val):
        self._prop_factory.add_minimum(val)

    def maximum(self, val):
        self._prop_factory.add_maximum(val)

class _NeedleColor(object):
    def needle_color(self, red, green, blue, alpha=255):
        self._prop_factory.add_needle_color(None, red, green, blue, alpha)

    def predefined_needle_color(self, name):
        self._prop_factory.add_needle_color(name, None, None, None, None)

class _KnobColor(object):
    def knob_color(self, red, green, blue, alpha=255):
        self._prop_factory.add_knob_color(None, red, green, blue, alpha)

    def predefined_knob_color(self, name):
        self._prop_factory.add_knob_color(name, None, None, None, None)

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
    def show_led(self, val):
        self._prop_factory.add_show_led(val)

class _Mode(object):
    def mode_toggle(self):
        self._prop_factory.add_mode(self._prop_factory.Mode.toggle)

    def mode_push(self):
        self._prop_factory.add_mode(self._prop_factory.Mode.push)

    def mode_push_inverted(self):
        self._prop_factory.add_mode(self._prop_factory.Mode.push_inverted)

class _Style(object):
    def style_group_box(self):
        self._prop_factory.add_style(self._prop_factory.GroupStyle.group_box)

    def style_title_bar(self):
        self._prop_factory.add_style(self._prop_factory.GroupStyle.title_bar)

    def style_line(self):
        self._prop_factory.add_style(self._prop_factory.GroupStyle.line)

    def no_style(self):
        self._prop_factory.add_style(self._prop_factory.GroupStyle.none)


class _ResizeBehavior(object):
    def no_resize(self):
        self._prop_factory.add_resize_behavior(self._prop_factory.Resize.no_resize)

    def size_content_to_fit_widget(self):
        self._prop_factory.add_resize_behavior(self._prop_factory.Resize.size_content_to_fit_widget)

    def size_widget_to_match_content(self):
        self._prop_factory.add_resize_behavior(self._prop_factory.Resize.size_widget_to_match_content)

    def stretch_content_to_fit_widget(self):
        self._prop_factory.add_resize_behavior(self._prop_factory.Resize.stretch_content_to_fit_widget)

    def crop_content(self):
        self._prop_factory.add_resize_behavior(self._prop_factory.Resize.crop_content)


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

class _URL(object):
    def url(self, url):
        self._prop_factory.add_url(url)

class _ShowToolbar(object):
    def show_toolbar(self, val):
        self._prop_factory.add_show_toolbar(val)

class _ButtonsOnLeft(object):
    def buttons_on_left(self, val):
        self._prop_factory.add_buttons_on_left(val)

class _Increment(object):
    def increment(self, val):
        self._prop_factory.add_increment(val)

class _FileComponent(object):
    def file_component_full_path(self):
        self._prop_factory.add_file_component(self._prop_factory.FileComponent.full_path)

    def file_component_directory(self):
        self._prop_factory.add_file_component(self._prop_factory.FileComponent.directory)

    def file_component_name_and_extension(self):
        self._prop_factory.add_file_component(self._prop_factory.FileComponent.name_and_extension)

    def file_component_base_name(self):
        self._prop_factory.add_file_component(self._prop_factory.FileComponent.base_name)

class _Editable(object):
    def editable(self, val):
        self._prop_factory.add_editable(val)

class _SelectedColor(object):
    def selected_color(self, red, green, blue, alpha=255):
        self._prop_factory.add_selected_color(None, red, green, blue, alpha)

    def predefined_selected_color(self, name):
        self._prop_factory.add_selected_color(name, None, None, None, None)

class _SelectionValuePV(object):
    def selection_value_pv(self, val):
        self._prop_factory.add_selection_value_pv(val)