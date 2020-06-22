import sys
sys.path.insert(1, '../phoebusgen/widget/')
sys.path.insert(1, './phoebusgen/widget/')
import unittest
import widgets
import property_helpers as ph


class TestTextUpdateClass(unittest.TestCase, ph.TestPVName, ph.TestFont, ph.TestForegroundColor,
                          ph.TestBackgroundColor, ph.TestTransparent, ph.TestFormat, ph.TestPrecision,
                          ph.TestShowUnits, ph.TestHorizontalAlignment, ph.TestVerticalAlignment,
                          ph.TestWrapWords, ph.TestRotationStep, ph.TestBorder):
    def setUp(self):
        self.pv_name = 'TEST:ME'
        self.name = 'Generic TextUpdate'
        self.x = 500
        self.y = 300
        self.width = 100
        self.height = 20
        self.element = widgets.TextUpdate(self.name, self.pv_name, self.x, self.y, self.width, self.height)


if __name__ == '__main__':
    unittest.main()
