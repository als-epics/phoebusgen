import sys
sys.path.insert(1, '../phoebusgen/widget/')
sys.path.insert(1, './phoebusgen/widget/')
import unittest
import widgets


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
