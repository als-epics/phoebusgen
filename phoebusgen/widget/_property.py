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

    def generic_property(self, prop_type, val=None):
        self.root.append(self.create_element(prop_type, val))

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
        try:
            v = int(val)
        except ValueError:
            print('Precision must be an integer, not: {}'.format(val))
            return
        self.generic_property('precision', v)

    def add_show_units(self, show):
        self.generic_property('show_units', show)

    def add_wrap_words(self, wrap):
        self.generic_property('wrap_words', wrap)

    def add_transparent(self, transparent):
        self.generic_property('transparent', transparent)

    def add_rotation(self, rotation):
        pass

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
        try:
            v = int(width)
        except ValueError:
            print('Width must be an integer, not: {}'.format(width))
            return
        self.generic_property('border_width', v)

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
        self.generic_property('auto_size', auto)

    def add_multi_line(self, val):
        self.generic_property('multi_line', val)

    def add_macro(self, name, val):
        root_macro = self.root.find('macro')
        if root_macro is None:
            root_macro = SubElement(self.root, 'macros')
        macro = SubElement(root_macro, name)
        macro.text = val

    def add_bit(self, val):
        self.generic_property('bit', val)

    def add_square(self, val):
        if type(val) is not bool:
            print('Must be boolean input')
        else:
            self.generic_property('square', val)

    def add_labels_from_pv(self, val):
        if type(val) is not bool:
            print('Must be boolean input')
        else:
            self.generic_property('labels_from_pv', val)

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
        self.generic_property('border_alarm_sensitive', val)

    def add_enabled(self, val):
        self.generic_property('enabled', val)

    def add_confirmation_dialog(self, val):
        self.generic_property('show_confirmation_dialog', val)

    def add_confirmation_message(self, message):
        self.generic_property('confirm_message', message)

    def add_password(self, password):
        self.generic_property('password', password)

    def add_corner_width(self, width):
        self.generic_property('corner_width', width)

    def add_corner_height(self, height):
        self.generic_property('corner_height', height)

    def add_line_width(self, width):
        self.generic_property('line_width', width)

    def add_angle_start(self, val):
        self.generic_property('start_angle', val)

    def add_angle_size(self, val):
        self.generic_property('total_angle', val)
