import sys
sys.path.insert(1, '../phoebusgen/widget/')
sys.path.insert(1, './phoebusgen/widget/')
import unittest
import widgets
import property_helpers as ph


class TestLabelClass(unittest.TestCase, ph.TestMacro, ph.TestText, ph.TestForegroundColor, ph.TestBackgroundColor,
                     ph.TestTransparent, ph.TestHorizontalAlignment, ph.TestVerticalAlignment, ph.TestRotationStep,
                     ph.TestAutoSize, ph.TestWrapWords, ph.TestBorder):
    def setUp(self):
        self.name = 'Label_1'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.text = 'TEST Label'
        self.element = widgets.Label(self.name, self.text, self.x, self.y, self.width, self.height)


if __name__ == '__main__':
    unittest.main()
