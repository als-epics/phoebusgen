import pytest

from phoebusgen.properties import HasBorderWidth, HasBorderColor, HasMarkers, HasGridVisible, HasGridColor, HasGridStepX, HasGridStepY, HasGridColor, HasKnobColor, HasNeedleColor, HasROIs, Color, HasSelectionPV, HasSelectRows, HasCursor, Marker, ROI
from phoebusgen.utils import prettify_xml

@pytest.mark.parametrize("property_cls, property_name, value", [
    (HasBorderWidth, "border_width", 5),
    (HasGridVisible, "grid_visible", True),
    (HasGridStepX, "grid_step_x", 20),
    (HasGridStepY, "grid_step_y", 30),
    (HasSelectionPV, "selection_pv", "test:PV"),
    (HasSelectRows, "select_rows", False),
])
def test_misc_primitive_properties(validate_primitive_property, property_cls, property_name, value):
    validate_primitive_property(property_cls, property_name, value)


def test_cursor_properties(property_factory, check_xml_element):
    prop = property_factory(HasCursor)
    assert hasattr(prop, "cursor_crosshair")
    assert hasattr(prop, "x_pv")
    assert hasattr(prop, "y_pv")
    assert hasattr(prop, "cursor_info_pv")
    prop.cursor_crosshair = True
    prop.x_pv = "CURSOR:X:PV"
    prop.y_pv = "CURSOR:Y:PV"
    prop.cursor_info_pv = "CURSOR:INFO:PV"
    assert prop.cursor_crosshair is True
    assert prop.x_pv == "CURSOR:X:PV"
    assert prop.y_pv == "CURSOR:Y:PV"
    assert prop.cursor_info_pv == "CURSOR:INFO:PV"
    check_xml_element(prop.root, "cursor_crosshair", "true")
    check_xml_element(prop.root, "x_pv", "CURSOR:X:PV")
    check_xml_element(prop.root, "y_pv", "CURSOR:Y:PV")
    check_xml_element(prop.root, "cursor_info_pv", "CURSOR:INFO:PV")


@pytest.mark.parametrize("property_cls, property_name, value", [
    (HasBorderColor, "border_color", (255, 0, 0)),
    (HasBorderColor, "border_color", (0, 255, 0, 128)),
    (HasNeedleColor, "needle_color", Color((0, 0, 255))),
    (HasKnobColor, "knob_color", (255, 255, 0)),
])
def test_misc_color_properties(validate_color_property, property_cls, property_name, value):
    validate_color_property(property_cls, property_name, value)

def test_marker_property(property_factory, check_xml_element, check_color_xml):
    prop = property_factory(HasMarkers)
    assert hasattr(prop, "markers")
    assert prop.markers == []
    prop.markers = [Marker(pv_name="PV1", color=(0, 0, 255)), Marker(pv_name="PV2", color=(255, 0, 0), interactive=True)]
    assert len(prop.markers) == 2
    assert prop.markers[0].pv_name == "PV1"
    assert prop.markers[0].color == (0, 0, 255)
    assert prop.markers[0].interactive is False
    del prop.markers[0]
    assert len(prop.markers) == 1
    assert prop.markers[0].pv_name == "PV2"
    assert prop.markers[0].color == (255, 0, 0)
    assert prop.markers[0].interactive is True
    prop.markers.append(Marker(pv_name="PV3", color=(0, 255, 0)))
    assert len(prop.markers) == 2
    assert prop.markers[1].pv_name == "PV3"
    markers_elem = prop.root.find("markers")
    assert markers_elem is not None
    marker_elems = markers_elem.findall("marker")
    assert len(marker_elems) == 2
    print(prettify_xml(prop.root))
    # assert False
    check_xml_element(marker_elems[0], "pv_name", "PV2")
    check_xml_element(marker_elems[1], "pv_name", "PV3")
    color_elem_0 = marker_elems[0].find("color").find("color")
    check_color_xml(color_elem_0, (255, 0, 0))
    color_elem_1 = marker_elems[1].find("color").find("color")
    check_color_xml(color_elem_1, (0, 255, 0))

def test_roi_property(property_factory, check_xml_element, check_color_xml):
    prop = property_factory(HasROIs)
    assert hasattr(prop, "rois")
    assert prop.rois == []
    prop.rois = [ROI(name="ROI1"), ROI(name="ROI2", color=(200, 100, 50), interactive=True, visible=False, x_pv="X:PV", y_pv="Y:PV", width_pv="W:PV", height_pv="H:PV")]
    assert len(prop.rois) == 2
    assert prop.rois[0].name == "ROI1"
    assert prop.rois[0].color == (0,255,0)
    assert prop.rois[0].interactive is False
    del prop.rois[0]
    assert len(prop.rois) == 1
    assert prop.rois[0].name == "ROI2"
    assert prop.rois[0].color == (200, 100, 50)
    assert prop.rois[0].interactive is True
    assert prop.rois[0].visible is False
    assert prop.rois[0].x_pv == "X:PV"
    assert prop.rois[0].y_pv == "Y:PV"
    assert prop.rois[0].width_pv == "W:PV"
    assert prop.rois[0].height_pv == "H:PV"
    prop.rois.append(ROI(name="ROI3", color=Color((0, 255, 0))))
    assert len(prop.rois) == 2
    rois_elem = prop.root.find("rois")
    assert rois_elem is not None
    roi_elems = rois_elem.findall("roi")
    assert len(roi_elems) == 2
    check_xml_element(roi_elems[0], "name", "ROI2")
    color_elem = roi_elems[0].find("color").find("color")
    check_color_xml(color_elem, (200, 100, 50))