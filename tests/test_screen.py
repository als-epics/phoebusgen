import sys
sys.path.insert(1, '../phoebusgen/screen/')
sys.path.insert(1, './phoebusgen/screen/')
sys.path.insert(1, '../phoebusgen/widget/')
sys.path.insert(1, './phoebusgen/widget/')
sys.path.insert(1, '../phoebusgen/')
sys.path.insert(1, './phoebusgen/')
import unittest
import screen as s
import widgets
from phoebusgen import colors


class TestScreen(unittest.TestCase):
    def setUp(self):
        self.name = 'test screen'
        self.file_name = './test.bob'
        self.test_screen = s.Screen(self.name, self.file_name)

    def child_element_test(self, parent_tag, tag_name, value, attrib, do_not_remove=False):
        parent = self.test_screen.find_widget(parent_tag)
        self.assertIsNotNone(parent)
        child = parent.find(tag_name)
        self.assertIsNotNone(child)
        if value is None:
            self.assertIsNone(child.text)
        else:
            self.assertEqual(child.text, str(value))
        self.assertEqual(child.attrib, attrib)

    def test_screen_blank(self):
        self.assertEqual(len(self.test_screen.root), 1)
        element = widgets.TextUpdate('Text Update 1', 'TEST:ME', 200, 200, 160, 20)
        self.test_screen.add_widget(element)
        self.assertEqual(len(self.test_screen.root), 2)
        element2 = widgets.TextUpdate('Text Update 2', 'TEST:ME', 200, 200, 160, 20)
        element3 = widgets.TextUpdate('Text Update 3', 'TEST:ME', 200, 200, 160, 20)
        self.test_screen.add_widget([element2, element3])
        self.assertEqual(len(self.test_screen.root), 4)

    def test_width(self):
        self.test_screen.width(500)
        elem = self.test_screen.find_widget('width')
        self.assertIsNotNone(elem)
        self.assertEqual(str(500), elem.text)

    def test_height(self):
        self.test_screen.height(102.2)
        elem = self.test_screen.find_widget('height')
        self.assertIsNotNone(elem)
        self.assertEqual(str(102.2), elem.text)

    def test_macro(self):
        self.test_screen.macro('test', 'mac1')
        self.child_element_test('macros', 'test', 'mac1', {}, True)
        self.test_screen.macro('test2', 'mac2')
        self.child_element_test('macros', 'test', 'mac1', {}, True)

    def test_predefined_background_color(self):
        tag_name = 'background_color'
        value = 'MINOR'
        self.test_screen.predefined_background_color(colors.MINOR)
        self.child_element_test(tag_name, 'color', None, {'name': 'MINOR', 'red': '255', 'green': '128', 'blue': '0', 'alpha': '255'})

    def test_background_color(self):
        tag_name = 'background_color'
        self.test_screen.background_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10', 'blue': '15', 'alpha': '255'})


if __name__ == '__main__':
    unittest.main()
