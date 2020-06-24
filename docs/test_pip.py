import unittest
import os


class TestPip(unittest.TestCase):
    def test_import(self):
        import phoebusgen.widget as w
        import phoebusgen.screen as s

        text_update_widget = w.TextUpdate('test widget', 'TEST:PV', 10, 20, 20, 50)
        self.assertEqual(text_update_widget.find_element('pv_name').text, 'TEST:PV')
        self.assertEqual(text_update_widget.find_element('name').text, 'test widget')
        self.assertEqual(text_update_widget.find_element('x').text, '10')
        self.assertEqual(text_update_widget.find_element('y').text, '20')
        self.assertEqual(text_update_widget.find_element('width').text, '20')
        self.assertEqual(text_update_widget.find_element('height').text, '50')

        text_update_widget.predefined_foreground_color('OK')
        self.assertEqual(text_update_widget.find_element('foreground_color').text, None)
        self.assertEqual(text_update_widget.find_element('foreground_color').find('color').attrib,
                         {'name': 'OK',
                          'red': '0',
                          'green': '255',
                          'blue': '0',
                          'alpha': '255'
                          })

        my_screen = s.Screen('test screen')


        curr_path = os.path.dirname(__file__)
        with open(curr_path + '/../files/new.bob') as f:
            xml = f.read()
            self.assertEqual(xml, my_screen.prettify(my_screen.root))

        self.assertEqual(len(my_screen.root), 1)

        my_screen.add_widget(text_update_widget)
        self.assertEqual(len(my_screen.root), 2)


if __name__ == '__main__':
    unittest.main()
