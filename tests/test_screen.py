import sys
sys.path.insert(1, '../phoebusgen/screen/')
sys.path.insert(1, './phoebusgen/screen/')
sys.path.insert(1, '../phoebusgen/widget/')
sys.path.insert(1, './phoebusgen/widget/')
import unittest
import screen as s
import widgets


class TestScreen(unittest.TestCase):
    def setUp(self):
        self.name = 'test screen'
        self.file_name = './test.bob'
        self.test_screen = s.Screen(self.name, self.file_name)

    def test_screen_blank(self):
        self.assertEqual(len(self.test_screen.root), 1)
        element = widgets.TextUpdate('Text Update 1', 'TEST:ME', 200, 200, 160, 20)
        self.test_screen.add_widget(element)
        self.assertEqual(len(self.test_screen.root), 2)
        element2 = widgets.TextUpdate('Text Update 2', 'TEST:ME', 200, 200, 160, 20)
        element3 = widgets.TextUpdate('Text Update 3', 'TEST:ME', 200, 200, 160, 20)
        self.test_screen.add_widget([element2, element3])
        self.assertEqual(len(self.test_screen.root), 4)


if __name__ == '__main__':
    unittest.main()
