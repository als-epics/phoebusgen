from xml.etree.ElementTree import Element, SubElement
import yaml
import os


# TO DO : Add check if property is already available
# TO DO : Add way to specify defaults in a config file
# TO DO : Default property value should delete element (can use remove element with self.root)
# TO DO : Probably should allow for 'array' input functions to also take in integer value
class Property(object):
    def __init__(self, root_element):
        self.root = root_element
        curr_path = os.path.dirname(__file__)
        with open(curr_path + '/colors.yaml') as f:
            self.predefined_colors = yaml.safe_load(f)
        with open(curr_path + '/fonts.yaml') as f:
            self.predefined_fonts = yaml.safe_load(f)
        self.rotation_steps_array = [0, 90, 180, -90]
        self.horizontal_alignment_array = ['left', 'center', 'right']
        self.vertical_alignment_array = ['top', 'middle', 'bottom']
        self.formats_array = ['default', 'decimal', 'exponential', 'engineering', 'hexadecimal',
                              'compact', 'string',  'sexagesimal hh:mm:ss', 'sexagesimal hms 24h rad',
                              'sexagesimal dms 360deg rad', 'binary']
        self.resize_array = ['no resize', 'size content to fit widget', 'size widget to match content',
                             'stretch content to fit widget', 'crop content']
        self.style_array = ['group box', 'title bar', 'line', 'none']

    def generic_property(self, prop_type, val=None):
        element = self.root.find(prop_type)
        if element is not None:
            self.root.remove(element)
        self.root.append(self.create_element(prop_type, val))

    def integer_property(self, prop_type, val=None):
        if type(val) == int or type(val) == float:
            self.generic_property(prop_type, int(val))
        else:
            print('Property {} must be an integer! Not: {}'.format(prop_type, val))

    def number_property(self, prop_type, val):
        if type(val) == int or type(val) == float:
            self.generic_property(prop_type, val)
        else:
            print('Property {} must be a number! Not: {}'.format(prop_type, val))

    def boolean_property(self, prop_type, val):
        if type(val) == bool:
            self.generic_property(prop_type, str(val).lower())
        elif type(val) == int:
            self.generic_property(prop_type, str(bool(val)).lower())
        elif val.lower() == 'true' or val.lower() == 'false':
            self.generic_property(prop_type, val.lower())
        else:
            print('Property {} must be a boolean value! Not: {}'.format(prop_type, val))

    def create_element(self, prop_type, val=None):
        element = Element(prop_type)
        if val is not None:
            if type(val) == bool:
                element.text = str(val).lower()
            else:
                element.text = str(val)
        return element

    def add_pv_name(self, name):
        self.generic_property('pv_name', name)

    def add_precision(self, val):
        self.integer_property('precision', val)

    def add_show_units(self, show):
        self.boolean_property('show_units', show)

    def add_wrap_words(self, wrap):
        self.boolean_property('wrap_words', wrap)

    def add_transparent(self, transparent):
        self.boolean_property('transparent', transparent)

    def add_rotation(self, rotation):
        self.number_property('rotation', rotation)

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
        self.generic_property('rotation_step', val)

    def add_horizontal_alignment(self, alignment):
        val = str(alignment).lower()
        try:
            v = self.horizontal_alignment_array.index(val)
        except ValueError:
            print('Wrong input to horizontal alignment: {}. Must be Left, Center, or Right'.format(val))
            return
        self.generic_property('horizontal_alignment', v)

    def add_vertical_alignment(self, alignment):
        val = str(alignment).lower()
        try:
            v = self.vertical_alignment_array.index(val)
        except ValueError:
            print('Wrong input to vertical alignment: {}. Must be Top, Middle, or Bottom'.format(val))
            return
        self.generic_property('vertical_alignment', v)

    # TO DO : limit RGB to 0-255
    def create_color_element(self, root_color_elem, name, red, green, blue, alpha):
        sub_e = self.create_element('color')
        if name is None:
            sub_e.attrib = {'red': str(red), 'blue': str(blue), 'green': str(green), 'alpha': str(alpha)}
        else:
            color_list = self.predefined_colors.get(name.lower())
            if color_list is None:
                print('Color name is undefined')
                return
            else:
                sub_e.attrib = color_list
                sub_e.attrib['name'] = name
        root_color_elem.append(sub_e)
        self.root.append(root_color_elem)

    def add_background_color(self, name, red, green, blue, alpha):
        e = self.create_element('background_color')
        self.create_color_element(e, name, red, green, blue, alpha)

    def add_foreground_color(self, name, red, green, blue, alpha):
        e = self.create_element('foreground_color')
        self.create_color_element(e, name, red, green, blue, alpha)

    # TO DO: Define possible fonts, possible sizes (if applicable), possible styles
    def add_font(self, family, style, size, name):
        e = self.create_element('font')
        if name is not None:
            font_attrib = self.predefined_fonts.get(name.lower())
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
        self.integer_property('border_width', width)

    def add_border_color(self, name, red, green, blue, alpha):
        e = self.create_element('border_color')
        self.create_color_element(e, name, red, green, blue, alpha)

    def add_format(self, format_val):
        val = str(format_val).lower()
        try:
            v = self.formats_array.index(val)
        except ValueError:
            print('Invalid format. Given format {}'.format(format))
            return
        self.generic_property('format', v)

    def add_text(self, text):
        self.generic_property('text', text)

    def add_auto_size(self, auto):
        self.boolean_property('auto_size', auto)

    def add_multi_line(self, val):
        self.boolean_property('multi_line', val)

    def add_macro(self, name, val):
        root_macro = self.root.find('macro')
        if root_macro is None:
            root_macro = SubElement(self.root, 'macros')
        macro = SubElement(root_macro, name)
        macro.text = val

    def add_bit(self, val):
        self.integer_property('bit', val)

    def add_square(self, val):
        self.boolean_property('square', val)

    def add_labels_from_pv(self, val):
        self.boolean_property('labels_from_pv', val)

    def add_off_color(self, name, red, green, blue, alpha):
        e = self.create_element('off_color')
        self.create_color_element(e, name, red, green, blue, alpha)

    def add_off_label(self, label):
        self.generic_property('off_label', label)

    def add_on_color(self, name, red, green, blue, alpha):
        e = self.create_element('on_color')
        self.create_color_element(e, name, red, green, blue, alpha)

    def add_on_label(self, label):
        self.generic_property('on_label', label)

    def add_line_color(self, name, red, green, blue, alpha):
        e = self.create_element('line_color')
        self.create_color_element(e, name, red, green, blue, alpha)

    def add_alarm_border(self, val):
        self.boolean_property('border_alarm_sensitive', val)

    def add_enabled(self, val):
        self.boolean_property('enabled', val)

    def add_confirmation_dialog(self, val):
        self.boolean_property('show_confirmation_dialog', val)

    def add_confirmation_message(self, message):
        self.generic_property('confirm_message', message)

    def add_password(self, password):
        self.generic_property('password', password)

    def add_corner_width(self, width):
        self.integer_property('corner_width', width)

    def add_corner_height(self, height):
        self.integer_property('corner_height', height)

    def add_line_width(self, width):
        self.integer_property('line_width', width)

    def add_angle_start(self, val):
        self.number_property('start_angle', val)

    def add_angle_size(self, val):
        self.number_property('total_angle', val)

    def add_file(self, val):
        self.generic_property('file', val)

    def add_stretch_to_fit(self, val):
        self.boolean_property('stretch_image', val)

    def add_rotation(self, val):
        self.number_property('rotation', val)

    def add_resize_behavior(self, resize):
        val = str(resize).lower()
        try:
            v = self.resize_array.index(val)
        except ValueError:
            print('Wrong input to resize behavior: {}'.format(val))
            return
        self.generic_property('resize', v)

    def add_group_name(self, val):
        self.generic_property('group_name', val)

    def add_style(self, style):
        val = str(style).lower()
        try:
            v = self.style_array.index(val)
        except ValueError:
            print('Wrong input to group style: {}'.format(val))
            return
        self.generic_property('style', v)

    def add_action(self, action_type, description, args):
        root_action = self.root.find('actions')
        if root_action is None:
            root_action = SubElement(self.root, 'actions')
        action = SubElement(root_action, 'action')
        action.attrib['type'] = action_type
        sub = SubElement(action, 'description')
        sub.text = description
        for arg, val in args.items():
            sub = SubElement(action, arg)
            sub.text = val

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
        self.generic_property('label', val)

    def add_horizontal(self, val):
        self.boolean_property('horizontal', val)

    def add_item(self, val):
        root_item = self.root.find('items')
        if root_item is None:
            root_item = SubElement(self.root, 'items')
        sub = SubElement(root_item, 'item')
        sub.text = val

    def add_items_from_pv(self, val):
        self.boolean_property('items_from_pv', val)
