from .property_helpers import PropertyBase, dynamic_property
from .types import Color, ROI, ObservableList, Marker

@dynamic_property("border_width", int)
class HasBorderWidth(PropertyBase):
    ...

@dynamic_property("border_color", Color)
class HasBorderColor(PropertyBase):
    ...

class HasBorder(HasBorderWidth, HasBorderColor):
    ...

@dynamic_property("markers", ObservableList[Marker])
class HasMarkers(PropertyBase):
    ...

@dynamic_property("grid_visible", bool)
class HasGridVisible(PropertyBase):
    ...

@dynamic_property("grid_color", Color)
class HasGridColor(PropertyBase):
    ...

@dynamic_property("grid_step_x", int)
class HasGridStepX(PropertyBase):
    ...

@dynamic_property("grid_step_y", int)
class HasGridStepY(PropertyBase):
    ...

@dynamic_property("needle_color", Color)
class HasNeedleColor(PropertyBase):
    ...

@dynamic_property("knob_color", Color)
class HasKnobColor(PropertyBase):
    ...

@dynamic_property("selection_pv", str)
class HasSelectionPV(PropertyBase):
    ...

@dynamic_property("select_rows", bool)
class HasSelectRows(PropertyBase):
    ...


@dynamic_property("cursor_crosshair", bool)
class HasCursorCrosshair(PropertyBase):
    ...

@dynamic_property("x_pv", str)
class HasCursorXPV(PropertyBase):
    ...

@dynamic_property("y_pv", str)
class HasCursorYPV(PropertyBase):
    ...

@dynamic_property("cursor_info_pv", str)
class HasCursorInfoPV(PropertyBase):
    ...

class HasCursor(
    HasCursorInfoPV,
    HasCursorXPV,
    HasCursorYPV,
    HasCursorCrosshair,
):
    ...

@dynamic_property("rois", ObservableList[ROI])
class HasROIs(PropertyBase):
    ...
