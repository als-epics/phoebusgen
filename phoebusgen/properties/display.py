from .property_helpers import PropertyBase, dynamic_property

from .types import Font, FontStyle, ArrowTypes, LineStyle, TabDirection, Color, Column,  Axis, ObservableList

@dynamic_property('visible', bool)
class HasVisible(PropertyBase):
    ...


@dynamic_property("font", Font)
class HasFont(PropertyBase):
    ...


@dynamic_property('arrow_length', int)
class HasArrowLength(PropertyBase):
    ...

@dynamic_property('arrows', ArrowTypes)
class HasArrows(HasArrowLength):
    ...

@dynamic_property("line_style", LineStyle)
class HasLineStyle(PropertyBase):
    ...

@dynamic_property('wrap_words', bool)
class HasWrapWords(PropertyBase):
    ...

@dynamic_property("auto_size", bool)
class HasAutoSize(PropertyBase):
    ...



@dynamic_property("point_size", int)
class HasPointSize(PropertyBase):
    ...

@dynamic_property("on_image", str)
class HasOnImage(PropertyBase):
    ...

@dynamic_property("off_image", str)
class HasOffImage(PropertyBase):
    ...

@dynamic_property("on_label", str)
class HasOnLabel(PropertyBase):
    ...

@dynamic_property("off_label", str)
class HasOffLabel(PropertyBase):
    ...



@dynamic_property("square", bool)
class HasSquare(PropertyBase):
    ...


@dynamic_property("corner_width", int)
class HasCornerWidth(PropertyBase):
    ...

@dynamic_property("corner_height", int)
class HasCornerHeight(PropertyBase):
    ...

class HasCorner(HasCornerWidth, HasCornerHeight):
    ...


@dynamic_property("multi_line", bool)
class HasMultiLine(PropertyBase):
    ...

@dynamic_property("start_angle", float)
class HasStartAngle(PropertyBase):
    ...

@dynamic_property("total_angle", float)
class HasTotalAngle(PropertyBase):
    ...


class HasAngle(
    HasStartAngle,
    HasTotalAngle,
):
    ...

@dynamic_property("horizontal_alignment", str)
class HasHorizontalAlignment(PropertyBase):
    ...

@dynamic_property("vertical_alignment", str)
class HasVerticalAlignment(PropertyBase):
    ...


@dynamic_property("rotation", float)
class HasRotation(PropertyBase):
    ...


@dynamic_property("rotation_step", str)
class HasRotationStep(PropertyBase):
    ...

@dynamic_property("line_color", Color)
class HasLineColor(PropertyBase):
    ...

@dynamic_property("background_color", Color)
class HasBackgroundColor(PropertyBase):
    ...

@dynamic_property("foreground_color", Color)
class HasForegroundColor(PropertyBase):
    ...


@dynamic_property("on_color", Color)
class HasOnColor(PropertyBase):
    ...

@dynamic_property("off_color", Color)
class HasOffColor(PropertyBase):
    ...


@dynamic_property('text', str)
class HasText(PropertyBase):
    ...

@dynamic_property("transparent", bool)
class HasTransparent(PropertyBase):
    ...


@dynamic_property("format", str)
class HasFormat(PropertyBase):
    ...


@dynamic_property("precision", int)
class HasPrecision(PropertyBase):
    ...

@dynamic_property("show_units", bool)
class HasShowUnits(PropertyBase):
    ...

@dynamic_property("pv_name", str)
class HasPVName(PropertyBase):
    ...


@dynamic_property("labels_from_pv", bool)
class HasLabelsFromPV(PropertyBase):
    ...

@dynamic_property("labels", ObservableList[str])
class HasLabels(PropertyBase):
    ...

@dynamic_property("border_alarm_sensitive", bool)
class HasAlarmBorder(PropertyBase):
    ...

@dynamic_property("err_pv", str)
class HasErrPV(PropertyBase):
    ...

@dynamic_property("height_pv", str)
class HasHeightPV(PropertyBase):
    ...

@dynamic_property("items_from_pv", bool)
class HasItemsFromPV(PropertyBase):
    ...

@dynamic_property("limits_from_pv", bool)
class HasLimitsFromPV(PropertyBase):
    ...

@dynamic_property("selection_value_pv", str)
class HasSelectionValuePV(PropertyBase):
    ...


@dynamic_property("show_toolbar", bool)
class HasShowToolbar(PropertyBase):
    ...

@dynamic_property("line_width", int)
class HasLineWidth(PropertyBase):
    ...

@dynamic_property("stretch_to_fit", bool)
class HasStretchToFit(PropertyBase):
    ...

@dynamic_property("direction", TabDirection)
class HasTabDirection(PropertyBase):
    ...

@dynamic_property("tab_width", int)
class HasTabWidth(PropertyBase):
    ...

@dynamic_property("tab_height", int)
class HasTabHeight(PropertyBase):
    ...

@dynamic_property("tab_spacing", int)
class HasTabSpacing(PropertyBase):
    ...

@dynamic_property("active_tab", int)
class HasActiveTab(PropertyBase):
    ...

@dynamic_property("horizontal", bool)
class HasHorizontal(PropertyBase):
    ...

@dynamic_property("show_led", bool)
class HasShowLED(PropertyBase):
    ...

@dynamic_property("selected_color", Color)
class HasSelectedColor(PropertyBase):
    ...

@dynamic_property("deselected_color", Color)
class HasDeselectedColor(PropertyBase):
    ...

@dynamic_property("show_value_tip", bool)
class HasShowValueTip(PropertyBase):
    ...

@dynamic_property("buttons_on_left", bool)
class HasButtonsOnLeft(PropertyBase):
    ...

@dynamic_property("show_scale", bool)
class HasShowScale(PropertyBase):
    ...

@dynamic_property("show_minor_ticks", bool)
class HasShowMinorTicks(PropertyBase):
    ...

@dynamic_property("major_ticks_pixel_dist", int)
class HasMajorTicksPixelDist(PropertyBase):
    ...

@dynamic_property("scale_format", str)
class HasScaleFormat(PropertyBase):
    ...

@dynamic_property("reverse_bits", bool)
class HasReverseBits(PropertyBase):
    ...

@dynamic_property("start_bit", int)
class HasStartBit(PropertyBase):
    ...

@dynamic_property("num_bits", int)
class HasNumBits(PropertyBase):
    ...

@dynamic_property("fill_color", Color)
class HasFillColor(PropertyBase):
    ...

@dynamic_property("show_value", bool)
class HasShowValue(PropertyBase):
    ...

@dynamic_property("initial_index", int)
class HasInitialIndex(PropertyBase):
    ...

@dynamic_property("show_index", bool)
class HasShowIndex(PropertyBase):
    ...

@dynamic_property("disconnect_overlay_color", Color)
class HasDisconnectOverlayColor(PropertyBase):
    ...

@dynamic_property("columns", ObservableList[Column])
class HasColumns(PropertyBase):
    ...

@dynamic_property("scale_visible", bool)
class HasScaleVisible(PropertyBase):
    ...

@dynamic_property("empty_color", Color)
class HasEmptyColor(PropertyBase):
    ...

@dynamic_property("x_axis", Axis)
class HasXAxis(PropertyBase):
    ...

@dynamic_property("y_axis", Axis)
class HasYAxis(PropertyBase):
    ...

@dynamic_property("y_axes", ObservableList[Axis], list_item_name="y_axis")
class HasYAxes(PropertyBase):
    ...