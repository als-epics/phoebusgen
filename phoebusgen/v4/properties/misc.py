from .property_helpers import PropertyBase
from .types import Color, ROI, ObservableList, Marker

class HasBorder(PropertyBase):
    border_width: int
    border_color: Color

class HasMarkers(PropertyBase):
    markers: ObservableList[Marker]

class HasGrid(PropertyBase):
    grid_visible: bool = True
    grid_color: Color = Color((128, 128, 128))
    grid_step_x: int = 10
    grid_step_y: int = 10


class HasKnobAndNeedleColor(PropertyBase):
    needle_color: Color
    knob_color: Color

class HasSelectionPV(PropertyBase):
    selection_pv: str

class HasSelectRows(PropertyBase):
    select_rows: bool

class HasCursor(PropertyBase):
    x_pv: str
    y_pv: str
    cursor_info_pv: str
    cursor_crosshair: bool

class HasROIs(PropertyBase):
    rois: ObservableList[ROI]
