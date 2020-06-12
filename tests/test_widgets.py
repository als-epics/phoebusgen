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
        self.widget.add_horizontal_alignment('right')
        self.widget.print_widget()


    def test_add_font_with_family(self):
        w = widgets.TextUpdate(self.name, self.pv_name, self.x, self.y, self.height, self.width)

        foundOuterFont = False
        foundInnerFont = False
        fam = 'Noto Sans Sinhala Thin'
        w.add_font(family=fam)
        self.assertEqual(len(w.root), 7)
        for child in w.root:
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
        w = widgets.TextUpdate(self.name, self.pv_name, self.x, self.y, self.height, self.width)
        foundOuterFont = False
        foundInnerFont = False

        fam = 'Noto Sans Sinhala Thin'
        size = 24
        w.add_font(size=24, family=fam)
        self.assertEqual(len(w.root), 7)
        for child in w.root:
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


    def test_add_font_with_family_and_size(self):
        w = widgets.TextUpdate(self.name, self.pv_name, self.x, self.y, self.height, self.width)

        fam = 'Noto Sans Sinhala Thin'
        size = 24
        style = 'BOLD'
        w.add_font(fam, style, size)
        self.assertEqual(len(w.root), 7)
        for child in w.root:
            if child.tag == 'font':
                self.assertEqual(child.text, None)
                for c in child:
                    if c.tag == 'font':
                        self.assertEqual(len(c.attrib), 3)
                        self.assertEqual(c.attrib['family'], fam)
                        self.assertEqual(c.attrib['style'], style)
                        self.assertEqual(c.attrib['size'], str(size))


class TestLabelClass(unittest.TestCase):
    def test_label(self):
        name = 'Label_1'
        x = 10
        y = 12
        width = 14
        height = 15
        text = 'TEST label'
        w = widgets.Label(name, x, y, width, height, text)

        self.assertEqual(w.root.tag, 'widget')
        self.assertEqual(w.root.attrib['type'], 'label')
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
            elif child.tag == 'text':
                self.assertEqual(child.text, text)


if __name__ == '__main__':
    unittest.main()
