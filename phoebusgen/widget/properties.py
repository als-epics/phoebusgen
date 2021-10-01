from xml.etree.ElementTree import Element, SubElement
from typing import Union

class _PVName(object):
    def pv_name(self, name: str) -> None:
        """
        Add PV name to widget

        :param name: PV name
        """
        self._shared.generic_property(self.root, 'pv_name', name)

class _Font(object):
    def _get_font_element(self):
        font_root_elem = self.root.find('font')
        if font_root_elem is None:
            font_root_elem = self._shared.create_element(self.root, 'font')
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

    def predefined_font(self, name: object) -> None:
        """
        Add named font property to widget

        :param name: <phoebusgen.fonts> Font name
        """
        self._shared.create_named_font_elemet(name)

    def font_family(self, family: str) -> None:
        """
        Change font family property for widget

        :param family: Font Family name
        """
        child_elem = self._get_font_element()
        child_elem.attrib['family'] = str(family)

    def font_size(self, size: int) -> None:
        """
        Change font size property for widget

        :param size: Font size
        """
        if type(size) == int or type(size) == float:
            child_elem = self._get_font_element()
            child_elem.attrib['size'] = str(int(size))
        else:
            print('Font size must be a number! Not: {}'.format(size))

    def font_style_bold(self) -> None:
        """
        Change font style to Bold
        """
        self._add_font_style(self._shared.FontStyle.bold)

    def font_style_italic(self) -> None:
        """
        Change font style to Italic
        """
        self._add_font_style(self._shared.FontStyle.italic)

    def font_style_bold_italic(self) -> None:
        """
        Change font style to Bold & Italic
        """
        self._add_font_style(self._shared.FontStyle.bold_and_italic)

    def font_style_regular(self) -> None:
        """
        Change font style to Regular
        """
        self._add_font_style(self._shared.FontStyle.regular)

class _ForegroundColor(object):
    def predefined_foreground_color(self, name: object) -> None:
        """
        Add named foreground color to widget

        :param name: <phoebusgen.colors> Predefined color name
        """
        e = self._shared.create_element(self.root, 'foreground_color')
        self._shared.create_color_element(e, name, None, None, None, None)

    def foreground_color(self, red: int, green: int, blue: int, alpha: int = 255) -> None:
        """
        Add foreground color property to widget with RGB values

        :param red: 0-255
        :param green: 0-255
        :param blue: 0-255
        :param alpha: 0-255. Default is 255
        """
        e = self._shared.create_element(self.root, 'foreground_color')
        self._shared.create_color_element(e, None, red, green, blue, alpha)

class _BackgroundColor(object):
    def predefined_background_color(self, name: object) -> None:
        """
        Add named background color to widget
        :param name: <phoebusgen.colors> Predefined color name
        """
        e = self._shared.create_element(self.root, 'background_color')
        self._shared.create_color_element(e, name, None, None, None, None)

    def background_color(self, red: int, green: int, blue: int, alpha: int = 255) -> None:
        """
        Add background color property to widget with RGB values

        :param red: 0-255
        :param green: 0-255
        :param blue: 0-255
        :param alpha: 0-255. Default is 255
        """
        e = self._shared.create_element(self.root, 'background_color')
        self._shared.create_color_element(e, None, red, green, blue, alpha)

class _Transparent(object):
    def transparent(self, transparent: bool = False) -> None:
        """
        Change widget transparent property. Default arg is False

        :param transparent: Is widget transparent?
        """
        self._shared.boolean_property(self.root, 'transparent', transparent)

class _Format(object):
    # this should use an enum
    def format(self, format_val: str) -> None:
        """
        Add format property to widget, i.e. Decimal, Exponential, Engineering, String, etc

        :param format_val: Format String name
        :return:
        """
        val = str(format_val).lower()
        try:
            v = self._shared.formats_array.index(val)
        except ValueError:
            print('Invalid format. Given format {}'.format(format_val))
            return
        self._shared.generic_property(self.root, 'format', v)

class _Precision(object):
    def precision(self, val: int) -> None:
        """
        Add precision value to widget

        :param val: Precision value
        """
        self._shared.integer_property(self.root, 'precision', val)

class _ShowUnits(object):
    def show_units(self, show: bool = True) -> None:
        """
        Change show units property to widget. Default arg is True

        :param show: Show units?
        """
        self._shared.boolean_property(self.root, 'show_units', show)

class _HorizontalAlignment(object):
    def _add_horizontal_alignment(self, alignment):
        if type(alignment) != self._shared.HorizontalAlignment:
            print('The component parameter must be of type HorizontalAlignment enum! Not: {}'.format(type(alignment)))
            return
        self._shared.generic_property(self.root, 'horizontal_alignment', alignment.value)

    def horizontal_alignment_left(self) -> None:
        """
        Change horizontal alignmnet to Left
        """
        self._add_horizontal_alignment(self._shared.HorizontalAlignment.left)

    def horizontal_alignment_center(self) -> None:
        """
        Change horizontal alignment to center
        """
        self._add_horizontal_alignment(self._shared.HorizontalAlignment.center)

    def horizontal_alignment_right(self) -> None:
        """
        Change horizontal alignment to right
        """
        self._add_horizontal_alignment(self._shared.HorizontalAlignment.right)

class _VerticalAlignment(object):
    def _add_vertical_alignment(self, alignment):
        if type(alignment) != self._shared.VerticalAlignment:
            print('The component parameter must be of type VerticalAlignment enum! Not: {}'.format(type(alignment)))
            return
        self._shared.generic_property(self.root, 'vertical_alignment', alignment.value)

    def vertical_alignment_top(self) -> None:
        """
        Change vertical alignment to Top
        """
        self._add_vertical_alignment(self._shared.VerticalAlignment.top)

    def vertical_alignment_middle(self) -> None:
        """
        Change vertical alignment to Middle
        """
        self._add_vertical_alignment(self._shared.VerticalAlignment.middle)

    def vertical_alignment_bottom(self) -> None:
        """
        Change vertical alignment to Bottom
        """
        self._add_vertical_alignment(self._shared.VerticalAlignment.bottom)

class _WrapWords(object):
    def wrap_words(self, wrap: bool = True) -> None:
        """
        Change wrap words property. Default arg value is True

        :param wrap: Wrap words?
        """
        self._shared.boolean_property(self.root, 'wrap_words', wrap)

class _Text(object):
    def text(self, text: str) -> None:
        """
        Add text property to widget

        :param text: Text string
        """
        self._shared.generic_property(self.root, 'text', text)

class _AutoSize(object):
    def auto_size(self, auto: bool = True) -> None:
        """
        Change auto size property on widget. Default arg is True

        :param auto: Auto size widget?
        """
        self._shared.boolean_property(self.root, 'auto_size', auto)

# 0, 90, 180, -90
class _RotationStep(object):
    def _add_rotation_step(self, rotation):
        if type(rotation) != self._shared.RotationStep:
            print('The component parameter must be of type Rotation enum! Not: {}'.format(type(rotation)))
            return
        self._shared.generic_property(self.root, 'rotation_step', rotation.value)

    def rotation_step_0(self) -> None:
        """
        Change rotation step value to 0
        """
        self._add_rotation_step(self._shared.RotationStep.zero)

    def rotation_step_90(self) -> None:
        """
        Change rotation step value to 90
        """
        self._add_rotation_step(self._shared.RotationStep.ninety)

    def rotation_step_180(self) -> None:
        """
        Change rotation step value to 180
        """
        self._add_rotation_step(self._shared.RotationStep.one_hundred_eighty)

    def rotation_step_negative_90(self) -> None:
        """
        Change rotation step value to -90
        """
        self._add_rotation_step(self._shared.RotationStep.negative_ninety)

class _Border(object):
    def border_width(self, width: int) -> None:
        """
        Add border width property to widget

        :param width: Border width value
        """
        self._shared.integer_property(self.root, 'border_width', width)

    def predefined_border_color(self, name: object) -> None:
        """
        Change border color with named color

        :param name: <phoebusgen.colors> Predefined color name
        """
        e = self._shared.create_element(self.root, 'border_color')
        self._shared.create_color_element(e, name, None, None, None, None)

    def border_color(self, red: int, green: int, blue: int, alpha: int = 255) -> None:
        """
        Change border color with RGB values

        :param red: 0-255
        :param green: 0-255
        :param blue: 0-255
        :param alpha: 0-255. Default is 255
        """
        e = self._shared.create_element(self.root, 'border_color')
        self._shared.create_color_element(e, None, red, green, blue, alpha)

class _Macro(object):
    def macro(self, name: str, val: Union[str, int, float]) -> None:
        """
        Add macro to widget

        :param name: Macro name
        :param val: Macro value
        """
        self._shared.add_macro(name, val, None)

class _Bit(object):
    def bit(self, val: int = -1) -> None:
        """
        Add bit property to widget. Default arg is -1

        :param val: Bit number
        """
        self._shared.integer_property(self.root, 'bit', val)

class _OffColor(object):
    def predefined_off_color(self, name: object) -> None:
        """
        Add named color for Off Color property

        :param name: <phoebusgen.colors> Predefined color name
        """
        e = self._shared.create_element(self.root, 'off_color')
        self._shared.create_color_element(e, name, None, None, None, None)

    def off_color(self, red: int, green: int, blue: int, alpha: int = 255) -> None:
        """
        Add Off color property using RGB values

        :param red: 0-255
        :param green: 0-255
        :param blue: 0-255
        :param alpha: 0-255. Default is 255
        """
        e = self._shared.create_element(self.root, 'off_color')
        self._shared.create_color_element(e, None, red, green, blue, alpha)

class _Off(_OffColor):
    def off_label(self, label: str) -> None:
        """
        Add Off label string to widget

        :param label: label
        """
        self._shared.generic_property(self.root, 'off_label', label)

class _OffImage(_Off):
    def off_image(self, image_file: str) -> None:
        """
        Add image for off property using file name

        :param image_file: Path to image file
        """
        self._shared.generic_property(self.root, 'off_image', image_file)

class _OnColor(object):
    def predefined_on_color(self, name: object) -> None:
        """
        Add named color for On Color property

        :param name: <phoebusgen.colors> Predefined color name
        """
        e = self._shared.create_element(self.root, 'on_color')
        self._shared.create_color_element(e, name, None, None, None, None)

    def on_color(self, red: int, green: int, blue: int, alpha: int = 255) -> None:
        """
        Add On color property using RGB values

        :param red: 0-255
        :param green: 0-255
        :param blue: 0-255
        :param alpha: 0-255. Default is 255
        """
        e = self._shared.create_element(self.root, 'on_color')
        self._shared.create_color_element(e, None, red, green, blue, alpha)

class _On(_OnColor):
    def on_label(self, label: str) -> None:
        """
        Add On label string to widget

        :param label: label
        """
        self._shared.generic_property(self.root, 'on_label', label)

class _OnImage(_On):
    def on_image(self, image_file: str) -> None:
        """
        Add image for on property using file name

        :param image_file: Path to image file
        """
        self._shared.generic_property(self.root, 'on_image', image_file)

class _LineColor(object):
    def predefined_line_color(self, name: object) -> None:
        """
        Add named line color property

        :param name: <phoebusgen.colors> Predefined color name
        """
        e = self._shared.create_element(self.root, 'line_color')
        self._shared.create_color_element(e, name, None, None, None, None)

    def line_color(self, red: int, green: int, blue: int, alpha: int = 255) -> None:
        """
        Add line color property using RGB values

        :param red: 0-255
        :param green: 0-255
        :param blue: 0-255
        :param alpha: 0-255. Default is 255
        """
        e = self._shared.create_element(self.root, 'line_color')
        self._shared.create_color_element(e, None, red, green, blue, alpha)

class _LineWidth(object):
    def line_width(self, width: int) -> None:
        """
        Add line width property to widget

        :param width: Line width
        """
        self._shared.integer_property(self.root, 'line_width', width)

class _Corner(object):
    def corner_width(self, width: int) -> None:
        """
        Add corner width property to widget

        :param width: Corner width
        """
        self._shared.integer_property(self.root, 'corner_width', width)

    def corner_height(self, height: int) -> None:
        """
        Add corner height property to widget

        :param height: Corner height
        """
        self._shared.integer_property(self.root, 'corner_height', height)

class _Square(object):
    def square(self, val: bool) -> None:
        """
        Change widget square property

        :param val: Is width square?
        """
        self._shared.boolean_property(self.root, 'square', val)

class _LabelsFromPV(object):
    def labels_from_pv(self, val: bool) -> None:
        """
        Change labels from pv property for widget

        :param val: Show labels from PV?
        """
        self._shared.boolean_property(self.root, 'labels_from_pv', val)

class _AlarmBorder(object):
    def alarm_border(self, val: bool) -> None:
        """
        Add alarm border property ON/OFF for widget

        :param val: Add alarm border to widget?
        """
        self._shared.boolean_property(self.root, 'border_alarm_sensitive', val)

class _Enabled(object):
    def enabled(self, val: bool) -> None:
        """
        Add enabled property to widget

        :param val: Is widget enabled?
        """
        self._shared.boolean_property(self.root, 'enabled', val)

class _Confirmation(object):
    def confirmation_dialog(self, message: str, password: str = None) -> None:
        """
        Add confirmation dialog to widget, i.e. Are you sure? . Default arg for password is None (no pw)

        :param message: Confirmation dialog message
        :param password: Password for dialog. Stored in plain text XML
        """
        self._shared.boolean_property(self.root, 'show_confirmation_dialog', True)
        self._shared.generic_property(self.root, 'confirm_message', message)
        if password is not None:
            self._shared.generic_property(self.root, 'password', password)

    def disable_confirmation_dialog(self) -> None:
        """
        Turn off confirmation dialog for widget
        """
        self._shared.boolean_property(self.root, 'show_confirmation_dialog', False)

class _MultiLine(object):
    def multi_line(self, val: bool) -> None:
        """
        Change Multi Line property for widget

        :param val: Use multi line?
        """
        self._shared.boolean_property(self.root, 'multi_line', val)

class _Angle(object):
    def angle_start(self, val: Union[float, int]) -> None:
        """
        Add angle start value for widget

        :param val: Start angle value
        """
        self._shared.number_property(self.root, 'start_angle', val)

    def angle_size(self, val: Union[float, int]) -> None:
        """
        Add angle size value for widget

        :param val: Angle size value
        """
        self._shared.number_property(self.root, 'total_angle', val)

class _Rotation(object):
    def rotation(self, val: Union[float, int]) -> None:
        """
        Add rotation value for widget

        :param val: Rotation value
        """
        self._shared.number_property(self.root, 'rotation', val)

class _File(object):
    def file(self, val: str) -> None:
        """
        Add file name property to widget

        :param val: File name
        """
        self._shared.generic_property(self.root, 'file', val)

class _StretchToFit(object):
    def stretch_to_fit(self, val: bool) -> None:
        """
        Add stretch to fit property to widget

        :param val: Stretch widget to fit?
        """
        self._shared.boolean_property(self.root, 'stretch_image', val)

class _Actions(object):
    def _add_action(self, action_type, description, args, macros=None):
        root_action = self.root.find('actions')
        if root_action is None:
            root_action = SubElement(self.root, 'actions')
        action = SubElement(root_action, 'action')
        action.attrib['type'] = action_type
        sub = SubElement(action, 'description')
        sub.text = str(description)
        if macros:
            if type(macros) is not dict:
                print("macros parameter must be of type dict, not: {}".format(type(macros)))
            else:
                for key, val in macros.items():
                    self._shared.add_macro(key, val, action)
        for arg, val in args.items():
            sub = SubElement(action, arg)
            sub.text = str(val)

    def action_execute_as_one(self, val: bool) -> None:
        """
        Add execute all actions as one property to widget (execute all actions on button press)

        :param val: Execute all actions as one?
        """
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

    # should actions be their own class?
    # target should be an enum
    def action_open_display(self, file: str, target: str, description: str = None, macros: dict = None) -> None:
        """
        Add open display action to widget. description and macros are optional params

        :param file: File name to open
        :param target: <specific strings only> tab, replace, window
        :param description: Description of action. Default is None
        :param macros: Dictionary of macros. key=macro name and value=macro value
        :return:
        """
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
        self._add_action('open_display', description, args, macros)

    def action_write_pv(self, pv_name: str, value: Union[str, int, float], description: str = None) -> None:
        """
        Add Write PV action to widget. description is optional

        :param pv_name: PV name to write to
        :param value: Value to write to PV
        :param description: Description of action. Default is None
        """
        if description is None:
            description = 'Write PV'
        args = {'pv_name': pv_name, 'value': value}
        self._add_action('write_pv', description, args)

    def action_execute_command(self, command: str, description: str = None) -> None:
        """
        Add Execute Command action to widget. description is optional

        :param command: Command to run in action
        :param description: Description of action. Default is None
        """
        if description is None:
            description = 'Execute Command'
        args = {'command': command}
        self._add_action('command', description, args)

    def action_open_file(self, file: str, description: str = None) -> None:
        """
        Add Open File action to widget. description is optional

        :param file: File name to open
        :param description: Description of action. Default is None
        """
        if description is None:
            description = 'Open File'
        args = {'file': file}
        self._add_action('open_file', description, args)

    def action_open_webpage(self, url: str, description: str = None) -> None:
        """
        Add Open Webpage action to widget. description is optional

        :param url: URL to open
        :param description: Description of action. Default is None
        """
        if description is None:
            description = 'Open Webpage'
        args = {'url': url}
        self._add_action('open_webpage', description, args)

class _Label(object):
    def label(self, val: str) -> None:
        """
        Add label to widget

        :param val: Label
        """
        self._shared.generic_property(self.root, 'label', val)

class _Horizontal(object):
    def horizontal(self, val: bool) -> None:
        """
        Change horizontal property of widget

        :param val: Is widget horizontal?
        """
        self._shared.boolean_property(self.root, 'horizontal', val)

class _Items(object):
    def item(self, item_text: str) -> None:
        """
        Add item property to widget

        :param item_text: Item text string
        """
        root_item = self.root.find('items')
        if root_item is None:
            root_item = SubElement(self.root, 'items')
        self._shared.generic_property(root_item, 'item', item_text)

class _ItemsFromPV(object):
    def items_from_pv(self, val: bool) -> None:
        """
        Change Items from PV property to widget

        :param val: Use items from pv?
        """
        self._shared.boolean_property(self.root, 'items_from_pv', val)

class _ShowValueTip(object):
    def show_value_tip(self, val: bool) -> None:
        """
        Change Show Value Tip property to widget

        :param val: Show value tip?
        """
        self._shared.boolean_property(self.root, 'show_value_tip', val)

class _BarLength(object):
    def bar_length(self, val: Union[float, int]) -> None:
        """
        Change bar length property of widget

        :param val: Bar length value
        """
        self._shared.number_property(self.root, 'bar_length', val)

class _ShowValue(object):
    def show_value(self, val: bool) -> None:
        """
        Change show value property of widget

        :param val: Show value?
        """
        self._shared.boolean_property(self.root, 'show_value', val)

class _ShowLimits(object):
    def show_limits(self, val: bool) -> None:
        """
        Change show limits property of widget

        :param val: Show limits?
        """
        self._shared.boolean_property(self.root, 'show_limits', val)

class _LimitsFromPV(object):
    def limits_from_pv(self, val: bool) -> None:
        """
        Change limits from PV property for widget

        :param val: Use limits from PV?
        """
        self._shared.boolean_property(self.root, 'limits_from_pv', val)

class _MinMax(object):
    def minimum(self, val: Union[float, int]) -> None:
        """
        Add minimum value property to widget

        :param val: Minimum value
        """
        self._shared.number_property(self.root, 'minimum', val)

    def maximum(self, val: Union[float, int]) -> None:
        """
        Add maximum value property to widget

        :param val: Maximum value
        """
        self._shared.number_property(self.root, 'maximum', val)

class _NeedleColor(object):
    def needle_color(self, red: int, green: int, blue: int, alpha: int = 255) -> None:
        """
        Add Needle Color property to widget with RGB values

        :param red: 0-255
        :param green: 0-255
        :param blue: 0-255
        :param alpha: 0-255. Default is 255
        """
        e = self._shared.create_element(self.root, 'needle_color')
        self._shared.create_color_element(e, None, red, green, blue, alpha)

    def predefined_needle_color(self, name: object) -> None:
        """
        Add named Needle Color property to widget

        :param name: <phoebusgen.colors> Predefined color name
        """
        e = self._shared.create_element(self.root, 'needle_color')
        self._shared.create_color_element(e, name, None, None, None, None)

class _KnobColor(object):
    def knob_color(self, red: int, green: int, blue: int, alpha: int = 255) -> None:
        """
        Add Knob Color property to widget with RGB values

        :param red: 0-255
        :param green: 0-255
        :param blue: 0-255
        :param alpha: 0-255. Default is 255
        """
        e = self._shared.create_element(self.root, 'knob_color')
        self._shared.create_color_element(e, None, red, green, blue, alpha)

    def predefined_knob_color(self, name: object) -> None:
        """
        Add named Knob Color property to widget

        :param name: <phoebusgen.colors> Predefined color name
        """
        e = self._shared.create_element(self.root, 'knob_color')
        self._shared.create_color_element(e, name, None, None, None, None)

class _FillColor(object):
    def fill_color(self, red: int, green: int, blue: int, alpha: int = 255) -> None:
        """
        Add Fill Color property to widget with RGB values

        :param red: 0-255
        :param green: 0-255
        :param blue: 0-255
        :param alpha: 0-255. Default is 255
        """
        e = self._shared.create_element(self.root, 'fill_color')
        self._shared.create_color_element(e, None, red, green, blue, alpha)

    def predefined_fill_color(self, name: object) -> None:
        """
        Add named Fill Color property to widget

        :param name: <phoebusgen.colors> Predefined color name
        """
        e = self._shared.create_element(self.root, 'fill_color')
        self._shared.create_color_element(e, name, None, None, None, None)

class _EmptyColor(object):
    def empty_color(self, red: int, green: int, blue: int, alpha: int = 255) -> None:
        """
        Add Empty Color property to widget with RGB values

        :param red: 0-255
        :param green: 0-255
        :param blue: 0-255
        :param alpha: 0-255. Default is 255
        """
        e = self._shared.create_element(self.root, 'empty_color')
        self._shared.create_color_element(e, None, red, green, blue, alpha)

    def predefined_empty_color(self, name: object) -> None:
        """
        Add named Empty Color property to widget

        :param name: <phoebusgen.colors> Predefined color name
        """
        e = self._shared.create_element(self.root, 'empty_color')
        self._shared.create_color_element(e, name, None, None, None, None)

class _ScaleVisible(object):
    def scale_visible(self, val: bool) -> None:
        """
        Change Scale Visible property on widget

        :param val: Is scale visible?
        """
        self._shared.boolean_property(self.root, 'scale_visible', val)

class _ShowLED(object):
    def show_led(self, val: bool) -> None:
        """
        Change Show LED property on widget

        :param val: Show LED?
        """
        self._shared.boolean_property(self.root, 'show_led', val)

class _Mode(object):
    def _add_mode(self, val):
        if type(val) != self._shared.Mode:
            print('The component parameter must be of type Mode enum! Not: {}'.format(type(val)))
            return
        self._shared.generic_property(self.root, 'mode', val.value)

    def mode_toggle(self) -> None:
        """
        Change mode to Toggle
        """
        self._add_mode(self._shared.Mode.toggle)

    def mode_push(self) -> None:
        """
        Change mode to Push
        """
        self._add_mode(self._shared.Mode.push)

    def mode_push_inverted(self) -> None:
        """
        Change mode to Push Inverted
        """
        self._add_mode(self._shared.Mode.push_inverted)

class _Style(object):
    def _add_style(self, style):
        if type(style) != self._shared.GroupStyle:
            print('Input type for param to group style must be of type GroupStyle. Not: {}'.format(type(style)))
            return
        self._shared.generic_property(self.root, 'style', style.value)

    def style_group_box(self) -> None:
        """
        Change widget style to Style Group Box
        """
        self._add_style(self._shared.GroupStyle.group_box)

    def style_title_bar(self) -> None:
        """
        Change widget style to Style Title Bar
        """
        self._add_style(self._shared.GroupStyle.title_bar)

    def style_line(self) -> None:
        """
        Change widget style to Style Line
        """
        self._add_style(self._shared.GroupStyle.line)

    def no_style(self) -> None:
        """
        Change widget style to No Style
        """
        self._add_style(self._shared.GroupStyle.none)

class _ResizeBehavior(object):
    def _add_resize_behavior(self, resize):
        if type(resize) != self._shared.Resize:
            print('Resize behavior input must be of type enum Resize. Not: {}'.format(type(resize)))
        self._shared.generic_property(self.root, 'resize', resize.value)

    def no_resize(self) -> None:
        """
        Change resize behavior to No Resize
        """
        self._add_resize_behavior(self._shared.Resize.no_resize)

    def size_content_to_fit_widget(self) -> None:
        """
        Change resize behavior to Size Content to Fit Widget
        """
        self._add_resize_behavior(self._shared.Resize.size_content_to_fit_widget)

    def size_widget_to_match_content(self) -> None:
        """
        Change resize behavior to Size Widget to Match Content
        """
        self._add_resize_behavior(self._shared.Resize.size_widget_to_match_content)

    def stretch_content_to_fit_widget(self) -> None:
        """
        Change resize behavior to Stretch Content to Fit Widget
        """
        self._add_resize_behavior(self._shared.Resize.stretch_content_to_fit_widget)

    def crop_content(self) -> None:
        """
        Change resize behavior to Crop Content
        """
        self._add_resize_behavior(self._shared.Resize.crop_content)

class _GroupName(object):
    def group_name(self, val: str) -> None:
        """
        Add group name to widget

        :param val: Name of group
        """
        self._shared.generic_property(self.root, 'group_name', val)

class _Structure(object):
    """
    This class is used for Structure widgets to be a method to add widgets to the structure
    """
    def add_widget(self, elem):
        """
        Add widget to structure element (group, etc.)

        :param elem: <Phoebusgen.widget> Element to add to structure
        """
        if type(elem) == list:
            for e in elem:
                self.root.append(e.root)
        else:
            self.root.append(elem.root)

class _URL(object):
    def url(self, url: str) -> None:
        """
        Add URL string property for widget

        :param url: URL string
        """
        self._shared.generic_property(self.root, 'url', url)

class _ShowToolbar(object):
    def show_toolbar(self, val: bool) -> None:
        """
        Change option to show toolbar property option for the widget

        :param val: Show toolbar?
        """
        self._shared.boolean_property(self.root, 'show_toolbar', val)

class _ButtonsOnLeft(object):
    def buttons_on_left(self, val: bool) -> None:
        """
        Change buttons on the left property option for widget

        :param val: Have button on the left?
        """
        self._shared.boolean_property(self.root, 'buttons_on_left', val)

class _Increment(object):
    def increment(self, val: Union[float, int]) -> None:
        """
        Change increment property for widget

        :param val: Increment value
        """
        self._shared.number_property(self.root, 'increment', val)

class _FileComponent(object):
    def _add_file_component(self, val):
        if type(val) != self._shared.FileComponent:
            print('The component parameter must be of type FileComponent enum! Not: {}'.format(type(val)))
            return
        self._shared.generic_property(self.root, 'component', val.value)

    def file_component_full_path(self) -> None:
        """
        Change file component to use full file path
        """
        self._add_file_component(self._shared.FileComponent.full_path)

    def file_component_directory(self) -> None:
        """
        Change file component to use directory name
        """
        self._add_file_component(self._shared.FileComponent.directory)

    def file_component_name_and_extension(self) -> None:
        """
        Change file component to only use file name and extension
        """
        self._add_file_component(self._shared.FileComponent.name_and_extension)

    def file_component_base_name(self) -> None:
        """
        Change file component to only use file base name
        """
        self._add_file_component(self._shared.FileComponent.base_name)

class _Editable(object):
    def editable(self, val: bool = True) -> None:
        """
        Change editable property on the widget. Default arg is True

        :param val: Is widget editable?
        """
        self._shared.boolean_property(self.root, 'editable', val)

class _SelectedColor(object):
    def selected_color(self, red: int, green: int, blue: int, alpha: int = 255) -> None:
        """
        Add selected color property to widget

        :param red: 0-255
        :param green: 0-255
        :param blue: 0-255
        :param alpha: 0-255. Default is 255
        """
        e = self._shared.create_element(self.root, 'selected_color')
        self._shared.create_color_element(e, None, red, green, blue, alpha)

    def predefined_selected_color(self, name: object) -> None:
        """
        Add predefined selected color name to widget

        :param name: <phoebusgen.colors> Predefined color name
        """
        e = self._shared.create_element(self.root, 'selected_color')
        self._shared.create_color_element(e, name, None, None, None, None)

class _DeselectedColor(object):
    def deselected_color(self, red: int, green: int, blue: int, alpha: int = 255) -> None:
        """
        Add deselected color property to widget

        :param red: 0-255
        :param green: 0-255
        :param blue: 0-255
        :param alpha: 0-255. Default is 255
        """
        e = self._shared.create_element(self.root, 'deselected_color')
        self._shared.create_color_element(e, None, red, green, blue, alpha)

    def predefined_deselected_color(self, name: object) -> None:
        """
        Add predefined deselected color name to widget

        :param name: <phoebusgen.colors> Predefined color name
        """
        e = self._shared.create_element(self.root, 'deselected_color')
        self._shared.create_color_element(e, name, None, None, None, None)

class _SelectionValuePV(object):
    def selection_value_pv(self, val: str) -> None:
        """
        Add selection value PV to widget

        :param val: PV Name for selection value pv
        """
        self._shared.generic_property(self.root, 'selection_value_pv', val)

class _Points(object):
    def point(self, x: int, y: int) -> None:
        """
        Add point to points property of a widget

        :param x: X position of the point
        :param y: Y position of the point
        """
        if type(x) != int and type(x) != float:
            print('Point X value must be an integer! Not: {}'.format(type(x)))
        elif type(y) != int and type(y) != float:
            print('Point Y value must be an integer! Not: {}'.format(type(y)))
        else:
            root_points = self.root.find('points')
            if root_points is None:
                root_points = SubElement(self.root, 'points')
            point = SubElement(root_points, 'point')
            point.attrib['x'] = str(int(x))
            point.attrib['y'] = str(int(y))

class _Arrow(object):
    def arrow_length(self, length: int) -> None:
        """
        Change arrow length widget property

        :param length: Arrow length
        """
        self._shared.integer_property(self.root, 'arrow_length', length)

    def arrows_none(self) -> None:
        """
        Change arrow property to "None" for no arrows
        """
        self._shared.generic_property(self.root, 'arrows', self._shared.arrow_types['None'])

    def arrows_from(self) -> None:
        """
        Change arrow property to "From" for arrow direction
        """
        self._shared.generic_property(self.root, 'arrows', self._shared.arrow_types['From'])

    def arrows_to(self) -> None:
        """
        Change arrow property to "To" for arrow direction
        """
        self._shared.generic_property(self.root, 'arrows', self._shared.arrow_types['To'])

    def arrows_both(self) -> None:
        """
        Change arrow property to "Both"
        """
        self._shared.generic_property(self.root, 'arrows', self._shared.arrow_types['Both'])

class _LineStyle(object):
    def line_style_solid(self) -> None:
        """
        Change widget line style to solid
        """
        self._shared.generic_property(self.root, 'line_style', self._shared.line_styles['Solid'])

    def line_style_dashed(self) -> None:
        """
        Change widget line style to dashed
        """
        self._shared.generic_property(self.root, 'line_style', self._shared.line_styles['Dashed'])

    def line_style_dot(self) -> None:
        """
        Change widget line style to dot
        """
        self._shared.generic_property(self.root, 'line_style', self._shared.line_styles['Dot'])

    def line_style_dash_dot(self) -> None:
        """
        Change widget line style to dash-dot
        """
        self._shared.generic_property(self.root, 'line_style', self._shared.line_styles['Dash-Dot'])

    def line_style_dash_dot_dot(self) -> None:
        """
        Change widget line style to dash-dot-dot
        """
        self._shared.generic_property(self.root, 'line_style', self._shared.line_styles['Dash-Dot-Dot'])

class _Tabs(object):
    def tab(self, name: str) -> None:
        """
        Add tab to the Tabs widget

        :param name: Tab name, should be unique
        """
        root_tab = self.root.find('tabs')
        if root_tab is None:
            root_tab = SubElement(self.root, 'tabs')
        tab_elem = SubElement(root_tab, 'tab')
        name_elem = SubElement(tab_elem, "name")
        name_elem.text = name
        children_elem = SubElement(tab_elem, "children")

    def add_widget(self, tab_name: str, elem: object) -> None:
        """
        Add widget to a specific tab with given tab_name

        :param tab_name: Name of the tab to add widget to
        :param elem: <Phoebusgen.widget> Widget to add to tab
        """
        root_tab = self.root.find('tabs')
        if root_tab is None:
            print("No tabs widget available!")
        else:
            tab_elem_list = root_tab.findall('tab')
            foundIt = False
            for tab in tab_elem_list:
                if tab.find('name').text == tab_name:
                    tab.find('children').append(elem.root)
                    foundIt = True
            if not foundIt:
                print("No tab with the given name: {}".format(tab_name))

class _NavTabs(object):
    def tab(self, name: str, file_name: str, group_name: str, macros: dict = None) -> None:
        """
        Add tab to the Navigation Tab widget. Nav tabs use bob files. Macro arg is optional

        :param name: Tab name
        :param file_name: .bob file name
        :param group_name: Tab group name
        :param macros: Dictionary of macros. key=macro name and value=macro value
        """
        root_tab = self.root.find('tabs')
        if root_tab is None:
            root_tab = SubElement(self.root, 'tabs')
        tab_elem = SubElement(root_tab, 'tab')
        self._shared.generic_property(tab_elem, "name", name)
        self._shared.generic_property(tab_elem, "file", file_name)
        self._shared.generic_property(tab_elem, "group_name", group_name)
        SubElement(tab_elem, "macros")
        if macros is not None:
            if type(macros) is not dict:
                print("macros parameter must be of type dict, not: {}".format(type(macros)))
            else:
                for key, val in macros.items():
                    self._shared.add_macro(key, val, tab_elem)

class _ActiveTab(object):
    def active_tab(self, tab_num: int) -> None:
        """
        Select active tab number for the widget

        :param tab_num: Tab number to be active on page open
        """
        self._shared.integer_property(self.root, 'active_tab', tab_num)

class _TabHeight(object):
    def tab_height(self, height: int) -> None:
        """
        Add tab height property to widget

        :param height: Height value for tabs
        """
        self._shared.integer_property(self.root, 'tab_height', height)

class _TabWidth(object):
    def tab_width(self, width: int) -> None:
        """
        Add tab width property to widget

        :param width: Width value for tabs
        """
        self._shared.integer_property(self.root, 'tab_width', width)

class _TabSpacing(object):
    def tab_spacing(self, spacing: int) -> None:
        """
        Add tab spacing property to widget

        :param spacing: Tab spacing value
        """
        self._shared.integer_property(self.root, 'tab_spacing', spacing)

class _Direction(object):
    def tab_direction_horizontal(self) -> None:
        """
        Change tab direction property to horizontal for widget
        """
        self._shared.integer_property(self.root, 'direction', 0)

    def tab_direction_vertical(self) -> None:
        """
        Change tab direction property to vertical for widget
        """
        self._shared.integer_property(self.root, 'direction', 1)

class _NumBits(object):
    def num_bits(self, number_of_bits: int) -> None:
        """
        Add number of bits property to widget

        :param number_of_bits: Number of bits
        """
        self._shared.integer_property(self.root, 'numBits', number_of_bits)

class _StartBit(object):
    def start_bit(self, start_bit: int) -> None:
        """
        Adding start bit property to widget

        :param start_bit: Start bit
        """
        self._shared.integer_property(self.root, 'startBit', start_bit)

class _ReverseBits(object):
    def reverse_bits(self, reverse_bits: bool = True) -> None:
        """
        Add reverse bits option on widget. Default arg value is True

        :param reverse_bits: Reverse bits?
        """
        self._shared.boolean_property(self.root, 'bitReverse', reverse_bits)

class _Labels(object):
    def labels(self, label_list_or_name: Union[list, str]) -> None:
        """
        Add label property to widget

        :param label_list_or_name: List of label strings or a single label string
        """
        if type(label_list_or_name) != list and type(label_list_or_name) != str:
            print("Parameter to labels must be a list of strings or a single string, not: {}".format(type(label_list_or_name)))
        else:
            root_label_tag = self.root.find('labels')
            if root_label_tag is None:
                root_label_tag = SubElement(self.root, 'labels')
            if type(label_list_or_name) == list:
                for label in label_list_or_name:
                    label_elem = SubElement(root_label_tag, "text")
                    label_elem.text = label
            else:
                self._shared.generic_property(root_label_tag, "text", label_list_or_name)

class _ArrayIndex(object):
    def array_index(self, index: int) -> None:
        """
        Add array index to widget

        :param index: Array index
        """
        self._shared.integer_property(self.root, 'array_index', index)

class _Symbols(object):
    def symbols(self, symbol_list_or_string: Union[list, str]) -> None:
        """
        Add symbol to widget. Symbols can be file name or text symbol

        :param symbol_list_or_string: List of strings/file names or single string/file name
        """
        if type(symbol_list_or_string) != list and type(symbol_list_or_string) != str:
            print("Parameter to labels must be a list of strings or a single string, not: {}".format(type(symbol_list_or_string)))
        else:
            root_label_tag = self.root.find('symbols')
            if root_label_tag is None:
                root_label_tag = SubElement(self.root, 'symbols')
            if type(symbol_list_or_string) == list:
                for label in symbol_list_or_string:
                    label_elem = SubElement(root_label_tag, "symbol")
                    label_elem.text = label
            else:
                self._shared.generic_property(root_label_tag, "symbol", symbol_list_or_string)

class _InitialIndex(object):
    def initial_index(self, index: int) -> None:
        """
        Add initial index to widget

        :param index: Index
        """
        self._shared.integer_property(self.root, 'initial_index', index)

class _ShowIndex(object):
    def show_index(self, show: bool = True) -> None:
        """
        Add show index option on widget. Default arg value is True

        :param show: Show index?
        """
        self._shared.boolean_property(self.root, 'show_index', show)

class _PreserveRatio(object):
    def preserve_ratio(self, preserve_ratio: bool = True) -> None:
        """
        Add preserve ratio option on widget. Default arg value is True

        :param preserve_ratio: Preserve ratio?
        """
        self._shared.boolean_property(self.root, 'preserve_ratio', preserve_ratio)

class _ShowScale(object):
    def show_scale(self, show: bool = True) -> None:
        """
        Add show scale option on widget. Default arg value is True

        :param show: Show scale?
        """
        self._shared.boolean_property(self.root, 'show_scale', show)

class _ShowMinorTicks(object):
    def show_minor_ticks(self, show: bool = True) -> None:
        """
        Add show minor ticks option on widget. Default arg value is True

        :param show: Show minor ticks?
        """
        self._shared.boolean_property(self.root, 'show_minor_ticks', show)

class _MajorTicksPixelDist(object):
    def major_ticks_pixel_dist(self, dist: int) -> None:
        """
        Add major ticks pixel distribution value to widget

        :param dist: Pixel distribution
        """
        self._shared.integer_property(self.root, 'major_tick_step_hint', dist)

class _ScaleFormat(object):
    def scale_format(self, format_string: str) -> None:
        """
        Add scale format string to widget

        :param format_string: Formatting string, ex: #.##
        """
        self._shared.generic_property(self.root, 'scale_format', format_string)

class _LevelsAndShow(object):
    def level_hihi(self, level: Union[float, int]) -> None:
        """
        Add HiHi level on widget

        :param level: HiHi level
        """
        self._shared.number_property(self.root, 'level_hihi', level)

    def level_high(self, level: Union[float, int]) -> None:
        """
        Add High level on widget

        :param level: High level
        """
        self._shared.number_property(self.root, 'level_high', level)

    def level_low(self, level: Union[float, int]) -> None:
        """
        Add Low level on widget

        :param level: Low level
        """
        self._shared.number_property(self.root, 'level_low', level)

    def level_lolo(self, level: Union[float, int]) -> None:
        """
        Add LoLo level on widget

        :param level: LoLo level
        """
        self._shared.number_property(self.root, 'level_lolo', level)

    def show_hihi(self, show: bool = True) -> None:
        """
        Add ShowHiHi option on widget. Default arg is True

        :param show: Show HiHi?
        """
        self._shared.boolean_property(self.root, 'show_hihi', show)

    def show_high(self, show: bool = True) -> None:
        """
        Add ShowHigh option on widget. Default arg is True

        :param show: Show High?
        """
        self._shared.boolean_property(self.root, 'show_high', show)

    def show_low(self, show: bool = True) -> None:
        """
        Add ShowLow option on widget. Default arg is True

        :param show: Show Low?
        """
        self._shared.boolean_property(self.root, 'show_low', show)

    def show_lolo(self, show: bool = True) -> None:
        """
        Add ShowLoLo option on widget. Default arg is True

        :param show: Show LoLo?
        """
        self._shared.boolean_property(self.root, 'show_lolo', show)

class _States(object):
    def _add_state(self, state_value, label, name, red, green, blue, alpha):
        root_states = self.root.find('states')
        if root_states is None:
            root_states = SubElement(self.root, 'states')
        root_state = SubElement(root_states, 'state')
        self._shared.integer_property(root_state, 'value', state_value)
        self._shared.generic_property(root_state, 'label', label)
        color_elem = SubElement(root_state, 'color')
        self._shared.create_color_element(color_elem, name, red, green, blue, alpha, False)

    def state(self, state_value: int, label: str, red: int, green: int, blue: int, alpha: int = 255) -> None:
        """
        Add state color to widget with RGB values

        :param state_value: Integer value of the state
        :param label: State label
        :param red: 0-255
        :param green: 0-255
        :param blue: 0-255
        :param alpha: 0-255. Default is 255
        """
        self._add_state(state_value, label, None, red, green, blue, alpha)

    def state_predefined_color(self, state_value: int, label: str, color_name: object) -> None:
        """
        Add state color to widget with a named color

        :param state_value: Integer value of the state
        :param label: State label
        :param color_name: <phoebusgen.colors> Predefined color name
        """
        self._add_state(state_value, label, color_name, None, None, None, None)

class _Fallback(object):
    def fallback_label(self, label: str) -> None:
        """
        Add fallback label to widget

        :param label: label
        """
        self._shared.generic_property(self.root, 'fallback_label', label)

    def predefined_fallback_color(self, name: object) -> None:
        """
        Add fallback color to widget with a named color

        :param name: <phoebusgen.colors> Predefined color name
        """
        e = self._shared.create_element(self.root, 'fallback_color')
        self._shared.create_color_element(e, name, None, None, None, None)

    def fallback_color(self, red: int, green: int, blue: int, alpha: int = 255) -> None:
        """
        Add fallback color to widget with RGB values

        :param red: 0-255
        :param green: 0-255
        :param blue: 0-255
        :param alpha: 0-255. Default is 255
        """
        e = self._shared.create_element(self.root, 'fallback_color')
        self._shared.create_color_element(e, None, red, green, blue, alpha)

class _SelectRows(object):
    def select_rows(self, select_rows: bool = True) -> None:
        """
        Add row selection mode to widget. Default arg is True

        :param select_rows: Are rows selectable?
        """
        self._shared.boolean_property(self.root, 'row_selection_mode', select_rows)

class _SelectionPV(object):
    def selection_pv(self, name: str) -> None:
        """
        Add selection PV to widget

        :param name: PV Name
        """
        self._shared.generic_property(self.root, 'selection_pv', name)

class _Columns(object):
    def column(self, name: str, width: int, editable: bool, options: Union[list, str]) -> None:
        """
        Add column property to widget

        :param name: Name of column
        :param width: Column width
        :param editable: Is column editable?
        :param options: List of strings or single string
        """
        columns_root = self.root.find("columns")
        if columns_root is None:
            columns_root = SubElement(self.root, "columns")
        column_elem = SubElement(columns_root, "column")
        self._shared.generic_property(column_elem, "name", name)
        self._shared.integer_property(column_elem, "width", width)
        self._shared.boolean_property(column_elem, "editable", editable)
        if options is None:
            return
        elif type(options) != list and type(options) != str:
            print("options parameter must be a list of strings or a single string")
            return
        options_root = column_elem.find("options")
        if options_root is None:
            options_root = SubElement(column_elem, "options")
        if type(options) == list:
            for opt in options:
                option_elem = SubElement(options_root, "option")
                option_elem.text = opt
        else:
            self._shared.generic_property(options_root, "option", options)

class _Title(object):
    def title(self, title: str) -> None:
        """
        Add title to widget

        :param title: Title
        """
        self._shared.generic_property(self.root, 'title', title)

class _AutoScale(object):
    def auto_scale(self, auto_scale: bool) -> None:
        """
        Add auto scale property to widget

        :param auto_scale: Auto scale image?
        """
        self._shared.boolean_property(self.root, 'autoscale', auto_scale)

class _DataHeightAndWidth(object):
    def data_height(self, height: int) -> None:
        """
        Add data height property to widget

        :param height: Data height
        """
        self._shared.integer_property(self.root, 'data_height', height)

    def data_width(self, width: int) -> None:
        """
        Add data width property to widget

        :param width: Data width
        """
        self._shared.integer_property(self.root, 'data_width', width)

class _UnsignedData(object):
    def unsigned_data(self, unsigned: bool = True) -> None:
        """
        Add unsigned data property to widget. Default arg is True

        :param unsigned: Is data unsigned?
        """
        self._shared.boolean_property(self.root, 'unsigned', unsigned)

class _LogScale(object):
    def log_scale(self, log_scale: bool = True) -> None:
        """
        Add log scale property to widget. Default arg is True

        :param log_scale: Use log scale?
        """
        self._shared.boolean_property(self.root, 'log_scale', log_scale)

class _ShowLegend(object):
    def show_legend(self, show_legend: bool = True) -> None:
        """
        Add show legend property to widget. Default arg is True

        :param show_legend: Show legend?
        """
        self._shared.boolean_property(self.root, 'show_legend', show_legend)

class _ShowGrid(object):
    def show_grid(self, show_grid: bool = True) -> None:
        """
        Add show grid property to widget. Default arg is True

        :param show_grid: Show grid?
        """
        self._shared.boolean_property(self.root, 'show_grid', show_grid)