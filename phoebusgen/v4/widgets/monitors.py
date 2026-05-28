from phoebusgen.v4.properties.behavior import (
    HasAlarmBorder,
    HasArrayIndex,
    HasEditable,
    HasEnabled,
    HasFallback,
    HasInteractive,
    HasLevelsAndShow,
    HasLimitsFromPV,
    HasLogScale,
    HasMinMax,
    HasPreserveRatio,
    HasShowLimits,
    HasStates,
    HasSymbols,
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
    HasPVName,
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
from phoebusgen.v4.properties.widget import HasBit

from .widget import Widget


class ByteMonitor(Widget, HasPVName,HasStartBit, HasNumBits, HasReverseBits, HasHorizontal, HasSquare,
                  HasOnOffColors, HasForegroundColor, HasFont, HasLabels, HasAlarmBorder):
    """ByteMonitor Phoebus Widget"""

    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
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

class LED(Widget, HasPVName, HasBit, HasOnOffColors, HasOnOffLabels, HasFont, HasForegroundColor, HasLineColor,
          HasSquare, HasLabelsFromPV, HasAlarmBorder):
    """LED Phoebus Widget"""

    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
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

    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
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
            HasLimitsFromPV, HasMinMax, HasKnobAndNeedleColor, HasKnobAndNeedleSize, HasLinearMeterColors, HasLevelsAndShow):
    """LinearMeter Phoebus Widget"""

    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
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

    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
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

    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
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

    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
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

    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
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

    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
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

    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
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

    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
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

    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
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
