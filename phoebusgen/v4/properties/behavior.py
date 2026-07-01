from pathlib import Path
from typing import List, Optional, Union

from .property_helpers import PropertyBase
from .types import (
    Action,
    Axis,
    ButtonMode,
    Color,
    ColorMode,
    ColorType,
    InterpolationType,
    ObservableList,
    Rule,
    Script,
    State,
    Trace,
)


class HasActionsRulesAndScripts(PropertyBase):
    actions: List[Action]
    rules: List[Rule]
    scripts: List[Script]

class HasToolTip(PropertyBase):
    tooltip: str

class HasShowLimits(PropertyBase):
    show_limits: bool

class HasWarningLevels(PropertyBase):
    level_hihi: float = 20.0
    level_high: float = 80.0
    level_low: float = 10.0
    level_lolo: float = 90.0

class HasWarningLevelsVisibility(PropertyBase):
    show_hihi: bool = True
    show_high: bool = True
    show_low: bool = True
    show_lolo: bool = True

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
    increment: float = 1.0

class HasWrapWords(PropertyBase):
    wrap_words: bool = True

class HasLimitsFromPV(PropertyBase):
    limits_from_pv: bool = True

class HasEditable(PropertyBase):
    editable: bool

class HasFallbackSymbol(PropertyBase):
    fallback_symbol: Optional[Union[Path, str]] = None

class HasPreserveRatio(PropertyBase):
    preserve_ratio: bool = True

class HasRunActionsOnMouseClick(PropertyBase):
    run_actions_on_mouse_click: bool

class HasArrayIndex(PropertyBase):
    array_index: int


class HasFallback(PropertyBase):
    fallback_label: str = 'Err'
    fallback_color: ColorType = Color((255, 0, 255))

class HasStates(PropertyBase):
    states: List[State] = ObservableList([State(label='State 1', color=Color((60, 100, 60))), State(value=1, label='State 2', color=Color((60, 255, 60)))])

class HasLogScale(PropertyBase):
    log_scale: bool

class HasSelectionValuePV(PropertyBase):
    selection_value_pv: str

class HasDataWidthAndHeight(PropertyBase):
    data_width: int = 100
    data_height: int = 100

class HasInterpolation(PropertyBase):
    interpolation: InterpolationType = InterpolationType.AUTOMATIC

class HasColorMode(PropertyBase):
    color_mode: ColorMode = ColorMode.TYPE_MONO

class HasItems(PropertyBase):
    items: List[str]

class HasTraces(PropertyBase):
    traces: List[Trace]

class HasXAxis(PropertyBase):
    x_axis: Axis

class HasYAxis(PropertyBase):
    y_axis: Axis

class HasYAxes(PropertyBase):
    y_axes: List[Axis]

class HasAutoScale(PropertyBase):
    auto_scale: bool = True

class HasUnisignedData(PropertyBase):
    unsigned_data: bool = False

class HasAlarmBorder(PropertyBase):
    border_alarm_sensitive: bool = False

class HasInteractive(PropertyBase):
    interactive: bool =  True
