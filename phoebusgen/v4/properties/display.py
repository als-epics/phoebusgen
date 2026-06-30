from pathlib import Path
from typing import Optional

from .property_helpers import PropertyBase
from .types import (
    ArrowTypes,
    Color,
    ColorBar,
    ColorMap,
    Column,
    Font,
    Format,
    GroupStyle,
    HorizontalAlignment,
    LinearMeterColors,
    LineStyle,
    ObservableList,
    Point,
    ResizeBehavior,
    RotationStep,
    TabDirection,
    VerticalAlignment,
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
    corner_width: int = 0
    corner_height: int = 0

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
    background_color: Color = Color((255, 255, 255))

class HasForegroundColor(PropertyBase):
    foreground_color: Color = Color((0, 0, 0))

class HasOnOffColors(PropertyBase):
    off_color: Color = Color((60, 100, 60))
    on_color: Color = Color((60, 255, 60))

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
    show_toolbar: bool = False

class HasLineWidth(PropertyBase):
    line_width: int = 3

class HasStretchToFit(PropertyBase):
    stretch_image: bool = False

class HasHorizontal(PropertyBase):
    horizontal: bool = True

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
    show_scale: bool = True

class HasShowMinorTicks(PropertyBase):
    show_minor_ticks: bool = True

class HasMajorTicksPixelDist(PropertyBase):
    major_ticks_pixel_dist: int = 40

class HasScaleFormat(PropertyBase):
    scale_format: str = '#.##'

class HasReverseBits(PropertyBase):
    reverse_bits: bool = False

class HasStartBit(PropertyBase):
    start_bit: int = 0

class HasNumBits(PropertyBase):
    num_bits: int = 8

class HasFillColor(PropertyBase):
    fill_color: Color = Color((60, 255, 60))

class HasShowValue(PropertyBase):
    show_value: bool = True

class HasInitialIndex(PropertyBase):
    initial_index: int

class HasShowIndex(PropertyBase):
    show_index: bool

class HasDisconnectOverlayColor(PropertyBase):
    disconnect_overlay_color: Color

class HasColumns(PropertyBase):
    columns: ObservableList[Column] = ObservableList([Column()])

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
    knob_size: float = 8
    needle_width: float = 1

class HasTabActiveHeightDirection(PropertyBase):
    tab_height: int = 30
    direction: TabDirection = TabDirection.HORIZONTAL
    active_tab: int = 1

class HasShowLimits(PropertyBase):
    show_limits: bool = True

class HasHighlightActiveRegion(PropertyBase):
    is_highlighting_of_active_regions_enabled: bool = True

class HasEnableGradient(PropertyBase):
    is_gradient_enabled: bool = False

class HasStatusColors(PropertyBase):
    normal_status_color: Color = Color((194, 198, 195))
    minor_warning_color: Color = Color((242, 148, 141))
    major_warning_color: Color = Color((240, 60, 46))
