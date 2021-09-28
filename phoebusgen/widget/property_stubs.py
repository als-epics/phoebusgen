from xml.etree.ElementTree import Element, SubElement

class _PVName(object):
    def pv_name(self, name):
        self._shared.generic_property('pv_name', name)

class _Font(object):
    def _get_font_element(self):
        font_root_elem = self.root.find('font')
        if font_root_elem is None:
            font_root_elem = self._shared.create_element('font')
            self.root.append(font_root_elem)
        child_font_elem = font_root_elem.find('font')
        if child_font_elem is None:
            child_font_elem = Element('font')
            child_font_elem.attrib = {'family': 'Liberation Sans', 'size': '14', 'style': 'REGULAR'}
            font_root_elem.append(child_font_elem)
        return child_font_elem

    def _add_font_style(self, val):
        if type(val) != self._shared.FontStyle:
            print('The font style parameter must be of type FontStyle enum! Not: {}'.format(type(val)))
            return
        child_elem = self._get_font_element()
        child_elem.attrib['style'] = val.value

    def predefined_font(self, name):
        self._shared.create_named_font_elemet(name)

    def font_family(self, family):
        child_elem = self._get_font_element()
        child_elem.attrib['family'] = str(family)

    def font_size(self, size):
        if type(size) == int or type(size) == float:
            child_elem = self._get_font_element()
            child_elem.attrib['size'] = str(int(size))
        else:
            print('Font size must be a number! Not: {}'.format(size))

    def font_style_bold(self):
        self._add_font_style(self._shared.FontStyle.bold)

    def font_style_italic(self):
        self._add_font_style(self._shared.FontStyle.italic)

    def font_style_bold_italic(self):
        self._add_font_style(self._shared.FontStyle.bold_and_italic)

    def font_style_regular(self):
        self._add_font_style(self._shared.FontStyle.regular)

class _ForegroundColor(object):
    def predefined_foreground_color(self, name):
        e = self._shared.create_element('foreground_color')
        self._shared.create_color_element(e, name, None, None, None, None)

    def foreground_color(self, red, green, blue, alpha=255):
        e = self._shared.create_element('foreground_color')
        self._shared.create_color_element(e, None, red, green, blue, alpha)

class _BackgroundColor(object):
    def predefined_background_color(self, name):
        e = self._shared.create_element('background_color')
        self._shared.create_color_element(e, name, None, None, None, None)

    def background_color(self, red, green, blue, alpha=255):
        e = self._shared.create_element('background_color')
        self._shared.create_color_element(e, None, red, green, blue, alpha)

class _Transparent(object):
    def transparent(self, transparent=False):
        self._shared.boolean_property('transparent', transparent)

class _Format(object):
    def format(self, format_val):
        val = str(format_val).lower()
        try:
            v = self._shared.formats_array.index(val)
        except ValueError:
            print('Invalid format. Given format {}'.format(format_val))
            return
        self._shared.generic_property('format', v)

class _Precision(object):
    def precision(self, val):
        self._shared.integer_property('precision', val)

class _ShowUnits(object):
    def show_units(self, show=True):
        self._shared.boolean_property('show_units', show)

class _HorizontalAlignment(object):
    def _add_horizontal_alignment(self, alignment):
        if type(alignment) != self._shared.HorizontalAlignment:
            print('The component parameter must be of type HorizontalAlignment enum! Not: {}'.format(type(alignment)))
            return
        self._shared.generic_property('horizontal_alignment', alignment.value)

    def horizontal_alignment_left(self):
        self._add_horizontal_alignment(self._shared.HorizontalAlignment.left)

    def horizontal_alignment_center(self):
        self._add_horizontal_alignment(self._shared.HorizontalAlignment.center)

    def horizontal_alignment_right(self):
        self._add_horizontal_alignment(self._shared.HorizontalAlignment.right)

class _VerticalAlignment(object):
    def _add_vertical_alignment(self, alignment):
        if type(alignment) != self._shared.VerticalAlignment:
            print('The component parameter must be of type VerticalAlignment enum! Not: {}'.format(type(alignment)))
            return
        self._shared.generic_property('vertical_alignment', alignment.value)

    def vertical_alignment_top(self):
        self._add_vertical_alignment(self._shared.VerticalAlignment.top)

    def vertical_alignment_middle(self):
        self._add_vertical_alignment(self._shared.VerticalAlignment.middle)

    def vertical_alignment_bottom(self):
        self._add_vertical_alignment(self._shared.VerticalAlignment.bottom)

class _WrapWords(object):
    def wrap_words(self, wrap=True):
        self._shared.boolean_property('wrap_words', wrap)

class _Text(object):
    def text(self, text):
        self._shared.generic_property('text', text)

class _AutoSize(object):
    def auto_size(self, auto=True):
        self._shared.boolean_property('auto_size', auto)

# 0, 90, 180, -90
class _RotationStep(object):
    def _add_rotation_step(self, rotation):
        if type(rotation) != self._shared.RotationStep:
            print('The component parameter must be of type Rotation enum! Not: {}'.format(type(rotation)))
            return
        self._shared.generic_property('rotation_step', rotation.value)

    def rotation_step_0(self):
        self._add_rotation_step(self._shared.RotationStep.zero)

    def rotation_step_90(self):
        self._add_rotation_step(self._shared.RotationStep.ninety)

    def rotation_step_180(self):
        self._add_rotation_step(self._shared.RotationStep.one_hundred_eighty)

    def rotation_step_negative_90(self):
        self._add_rotation_step(self._shared.RotationStep.negative_ninety)

class _Border(object):
    def border_width(self, width):
        self._shared.integer_property('border_width', width)

    def predefined_border_color(self, name):
        e = self._shared.create_element('border_color')
        self._shared.create_color_element(e, name, None, None, None, None)

    def border_color(self, red, green, blue, alpha=255):
        e = self._shared.create_element('border_color')
        self._shared.create_color_element(e, None, red, green, blue, alpha)

class _Macro(object):
    def macro(self, name, val):
        self._shared.add_macro(name, val, None)

class _Bit(object):
    def bit(self, val=-1):
        self._shared.integer_property('bit', val)

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

    # should actions be their own class?
    def action_open_display(self, file, target, description=None, macros=None):
        if description is None:
            description = 'Open Display'
        possible_targets = ['tab', 'replace', 'window']
        if target.lower() not in possible_targets:
            print('Target must be one of {}, not: {}'.format(possible_targets, target))
            return
        if macros is not None and type(macros) is not dict:
            print('The macro parameter must be a dictionary with key=MacroName and val=MacroValue')
            return
        args = {'file': file, 'target': target.lower()}
        self._prop_factory.add_action('open_display', description, args, macros)

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

class _Points(object):
    def point(self, x, y):
        self._prop_factory.add_point(x, y)

class _Arrow(object):
    def arrow_length(self, length):
        self._shared.integer_property('arrow_length', length)

    def arrows_none(self):
        self._shared.generic_property('arrows', self._shared.arrow_types['None'])

    def arrows_from(self):
        self._shared.generic_property('arrows', self._shared.arrow_types['From'])

    def arrows_to(self):
        self._shared.generic_property('arrows', self._shared.arrow_types['To'])

    def arrows_both(self):
        self._shared.generic_property('arrows', self._shared.arrow_types['Both'])

class _LineStyle(object):
    def line_style_solid(self):
        self._shared.generic_property('line_style', self._shared.line_styles['Solid'])

    def line_style_dashed(self):
        self._shared.generic_property('line_style', self._shared.line_styles['Dashed'])

    def line_style_dot(self):
        self._shared.generic_property('line_style', self._shared.line_styles['Dot'])

    def line_style_dash_dot(self):
        self._shared.generic_property('line_style', self._shared.line_styles['Dash-Dot'])

    def line_style_dash_dot_dot(self):
        self._shared.generic_property('line_style', self._shared.line_styles['Dash-Dot-Dot'])
