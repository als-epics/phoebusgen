
from phoebusgen.v4.properties.position import HasPosition
from phoebusgen.v4.utils import prettify_xml

def test_has_position(property_factory):
    pos = property_factory(HasPosition)
    pos.x = 10
    pos.y = 20
    pos.width = 300
    pos.height = 150

    assert pos.x == 10
    assert pos.y == 20
    assert pos.width == 300
    assert pos.height == 150

    pos_xml = prettify_xml(pos.root)
    assert pos_xml == """<?xml version="1.0" ?>
<widget>
  <x>10</x>
  <y>20</y>
  <width>300</width>
  <height>150</height>
</widget>
"""
