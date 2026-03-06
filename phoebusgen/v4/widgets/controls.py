from .widget import WidgetType, Widget
from phoebusgen.v4.properties import (
    HasText,
    HasFont,
    HasForegroundColor,
    HasBackgroundColor,
    HasTransparent,
    HasHorizontalAlignment,
    HasVerticalAlignment,
    HasRotationStep,
    HasAlarmBorder,
    HasConfirmation,
    HasBit,
    HasOnOffImages,
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
    HasOnOffColors,
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
    HasWrapWords,
    HasPVName,
)

class ActionButton(Widget, HasPVName, HasText, HasFont, HasForegroundColor, HasBackgroundColor,
                   HasTransparent, HasHorizontalAlignment, HasVerticalAlignment, HasRotationStep, HasEnabled, HasAlarmBorder, HasConfirmation):
    """ ActionButton Phoebus Widget """

    _widget_type: WidgetType | None = WidgetType.ACTION_BUTTON
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
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name
        self.text = text

class BooleanButton(Widget, HasPVName, HasBit, HasOnOffImages, HasShowLED, HasFont, HasForegroundColor, HasBackgroundColor,
                    HasLabelsFromPV, HasAlarmBorder, HasEnabled, HasButtonMode, HasConfirmation, HasHorizontalAlignment, HasVerticalAlignment):
    """ BooleanButton Phoebus Widget """

    _widget_type: WidgetType | None = WidgetType.BOOL_BUTTON

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
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class CheckBox(Widget, HasPVName, HasBit, HasLabel, HasFont, HasForegroundColor, HasAutoSize,
               HasAlarmBorder, HasConfirmation):
    """ CheckBox Phoebus Widget """

    _widget_type: WidgetType | None = WidgetType.CHECKBOX

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
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name
        self.label = label

class ChoiceButton(Widget, HasPVName, HasFont, HasForegroundColor, HasBackgroundColor, HasSelectedColor,
                   HasAlarmBorder, HasItems, HasItemsFromPV, HasConfirmation, HasHorizontalAlignment, HasVerticalAlignment):
    """ ChoiceButton Phoebus Widget """
    _widget_type: WidgetType | None = WidgetType.CHOICE
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
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class ComboBox(Widget, HasPVName, HasFont, HasForegroundColor, HasBackgroundColor, HasAlarmBorder, HasItems,
               HasItemsFromPV, HasEditable, HasEnabled, HasConfirmation):
    """ ComboBox Phoebus Widget """
    _widget_type: WidgetType | None = WidgetType.COMBO
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
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name


class FileSelector(Widget, HasPVName, HasFileComponent, HasAlarmBorder, HasEnabled):
    """ FileSelector Phoebus Widget """
    _widget_type: WidgetType | None = WidgetType.FILE_SELECTOR
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
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class RadioButton(Widget, HasPVName, HasFont, HasForegroundColor, HasHorizontalAlignment, HasAlarmBorder,
                  HasItems, HasItemsFromPV, HasEnabled, HasConfirmation):
    """ RadioButton Phoebus Widget """
    _widget_type: WidgetType | None = WidgetType.RADIO
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
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class ScaledSlider(Widget, HasPVName, HasHorizontalAlignment, HasForegroundColor, HasBackgroundColor, HasTransparent, HasFont,
                   HasShowScale, HasShowMinorTicks, HasMajorTicksPixelDist, HasScaleFormat, HasLevelsAndShow, HasAlarmBorder,
                   HasIncrement, HasMinMax, HasLimitsFromPV, HasEnabled):
    """ ScaledSlider Phoebus Widget """
    _widget_type: WidgetType | None = WidgetType.SCALED_SLIDER
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
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class Scrollbar(Widget, HasPVName, HasHorizontalAlignment, HasShowValueTip, HasAlarmBorder, HasMinMax,
                HasLimitsFromPV, HasBarLength, HasIncrement, HasEnabled):
    """ Scrollbar Phoebus Widget """
    _widget_type: WidgetType | None = WidgetType.SCROLLBAR
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
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class SlideButton(Widget, HasPVName, HasBit, HasLabel, HasOnOffColors, HasFont, HasForegroundColor,
                  HasAutoSize, HasAlarmBorder, HasEnabled, HasConfirmation):
    """ SlideButton Phoebus Widget """
    _widget_type: WidgetType | None = WidgetType.SLIDE_BUTTON
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
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name
        self.label = label

class Spinner(Widget, HasPVName, HasFormat, HasPrecision, HasShowUnits, HasForegroundColor, HasBackgroundColor,
              HasButtonsOnLeft, HasAlarmBorder, HasMinMax, HasLimitsFromPV, HasIncrement, HasEnabled):
    """ Spinner Phoebus Widget """
    _widget_type: WidgetType | None = WidgetType.SPINNER
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
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name

class TextEntry(Widget, HasPVName, HasFont, HasForegroundColor, HasBackgroundColor, HasFormat,
                HasPrecision, HasShowUnits, HasWrapWords, HasMultiLine, HasAlarmBorder, HasEnabled,
                HasBorder, HasHorizontalAlignment, HasVerticalAlignment):
    """ TextEntry Phoebus Widget """

    _widget_type: WidgetType | None = WidgetType.TEXT_ENTRY

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
        Widget.__init__(self, name, x, y, width, height)
        self.pv_name = pv_name


class Thumbwheel(Widget, HasPVName, HasFont, HasForegroundColor, HasBackgroundColor):
    """ Thumbwheel Phoebus Widget """

    _widget_type: WidgetType | None = WidgetType.THUMBWHEEL

    def __init__(self, name: str, pv_name: str, x: int, y: int, width: int, height: int) -> None:
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
