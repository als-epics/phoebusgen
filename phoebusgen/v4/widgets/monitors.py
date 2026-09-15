from phoebusgen.v4.properties.behavior import (
    HasAlarmBorder,
    HasArrayIndex,
    HasEditable,
    HasEnabled,
    HasFallback,
    HasInteractive,
    HasWarningLevels,
    HasLimitsFromPV,
    HasLogScale,
    HasMinMax,
    HasPreserveRatio,
    HasShowLimits,
    HasStates,
    HasWrapWords,
)
from phoebusgen.v4.properties.display import (
    HasAutoSize,
    HasBackgroundColor,
    HasColumns,
    HasEmptyColor,
    HasFillColor,
    HasFont,
    HasForegroundColor,
    HasFormat,
    HasHorizontal,
    HasHorizontalAlignment,
    HasInitialIndex,
    HasKnobAndNeedleSize,
    HasLabels,
    HasLabelsFromPV,
    HasLinearMeterColors,
    HasLineColor,
    HasNumBits,
    HasOnOffColors,
    HasOnOffLabels,
    HasPrecision,
    HasReverseBits,
    HasRotation,
    HasRotationStep,
    HasScaleVisible,
    HasShowIndex,
    HasShowToolbar,
    HasShowUnits,
    HasShowValue,
    HasSquare,
    HasStartBit,
    HasTransparent,
    HasVerticalAlignment,
)
from phoebusgen.v4.properties.misc import (
    HasBorder,
    HasKnobAndNeedleColor,
    HasSelectionPV,
    HasSelectRows,
)
from phoebusgen.v4.properties.types import Color, ColorType, Format, HorizontalAlignment, VerticalAlignment
from phoebusgen.v4.properties.widget import HasBit, HasPVName, HasSymbols

from .widget import Widget, STANDARD_TOOLTIP

OFF_COLOR = Color((60, 100, 60))
ON_COLOR = Color((60, 255, 60))

class ByteMonitor(Widget, HasPVName,HasStartBit, HasNumBits, HasReverseBits, HasHorizontal, HasSquare,
                  HasOnOffColors, HasForegroundColor, HasFont, HasLabels, HasAlarmBorder):
    """ByteMonitor Phoebus Widget"""

    tooltip: str = STANDARD_TOOLTIP
    width: int = 160

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 160, height: int = 20) -> None:
        """
        Create ByteMonitor Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

# Phoebus uses camelCase tag names for these ByteMonitor bit properties.
ByteMonitor._override_property_tag_name('start_bit', 'startBit')
ByteMonitor._override_property_tag_name('num_bits', 'numBits')
ByteMonitor._override_property_tag_name('reverse_bits', 'bitReverse')

class LED(Widget, HasPVName, HasBit, HasOnOffColors, HasOnOffLabels, HasFont, HasForegroundColor, HasLineColor,
          HasSquare, HasLabelsFromPV, HasAlarmBorder):
    """LED Phoebus Widget"""

    line_color: ColorType = Color((50, 50, 50, 178))
    bit: int = -1
    on_color: ColorType = Color((0, 255, 0))
    tooltip: str = STANDARD_TOOLTIP
    width: int = 20

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 20, height: int = 20) -> None:
        """
        Create LED Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class LEDMultiState(Widget, HasPVName, HasFont, HasForegroundColor, HasLineColor, HasSquare,
                    HasAlarmBorder, HasStates, HasFallback):
    """LEDMultiState Phoebus Widget"""

    line_color: ColorType = Color((50, 50, 50, 178))
    tooltip: str = STANDARD_TOOLTIP
    width: int = 20

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 20, height: int = 20) -> None:
        """
        Create LEDMultiState Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class LinearMeter(Widget, HasPVName, HasForegroundColor, HasBackgroundColor, HasFont, HasFormat,
            HasPrecision, HasShowValue, HasShowUnits, HasShowLimits, HasAlarmBorder, HasScaleVisible, HasHorizontal,
            HasLimitsFromPV, HasMinMax, HasKnobAndNeedleColor, HasKnobAndNeedleSize, HasLinearMeterColors, HasWarningLevels):
    """LinearMeter Phoebus Widget"""

    width: int = 240
    height: int = 120

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 240, height: int = 120) -> None:
        """
        Create LinearMeter Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class Meter(Widget, HasPVName, HasForegroundColor, HasBackgroundColor, HasFont, HasFormat,
            HasPrecision, HasShowValue, HasShowUnits, HasShowLimits, HasAlarmBorder,
            HasLimitsFromPV, HasMinMax, HasKnobAndNeedleColor):
    """Meter Phoebus Widget"""

    needle_color: ColorType = Color((255, 5, 7))
    knob_color: ColorType = Color((177, 166, 155))
    format: Format = Format.DEFAULT
    show_limits: bool = True
    tooltip: str = STANDARD_TOOLTIP
    width: int = 240
    height: int = 120

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 240, height: int = 120) -> None:
        """
        Create Meter Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class ProgressBar(Widget, HasPVName, HasFillColor, HasBackgroundColor, HasHorizontal,
                  HasAlarmBorder, HasLimitsFromPV, HasMinMax):
    """ ProgressBar Phoebus Widget """

    background_color: ColorType = Color((250, 250, 250))
    tooltip: str = STANDARD_TOOLTIP

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 100, height: int = 20) -> None:
        """
        Create ProgressBar Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class Symbol(Widget, HasPVName, HasSymbols, HasBackgroundColor, HasInitialIndex,
             HasRotation, HasShowIndex, HasTransparent, HasAlarmBorder, HasArrayIndex,
             HasAutoSize, HasEnabled, HasPreserveRatio):
    """ Symbol Phoebus Widget """

    transparent: bool = True
    tooltip: str = '$(pv_name)\n$(pv_value)\n$(actions)'
    height: int = 100

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 100, height: int = 100) -> None:
        """
        Create Symbol Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class Table(Widget, HasPVName, HasFont, HasForegroundColor, HasBackgroundColor, HasShowToolbar,
            HasAlarmBorder, HasEditable, HasSelectRows, HasSelectionPV, HasColumns):
    """ Table Phoebus Widget """

    editable: bool = True
    width: int = 500
    height: int = 300

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 500, height: int = 300) -> None:
        """
        Create Table Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class Tank(Widget, HasPVName, HasFont, HasForegroundColor, HasBackgroundColor,
           HasFillColor, HasEmptyColor, HasScaleVisible, HasAlarmBorder, HasLimitsFromPV,
           HasMinMax, HasLogScale, HasHorizontal):
    """ Tank Phoebus Widget """

    background_color: ColorType = Color((240, 240, 240))
    fill_color: ColorType = Color((0, 0, 255))
    empty_color: ColorType = Color((192, 192, 192))
    horizontal: bool = False
    tooltip: str = STANDARD_TOOLTIP
    width: int = 150
    height: int = 200

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 150, height: int = 200) -> None:
        """
        Create Tank Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height:
        """
        Widget.__init__(self, name,x, y, width, height)
        self.pv_name = pv_name

class TextSymbol(Widget, HasPVName, HasFont, HasForegroundColor, HasBackgroundColor, HasTransparent,
                 HasHorizontalAlignment, HasVerticalAlignment, HasRotation, HasWrapWords,
                 HasAlarmBorder, HasEnabled, HasArrayIndex, HasSymbols):
    """ TextSymbol Phoebus Widget """

    horizontal_alignment: HorizontalAlignment = HorizontalAlignment.CENTER
    vertical_alignment: VerticalAlignment = VerticalAlignment.MIDDLE
    transparent: bool = True
    tooltip: str = '$(pv_name)\n$(pv_value)\n$(symbol_value)'
    width: int = 32
    height: int = 32

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 32, height: int = 32) -> None:
        """
        Create TextSymbol Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self,  name, x, y, width, height)
        self.pv_name = pv_name

class TextUpdate(Widget, HasPVName, HasFont, HasForegroundColor, HasBackgroundColor, HasTransparent,
                 HasFormat, HasPrecision, HasShowUnits, HasHorizontalAlignment, HasVerticalAlignment, HasWrapWords,
                 HasRotationStep, HasBorder, HasAlarmBorder, HasInteractive):
    """TextUpdate Phoebus Widget"""

    background_color: ColorType = Color((240, 240, 240))
    format: Format = Format.DEFAULT
    horizontal_alignment: HorizontalAlignment = HorizontalAlignment.LEFT
    vertical_alignment: VerticalAlignment = VerticalAlignment.TOP
    tooltip: str = STANDARD_TOOLTIP

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 100, height: int = 20) -> None:
        """
        Create TextUpdate Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class Thermometer(Widget, HasPVName, HasFillColor, HasAlarmBorder, HasLimitsFromPV, HasMinMax):
    """Thermometer Phoebus Widget"""

    tooltip: str = STANDARD_TOOLTIP
    width: int = 40
    height: int = 160

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 40, height: int = 160) -> None:
        """
        Create Thermometer Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name
