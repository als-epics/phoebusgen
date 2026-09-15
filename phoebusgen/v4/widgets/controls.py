from pathlib import Path
from typing import Optional, Union

from phoebusgen.v4.properties.behavior import (
    HasAlarmBorder,
    HasBarLength,
    HasButtonMode,
    HasConfirmation,
    HasEditable,
    HasEnabled,
    HasIncrement,
    HasItems,
    HasWarningLevels,
    HasWarningLevelsVisibility,
    HasLimitsFromPV,
    HasMinMax,
    HasWrapWords,
)
from phoebusgen.v4.properties.display import (
    HasAutoSize,
    HasBackgroundColor,
    HasButtonsOnLeft,
    HasFont,
    HasForegroundColor,
    HasFormat,
    HasHorizontalAlignment,
    HasItemsFromPV,
    HasLabelsFromPV,
    HasMajorTicksPixelDist,
    HasMultiLine,
    HasOnOffColors,
    HasOnOffImages,
    HasPrecision,
    HasRotationStep,
    HasScaleFormat,
    HasSelectedColor,
    HasShowLED,
    HasShowMinorTicks,
    HasShowScale,
    HasShowUnits,
    HasShowValueTip,
    HasText,
    HasTransparent,
    HasVerticalAlignment,
)
from phoebusgen.v4.properties.misc import HasBorder
from phoebusgen.v4.properties.types import Color, ColorType, Format, HorizontalAlignment
from phoebusgen.v4.properties.widget import HasBit, HasFileComponent, HasLabel, HasPVName

from .widget import Widget, STANDARD_TOOLTIP

class ActionButton(Widget, HasPVName, HasText, HasFont, HasForegroundColor, HasBackgroundColor,
                   HasTransparent, HasHorizontalAlignment, HasVerticalAlignment, HasRotationStep,
                   HasEnabled, HasAlarmBorder, HasConfirmation):
    """ActionButton Phoebus Widget"""

    background_color: ColorType = Color((210, 210, 210))
    tooltip: str = '$(pv_name)\n$(actions)'
    text: str = '$(actions)'
    height: int = 30

    def __init__(self, name: str = '', text: str = '$(actions)', pv_name: str = '', x: int = 0, y: int = 0, width: int = 100, height: int = 30) -> None:
        """
        Create ActionButton Widget

        :param name: Widget name
        :param text: Button text
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name
        self.text = text

class BooleanButton(Widget, HasPVName, HasBit, HasOnOffImages, HasShowLED, HasFont, HasForegroundColor, HasBackgroundColor,
                    HasLabelsFromPV, HasAlarmBorder, HasEnabled, HasButtonMode, HasConfirmation, HasHorizontalAlignment, HasVerticalAlignment):
    """BooleanButton Phoebus Widget"""

    background_color: ColorType = Color((210, 210, 210))
    tooltip: str = STANDARD_TOOLTIP
    off_image: Optional[Union[Path, str]] = Path('.')
    on_image: Optional[Union[Path, str]] = Path('.')
    height: int = 30

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 100, height: int = 30) -> None:
        """
        Create BooleanButton Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class CheckBox(Widget, HasPVName, HasBit, HasLabel, HasFont, HasForegroundColor, HasAutoSize,
               HasAlarmBorder, HasConfirmation):
    """CheckBox Phoebus Widget"""

    tooltip: str = STANDARD_TOOLTIP

    def __init__(self, name: str = '', label: str = 'Label', pv_name: str = '', x: int = 0, y: int = 0, width: int = 100, height: int = 20) -> None:
        """
        Create CheckBox Widget

        :param name: Widget name
        :param label: Label text
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name
        self.label = label

class ChoiceButton(Widget, HasPVName, HasFont, HasForegroundColor, HasBackgroundColor, HasSelectedColor,
                   HasAlarmBorder, HasItems, HasItemsFromPV, HasConfirmation, HasHorizontalAlignment, HasVerticalAlignment):
    """ChoiceButton Phoebus Widget"""

    background_color: ColorType = Color((210, 210, 210))
    selected_color: Color = Color((200, 200, 200))
    tooltip: str = STANDARD_TOOLTIP
    height: int = 43

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 100, height: int = 43) -> None:
        """
        Create ChoiceButton Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class ComboBox(Widget, HasPVName, HasFont, HasForegroundColor, HasBackgroundColor, HasAlarmBorder, HasItems,
               HasItemsFromPV, HasEditable, HasEnabled, HasConfirmation):
    """ComboBox Phoebus Widget"""

    background_color: ColorType = Color((210, 210, 210))
    tooltip: str = STANDARD_TOOLTIP
    height: int = 30

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 100, height: int = 30) -> None:
        """
        Create ComboBox Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name


class FileSelector(Widget, HasPVName, HasFileComponent, HasAlarmBorder, HasEnabled):
    """FileSelector Phoebus Widget"""

    tooltip: str = STANDARD_TOOLTIP
    width: int = 40
    height: int = 25

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 40, height: int = 25) -> None:
        """
        Create FileSelector Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class RadioButton(Widget, HasPVName, HasFont, HasForegroundColor, HasHorizontalAlignment, HasAlarmBorder,
                  HasItems, HasItemsFromPV, HasEnabled, HasConfirmation):
    """RadioButton Phoebus Widget"""

    tooltip: str = STANDARD_TOOLTIP
    height: int = 60

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 100, height: int = 60) -> None:
        """
        Create RadioButton Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class ScaledSlider(Widget, HasPVName, HasHorizontalAlignment, HasForegroundColor, HasBackgroundColor, HasTransparent, HasFont,
                   HasShowScale, HasShowMinorTicks, HasMajorTicksPixelDist, HasScaleFormat, HasWarningLevels, HasWarningLevelsVisibility, HasAlarmBorder,
                   HasIncrement, HasMinMax, HasLimitsFromPV, HasEnabled):
    """ScaledSlider Phoebus Widget"""

    transparent: bool = True
    tooltip: str = STANDARD_TOOLTIP
    width: int = 400
    height: int = 55

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 400, height: int = 55) -> None:
        """
        Create ScaledSlider Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class Scrollbar(Widget, HasPVName, HasHorizontalAlignment, HasShowValueTip, HasAlarmBorder, HasMinMax,
                HasLimitsFromPV, HasBarLength, HasIncrement, HasEnabled):
    """Scrollbar Phoebus Widget"""

    tooltip: str = STANDARD_TOOLTIP

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 100, height: int = 20) -> None:
        """
        Create Scrollbar Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class SlideButton(Widget, HasPVName, HasBit, HasLabel, HasOnOffColors, HasFont, HasForegroundColor,
                  HasAutoSize, HasAlarmBorder, HasEnabled, HasConfirmation):
    """SlideButton Phoebus Widget"""

    off_color: ColorType = Color((210, 210, 210))
    on_color: ColorType = Color((0, 255, 0))
    tooltip: str = STANDARD_TOOLTIP
    height: int = 30

    def __init__(self, name: str = '', label: str = 'Label', pv_name: str = '', x: int = 0, y: int = 0, width: int = 100, height: int = 30) -> None:
        """
        Create SlideButton Widget

        :param name: Widget name
        :param label: Label text
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name
        self.label = label

class Spinner(Widget, HasPVName, HasFormat, HasPrecision, HasShowUnits, HasForegroundColor, HasBackgroundColor,
              HasButtonsOnLeft, HasAlarmBorder, HasMinMax, HasLimitsFromPV, HasIncrement, HasEnabled):
    """Spinner Phoebus Widget"""

    show_units: bool = False
    background_color: ColorType = Color((128, 255, 255))
    tooltip: str = STANDARD_TOOLTIP

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 100, height: int = 20) -> None:
        """
        Create Spinner Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class TextEntry(Widget, HasPVName, HasFont, HasForegroundColor, HasBackgroundColor, HasFormat,
                HasPrecision, HasShowUnits, HasWrapWords, HasMultiLine, HasAlarmBorder, HasEnabled,
                HasBorder, HasHorizontalAlignment, HasVerticalAlignment):
    """TextEntry Phoebus Widget"""

    background_color: ColorType = Color((128, 255, 255))
    format: Format = Format.DEFAULT
    horizontal_alignment: HorizontalAlignment = HorizontalAlignment.LEFT
    wrap_words: bool = False
    tooltip: str = STANDARD_TOOLTIP

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 100, height: int = 20) -> None:
        """
        Create TextEntry Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name


class Thumbwheel(Widget, HasPVName, HasFont, HasForegroundColor, HasBackgroundColor):
    """Thumbwheel Phoebus Widget"""

    height: int = 50

    def __init__(self, name: str = '', pv_name: str = '', x: int = 0, y: int = 0, width: int = 100, height: int = 50) -> None:
        """
        Create Thumbwheel Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name
