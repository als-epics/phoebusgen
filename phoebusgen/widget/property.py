from xml.etree.ElementTree import Element, SubElement
from phoebusgen._shared_property_helpers import _SharedPropertyFunctions
from enum import Enum


class Property(object):
    def __init__(self, root_element):
        self.root = root_element
        self.formats_array = ['default', 'decimal', 'exponential', 'engineering', 'hexadecimal',
                              'compact', 'string',  'sexagesimal hh:mm:ss', 'sexagesimal hms 24h rad',
                              'sexagesimal dms 360deg rad', 'binary']
        self.shared_functions = _SharedPropertyFunctions(self.root)

    class RotationStep(Enum):
        zero = 0
        ninety = 1
        one_hundred_eighty = 2
        negative_ninety = 3

    class HorizontalAlignment(Enum):
        left = 0
        center = 1
        right = 2

    class VerticalAlignment(Enum):
        top = 0
        middle = 1
        bottom = 2

    class FontStyle(Enum):
        regular = 'REGULAR'
        italic = 'ITALIC'
        bold = 'BOLD'
        bold_and_italic = 'BOLD_ITALIC'

    class GroupStyle(Enum):
        group_box = 0
        title_bar = 1
        line = 2
        none = 3

    class Resize(Enum):
        no_resize = 0
        size_content_to_fit_widget = 1
        size_widget_to_match_content = 2
        stretch_content_to_fit_widget = 3
        crop_content = 4

    class FileComponent(Enum):
        full_path = 0
        directory = 1
        name_and_extension = 2
        base_name = 3

    class Mode(Enum):
        toggle = 0
        push = 1
        push_inverted = 2


    def add_pv_name(self, name):
        self.shared_functions.generic_property('pv_name', name)

    def add_precision(self, val):
        self.shared_functions.integer_property('precision', val)

    def add_show_units(self, show):
        self.shared_functions.boolean_property('show_units', show)

    def add_wrap_words(self, wrap):
        self.shared_functions.boolean_property('wrap_words', wrap)

    def add_transparent(self, transparent):
        self.shared_functions.boolean_property('transparent', transparent)

    def add_rotation(self, rotation):
        self.shared_functions.number_property('rotation', rotation)

    def add_rotation_step(self, rotation):
        if type(rotation) != self.RotationStep:
            print('The component parameter must be of type Rotation enum! Not: {}'.format(type(rotation)))
            return
        self.shared_functions.generic_property('rotation_step', rotation.value)

    def add_horizontal_alignment(self, alignment):
        if type(alignment) != self.HorizontalAlignment:
            print('The component parameter must be of type HorizontalAlignment enum! Not: {}'.format(type(alignment)))
            return
        self.shared_functions.generic_property('horizontal_alignment', alignment.value)

    def add_vertical_alignment(self, alignment):
        if type(alignment) != self.VerticalAlignment:
            print('The component parameter must be of type VerticalAlignment enum! Not: {}'.format(type(alignment)))
            return
        self.shared_functions.generic_property('vertical_alignment', alignment.value)

    def add_background_color(self, name, red, green, blue, alpha):
        e = self.shared_functions.create_element('background_color')
        self.shared_functions.create_color_element(e, name, red, green, blue, alpha)

    def add_foreground_color(self, name, red, green, blue, alpha):
        e = self.shared_functions.create_element('foreground_color')
        self.shared_functions.create_color_element(e, name, red, green, blue, alpha)

    def add_fill_color(self, name, red, green, blue, alpha):
        e = self.shared_functions.create_element('fill_color')
        self.shared_functions.create_color_element(e, name, red, green, blue, alpha)

    def add_empty_color(self, name, red, green, blue, alpha):
        e = self.shared_functions.create_element('empty_color')
        self.shared_functions.create_color_element(e, name, red, green, blue, alpha)

    def add_named_font(self, name):
        self.shared_functions.create_named_font_elemet(name)

    def get_font_element(self):
        font_root_elem = self.root.find('font')
        if font_root_elem is None:
            font_root_elem = self.shared_functions.create_element('font')
            self.root.append(font_root_elem)
        child_font_elem = font_root_elem.find('font')
        if child_font_elem is None:
            child_font_elem = Element('font')
            child_font_elem.attrib = {'family': 'Liberation Sans', 'size': '14', 'style': 'REGULAR'}
            font_root_elem.append(child_font_elem)
        return child_font_elem

    def add_font_family(self, val):
        child_elem = self.get_font_element()
        child_elem.attrib['family'] = str(val)

    def add_font_style(self, val):
        if type(val) != self.FontStyle:
            print('The font style parameter must be of type FontStyle enum! Not: {}'.format(type(val)))
            return
        child_elem = self.get_font_element()
        child_elem.attrib['style'] = val.value

    def add_font_size(self, val):
        if type(val) == int or type(val) == float:
            child_elem = self.get_font_element()
            child_elem.attrib['size'] = str(int(val))
        else:
            print('Font size must be a number! Not: {}'.format(val))

    def add_border_width(self, width):
        self.shared_functions.integer_property('border_width', width)

    def add_border_color(self, name, red, green, blue, alpha):
        e = self.shared_functions.create_element('border_color')
        self.shared_functions.create_color_element(e, name, red, green, blue, alpha)

    def add_format(self, format_val):
        val = str(format_val).lower()
        try:
            v = self.formats_array.index(val)
        except ValueError:
            print('Invalid format. Given format {}'.format(format))
            return
        self.shared_functions.generic_property('format', v)

    def add_text(self, text):
        self.shared_functions.generic_property('text', text)

    def add_auto_size(self, auto):
        self.shared_functions.boolean_property('auto_size', auto)

    def add_multi_line(self, val):
        self.shared_functions.boolean_property('multi_line', val)

    def add_macro(self, name, val):
        self.shared_functions.add_macro(name, val)

    def add_bit(self, val):
        self.shared_functions.integer_property('bit', val)

    def add_square(self, val):
        self.shared_functions.boolean_property('square', val)

    def add_labels_from_pv(self, val):
        self.shared_functions.boolean_property('labels_from_pv', val)

    def add_off_color(self, name, red, green, blue, alpha):
        e = self.shared_functions.create_element('off_color')
        self.shared_functions.create_color_element(e, name, red, green, blue, alpha)

    def add_off_label(self, label):
        self.shared_functions.generic_property('off_label', label)

    def add_on_color(self, name, red, green, blue, alpha):
        e = self.shared_functions.create_element('on_color')
        self.shared_functions.create_color_element(e, name, red, green, blue, alpha)

    def add_on_label(self, label):
        self.shared_functions.generic_property('on_label', label)

    def add_line_color(self, name, red, green, blue, alpha):
        e = self.shared_functions.create_element('line_color')
        self.shared_functions.create_color_element(e, name, red, green, blue, alpha)

    def add_on_image(self, image_file):
        self.shared_functions.generic_property('on_image', image_file)

    def add_off_image(self, image_file):
        self.shared_functions.generic_property('off_image', image_file)

    def add_alarm_border(self, val):
        self.shared_functions.boolean_property('border_alarm_sensitive', val)

    def add_enabled(self, val):
        self.shared_functions.boolean_property('enabled', val)

    def add_confirmation_dialog(self, val):
        self.shared_functions.boolean_property('show_confirmation_dialog', val)

    def add_confirmation_message(self, message):
        self.shared_functions.generic_property('confirm_message', message)

    def add_password(self, password):
        self.shared_functions.generic_property('password', password)

    def add_corner_width(self, width):
        self.shared_functions.integer_property('corner_width', width)

    def add_corner_height(self, height):
        self.shared_functions.integer_property('corner_height', height)

    def add_line_width(self, width):
        self.shared_functions.integer_property('line_width', width)

    def add_angle_start(self, val):
        self.shared_functions.number_property('start_angle', val)

    def add_angle_size(self, val):
        self.shared_functions.number_property('total_angle', val)

    def add_file(self, val):
        self.shared_functions.generic_property('file', val)

    def add_stretch_to_fit(self, val):
        self.shared_functions.boolean_property('stretch_image', val)

    def add_rotation(self, val):
        self.shared_functions.number_property('rotation', val)

    def add_resize_behavior(self, resize):
        if type(resize) != self.Resize:
            print('Resize behavior input must be of type enum Resize. Not: {}'.format(type(resize)))
        self.shared_functions.generic_property('resize', resize.value)

    def add_group_name(self, val):
        self.shared_functions.generic_property('group_name', val)

    def add_style(self, style):
        if type(style) != self.GroupStyle:
            print('Input type for param to group style must be of type GroupStyle. Not: {}'.format(type(style)))
            return
        self.shared_functions.generic_property('style', style.value)

    def add_action(self, action_type, description, args):
        root_action = self.root.find('actions')
        if root_action is None:
            root_action = SubElement(self.root, 'actions')
        action = SubElement(root_action, 'action')
        action.attrib['type'] = action_type
        sub = SubElement(action, 'description')
        sub.text = str(description)
        for arg, val in args.items():
            sub = SubElement(action, arg)
            sub.text = str(val)

    def add_action_execute_as_one(self, val):
        if type(val) == bool:
            action = str(val).lower()
        elif type(val) == int:
            action = str(bool(val)).lower()
        elif val.lower() == 'true' or val.lower() == 'false':
            action = val.lower()
        else:
            print('action_execute_as_one must take a boolean value! Not: {}'.format(val))
            return
        root_action = self.root.find('actions')
        if root_action is None:
            root_action = SubElement(self.root, 'actions')
        root_action.attrib['execute_as_one'] = action

    def add_label(self, val):
        self.shared_functions.generic_property('label', val)

    def add_horizontal(self, val):
        self.shared_functions.boolean_property('horizontal', val)

    def add_item(self, val):
        root_item = self.root.find('items')
        if root_item is None:
            root_item = SubElement(self.root, 'items')
        sub = SubElement(root_item, 'item')
        sub.text = val

    def add_items_from_pv(self, val):
        self.shared_functions.boolean_property('items_from_pv', val)

    def add_minimum(self, val):
        self.shared_functions.number_property('minimum', val)

    def add_maximum(self, val):
        self.shared_functions.number_property('maximum', val)

    def add_limits_from_pv(self, val):
        self.shared_functions.boolean_property('limits_from_pv', val)

    def add_scale_visible(self, val):
        self.shared_functions.boolean_property('scale_visible', val)

    def add_url(self, url):
        self.shared_functions.generic_property('url', url)

    def add_show_toolbar(self, val):
        self.shared_functions.boolean_property('show_toolbar', val)

    def add_buttons_on_left(self, val):
        self.shared_functions.boolean_property('buttons_on_left', val)

    def add_increment(self, val):
        self.shared_functions.number_property('increment', val)

    def add_file_component(self, val):
        if type(val) != self.FileComponent:
            print('The component parameter must be of type FileComponent enum! Not: {}'.format(type(val)))
            return
        self.shared_functions.generic_property('component', val.value)

    def add_editable(self, val):
        self.shared_functions.boolean_property('editable', val)

    def add_selected_color(self, name, red, green, blue, alpha):
        e = self.shared_functions.create_element('selected_color')
        self.shared_functions.create_color_element(e, name, red, green, blue, alpha)

    def add_show_led(self, val):
        self.shared_functions.generic_property('show_led', val)

    def add_mode(self, val):
        if type(val) != self.Mode:
            print('The component parameter must be of type Mode enum! Not: {}'.format(type(val)))
            return
        self.shared_functions.generic_property('mode', val.value)

    def add_show_value(self, val):
        self.shared_functions.boolean_property('show_value', val)

    def add_show_limits(self, val):
        self.shared_functions.boolean_property('show_limits', val)

    def add_needle_color(self, name, red, green, blue, alpha):
        e = self.shared_functions.create_element('needle_color')
        self.shared_functions.create_color_element(e, name, red, green, blue, alpha)

    def add_knob_color(self, name, red, green, blue, alpha):
        e = self.shared_functions.create_element('knob_color')
        self.shared_functions.create_color_element(e, name, red, green, blue, alpha)

    def add_show_value_tip(self, val):
        self.shared_functions.boolean_property('show_value_tip', val)

    def add_bar_length(self, val):
        self.shared_functions.number_property('bar_length', val)

    def add_selection_value_pv(self, val):
        self.shared_functions.generic_property('selection_value_pv', val)