from .property_helpers import PropertyBase

from .types import ColorBar, Font, ArrowTypes, LineStyle, TabDirection, Color, Column,  Axis, ObservableList, ResizeBehavior, GroupStyle, RotationStep, Point, LinearMeterColors

class HasVisible(PropertyBase):
    visible: bool = True

class HasFont(PropertyBase):
    font: Font

class HasArrows(PropertyBase):
    arrows: ArrowTypes
    arrow_length: int

class HasLineStyle(PropertyBase):
    line_style: LineStyle

class HasWrapWords(PropertyBase):
    wrap_words: bool

class HasAutoSize(PropertyBase):
    auto_size: bool

class HasPointSize(PropertyBase):
    point_size: int

class HasOnOffImages(PropertyBase):
    off_image: str
    on_image: str

class HasOnOffLabels(PropertyBase):
    on_label: str
    off_label: str

class HasSquare(PropertyBase):
    square: bool

class HasCorners(PropertyBase):
    corner_width: int
    corner_height: int

class HasMultiLine(PropertyBase):
    multi_line: bool

class HasAngle(PropertyBase):
    start_angle: float
    total_angle: float

class HasHorizontalAlignment(PropertyBase):
    horizontal_alignment: str

class HasVerticalAlignment(PropertyBase):
    vertical_alignment: str

class HasRotation(PropertyBase):
    rotation: float

class HasRotationStep(PropertyBase):
    rotation_step: RotationStep

class HasLineColor(PropertyBase):
    line_color: Color

class HasBackgroundColor(PropertyBase):
    background_color: Color

class HasForegroundColor(PropertyBase):
    foreground_color: Color

class HasOnOffColors(PropertyBase):
    off_color: Color
    on_color: Color


class HasText(PropertyBase):
    text: str

class HasTransparent(PropertyBase):
    transparent: bool


class HasFormat(PropertyBase):
    format: str


class HasPrecision(PropertyBase):
    precision: int

class HasShowUnits(PropertyBase):
    show_units: bool

class HasPVName(PropertyBase):
    pv_name: str


class HasLabelsFromPV(PropertyBase):
    labels_from_pv: bool

class HasLabels(PropertyBase):
    labels: ObservableList[str]

class HasAlarmBorder(PropertyBase):
    border_alarm_sensitive: bool

class HasErrPV(PropertyBase):
    err_pv: str

class HasHeightPV(PropertyBase):
    height_pv: str

class HasItemsFromPV(PropertyBase):
    items_from_pv: bool

class HasLimitsFromPV(PropertyBase):
    limits_from_pv: bool

class HasSelectionValuePV(PropertyBase):
    selection_value_pv: str


class HasShowToolbar(PropertyBase):
    show_toolbar: bool

class HasLineWidth(PropertyBase):
    line_width: int

class HasStretchToFit(PropertyBase):
    stretch_to_fit: bool

class HasHorizontal(PropertyBase):
    horizontal: bool

class HasShowLED(PropertyBase):
    show_led: bool

class HasSelectedColor(PropertyBase):
    selected_color: Color

class HasDeselectedColor(PropertyBase):
    deselected_color: Color

class HasShowValueTip(PropertyBase):
    show_value_tip: bool

class HasButtonsOnLeft(PropertyBase):
    buttons_on_left: bool

class HasShowScale(PropertyBase):
    show_scale: bool

class HasShowMinorTicks(PropertyBase):
    show_minor_ticks: bool

class HasMajorTicksPixelDist(PropertyBase):
    major_ticks_pixel_dist: int

class HasScaleFormat(PropertyBase):
    scale_format: str

class HasReverseBits(PropertyBase):
    reverse_bits: bool

class HasStartBit(PropertyBase):
    start_bit: int

class HasNumBits(PropertyBase):
    num_bits: int

class HasFillColor(PropertyBase):
    fill_color: Color

class HasShowValue(PropertyBase):
    show_value: bool

class HasInitialIndex(PropertyBase):
    initial_index: int

class HasShowIndex(PropertyBase):
    show_index: bool

class HasDisconnectOverlayColor(PropertyBase):
    disconnect_overlay_color: Color

class HasColumns(PropertyBase):
    columns: ObservableList[Column]

class HasScaleVisible(PropertyBase):
    scale_visible: bool

class HasEmptyColor(PropertyBase):
    empty_color: Color

class HasGroupName(PropertyBase):
    group_name: str

class HasResizeBehavior(PropertyBase):
    resize_behavior: ResizeBehavior

class HasGroupStyle(PropertyBase):
    style: GroupStyle

class HasColorBar(PropertyBase):
    color_bar: ColorBar

class HasScaleFont(PropertyBase):
    scale_font: Font

class HasLabelFont(PropertyBase):
    label_font: Font

class HasTimeRange(PropertyBase):
    start: str
    end: str

class HasTitle(PropertyBase):
    title: str

class HasTitleFont(PropertyBase):
    title_font: Font

class HasShowGrid(PropertyBase):
    show_grid: bool

class HasShowLegend(PropertyBase):
    show_legend: bool

class HasGap(PropertyBase):
    gap: int

class HasWrapCount(PropertyBase):
    wrap_count: int

class HasOpacity(PropertyBase):
    opacity: float

class HasPoints(PropertyBase):
    points: ObservableList[Point]

class HasLinearMeterColors(PropertyBase):
    colors: LinearMeterColors

class HasKnobAndNeedleSize(PropertyBase):
    knob_size: float
    needle_width: float
