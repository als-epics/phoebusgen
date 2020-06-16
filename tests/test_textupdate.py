import sys
sys.path.insert(1, '../phoebusgen/widget/')
sys.path.insert(1, './phoebusgen/widget/')
import unittest
import widgets


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

    def test_predefined_foreground_color(self):
        self.widget.add_predefined_foreground_color('DISCONNECTED')

    def test_foreground_color(self):
        w = widgets.TextUpdate(self.name, self.pv_name, self.x, self.y, self.height, self.width)
        w.add_foreground_color(255, 255, 200)



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
        self.assertEqual(self.widget.find_element('font'), None)

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
        self.assertEqual(self.widget.find_element('font'), None)
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
        self.assertEqual(self.widget.find_element('font'), None)

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


if __name__ == '__main__':
    unittest.main()
