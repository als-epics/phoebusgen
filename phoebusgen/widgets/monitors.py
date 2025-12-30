from .widget import Widget
from phoebusgen.properties import (
    HasName,
    HasStartBit,
    HasNumBits,
    HasReverseBits,
    HasHorizontal,
    HasSquare,
    HasOffColor,
    HasOnColor,
    HasForegroundColor,
    HasFont,
    HasLabels,
    HasAlarmBorder,
    HasBit,
    HasOffLabel,
    HasOnLabel,
    HasLineColor,
    HasStates,
    HasFallbackSymbol,
    HasBackgroundColor,
    HasFormat,
    HasPrecision,
    HasShowValue,
    HasShowUnits,
    HasShowLimits,
    HasLimitsFromPV,
    HasMinMax,
    HasNeedleColor,
    HasKnobColor,
    HasFillColor,
    HasSymbols,
    HasInitialIndex,
    HasRotation,
    HasShowIndex,
    HasTransparent,
    HasArrayIndex,
    HasAutoSize,
    HasEnabled,
    HasPreserveRatio,
    HasShowToolbar,
    HasEditable,
    HasSelectRows,
    HasSelectionPV,
    HasColumns,
    HasScaleVisible,
    HasEmptyColor,
    HasHorizontalAlignment,
    HasVerticalAlignment,
    HasRotationStep,
    HasWrapWords,
    HasBorder,
    HasLabelsFromPV,
    HasLogScale
)

class ByteMonitor(Widget, HasName, HasStartBit, HasNumBits, HasReverseBits, HasHorizontal, HasSquare,
                  HasOffColor, HasOnColor, HasForegroundColor, HasFont, HasLabels, HasAlarmBorder):
    """ ByteMonitor Phoebus Widget """
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
        Widget.__init__(self, 'byte_monitor', name, x, y, width, height)
        self.pv_name = pv_name

class LED(Widget, HasName, HasBit, HasOffLabel, HasOnLabel, HasFont, HasForegroundColor, HasLineColor,
          HasSquare, HasLabelsFromPV, HasAlarmBorder):
    """ LED Phoebus Widget """
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
        Widget.__init__(self, 'led', name, x, y, width, height)
        self.pv_name = pv_name

class LEDMultiState(Widget, HasName, HasFont, HasForegroundColor, HasLineColor, HasSquare,
                    HasAlarmBorder, HasStates, HasFallbackSymbol):
    """ LEDMultiState Phoebus Widget """
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
        Widget.__init__(self, 'multi_state_led', name, x, y, width, height)
        self.pv_name = pv_name

class Meter(Widget, HasName, HasForegroundColor, HasBackgroundColor, HasFont, HasFormat,
            HasPrecision, HasShowValue, HasShowUnits, HasShowLimits, HasAlarmBorder,
            HasLimitsFromPV, HasMinMax, HasNeedleColor, HasKnobColor):
    """ Meter Phoebus Widget """
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
        Widget.__init__(self, 'meter', name, x, y, width, height)
        self.pv_name = pv_name

class ProgressBar(Widget, HasName, HasFillColor, HasBackgroundColor, HasHorizontal,
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
        Widget.__init__(self, 'progressbar', name, x, y, width, height)
        self.pv_name = pv_name

class Symbol(Widget, HasSymbols, HasBackgroundColor, HasInitialIndex,
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
        Widget.__init__(self, 'symbol', name, x, y, width, height)
        self.pv_name = pv_name

class Table(Widget, HasName, HasFont, HasForegroundColor, HasBackgroundColor, HasShowToolbar,
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
        Widget.__init__(self, 'table', name, x, y, width, height)
        self.pv_name = pv_name

class Tank(Widget, HasName, HasFont, HasForegroundColor, HasBackgroundColor,
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
        Widget.__init__(self, 'tank', name, x, y, width, height)
        self.pv_name = pv_name

class TextSymbol(Widget, HasName, HasFont, HasForegroundColor, HasBackgroundColor, HasTransparent,
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
        Widget.__init__(self, 'text-symbol', name, x, y, width, height)
        self.pv_name = pv_name

class TextUpdate(Widget, HasName, HasFont, HasForegroundColor, HasBackgroundColor, HasTransparent,
                 HasFormat, HasPrecision, HasShowUnits, HasHorizontalAlignment, HasVerticalAlignment, HasWrapWords,
                 HasRotationStep, HasBorder, HasAlarmBorder):
    """ TextUpdate Phoebus Widget """
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
        Widget.__init__(self, 'textupdate', name, x, y, width, height)
        self.pv_name = pv_name

class Thermometer(Widget, HasName, HasFillColor, HasAlarmBorder, HasLimitsFromPV, HasMinMax):
    """ Thermometer Phoebus Widget """
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
        Widget.__init__(self, 'thermometer', name, x, y, width, height)
        self.pv_name = pv_name