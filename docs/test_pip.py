import unittest


class TestPip(unittest.TestCase):
    def test_import(self):
        import phoebusgen.widget as w

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


if __name__ == '__main__':
    unittest.main()
