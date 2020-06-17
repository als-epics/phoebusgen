import sys
sys.path.insert(1, '../phoebusgen/widget/')
sys.path.insert(1, './phoebusgen/widget/')
import unittest
import os
import widgets

def create_text_update():
    return widgets.TextUpdate('Generic TextUpdate', 'TEST:ME', 500, 300, 100, 20)


class TestTextUpdateClass(unittest.TestCase):
    def setUp(self):
        self.name = 'txt1'
        self.x = 11
        self.y = 13
        self.width = 16
        self.height = 19
        self.pv_name = 'test:pv'
        self.widget = widgets.TextUpdate(self.name, self.pv_name, self.x, self.y, self.width, self.height)

    def test_textupdate(self):
        name = 'Text Update'
        x = 10
        y = 12
        width = 14
        height = 15
        pv_name = 'tester'
        w = widgets.TextUpdate(name, pv_name, x, y, width, height)

        self.assertEqual(w.root.tag, 'widget')
        self.assertEqual(w.root.attrib['type'], 'textupdate')
        self.assertEqual(w.root.attrib['version'], '2.0.0')

        self.assertEqual(len(w.root), 6)
        for child in w.root:
            if child.tag == 'name':
                self.assertEqual(child.text, name)
            elif child.tag == 'x':
                self.assertEqual(child.text, str(x))
            elif child.tag == 'y':
                self.assertEqual(child.text, str(y))
            elif child.tag == 'width':
                self.assertEqual(child.text, str(width))
            elif child.tag == 'height':
                self.assertEqual(child.text, str(height))
            elif child.tag == 'pv_name':
                self.assertEqual(child.text, pv_name)

    def test_add_precision(self):
        self.widget.add_precision(2)
        foundIt = False
        for child in self.widget.root:
            if child.tag == 'precision':
                self.assertEqual(child.text, '2')
                foundIt = True
        self.assertTrue(foundIt)


class TestTextUpdateColors(unittest.TestCase):
    def setUp(self):
        self.name = 'txt1'
        self.x = 11
        self.y = 13
        self.width = 16
        self.height = 19
        self.pv_name = 'test:pv'
        self.widget = widgets.TextUpdate(self.name, self.pv_name, self.x, self.y, self.width, self.height)

    def test_predefined_foreground_color(self):
        self.widget.remove_element('foreground_color')
        self.assertIsNone(self.widget.find_element('foreground_color'))

        self.widget.add_predefined_foreground_color('DISCONNECTED')
        foreground_element = self.widget.find_element('foreground_color')
        self.assertIsNotNone(foreground_element)
        color_element = foreground_element.find('color')
        self.assertIsNotNone(color_element)
        # alpha shouldn't be there if it is default 255 (fix in code)
        self.assertEqual(len(color_element.attrib), 5)
        self.assertEqual(color_element.attrib['name'], 'DISCONNECTED')
        self.assertEqual(color_element.attrib['red'], '200')
        self.assertEqual(color_element.attrib['green'], '0')
        self.assertEqual(color_element.attrib['blue'], '200')
        self.assertEqual(color_element.attrib['alpha'], '200')

    def test_foreground_color(self):
        self.widget.remove_element('foreground_color')
        self.assertIsNone(self.widget.find_element('foreground_color'))

        self.widget.add_foreground_color(255, 255, 200)
        foreground_element = self.widget.find_element('foreground_color')
        self.assertIsNotNone(foreground_element)
        color_element = foreground_element.find('color')
        self.assertIsNotNone(color_element)
        # alpha shouldn't be there if it is default 255 (fix in code)
        self.assertEqual(len(color_element.attrib), 4)
        self.assertEqual(color_element.attrib['red'], '255')
        self.assertEqual(color_element.attrib['green'], '255')
        self.assertEqual(color_element.attrib['blue'], '200')
        self.assertEqual(color_element.attrib['alpha'], '255')

    def test_background_color(self):
        self.widget.remove_element('background_color')
        self.assertIsNone(self.widget.find_element('background_color'))

        self.widget.add_background_color(201, 100, 41, 2)
        background_element = self.widget.find_element('background_color')
        self.assertIsNotNone(background_element)
        color_element = background_element.find('color')
        self.assertIsNotNone(color_element)
        # alpha shouldn't be there if it is default 255 (fix in code)
        self.assertEqual(len(color_element.attrib), 4)
        self.assertEqual(color_element.attrib['red'], '201')
        self.assertEqual(color_element.attrib['green'], '100')
        self.assertEqual(color_element.attrib['blue'], '41')
        self.assertEqual(color_element.attrib['alpha'], '2')

    def test_predefined_background_color(self):
        self.widget.remove_element('background_color')
        self.assertIsNone(self.widget.find_element('background_color'))

        self.widget.add_predefined_background_color('On')
        background_color = self.widget.find_element('background_color')
        self.assertIsNotNone(background_color)
        color_element = background_color.find('color')
        self.assertIsNotNone(color_element)
        # alpha shouldn't be there if it is default 255 (fix in code)
        self.assertEqual(len(color_element.attrib), 5)
        self.assertEqual(color_element.attrib['name'], 'On')
        self.assertEqual(color_element.attrib['red'], '0')
        self.assertEqual(color_element.attrib['green'], '255')
        self.assertEqual(color_element.attrib['blue'], '0')
        self.assertEqual(color_element.attrib['alpha'], '255')


class TestTextUpdateFont(unittest.TestCase):
    def setUp(self):
        self.name = 'txt1'
        self.x = 11
        self.y = 13
        self.width = 16
        self.height = 19
        self.pv_name = 'test:pv'
        self.widget = widgets.TextUpdate(self.name, self.pv_name, self.x, self.y, self.width, self.height)

    def test_add_font(self):
        self.widget.remove_element('font')
        self.assertIsNone(self.widget.find_element('font'))
        self.widget.add_font()
        foundOuterFont = False
        foundInnerFont = False
        for child in self.widget.root:
            if child.tag == 'font':
                foundOuterFont = True
                self.assertEqual(child.text, None)
                for c in child:
                    if c.tag == 'font':
                        foundInnerFont = True
                        self.assertEqual(len(c.attrib), 3)
                        self.assertEqual(c.attrib['family'], 'Liberation Sans')
                        self.assertEqual(c.attrib['style'], 'Regular')
                        self.assertEqual(c.attrib['size'], '14')

        self.assertTrue(foundOuterFont)
        self.assertTrue(foundInnerFont)

    def test_add_font_with_name(self):
        self.widget.remove_element('font')
        self.assertIsNone(self.widget.find_element('font'))
        self.widget.add_predefined_font('Header 1')
        foundOuterFont = False
        foundInnerFont = False
        for child in self.widget.root:
            if child.tag == 'font':
                foundOuterFont = True
                self.assertEqual(child.text, None)
                for c in child:
                    if c.tag == 'font':
                        foundInnerFont = True
                        self.assertEqual(len(c.attrib), 3)
                        self.assertEqual(c.attrib['family'], 'Liberation Sans')
                        self.assertEqual(c.attrib['style'], 'Bold')
                        self.assertEqual(c.attrib['size'], '22')

        self.assertTrue(foundOuterFont)
        self.assertTrue(foundInnerFont)

    def test_add_font_with_family(self):
        self.widget.remove_element('font')
        self.assertIsNone(self.widget.find_element('font'))

        foundOuterFont = False
        foundInnerFont = False
        fam = 'Noto Sans Sinhala Thin'
        self.widget.add_font(family=fam)
        self.assertEqual(len(self.widget.root), 7)
        for child in self.widget.root:
            if child.tag == 'font':
                foundOuterFont = True
                self.assertEqual(child.text, None)
                for c in child:
                    if c.tag == 'font':
                        foundInnerFont = True
                        self.assertEqual(len(c.attrib), 3)
                        self.assertEqual(c.attrib['family'], fam)
                        self.assertEqual(c.attrib['style'], 'Regular')
                        self.assertEqual(c.attrib['size'], '14')

        self.assertTrue(foundOuterFont)
        self.assertTrue(foundInnerFont)

    def test_add_font_with_family_and_size(self):
        self.widget.remove_element('font')
        self.assertIsNone(self.widget.find_element('font'))
        foundOuterFont = False
        foundInnerFont = False

        fam = 'Noto Sans Sinhala Thin'
        size = 24
        self.widget.add_font(size=24, family=fam)
        self.assertEqual(len(self.widget.root), 7)
        for child in self.widget.root:
            if child.tag == 'font':
                foundOuterFont = True
                self.assertEqual(child.text, None)
                for c in child:
                    if c.tag == 'font':
                        foundInnerFont = True
                        self.assertEqual(len(c.attrib), 3)
                        self.assertEqual(c.attrib['family'], fam)
                        self.assertEqual(c.attrib['style'], 'Regular')
                        self.assertEqual(c.attrib['size'], str(size))

        self.assertTrue(foundOuterFont)
        self.assertTrue(foundInnerFont)


    def test_add_font_with_family_and_size_and_style(self):
        self.widget.remove_element('font')
        self.assertIsNone(self.widget.find_element('font'))

        fam = 'Noto Sans Sinhala Thin'
        size = 24
        style = 'BOLD'
        self.widget.add_font(fam, style, size)
        self.assertEqual(len(self.widget.root), 7)
        for child in self.widget.root:
            if child.tag == 'font':
                self.assertEqual(child.text, None)
                for c in child:
                    if c.tag == 'font':
                        self.assertEqual(len(c.attrib), 3)
                        self.assertEqual(c.attrib['family'], fam)
                        self.assertEqual(c.attrib['style'], style)
                        self.assertEqual(c.attrib['size'], str(size))


class TestTextUpdateBorder(unittest.TestCase):
    def setUp(self):
        self.widget = create_text_update()

    def test_border_width(self):
        pass


class TestTextUpdateProperties(unittest.TestCase):
    def setUp(self):
        self.textupdate = create_text_update()

    def test_init(self):
        curr_path = os.path.dirname(__file__)
        with open(curr_path + '/../files/widgets/text-update.bob') as f:
            xml = f.read()
            self.assertEqual(xml, self.textupdate.prettify(self.textupdate.root))

    def generic_element_test(self, tag_name, value):
        element = self.textupdate.find_element(tag_name)
        self.assertIsNotNone(element)
        if value is None:
            self.assertIsNone(element.text)
        else:
            self.assertEqual(element.text, str(value))
        self.textupdate.remove_element(tag_name)
        self.assertIsNone(self.textupdate.find_element(tag_name))

    def child_element_test(self, parent_tag, tag_name, value, attrib):
        parent = self.textupdate.find_element(parent_tag)
        self.assertIsNotNone(parent)
        child = parent.find(tag_name)
        self.assertIsNotNone(child)
        if value is None:
            self.assertIsNone(child.text)
        else:
            self.assertEqual(child.text, str(value))
        self.assertEqual(child.attrib, attrib)

        self.textupdate.remove_element(parent_tag)
        self.assertIsNone(self.textupdate.find_element(parent_tag))

    def test_font(self):
        tag_name = 'font'
        value = 'Header 1'
        self.textupdate.add_predefined_font(value)
        self.child_element_test(tag_name, 'font', None, {'family': 'Liberation Sans', 'size': '22', 'style': 'Bold'})

    def test_predefined_foreground_color(self):
        tag_name = 'foreground_color'
        value = 'Background'
        self.textupdate.add_predefined_foreground_color(value)
        self.child_element_test(tag_name, 'color', None, {'name': 'Background', 'red': '255', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})

    def test_foreground_color(self):
        tag_name = 'foreground_color'
        self.textupdate.add_foreground_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '255'})

    def test_predefined_background_color(self):
        tag_name = 'background_color'
        value = 'MINOR'
        self.textupdate.add_predefined_background_color(value)
        self.child_element_test(tag_name, 'color', None, {'name': 'MINOR', 'red': '255', 'green': '128', 'blue': '0', 'alpha': '255'})

    def test_foreground_color(self):
        tag_name = 'background_color'
        self.textupdate.add_background_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10', 'blue': '15', 'alpha': '255'})

    def test_transparent(self):
        tag_name = 'transparent'
        value = True
        self.textupdate.add_transparent(value)
        self.generic_element_test(tag_name, str(value))

    def test_format(self):
        tag_name = 'format'
        value = 'Engineering'
        xml_value = '3'
        self.textupdate.add_format(value)
        self.generic_element_test(tag_name, xml_value)

    def test_precision(self):
        tag_name = 'precision'
        value = 25.3
        real_value = '25'
        self.textupdate.add_precision(value)
        self.generic_element_test(tag_name, real_value)

    def test_show_units(self):
        tag_name = 'show_units'
        value = False
        self.textupdate.add_show_units(value)
        self.generic_element_test(tag_name, value)

    def test_horizontal_alignment(self):
        tag_name = 'horizontal_alignment'
        value = 'Center'
        xml_value = 1
        self.textupdate.add_horizontal_alignment(value)
        self.generic_element_test(tag_name, xml_value)

    def test_vertical_alignment(self):
        tag_name = 'vertical_alignment'
        value = 'Middle'
        xml_value = 1
        self.textupdate.add_vertical_alignment(value)
        self.generic_element_test(tag_name, xml_value)

    def test_wrap_words(self):
        tag_name = 'wrap_words'
        value = False
        self.textupdate.add_wrap_words(value)
        self.generic_element_test(tag_name, value)

    def test_rotation_step(self):
        tag_name = 'rotation_step'
        value = 180
        xml_value = 2
        self.textupdate.add_rotation_step(value)
        self.generic_element_test(tag_name, xml_value)

    def test_border_width(self):
        tag_name = 'border_width'
        value = 2
        self.textupdate.add_border_width(value)
        self.generic_element_test(tag_name, value)

    def test_border_color(self):
        tag_name = 'border_color'
        self.textupdate.add_border_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10', 'blue': '15', 'alpha': '255'})

    def test_predefined_border_color(self):
        tag_name = 'border_color'
        value = 'Attention'
        self.textupdate.add_predefined_border_color(value)
        self.child_element_test(tag_name, 'color', None, {'name': 'Attention', 'red': '255', 'green': '160',
                                                          'blue': '0', 'alpha': '255'})


if __name__ == '__main__':
    unittest.main()
