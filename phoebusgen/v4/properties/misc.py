from .property_helpers import PropertyBase
from .types import ROI, Color, Marker, ObservableList


class HasBorder(PropertyBase):
    border_width: int = 0
    border_color: Color = Color((0, 0, 0))

class HasMarkers(PropertyBase):
    markers: ObservableList[Marker]

class HasGrid(PropertyBase):
    grid_visible: bool = True
    grid_color: Color = Color((128, 128, 128))
    grid_step_x: int = 10
    grid_step_y: int = 10

class HasKnobAndNeedleColor(PropertyBase):
    needle_color: Color = Color((0, 0, 0))
    knob_color: Color = Color((0, 0, 0))

class HasSelectionPV(PropertyBase):
    selection_pv: str = ''

class HasSelectRows(PropertyBase):
    select_rows: bool = False

class HasCursor(PropertyBase):
    x_pv: str = ''
    y_pv: str = ''
    cursor_info_pv: str = ''
    cursor_crosshair: bool = False

class HasROIs(PropertyBase):
    rois: ObservableList[ROI]
