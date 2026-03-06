from .property_helpers import PropertyBase
from .types import Axis, ButtonMode, Color, State, InterpolationType, ColorMap, ColorMode, Script, Action, Rule, ObservableList, Trace


class HasActionsRulesAndScripts(PropertyBase):
    actions: ObservableList[Action]
    rules: ObservableList[Rule]
    scripts: ObservableList[Script]

class HasToolTip(PropertyBase):
    tooltip: str


class HasShowLimits(PropertyBase):
    show_limits: bool

class HasLevelsAndShow(PropertyBase):
    level_hihi: float
    level_high: float
    level_low: float
    level_lolo: float
    show_hihi: bool
    show_high: bool
    show_low: bool
    show_lolo: bool

class HasEnabled(PropertyBase):
    enabled: bool

class HasConfirmation(PropertyBase):
    show_confirm_dialog: bool
    confirm_message: str
    password: str

class HasButtonMode(PropertyBase):
    mode: ButtonMode

class HasMinMax(PropertyBase):
    minimum: float
    maximum: float

class HasBarLength(PropertyBase):
    bar_length: float

class HasIncrement(PropertyBase):
    increment: float

class HasWrapWords(PropertyBase):
    wrap_words: bool

class HasLimitsFromPV(PropertyBase):
    limits_from_pv: bool

class HasEditable(PropertyBase):
    editable: bool

class HasFallbackSymbol(PropertyBase):
    fallback_symbol: str

class HasPreserveRatio(PropertyBase):
    preserve_ratio: bool

class HasRunActionsOnMouseClick(PropertyBase):
    run_actions_on_mouse_click: bool

class HasArrayIndex(PropertyBase):
    array_index: int

class HasSymbols(PropertyBase):
    symbols: ObservableList[str]


class HasFallback(PropertyBase):
    fallback_label: str
    fallback_color: Color

class HasStates(PropertyBase):
    states: ObservableList[State]

class HasLogScale(PropertyBase):
    log_scale: bool

class HasSelectionValuePV(PropertyBase):
    selection_value_pv: str

class HasDataWidthAndHeight(PropertyBase):
    data_width: int
    data_height: int

class HasInterpolation(PropertyBase):
    interpolation: InterpolationType

class HasColorMode(PropertyBase):
    color_mode: ColorMode

class HasColorMap(PropertyBase):
    color_map: ColorMap

class HasItems(PropertyBase):
    items: ObservableList[str]

class HasTraces(PropertyBase):
    traces: ObservableList[Trace]

class HasXAxis(PropertyBase):
    x_axis: Axis

class HasYAxis(PropertyBase):
    y_axis: Axis

class HasYAxes(PropertyBase):
    y_axes: ObservableList[Axis]

class HasAutoScale(PropertyBase):
    auto_scale: bool

class HasUnisignedData(PropertyBase):
    unsigned_data: bool
