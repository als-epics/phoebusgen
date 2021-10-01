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
        self.type = 'arc'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.Arc(self.name, self.x, self.y, self.width, self.height)

class TestEllipse(unittest.TestCase, ph.TestMacro, ph.TestLineWidth, ph.TestLineColor, ph.TestBackgroundColor,
                  ph.TestTransparent):
    def setUp(self):
        self.name = 'My_Ellipse'
        self.type = 'ellipse'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.Ellipse(self.name, self.x, self.y, self.width, self.height)

class TestRectangle(unittest.TestCase, ph.TestMacro, ph.TestLineWidth, ph.TestLineColor, ph.TestBackgroundColor,
                    ph.TestTransparent, ph.TestCorner):
    def setUp(self):
        self.name = 'My_Rectangle'
        self.type = 'rectangle'
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
        self.type = 'label'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.text = 'TEST Label'
        self.element = widgets.Label(self.name, self.text, self.x, self.y, self.width, self.height)

class TestPicture(unittest.TestCase, ph.TestMacro, ph.TestFile, ph.TestStretchToFit, ph.TestRotation):
    def setUp(self):
        self.name = 'Picture_1'
        self.type = 'picture'
        self.x = 123
        self.y = 12
        self.width = 10
        self.height = 12
        self.file = '/home/user/my-pic.png'
        self.element = widgets.Picture(self.name, self.file, self.x, self.y, self.width, self.height)

class TestPolygon(unittest.TestCase, ph.TestMacro, ph.TestLineWidth, ph.TestLineColor,
                  ph.TestBackgroundColor, ph.TestPoints):
    def setUp(self):
        self.name = 'polygon'
        self.type = 'polygon'
        self.x = 123
        self.y = 12
        self.width = 10
        self.height = 12
        self.element = widgets.Polygon(self.name, self.x, self.y, self.width, self.height)

class TestPolyline(unittest.TestCase, ph.TestMacro, ph.TestLineWidth, ph.TestLineColor,
                   ph.TestLineStyle, ph.TestPoints, ph.TestArrow):
    def setUp(self):
        self.name = 'polyline1'
        self.type = 'polyline'
        self.x = 123
        self.y = 12
        self.width = 10
        self.height = 12
        self.element = widgets.Polyline(self.name, self.x, self.y, self.width, self.height)

class TestByteMonitor(unittest.TestCase, ph.TestPVName, ph.TestStartBit, ph.TestNumBits, ph.TestReverseBits,
                      ph.TestHorizontal, ph.TestSquare, ph.TestOffColor, ph.TestOnColor, ph.TestForegroundColor,
                      ph.TestFont, ph.TestLabels, ph.TestAlarmBorder):
    def setUp(self):
        self.name = 'bytemonitorname'
        self.pv_name = 'TEST:PV:ENTRY'
        self.type = 'byte_monitor'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.ByteMonitor(self.name, self.pv_name, self.x, self.y, self.width, self.height)


class TestLED(unittest.TestCase, ph.TestPVName, ph.TestBit, ph.TestOn, ph.TestOff, ph.TestFont, ph.TestForegroundColor,
              ph.TestLineColor, ph.TestSquare, ph.TestLabelsFromPV, ph.TestAlarmBorder):
    def setUp(self):
        self.name = 'Label_1'
        self.pv_name = 'TEST:PV:ENTRY'
        self.type = 'led'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.LED(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestLEDMultiState(unittest.TestCase, ph.TestPVName, ph.TestFont, ph.TestForegroundColor, ph.TestLineColor,
                        ph.TestSquare, ph.TestAlarmBorder, ph.TestStates, ph.TestFallback):
    def setUp(self):
        self.name = 'Ledmulti'
        self.pv_name = 'PV:Multi'
        self.type = 'multi_state_led'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.LEDMultiState(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestMeter(unittest.TestCase, ph.TestPVName, ph.TestForegroundColor, ph.TestBackgroundColor, ph.TestFont,
                ph.TestFormat, ph.TestPrecision, ph.TestShowValue, ph.TestShowUnits, ph.TestAlarmBorder, ph.TestShowLimits,
                ph.TestLimitsFromPV, ph.TestMinMax, ph.TestNeedleColor, ph.TestKnobColor):
    def setUp(self):
        self.name = 'Cool meter'
        self.type = 'meter'
        self.x = 123
        self.y = 12
        self.width = 10
        self.height = 12
        self.pv_name = 'test:pv'
        self.element = widgets.Meter(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestProgressBar(unittest.TestCase, ph.TestPVName, ph.TestFillColor, ph.TestBackgroundColor,
                      ph.TestHorizontal, ph.TestAlarmBorder, ph.TestLimitsFromPV, ph.TestMinMax):
    def setUp(self):
        self.type = 'progressbar'
        self.name = 'Progress bar'
        self.x = 123
        self.y = 12
        self.width = 10
        self.height = 12
        self.pv_name = 'test:pv:forprogressbar'
        self.element = widgets.ProgressBar(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestSymbol(unittest.TestCase, ph.TestPVName, ph.TestRotation, ph.TestBackgroundColor, ph.TestArrayIndex,
                 ph.TestTransparent, ph.TestAlarmBorder, ph.TestAutoSize, ph.TestEnabled, ph.TestSymbols,
                 ph.TestInitialIndex, ph.TestShowIndex, ph.TestPreserveRatio):
    def setUp(self):
        self.type = 'symbol'
        self.name = 'SymbolWidget'
        self.x = 13
        self.y = 1422
        self.width = 2310
        self.height = 109
        self.pv_name = 'test:pv'
        self.element = widgets.Symbol(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestTable(unittest.TestCase, ph.TestPVName, ph.TestFont, ph.TestForegroundColor, ph.TestBackgroundColor,
                ph.TestShowToolbar, ph.TestAlarmBorder, ph.TestEditable, ph.TestSelectRows, ph.TestSelectionPV,
                ph.TestColumns):
    def setUp(self):
        self.type = 'table'
        self.name = 'TableName'
        self.pv_name = 'test:pv'
        self.x = 13
        self.y = 1422
        self.width = 2310
        self.height = 109
        self.element = widgets.Table(self.name, self.pv_name, self.x, self.y, self.width, self.height)


class TestTank(unittest.TestCase, ph.TestPVName, ph.TestFont, ph.TestForegroundColor, ph.TestBackgroundColor,
               ph.TestFillColor, ph.TestEmptyColor, ph.TestScaleVisible, ph.TestAlarmBorder, ph.TestLimitsFromPV):
    def setUp(self):
        self.name = 'my cool tank'
        self.type = 'tank'
        self.x = 24
        self.y = 12
        self.width = 2424
        self.height = 92
        self.pv_name = 'TANK'
        self.element = widgets.Tank(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestTextSymbol(unittest.TestCase, ph.TestPVName, ph.TestFont, ph.TestForegroundColor, ph.TestBackgroundColor,
                     ph.TestTransparent, ph.TestHorizontalAlignment, ph.TestVerticalAlignment, ph.TestRotation,
                     ph.TestWrapWords, ph.TestAlarmBorder, ph.TestEnabled, ph.TestArrayIndex, ph.TestSymbols):
    def setUp(self):
        self.name = 'text symbol widget'
        self.type = 'text-symbol'
        self.x = 24
        self.y = 12
        self.width = 24
        self.height = 92
        self.pv_name = 'symbol'
        self.element = widgets.TextSymbol(self.name, self.pv_name, self.x, self.y, self.width, self.height)


class TestTextUpdate(unittest.TestCase, ph.TestPVName, ph.TestFont, ph.TestForegroundColor,
                          ph.TestBackgroundColor, ph.TestTransparent, ph.TestFormat, ph.TestPrecision,
                          ph.TestShowUnits, ph.TestHorizontalAlignment, ph.TestVerticalAlignment,
                          ph.TestWrapWords, ph.TestRotationStep, ph.TestBorder):
    def setUp(self):
        self.pv_name = 'TEST:ME'
        self.name = 'Generic TextUpdate'
        self.type = 'textupdate'
        self.x = 500
        self.y = 300
        self.width = 100
        self.height = 20
        self.element = widgets.TextUpdate(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestThermometer(unittest.TestCase, ph.TestPVName, ph.TestFillColor, ph.TestAlarmBorder,
                      ph.TestLimitsFromPV, ph.TestMinMax):
    def setUp(self):
        self.name = 'testing thermometer'
        self.type = 'thermometer'
        self.x = 123
        self.y = 12
        self.width = 10
        self.height = 12
        self.pv_name = 'test:temp'
        self.element = widgets.Thermometer(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestActionButton(unittest.TestCase, ph.TestPVName, ph.TestText, ph.TestFont, ph.TestForegroundColor, ph.TestBackgroundColor,
                       ph.TestTransparent, ph.TestRotationStep, ph.TestEnabled, ph.TestConfirmation, ph.TestActions):
    def setUp(self):
        self.name = 'Label_1'
        self.type = 'action_button'
        self.pv_name = 'TEST:PV:ENTRY'
        self.text = 'TEST TTEST TEST'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.ActionButton(self.name, self.text, self.pv_name, self.x, self.y, self.width, self.height)

class TestBooleanButton(unittest.TestCase, ph.TestOffImage, ph.TestPVName, ph.TestBit, ph.TestShowLED, ph.TestFont,
                        ph.TestForegroundColor, ph.TestBackgroundColor, ph.TestLabelsFromPV, ph.TestAlarmBorder,
                        ph.TestEnabled, ph.TestMode, ph.TestConfirmation):
    def setUp(self):
        self.name = 'boolean button'
        self.type = 'bool_button'
        self.pv_name = 'tester_pv'
        self.x = 23
        self.y = 3245
        self.width = 1
        self.height = 2
        self.element = widgets.BooleanButton(self.name, self.pv_name, 23.2, 3245.9, 1.1, 2.8)

class TestCheckBox(unittest.TestCase, ph.TestPVName, ph.TestBit, ph.TestFont, ph.TestForegroundColor,
                   ph.TestAutoSize, ph.TestAlarmBorder, ph.TestConfirmation, ph.TestLabel):
    def setUp(self):
        self.name = 'Check box 1'
        self.pv_name = 'TEST:PV:BOOL'
        self.type = 'checkbox'
        self.label = 'My check box'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.CheckBox(self.name, self.label, self.pv_name, self.x, self.y, self.width, self.height)

class TestChoiceButton(unittest.TestCase, ph.TestPVName, ph.TestFont, ph.TestForegroundColor, ph.TestBackgroundColor,
                    ph.TestSelectedColor, ph.TestHorizontal, ph.TestAlarmBorder, ph.TestItems, ph.TestItemsFromPV,
                    ph.TestConfirmation):
    def setUp(self):
        self.name = 'choice box'
        self.pv_name = 'TEST:PV:BOOL'
        self.type = 'choice'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.ChoiceButton(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestComboBox(unittest.TestCase, ph.TestPVName, ph.TestFont, ph.TestForegroundColor, ph.TestBackgroundColor,
                   ph.TestItems, ph.TestAlarmBorder, ph.TestItemsFromPV, ph.TestEditable, ph.TestEnabled, ph.TestConfirmation):
    def setUp(self):
        self.name = '1'
        self.pv_name = 'TEST:PV:BOOL'
        self.type = 'combo'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.ComboBox(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestFileSelector(unittest.TestCase, ph.TestPVName, ph.TestFileComponent, ph.TestAlarmBorder, ph.TestEnabled):
    def setUp(self):
        self.name = 'My file selector'
        self.pv_name = 'TEST:PV:BOOL'
        self.type = 'fileselector'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.FileSelector(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestRadioButton(unittest.TestCase, ph.TestPVName, ph.TestFont, ph.TestForegroundColor, ph.TestHorizontal,
                      ph.TestAlarmBorder, ph.TestItemsFromPV, ph.TestItems, ph.TestEnabled, ph.TestConfirmation):
    def setUp(self):
        self.name = 'Radio_1'
        self.pv_name = 'TEST:PV:BOOL'
        self.type = 'radio'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.RadioButton(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestScaledSlider(unittest.TestCase, ph.TestPVName, ph.TestHorizontal, ph.TestForegroundColor, ph.TestBackgroundColor,
                       ph.TestTransparent, ph.TestFont, ph.TestAlarmBorder, ph.TestIncrement, ph.TestMinMax,
                       ph.TestLimitsFromPV, ph.TestEnabled, ph.TestShowScale, ph.TestShowMinorTicks,
                       ph.TestMajorTicksPixelDist, ph.TestScaleFormat, ph.TestLevelsAndShow):
    def setUp(self):
        self.name = 'Radio_1'
        self.pv_name = 'TEST:PV:BOOL'
        self.type = 'scaledslider'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.ScaledSlider(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestScrollbar(unittest.TestCase, ph.TestPVName, ph.TestHorizontal, ph.TestShowValueTip, ph.TestAlarmBorder,
                    ph.TestMinMax, ph.TestLimitsFromPV, ph.TestBarLength, ph.TestIncrement, ph.TestEnabled):
    def setUp(self):
        self.name = 'Radio_1'
        self.pv_name = 'TEST:PV:BOOL'
        self.type = 'scrollbar'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.Scrollbar(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestSlideButton(unittest.TestCase, ph.TestPVName, ph.TestBit, ph.TestLabel, ph.TestFont, ph.TestForegroundColor,
                      ph.TestAutoSize, ph.TestAlarmBorder, ph.TestEnabled, ph.TestConfirmation, ph.TestOffColor,
                      ph.TestOnColor):
    def setUp(self):
        self.name = 'slider button'
        self.pv_name = 'TEST:PV'
        self.type = 'slide_button'
        self.label = 'this is a slide button'
        self.x = 24
        self.y = 234
        self.width = 12
        self.height = 24
        self.element = widgets.SlideButton(self.name, self.label, self.pv_name, self.x, self.y, self.width, self.height)

class TestSpinner(unittest.TestCase, ph.TestPVName, ph.TestFormat, ph.TestPrecision, ph.TestShowUnits, ph.TestForegroundColor,
                   ph.TestBackgroundColor, ph.TestButtonsOnLeft, ph.TestAlarmBorder, ph.TestMinMax, ph.TestLimitsFromPV,
                   ph.TestIncrement, ph.TestEnabled):
    def setUp(self):
        self.name = 'SpinnerWidget'
        self.pv_name = 'TESTpv'
        self.type = 'spinner'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.Spinner(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestTextEntry(unittest.TestCase, ph.TestPVName, ph.TestFont, ph.TestForegroundColor, ph.TestBackgroundColor,
                     ph.TestFormat, ph.TestPrecision, ph.TestShowUnits, ph.TestWrapWords, ph.TestMultiLine,
                     ph.TestAlarmBorder, ph.TestEnabled, ph.TestBorder):
    def setUp(self):
        self.name = 'Label_1'
        self.pv_name = 'TEST:PV:ENTRY'
        self.type = 'textentry'
        self.x = 10
        self.y = 12
        self.width = 14
        self.height = 15
        self.element = widgets.TextEntry(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestDataBrowser(unittest.TestCase, ph.TestMacro, ph.TestFile, ph.TestShowToolbar, ph.TestSelectionValuePV):
    def setUp(self):
        self.name = 'my data browser'
        self.file = '/home/tynan/plots/my-cool-plot.plt'
        self.type = 'databrowser'
        self.x = 24
        self.y = 1224
        self.width = 1239
        self.height = 1
        self.element = widgets.DataBrowser(self.name, self.file, self.x, self.y, self.width, self.height)

class TestImage(unittest.TestCase, ph.TestPVName, ph.TestForegroundColor, ph.TestBackgroundColor,
                ph.TestShowToolbar, ph.TestAlarmBorder, ph.TestMinMax, ph.TestAutoScale, ph.TestDataHeightAndWidth,
                ph.TestLogScale, ph.TestUnsignedData):
    def setUp(self):
        self.name = 'my data browser'
        self.pv_name = "Image:PV"
        self.type = 'image'
        self.x = 24
        self.y = 1224
        self.width = 1239
        self.height = 1
        self.element = widgets.Image(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestStripChart(unittest.TestCase, ph.TestForegroundColor, ph.TestBackgroundColor,
                ph.TestShowToolbar, ph.TestTitle, ph.TestShowLegend, ph.TestShowGrid):
    def setUp(self):
        self.name = 'strippers'
        self.type = 'stripchart'
        self.x = 24
        self.y = 1224
        self.width = 1239
        self.height = 1
        self.element = widgets.StripChart(self.name, self.x, self.y, self.width, self.height)

class TestXYPlot(unittest.TestCase, ph.TestForegroundColor, ph.TestBackgroundColor,
                ph.TestShowToolbar, ph.TestTitle):
    def setUp(self):
        self.name = 'xyxyxyxyx'
        self.type = 'xyplot'
        self.x = 24
        self.y = 1224
        self.width = 1239
        self.height = 1
        self.element = widgets.XYPlot(self.name, self.x, self.y, self.width, self.height)

class TestArray(unittest.TestCase, ph.TestPVName, ph.TestMacro, ph.TestForegroundColor, ph.TestBackgroundColor,
                ph.TestAlarmBorder):
    def setUp(self):
        self.name = 'test array'
        self.type = 'array'
        self.x = 124
        self.y = 1
        self.width = 129
        self.height = 20
        self.pv_name = 'MY:ARRAY:PV'
        self.element = widgets.Array(self.name, self.pv_name, self.x, self.y, self.width, self.height)

class TestEmbeddedDisplay(unittest.TestCase, ph.TestMacro, ph.TestFile, ph.TestResizeBehavior,
                          ph.TestGroupName, ph.TestTransparent, ph.TestBorder):
    def setUp(self):
        self.name = 'EmbeddedDisplay'
        self.type = 'embedded'
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
        self.type = 'group'
        self.x = 123
        self.y = 12
        self.width = 10
        self.height = 12
        self.element = widgets.Group(self.name, self.x, self.y, self.width, self.height)

class TestNavigationTabs(unittest.TestCase, ph.TestNavTabs, ph.TestActiveTab, ph.TestTabWidth, ph.TestTabSpacing,
                         ph.TestTabHeight, ph.TestSelectedColor, ph.TestDeselectedColor, ph.TestDirection,
                         ph.TestFont):
    def setUp(self):
        self.name = 'Tab widget'
        self.type = 'navtabs'
        self.x = 123
        self.y = 12
        self.width = 10
        self.height = 12
        self.element = widgets.NavigationTabs(self.name, self.x, self.y, self.width, self.height)

class TestTabs(unittest.TestCase, ph.TestMacro, ph.TestTabs, ph.TestFont, ph.TestActiveTab,
               ph.TestTabHeight, ph.TestBackgroundColor, ph.TestDirection):
    def setUp(self):
        self.name = 'Tab widget'
        self.type = 'tabs'
        self.x = 123
        self.y = 12
        self.width = 10
        self.height = 12
        self.element = widgets.Tabs(self.name, self.x, self.y, self.width, self.height)


class TestThreeDViewer(unittest.TestCase, ph.TestFile):
    def setUp(self):
        self.name = 'cool 3d viewer'
        self.file = '/users/test/3dviewerfile'
        self.type = '3dviewer'
        self.x = 123
        self.y = 12
        self.width = 10
        self.height = 12
        self.element = widgets.ThreeDViewer(self.name, self.file, self.x, self.y, self.width, self.height)

class TestWebBrowser(unittest.TestCase, ph.TestUrl, ph.TestShowToolbar):
    def setUp(self):
        self.name = 'my web browser'
        self.url = 'https://tynanford.com'
        self.type = 'webbrowser'
        self.x = 123
        self.y = 12
        self.width = 10
        self.height = 12
        self.element = widgets.WebBrowser(self.name, self.url, self.x, self.y, self.width, self.height)


if __name__ == '__main__':
    unittest.main()
