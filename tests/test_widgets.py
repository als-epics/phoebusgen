import sys
sys.path.insert(1, '../phoebusgen/widget/')
sys.path.insert(1, './phoebusgen/widget/')
import unittest
import widgets
import property_helpers as ph


class TestArc(unittest.TestCase, ph.TestMacro, ph.TestAngle, ph.TestLineWidth, ph.TestLineColor,
              ph.TestBackgroundColor, ph.TestTransparent):
    def setUp(self):
        self.name = 'My_Arc'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.Arc(self.name, self.x, self.y, self.width, self.height)


class TestEllipse(unittest.TestCase, ph.TestMacro, ph.TestLineWidth, ph.TestLineColor, ph.TestBackgroundColor,
                  ph.TestTransparent):
    def setUp(self):
        self.name = 'My_Ellipse'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.Ellipse(self.name, self.x, self.y, self.width, self.height)


class TestRectangle(unittest.TestCase, ph.TestMacro, ph.TestLineWidth, ph.TestLineColor, ph.TestBackgroundColor,
                    ph.TestTransparent, ph.TestCorner):
    def setUp(self):
        self.name = 'My_Rectangle'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.Rectangle(self.name, self.x, self.y, self.width, self.height)


class TestLabel(unittest.TestCase, ph.TestMacro, ph.TestText, ph.TestForegroundColor, ph.TestBackgroundColor,
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


class TestPicture(unittest.TestCase, ph.TestMacro, ph.TestFile, ph.TestStretchToFit, ph.TestRotation):
    def setUp(self):
        self.name = 'Picture_1'
        self.x = 123
        self.y = 12
        self.width = 10
        self.height = 12
        self.file = '/home/user/my-pic.png'
        self.element = widgets.Picture(self.name, self.file, self.x, self.y, self.width, self.height)


class TestTextUpdate(unittest.TestCase, ph.TestPVName, ph.TestFont, ph.TestForegroundColor,
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




class TestTextEntry(unittest.TestCase, ph.TestPVName, ph.TestFont, ph.TestForegroundColor, ph.TestBackgroundColor,
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


class TestEmbeddedDisplay(unittest.TestCase, ph.TestMacro, ph.TestFile, ph.TestResizeBehavior,
                          ph.TestGroupName, ph.TestTransparent, ph.TestBorder):
    def setUp(self):
        self.name = 'EmbeddedDisplay'
        self.x = 123
        self.y = 12
        self.width = 10
        self.height = 12
        self.file = '/home/user/_my-embedded-file.bob'
        self.element = widgets.EmbeddedDisplay(self.name, self.file, self.x, self.y, self.width, self.height)


class TestGroup(unittest.TestCase, ph.TestMacro, ph.TestStyle, ph.TestForegroundColor,
                ph.TestBackgroundColor, ph.TestTransparent):
    def setUp(self):
        self.name = 'MyGroup Display'
        self.x = 123
        self.y = 12
        self.width = 10
        self.height = 12
        self.element = widgets.Group(self.name, self.x, self.y, self.width, self.height)


if __name__ == '__main__':
    unittest.main()
