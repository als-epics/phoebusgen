import sys
sys.path.insert(1, '../phoebusgen/widget/')
sys.path.insert(1, './phoebusgen/widget/')
import unittest
from xml.etree.ElementTree import Element, SubElement
import _property


class TestGenericPropertyElements(unittest.TestCase):
    def setUp(self):
        self.element = Element('test_root')
        self.prop_factory = _property.Property(self.element)

    def test_init(self):
        self.assertIsInstance(self.prop_factory.root, Element)

    def generic_element_test(self, tag_name, tag_value):
        new_element = self.prop_factory.root.find(tag_name)
        self.assertIsNotNone(new_element)
        if type(tag_value) == bool:
            self.assertEqual(new_element.text, str(tag_value).lower())
        else:
            self.assertEqual(new_element.text, str(tag_value))
        self.assertEqual(new_element.attrib, {})
        self.prop_factory.root.remove(new_element)
        self.assertIsNone(self.prop_factory.root.find(tag_name))

    def test_pv_name(self):
        tag_name = 'pv_name'
        pv = 'test:pv'
        self.prop_factory.add_pv_name(pv)
        self.generic_element_test(tag_name, pv)

    def test_precision(self):
        tag_name = 'precision'
        precision = 2
        self.prop_factory.add_precision(precision)
        self.generic_element_test(tag_name, precision)

    def test_show_units(self):
        tag_name = 'show_units'
        show = False
        self.prop_factory.add_show_units(show)
        self.generic_element_test(tag_name, show)

    def test_multi_line(self):
        tag_name = 'multi_line'
        show = True
        self.prop_factory.add_multi_line(show)
        self.generic_element_test(tag_name, show)

    def test_wrap_words(self):
        tag_name = 'wrap_words'
        wrap = True
        self.prop_factory.add_wrap_words(wrap)
        self.generic_element_test(tag_name, wrap)

    def test_bit(self):
        tag_name = 'bit'
        val = 124
        self.prop_factory.add_bit(val)
        self.generic_element_test(tag_name, val)

    def test_transparent(self):
        tag_name = 'transparent'
        transparent = False
        self.prop_factory.add_transparent(transparent)
        self.generic_element_test(tag_name, transparent)

    def test_horizontal_alignment_top(self):
        tag_name = 'horizontal_alignment'
        alignment = 'LeFT'
        xml_alignment_value = 0
        self.prop_factory.add_horizontal_alignment(alignment)
        self.generic_element_test(tag_name, xml_alignment_value)

    def test_horizontal_alignment_middle(self):
        tag_name = 'horizontal_alignment'
        alignment = 'center'
        xml_alignment_value = 1
        self.prop_factory.add_horizontal_alignment(alignment)
        self.generic_element_test(tag_name, xml_alignment_value)

    def test_horizontal_alignment_bottom(self):
        tag_name = 'horizontal_alignment'
        alignment = 'RIGHt'
        xml_alignment_value = 2
        self.prop_factory.add_horizontal_alignment(alignment)
        self.generic_element_test(tag_name, xml_alignment_value)

    def test_horizontal_alignment_wrong_input(self):
        tag_name = 'horizontal_alignment'
        alignment = 'L'
        self.prop_factory.add_horizontal_alignment(alignment)
        self.assertIsNone(self.prop_factory.root.find(tag_name))

    def test_vertical_alignment_top(self):
        tag_name = 'vertical_alignment'
        alignment = 'ToP'
        xml_alignment_value = 0
        self.prop_factory.add_vertical_alignment(alignment)
        self.generic_element_test(tag_name, xml_alignment_value)

    def test_vertical_alignment_middle(self):
        tag_name = 'vertical_alignment'
        alignment = 'Middle'
        xml_alignment_value = 1
        self.prop_factory.add_vertical_alignment(alignment)
        self.generic_element_test(tag_name, xml_alignment_value)

    def test_vertical_alignment_bottom(self):
        tag_name = 'vertical_alignment'
        alignment = 'BOTTOM'
        xml_alignment_value = 2
        self.prop_factory.add_vertical_alignment(alignment)
        self.generic_element_test(tag_name, xml_alignment_value)

    def test_vertical_alignment_wrong_input(self):
        tag_name = 'vertical_alignment'
        alignment = 'BOTTO'
        self.prop_factory.add_vertical_alignment(alignment)
        self.assertIsNone(self.prop_factory.root.find(tag_name))

    def test_rotation_step(self):
        tag_name = 'rotation_step'
        rotation = -90
        xml_rotation_value = 3
        self.prop_factory.add_rotation_step(rotation)
        self.generic_element_test(tag_name, xml_rotation_value)

    def test_rotation_step_wrong_input(self):
        rotation = 234
        self.prop_factory.add_rotation_step(rotation)
        self.assertIsNone(self.prop_factory.root.find('rotation_step'))

    def test_border_width(self):
        tag_name = 'border_width'
        width = 5
        self.prop_factory.add_border_width(width)
        self.generic_element_test(tag_name, width)

    def test_border_width_float(self):
        tag_name = 'border_width'
        width = 2.5
        self.prop_factory.add_border_width(width)
        self.generic_element_test(tag_name, int(width))

    def test_border_width_wrong(self):
        tag_name = 'border_width'
        width = 'dsfds'
        self.prop_factory.add_border_width(width)
        self.assertIsNone(self.prop_factory.root.find(tag_name))

    def test_format_binary(self):
        tag_name = 'format'
        format = 'Binary'
        xml_format_value = 10
        self.prop_factory.add_format(format)
        self.generic_element_test(tag_name, xml_format_value)

    def test_format_decimal(self):
        tag_name = 'format'
        format = 'dEcimal'
        xml_format_value = 1
        self.prop_factory.add_format(format)
        self.generic_element_test(tag_name, xml_format_value)

    def test_format_wrong_input(self):
        tag_name = 'format'
        format = 'dsfds'
        self.prop_factory.add_format(format)
        self.assertIsNone(self.prop_factory.root.find(tag_name))

    def test_auto_size_true(self):
        tag_name = 'auto_size'
        auto = True
        self.prop_factory.add_auto_size(auto)
        self.generic_element_test(tag_name, str(auto).lower())

    def test_auto_size_false(self):
        tag_name = 'auto_size'
        auto = False
        self.prop_factory.add_auto_size(auto)
        self.generic_element_test(tag_name, auto)

    def test_text(self):
        tag_name = 'text'
        text = 'TEST TEST TEST'
        self.prop_factory.add_text(text)
        self.generic_element_test(tag_name, text)


class TestColorPropertyElements(unittest.TestCase):
    def setUp(self):
        self.element = Element('test_root')
        self.prop_factory = _property.Property(self.element)
        self.color_dict = {'activetext': {'red': '255', 'green': '255', 'blue': '0', 'alpha': '255'},
                           'attention': {'red': '255', 'green': '160', 'blue': '0', 'alpha': '255'},
                           'background': {'red': '255', 'green': '255', 'blue': '255', 'alpha': '255'},
                           'button_background': {'red': '210', 'green': '210', 'blue': 210, 'alpha': '255'},
                           'disconnected': {'red': '200', 'green': '0', 'blue': '200', 'alpha': '200'},
                           'grid': {'red': '128', 'green': '128', 'blue': '128', 'alpha': '255'},
                           'header_background': {'red': '77', 'green': '77', 'blue': '77', 'alpha': '255'},
                           'header_foreground': {'red': '255', 'green': '255', 'blue': '255', 'alpha': '255'},
                           'invalid': {'red': '255', 'green': '0', 'blue': '255', 'alpha': '255'},
                           'major': {'red': '255', 'green': '0', 'blue': '0', 'alpha': '255'},
                           'minor': {'red': '255', 'green': '128', 'blue': '0', 'alpha': '255'},
                           'off': {'red': '60', 'green': '100', 'blue': '60', 'alpha': '255'},
                           'ok': {'red': '0', 'green': '255', 'blue': '0', 'alpha': '255'},
                           'on': {'red': '0', 'green': '255', 'blue': '0', 'alpha': '255'},
                           'read_background': {'red': '240', 'green': '240', 'blue': '240', 'alpha': '255'},
                           'stop': {'red': '255', 'green': '0', 'blue': '0', 'alpha': '255'},
                           'text': {'red': '0', 'green': '0', 'blue': '0', 'alpha': '255'},
                           'transparent': {'red': '255', 'green': '255', 'blue': '255', 'alpha': '0'},
                           'write_background': {'red': '128', 'green': '255', 'blue': '255', 'alpha': '255'}}

    def test_init(self):
        self.assertIsInstance(self.prop_factory.root, Element)
        self.assertEqual(self.prop_factory.root.tag, 'test_root')

    def color_test(self, tag_name, name, red, green, blue, alpha):
        parent_element = self.prop_factory.root.find(tag_name)
        self.assertIsNotNone(parent_element)
        self.assertIsNone(parent_element.text)
        child_element = parent_element.find('color')
        self.assertIsNotNone(child_element)
        if name is None:
            attrib_dict = {'red': str(red), 'green': str(green), 'blue': str(blue), 'alpha': str(alpha)}
        else:
            color_item = self.color_dict.get(name.lower())
            self.assertIsNotNone(color_item)
            new_red = color_item['red']
            new_green = color_item['green']
            new_blue = color_item['blue']
            new_alpha = color_item['alpha']
            attrib_dict = {'name': name, 'red': new_red, 'green': new_green, 'blue': new_blue, 'alpha': new_alpha}
        self.assertEqual(child_element.attrib, attrib_dict)
        self.assertIsNone(child_element.text)
        # clean up so we can run multiple tests on same element
        self.prop_factory.root.remove(parent_element)
        self.assertIsNone(self.prop_factory.root.find(tag_name))
        self.assertIsNone(self.prop_factory.root.find('color'))

    def test_background_color(self):
        tag_name = 'background_color'
        red = 255
        green = 255
        blue = 255
        alpha = 255
        name = None
        self.prop_factory.add_background_color(name, red, green, blue, alpha)
        self.color_test(tag_name, name, red, green, blue, alpha)

    def test_background_color_2(self):
        tag_name = 'background_color'
        red = '25'
        green = 265
        blue = 21
        alpha = 32
        name = None
        self.prop_factory.add_background_color(name, red, green, blue, alpha)
        self.color_test(tag_name, name, red, green, blue, alpha)

    def test_predefined_background_color(self):
        tag_name = 'background_color'
        red = 255
        green = 255
        blue = 255
        alpha = 255
        name = 'OFF'
        self.prop_factory.add_background_color(name, red, green, blue, alpha)
        self.color_test(tag_name, name, red, green, blue, alpha)

    def test_predefined_background_color_wrong(self):
        tag_name = 'background_color'
        red = 255
        green = 255
        blue = 255
        alpha = 255
        name = 'sdaflkdasf'
        self.prop_factory.add_background_color(name, red, green, blue, alpha)
        self.assertIsNone(self.prop_factory.root.find(tag_name))
        self.assertIsNone(self.prop_factory.root.find('color'))

    def test_foreground_color(self):
        tag_name = 'foreground_color'
        red = 255
        green = 255
        blue = 255
        alpha = 255
        name = None
        self.prop_factory.add_foreground_color(name, red, green, blue, alpha)
        self.color_test(tag_name, name, red, green, blue, alpha)

    def test_foreground_color_2(self):
        tag_name = 'foreground_color'
        red = '25'
        green = 265
        blue = 21
        alpha = 32
        name = None
        self.prop_factory.add_foreground_color(name, red, green, blue, alpha)
        self.color_test(tag_name, name, red, green, blue, alpha)

    def test_predefined_foreground_color(self):
        tag_name = 'foreground_color'
        red = 255
        green = 255
        blue = 255
        alpha = 255
        name = 'Header_Foreground'
        self.prop_factory.add_foreground_color(name, red, green, blue, alpha)
        self.color_test(tag_name, name, red, green, blue, alpha)

    def test_predefined_foreground_color_wrong(self):
        tag_name = 'foreground_color'
        red = 255
        green = 255
        blue = 255
        alpha = 255
        name = 'sdaflkdasf'
        self.prop_factory.add_foreground_color(name, red, green, blue, alpha)
        self.assertIsNone(self.prop_factory.root.find(tag_name))
        self.assertIsNone(self.prop_factory.root.find('color'))

    def test_border_color(self):
        tag_name = 'border_color'
        red = 0
        green = 0
        blue = 0
        alpha = 255
        name = None
        self.prop_factory.add_border_color(name, red, green, blue, alpha)
        self.color_test(tag_name, name, red, green, blue, alpha)

    def test_border_color_2(self):
        tag_name = 'border_color'
        red = 0
        green = 0
        blue = 21
        alpha = 255
        name = None
        self.prop_factory.add_border_color(name, red, green, blue, alpha)
        self.color_test(tag_name, name, red, green, blue, alpha)

    def test_predefined_border_color(self):
        tag_name = 'border_color'
        red = 255
        green = 255
        blue = 255
        alpha = 0
        name = 'MAJOR'
        self.prop_factory.add_border_color(name, red, green, blue, alpha)
        self.color_test(tag_name, name, red, green, blue, alpha)

    def test_predefined_border_color_wrong(self):
        tag_name = 'border_color'
        red = 255
        green = 255
        blue = 255
        alpha = 255
        name = 'sdaflkdasf'
        self.prop_factory.add_border_color(name, red, green, blue, alpha)
        self.assertIsNone(self.prop_factory.root.find(tag_name))
        self.assertIsNone(self.prop_factory.root.find('color'))


class TestFontPropertyElements(unittest.TestCase):
    def setUp(self):
        self.element = Element('test_ROOT_tag test')
        self.prop_factory = _property.Property(self.element)
        self.font_dict = {'comment': {'family': 'Liberation Sans', 'size': '14', 'style': 'Italic'},
                          'default': {'family': 'Liberation Sans', 'size': '14', 'style': 'Regular'},
                          'default bold': {'family': 'Liberation Sans', 'size': '14', 'style': 'Bold'},
                          'fine print': {'family': 'Liberation Sans', 'size': '12', 'style': 'Regular'},
                          'header 1': {'family': 'Liberation Sans', 'size': '22', 'style': 'Bold'},
                          'header 2': {'family': 'Liberation Sans', 'size': '18', 'style': 'Bold'},
                          'header 3': {'family': 'Liberation Sans', 'size': '16', 'style': 'Bold'},
                          'oddball': {'family': 'Liberation Sans', 'size': '40', 'style': 'Regular'}}

    def test_init(self):
        self.assertIsInstance(self.prop_factory.root, Element)
        self.assertEqual(self.prop_factory.root.tag, 'test_ROOT_tag test')

    def font_test(self, name, family, style, size):
        outer_font_element = self.prop_factory.root.find('font')
        self.assertIsNotNone(outer_font_element)
        inner_font_element = outer_font_element.find('font')
        self.assertIsNotNone(inner_font_element)

        self.assertIsNone(outer_font_element.text)
        self.assertIsNone(inner_font_element.text)

        if name is None:
            attrib_dict = {'family': str(family), 'style': str(style), 'size': str(size)}
        else:
            font_item = self.font_dict.get(name.lower())
            self.assertIsNotNone(font_item)
            new_family = font_item['family']
            new_style = font_item['style']
            new_size = font_item['size']
            attrib_dict = {'family': new_family, 'style': new_style, 'size': new_size}

        self.assertEqual(inner_font_element.attrib, attrib_dict)
        self.assertEqual(outer_font_element.attrib, {})

        self.prop_factory.root.remove(outer_font_element)
        self.assertIsNone(self.prop_factory.root.find('font'))

    def test_predefined_font(self):
        name = 'OddBall'
        family = 'dont care bc we have a name'
        style = 'Not a style'
        size = 523
        self.prop_factory.add_font(family, style, size, name)
        self.font_test(name, family, style, size)

    def test_predefined_font_wrong(self):
        name = 'NotAFont'
        family = 'dont care bc we are wrong'
        style = 'Not a style'
        size = 5
        self.prop_factory.add_font(family, style, size, name)
        self.assertIsNone(self.prop_factory.root.find('font'))

    def test_random_font(self):
        name = None
        family = 'Lohit Gujarati'
        style = 'Bold'
        size = 12
        self.prop_factory.add_font(family, style, size, name)
        self.font_test(name, family, style, size)


if __name__ == '__main__':
    unittest.main()
