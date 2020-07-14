import sys
sys.path.insert(1, '../phoebusgen/widget/')
sys.path.insert(1, './phoebusgen/widget/')
import unittest
import widgets
import property_helpers as ph


class TestRectangle(unittest.TestCase, ph.TestMacro, ph.TestLineWidth, ph.TestLineColor, ph.TestBackgroundColor,
                    ph.TestTransparent, ph.TestCorner):
    def setUp(self):
        self.name = 'My_Rectangle'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.Rectangle(self.name, self.x, self.y, self.width, self.height)


class TestArc(unittest.TestCase, ph.TestMacro, ph.TestAngle, ph.TestLineWidth, ph.TestLineColor,
              ph.TestBackgroundColor, ph.TestTransparent):
    def setUp(self):
        self.name = 'My_Arc'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.Arc(self.name, self.x, self.y, self.width, self.height)


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




class TestTextEntryClass(unittest.TestCase, ph.TestPVName, ph.TestFont, ph.TestForegroundColor, ph.TestBackgroundColor,
                     ph.TestFormat, ph.TestPrecision, ph.TestShowUnits, ph.TestWrapWords, ph.TestMultiLine,
                     ph.TestAlarmBorder, ph.TestEnabled, ph.TestBorder):
    def setUp(self):
        self.name = 'Label_1'
        self.pv_name = 'TEST:PV:ENTRY'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.TextEntry(self.name, self.pv_name, self.x, self.y, self.width, self.height)


class TestActionButton(unittest.TestCase, ph.TestPVName, ph.TestText, ph.TestFont, ph.TestForegroundColor, ph.TestBackgroundColor,
                         ph.TestTransparent, ph.TestRotationStep, ph.TestEnabled, ph.TestConfirmation):
    def setUp(self):
        self.name = 'Label_1'
        self.pv_name = 'TEST:PV:ENTRY'
        self.text = 'TEST TTEST TEST'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.ActionButton(self.name, self.text, self.pv_name, self.x, self.y, self.width, self.height)


class TestLED(unittest.TestCase, ph.TestPVName, ph.TestBit, ph.TestOn, ph.TestOff, ph.TestFont, ph.TestForegroundColor,
                       ph.TestLineColor, ph.TestSquare, ph.TestLabelsFromPV, ph.TestAlarmBorder):
    def setUp(self):
        self.name = 'Label_1'
        self.pv_name = 'TEST:PV:ENTRY'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.LED(self.name, self.pv_name, self.x, self.y, self.width, self.height)




if __name__ == '__main__':
    unittest.main()
