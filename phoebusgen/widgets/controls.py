from .widget import Widget
from phoebusgen.properties import (
    HasName,
    HasActions,
    HasText,
    HasFont,
    HasForegroundColor,
    HasBackgroundColor,
    HasTransparent,
    HasHorizontalAlignment,
    HasVerticalAlignment,
    HasRotationStep,
    HasEnabled,
    HasAlarmBorder,
    HasConfirmation,
    HasBit,
    HasOffImage,
    HasOnImage,
    HasShowLED,
    HasLabelsFromPV,
    HasButtonMode,
    HasEnabled,
    HasLevelsAndShow,
    HasFileComponent,
    HasAutoSize,
    HasLabel,
    HasItemsFromPV,
    HasSelectedColor,
    HasItems,
    HasShowValueTip,
    HasMinMax,
    HasLimitsFromPV,
    HasBarLength,
    HasIncrement,
    HasOffColor,
    HasOnColor,
    HasMultiLine,
    HasFormat,
    HasPrecision,
    HasShowUnits,
    HasButtonsOnLeft,
    HasEditable,
    HasBorder,
    HasShowScale,
    HasShowMinorTicks,
    HasMajorTicksPixelDist,
    HasScaleFormat,
    HasWrapWords
)

class ActionButton(Widget, HasName, HasActions, HasText, HasFont, HasForegroundColor, HasBackgroundColor,
                   HasTransparent, HasHorizontalAlignment, HasVerticalAlignment, HasRotationStep, HasEnabled, HasAlarmBorder, HasConfirmation):
    """ ActionButton Phoebus Widget """
    def __init__(self, name: str, text: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
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
        Widget.__init__(self, 'action_button', name, x, y, width, height)
        self.pv_name = pv_name
        self.text = text

class BooleanButton(Widget, HasName, HasBit, HasOffImage, HasOnImage, HasShowLED, HasFont, HasForegroundColor, HasBackgroundColor,
                    HasLabelsFromPV, HasAlarmBorder, HasEnabled, HasButtonMode, HasConfirmation, HasHorizontalAlignment, HasVerticalAlignment):
    """ BooleanButton Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create BooleanButton Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, 'bool_button', name, x, y, width, height)
        self.pv_name = pv_name

class CheckBox(Widget, HasName, HasBit, HasLabel, HasFont, HasForegroundColor, HasAutoSize,
               HasAlarmBorder, HasConfirmation):
    """ CheckBox Phoebus Widget """
    def __init__(self, name: str, label: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
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
        Widget.__init__(self, 'checkbox', name, x, y, width, height)
        self.pv_name = pv_name
        self.label = label

class ChoiceButton(Widget, HasName, HasFont, HasForegroundColor, HasBackgroundColor, HasSelectedColor,
                   HasAlarmBorder, HasItems, HasItemsFromPV, HasConfirmation, HasHorizontalAlignment, HasVerticalAlignment):
    """ ChoiceButton Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create ChoiceButton Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, 'choice', name, x, y, width, height)
        self.pv_name = pv_name

class ComboBox(Widget, HasName, HasFont, HasForegroundColor, HasBackgroundColor, HasAlarmBorder, HasItems,
               HasItemsFromPV, HasEditable, HasEnabled, HasConfirmation):
    """ ComboBox Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create ComboBox Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, 'combo', name, x, y, width, height)
        self.pv_name = pv_name


class FileSelector(Widget, HasName, HasFileComponent, HasAlarmBorder, HasEnabled):
    """ FileSelector Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create FileSelector Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, 'fileselector', name, x, y, width, height)
        self.pv_name = pv_name

class RadioButton(Widget, HasName, HasFont, HasForegroundColor, HasHorizontalAlignment, HasAlarmBorder,
                  HasItems, HasItemsFromPV, HasEnabled, HasConfirmation):
    """ RadioButton Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create RadioButton Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, 'radio', name, x, y, width, height)
        self.pv_name = pv_name

class ScaledSlider(Widget, HasName, HasHorizontalAlignment, HasForegroundColor, HasBackgroundColor, HasTransparent, HasFont,
                   HasShowScale, HasShowMinorTicks, HasMajorTicksPixelDist, HasScaleFormat, HasLevelsAndShow, HasAlarmBorder,
                   HasIncrement, HasMinMax, HasLimitsFromPV, HasEnabled):
    """ ScaledSlider Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create ScaledSlider Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, 'scaledslider', name, x, y, width, height)
        self.pv_name = pv_name

class Scrollbar(Widget, HasName, HasHorizontalAlignment, HasShowValueTip, HasAlarmBorder, HasMinMax,
                HasLimitsFromPV, HasBarLength, HasIncrement, HasEnabled):
    """ Scrollbar Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Scrollbar Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, 'scrollbar', name, x, y, width, height)
        self.pv_name = pv_name

class SlideButton(Widget, HasName, HasBit, HasLabel, HasOffColor, HasOnColor, HasFont, HasForegroundColor,
                  HasAutoSize, HasAlarmBorder, HasEnabled, HasConfirmation):
    """ SlideButton Phoebus Widget """
    def __init__(self, name: str, label: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
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
        Widget.__init__(self, 'slide_button', name, x, y, width, height)
        self.pv_name = pv_name
        self.label(label)

class Spinner(Widget, HasName, HasFormat, HasPrecision, HasShowUnits, HasForegroundColor, HasBackgroundColor,
              HasButtonsOnLeft, HasAlarmBorder, HasMinMax, HasLimitsFromPV, HasIncrement, HasEnabled):
    """ Spinner Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create Spinner Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, 'spinner', name, x, y, width, height)
        self.pv_name = pv_name

class TextEntry(Widget, HasName, HasFont, HasForegroundColor, HasBackgroundColor, HasFormat,
                HasPrecision, HasShowUnits, HasWrapWords, HasMultiLine, HasAlarmBorder, HasEnabled,
                HasBorder, HasHorizontalAlignment, HasVerticalAlignment):
    """ TextEntry Phoebus Widget """
    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create TextEntry Widget

        :param name: Widget name
        :param pv_name: Widget PV
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, 'textentry', name, x, y, width, height)
        self.pv_name = pv_name
