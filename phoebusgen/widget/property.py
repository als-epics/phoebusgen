from xml.etree.ElementTree import Element, SubElement
from phoebusgen.shared_property_helpers import SharedPropertyFunctions


# TO DO : Add check if property is already available
# TO DO : Add way to specify defaults in a config file
# TO DO : Default property value should delete element (can use remove element with self.root)
# TO DO : Probably should allow for 'array' input functions to also take in integer value
class Property(object):
    def __init__(self, root_element):
        self.root = root_element
        self.rotation_steps_array = [0, 90, 180, -90]
        self.horizontal_alignment_array = ['left', 'center', 'right']
        self.vertical_alignment_array = ['top', 'middle', 'bottom']
        self.formats_array = ['default', 'decimal', 'exponential', 'engineering', 'hexadecimal',
                              'compact', 'string',  'sexagesimal hh:mm:ss', 'sexagesimal hms 24h rad',
                              'sexagesimal dms 360deg rad', 'binary']
        self.resize_array = ['no resize', 'size content to fit widget', 'size widget to match content',
                             'stretch content to fit widget', 'crop content']
        self.style_array = ['group box', 'title bar', 'line', 'none']
        self.shared_functions = SharedPropertyFunctions(self.root)

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
        try:
            value = int(rotation)
        except ValueError:
            print('Rotation step must be an integer, not: {}'.format(value))
            return
        try:
            val = self.rotation_steps_array.index(value)
        except ValueError:
            print('Invalid rotation given. Must be 0, 90, 180, -90')
            return
        self.shared_functions.generic_property('rotation_step', val)

    def add_horizontal_alignment(self, alignment):
        val = str(alignment).lower()
        try:
            v = self.horizontal_alignment_array.index(val)
        except ValueError:
            print('Wrong input to horizontal alignment: {}. Must be Left, Center, or Right'.format(val))
            return
        self.shared_functions.generic_property('horizontal_alignment', v)

    def add_vertical_alignment(self, alignment):
        val = str(alignment).lower()
        try:
            v = self.vertical_alignment_array.index(val)
        except ValueError:
            print('Wrong input to vertical alignment: {}. Must be Top, Middle, or Bottom'.format(val))
            return
        self.shared_functions.generic_property('vertical_alignment', v)

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

    # TO DO: Define possible fonts, possible sizes (if applicable), possible styles
    def add_font(self, family, style, size, name):
        e = self.shared_functions.create_element('font')
        if name is not None:
            font_attrib = self.shared_functions.predefined_fonts.get(name.lower())
            if font_attrib is None:
                print('Font name is wrong')
                return
        else:
            font_attrib = {'family': 'Liberation Sans' if family is None else family,
                           'style': 'Regular' if style is None else style,
                           'size': '14' if size is None else str(size)}
        SubElement(e, 'font', attrib=font_attrib)
        self.root.append(e)

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
        val = str(resize).lower()
        try:
            v = self.resize_array.index(val)
        except ValueError:
            print('Wrong input to resize behavior: {}'.format(val))
            return
        self.shared_functions.generic_property('resize', v)

    def add_group_name(self, val):
        self.shared_functions.generic_property('group_name', val)

    def add_style(self, style):
        val = str(style).lower()
        try:
            v = self.style_array.index(val)
        except ValueError:
            print('Wrong input to group style: {}'.format(val))
            return
        self.shared_functions.generic_property('style', v)

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
