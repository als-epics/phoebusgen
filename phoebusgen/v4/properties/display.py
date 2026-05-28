from pathlib import Path
from typing import Optional

from .property_helpers import PropertyBase

from .types import (
    ColorBar,
    ColorMap,
    Font,
    ArrowTypes,
    Format,
    HorizontalAlignment,
    LineStyle,
    Color,
    Column,
    ObservableList,
    ResizeBehavior,
    GroupStyle,
    RotationStep,
    Point,
    LinearMeterColors,
    TabDirection,
    VerticalAlignment
)

class HasVisible(PropertyBase):
    visible: bool = True

class HasFont(PropertyBase):
    font: Font

class HasArrows(PropertyBase):
    arrows: ArrowTypes = ArrowTypes.NONE
    arrow_length: int = 20

class HasLineStyle(PropertyBase):
    line_style: LineStyle = LineStyle.SOLID

class HasWrapWords(PropertyBase):
    wrap_words: bool = True

class HasAutoSize(PropertyBase):
    auto_size: bool = False

class HasPointSize(PropertyBase):
    point_size: int

class HasOnOffImages(PropertyBase):
    off_image: Optional[Path] = None
    on_image: Optional[Path] = None

class HasOnOffLabels(PropertyBase):
    on_label: str = ''
    off_label: str = ''

class HasSquare(PropertyBase):
    square: bool = False

class HasCorners(PropertyBase):
    corner_width: int
    corner_height: int

class HasMultiLine(PropertyBase):
    multi_line: bool

class HasAngle(PropertyBase):
    start_angle: float = 0.0
    total_angle: float = 90.0

class HasHorizontalAlignment(PropertyBase):
    horizontal_alignment: HorizontalAlignment = HorizontalAlignment.CENTER

class HasVerticalAlignment(PropertyBase):
    vertical_alignment: VerticalAlignment = VerticalAlignment.MIDDLE

class HasRotation(PropertyBase):
    rotation: float = 0.0

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
    text: str = ''

class HasTransparent(PropertyBase):
    transparent: bool = False

class HasFormat(PropertyBase):
    format: Format = Format.DECIMAL

class HasPrecision(PropertyBase):
    precision: int = -1

class HasShowUnits(PropertyBase):
    show_units: bool = True

class HasPVName(PropertyBase):
    pv_name: str = ''

class HasLabelsFromPV(PropertyBase):
    labels_from_pv: bool = False

class HasLabels(PropertyBase):
    labels: ObservableList[str]

class HasErrPV(PropertyBase):
    err_pv: str

class HasHeightPV(PropertyBase):
    height_pv: str

class HasItemsFromPV(PropertyBase):
    items_from_pv: bool

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

class HasColorMap(PropertyBase):
    color_map: ColorMap = ColorMap.VIRIDIS

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
    opacity: float = 1.0

class HasPoints(PropertyBase):
    points: ObservableList[Point]

class HasLinearMeterColors(PropertyBase):
    colors: LinearMeterColors

class HasKnobAndNeedleSize(PropertyBase):
    knob_size: float
    needle_width: float

class HasTabActiveHeightDirection(PropertyBase):
    tab_height: int = 30
    direction: TabDirection = TabDirection.HORIZONTAL
    active_tab: int = 1
