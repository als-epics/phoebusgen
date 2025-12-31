from .property_helpers import PropertyBase, dynamic_property
from .types import ButtonMode, Color, State, InterpolationType, ColorMap, ColorMode, Script, Action, Rule, ObservableList, Trace

@dynamic_property("rules", ObservableList[Rule])
class HasRules(PropertyBase):
    ...


@dynamic_property("scripts", ObservableList[Script])
class HasScripts(PropertyBase):
    ...

@dynamic_property("actions", ObservableList[Action], list_item_name="action")
class HasActions(PropertyBase):
    ...

@dynamic_property("tooltip", str)
class HasToolTip(PropertyBase):
    ...


@dynamic_property("show_limits", bool)
class HasShowLimits(PropertyBase):
    ...

@dynamic_property("level_hihi", float)
class HasLevelHiHi(PropertyBase):
    ...

@dynamic_property("level_high", float)
class HasLevelHigh(PropertyBase):
    ...

@dynamic_property("level_low", float)
class HasLevelLow(PropertyBase):
    ...

@dynamic_property("level_lolo", float)
class HasLevelLoLo(PropertyBase):
    ...

@dynamic_property("show_hihi", bool)
class HasShowHiHi(PropertyBase):
    ...

@dynamic_property("show_high", bool)
class HasShowHigh(PropertyBase):
    ...

@dynamic_property("show_low", bool)
class HasShowLow(PropertyBase):
    ...

@dynamic_property("show_lolo", bool)
class HasShowLoLo(PropertyBase):
    ...

class HasLevelsAndShow(
    HasLevelHiHi,
    HasLevelHigh,
    HasLevelLow,
    HasLevelLoLo,
    HasShowHiHi,
    HasShowHigh,
    HasShowLow,
    HasShowLoLo,
):
    ...

@dynamic_property("enabled", bool)
class HasEnabled(PropertyBase):
    ...

@dynamic_property("show_confirm_dialog", bool)
class HasShowConfirmDialog(PropertyBase):
    ...

@dynamic_property("confirm_message", str)
class HasConfirmMessage(PropertyBase):
    ...

@dynamic_property("password", str)
class HasPassword(PropertyBase):
    ...

class HasConfirmation(HasShowConfirmDialog, HasConfirmMessage, HasPassword):
    ...

@dynamic_property("mode", ButtonMode)
class HasButtonMode(PropertyBase):
    ...

@dynamic_property("minimum", float)
class HasMin(PropertyBase):
    ...

@dynamic_property("maximum", float)
class HasMax(PropertyBase):
    ...

class HasMinMax(HasMin, HasMax):
    ...

@dynamic_property("bar_length", float)
class HasBarLength(PropertyBase):
    ...

@dynamic_property("increment", float)
class HasIncrement(PropertyBase):
    ...

@dynamic_property("wrap_words", bool)
class HasWrapWords(PropertyBase):
    ...

@dynamic_property("limits_from_pv", bool)
class HasLimitsFromPV(PropertyBase):
    ...

@dynamic_property("editable", bool)
class HasEditable(PropertyBase):
    ...

@dynamic_property("fallback_symbol", str)
class HasFallbackSymbol(PropertyBase):
    ...

@dynamic_property("preserve_ratio", bool)
class HasPreserveRatio(PropertyBase):
    ...

@dynamic_property("run_actions_on_mouse_click", bool)
class HasRunActionsOnMouseClick(PropertyBase):
    ...

@dynamic_property("array_index", int)
class HasArrayIndex(PropertyBase):
    ...

@dynamic_property("symbols", ObservableList[str])
class HasSymbols(PropertyBase):
    ...

@dynamic_property("fallback_label", str)
class HasFallbackLabel(PropertyBase):
    ...

@dynamic_property("fallback_color", Color)
class HasFallbackColor(PropertyBase):
    ...

class HasFallback(HasFallbackLabel, HasFallbackColor):
    ...

@dynamic_property("states", ObservableList[State])
class HasStates(PropertyBase):
    ...

@dynamic_property("log_scale", bool)
class HasLogScale(PropertyBase):
    ...

@dynamic_property("selection_value_pv", str)
class HasSelectionValuePV(PropertyBase):
    ...


@dynamic_property("data_width", int)
class HasDataWidth(PropertyBase):
    ...

@dynamic_property("data_height", int)
class HasDataHeight(PropertyBase):
    ...

@dynamic_property("interpolation", InterpolationType)
class HasInterpolation(PropertyBase):
    ...

@dynamic_property("color_mode", ColorMode)
class HasColorMode(PropertyBase):
    ...

@dynamic_property("color_map", ColorMap)
class HasColorMap(PropertyBase):
    ...

@dynamic_property("items", ObservableList[str])
class HasItems(PropertyBase):
    ...

@dynamic_property("traces", ObservableList[Trace])
class HasTraces(PropertyBase):
    ...