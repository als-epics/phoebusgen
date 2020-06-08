import sys
sys.path.insert(1, '../phoebusgen/widget/')
sys.path.insert(1, './phoebusgen/widget/')
import unittest
import widget


class TestWidgetClass(unittest.TestCase):
    def setUp(self):
        self.base_type = 'test_widget_type'
        self.base_name = 'Just Basic Widget Test'
        self.base_x = 10
        self.base_y = 12
        self.base_width = 14
        self.base_height = 15

    def create_basic_widget(self):
        return widget.Widget(self.base_type, self.base_name, self.base_x,
                             self.base_y, self.base_width, self.base_height)

    def test_basic_widget(self):
        widget_type = 'label'
        name = 'Label_1'
        x = 10
        y = 12
        width = 14
        height = 15
        w = widget.Widget(widget_type, name, x, y, width, height)
        self.assertEqual(w.root.tag, 'widget')
        self.assertEqual(w.root.attrib['type'], 'label')
        self.assertEqual(w.root.attrib['version'], '2.0.0')

        self.assertEqual(len(w.root), 5)
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

    def test_visible_macro(self):
        w = self.create_basic_widget()

        self.assertEqual(w.root.tag, 'widget')
        self.assertEqual(w.root.attrib['type'], 'test_widget_type')
        self.assertEqual(w.root.attrib['version'], '2.0.0')

        self.assertEqual(len(w.root), 5)
        for child in w.root:
            if child.tag == 'name':
                self.assertEqual(child.text, self.base_name)
            elif child.tag == 'x':
                self.assertEqual(child.text, str(self.base_x))
            elif child.tag == 'y':
                self.assertEqual(child.text, str(self.base_y))
            elif child.tag == 'width':
                self.assertEqual(child.text, str(self.base_width))
            elif child.tag == 'height':
                self.assertEqual(child.text, str(self.base_height))

        w.set_visible(False)
        self.assertEqual(len(w.root), 6)
        for child in w.root:
            if child.tag == 'visible':
                self.assertEqual(child.text, 'False')

        w.add_macro('test', 'mac1')
        self.assertEqual(len(w.root), 7)
        for child in w.root:
            if child.tag == 'macros':
                self.assertEqual(len(child), 1)
                for macro in child:
                    self.assertEqual(macro.tag, 'test')
                    self.assertEqual(macro.text, 'mac1')
        w.add_macro('test2', 'mac2')
        self.assertEqual(len(w.root), 7)
        for child in w.root:
            if child.tag == 'macros':
                self.assertEqual(len(child), 2)
                for macro in child:
                    if child.tag == 'test2':
                        self.assertEqual(macro.text, 'mac2')


if __name__ == '__main__':
    unittest.main()
