from pathlib import Path
from xml.etree.ElementTree import fromstring

from phoebusgen.v4.properties.types import (
    ArrowTypes,
    Color,
    LineStyle,
    Point,
)
from phoebusgen.v4.widgets import (
    Arc,
    Ellipse,
    Label,
    Picture,
    Polygon,
    Polyline,
    Rectangle,
)


def test_create_label_widget():
    label = Label(name='Test Label', text='Hello World', x=10, y=20, width=200, height=30)
    assert label is not None
    assert label.name == 'Test Label'
    assert label.text == 'Hello World'
    assert label.x == 10
    assert label.y == 20
    assert label.width == 200
    assert label.height == 30

    assert str(label) == """<?xml version="1.0" ?>
<widget type="label" version="2.0.0">
  <name>Test Label</name>
  <x>10</x>
  <y>20</y>
  <width>200</width>
  <height>30</height>
  <text>Hello World</text>
</widget>
"""


def test_label_widget_from_xml():
    label_xml = """<widget type="label" version="2.0.0">
  <name>My Label</name>
  <x>5</x>
  <y>15</y>
  <width>150</width>
  <height>25</height>
  <text>Some text</text>
</widget>"""
    label = Label.from_element(fromstring(label_xml))
    assert label is not None
    assert isinstance(label, Label)
    assert label.name == 'My Label'
    assert label.x == 5
    assert label.y == 15
    assert label.width == 150
    assert label.height == 25
    assert label.text == 'Some text'


def test_create_arc_widget():
    arc = Arc(name='Test Arc', x=0, y=0, width=100, height=100)
    assert arc is not None
    assert arc.name == 'Test Arc'
    assert arc.x == 0
    assert arc.y == 0
    assert arc.width == 100
    assert arc.height == 100

    # Set arc-specific properties
    arc.start_angle = 45.0
    arc.total_angle = 180.0
    arc.line_width = 3
    arc.line_color = Color((255, 0, 0))
    arc.line_style = LineStyle.DASHED

    assert arc.start_angle == 45.0
    assert arc.total_angle == 180.0
    assert arc.line_width == 3
    assert arc.line_color == Color((255, 0, 0))
    assert arc.line_style == LineStyle.DASHED

    assert str(arc) == """<?xml version="1.0" ?>
<widget type="arc" version="2.0.0">
  <name>Test Arc</name>
  <x>0</x>
  <y>0</y>
  <width>100</width>
  <height>100</height>
  <start_angle>45.0</start_angle>
  <total_angle>180.0</total_angle>
  <line_width>3</line_width>
  <line_color>
    <color red="255" green="0" blue="0" alpha="255"/>
  </line_color>
  <line_style>1</line_style>
</widget>
"""


def test_arc_widget_from_xml():
    arc_xml = """<widget type="arc" version="2.0.0">
  <name>Arc 1</name>
  <x>10</x>
  <y>20</y>
  <width>80</width>
  <height>80</height>
  <start_angle>30.0</start_angle>
  <total_angle>120.0</total_angle>
  <line_width>2</line_width>
</widget>"""
    arc = Arc.from_element(fromstring(arc_xml))
    assert arc is not None
    assert isinstance(arc, Arc)
    assert arc.name == 'Arc 1'
    assert arc.x == 10
    assert arc.y == 20
    assert arc.width == 80
    assert arc.height == 80
    assert arc.start_angle == 30.0
    assert arc.total_angle == 120.0
    assert arc.line_width == 2


def test_create_ellipse_widget():
    ellipse = Ellipse(name='Test Ellipse', x=5, y=10, width=150, height=100)
    assert ellipse is not None
    assert ellipse.name == 'Test Ellipse'
    assert ellipse.x == 5
    assert ellipse.y == 10
    assert ellipse.width == 150
    assert ellipse.height == 100

    ellipse.line_width = 2
    ellipse.line_color = Color((0, 128, 255))
    ellipse.background_color = Color((200, 200, 200))

    assert ellipse.line_width == 2
    assert ellipse.line_color == Color((0, 128, 255))
    assert ellipse.background_color == Color((200, 200, 200))

    assert str(ellipse) == """<?xml version="1.0" ?>
<widget type="ellipse" version="2.0.0">
  <name>Test Ellipse</name>
  <x>5</x>
  <y>10</y>
  <width>150</width>
  <height>100</height>
  <line_width>2</line_width>
  <line_color>
    <color red="0" green="128" blue="255" alpha="255"/>
  </line_color>
  <background_color>
    <color red="200" green="200" blue="200" alpha="255"/>
  </background_color>
</widget>
"""


def test_ellipse_widget_from_xml():
    ellipse_xml = """<widget type="ellipse" version="2.0.0">
  <name>Ellipse 1</name>
  <x>20</x>
  <y>30</y>
  <width>60</width>
  <height>40</height>
  <line_width>3</line_width>
</widget>"""
    ellipse = Ellipse.from_element(fromstring(ellipse_xml))
    assert ellipse is not None
    assert isinstance(ellipse, Ellipse)
    assert ellipse.name == 'Ellipse 1'
    assert ellipse.x == 20
    assert ellipse.y == 30
    assert ellipse.width == 60
    assert ellipse.height == 40
    assert ellipse.line_width == 3


def test_create_rectangle_widget():
    rect = Rectangle(name='Test Rect', x=10, y=10, width=200, height=100)
    assert rect.name == 'Test Rect'
    assert rect.x == 10
    assert rect.y == 10
    assert rect.width == 200
    assert rect.height == 100

    rect.line_width = 2
    rect.line_color = Color((0, 0, 0))
    rect.background_color = Color((255, 255, 0))
    rect.corner_width = 10
    rect.corner_height = 10

    assert rect.line_width == 2
    assert rect.line_color == Color((0, 0, 0))
    assert rect.background_color == Color((255, 255, 0))
    assert rect.corner_width == 10
    assert rect.corner_height == 10

    assert str(rect) == """<?xml version="1.0" ?>
<widget type="rectangle" version="2.0.0">
  <name>Test Rect</name>
  <x>10</x>
  <y>10</y>
  <width>200</width>
  <height>100</height>
  <line_width>2</line_width>
  <line_color>
    <color red="0" green="0" blue="0" alpha="255"/>
  </line_color>
  <background_color>
    <color red="255" green="255" blue="0" alpha="255"/>
  </background_color>
  <corner_width>10</corner_width>
  <corner_height>10</corner_height>
</widget>
"""


def test_rectangle_widget_from_xml():
    rect_xml = """<widget type="rectangle" version="2.0.0">
  <name>Rect 1</name>
  <x>5</x>
  <y>5</y>
  <width>300</width>
  <height>150</height>
  <corner_width>5</corner_width>
  <corner_height>5</corner_height>
</widget>"""
    rect = Rectangle.from_element(fromstring(rect_xml))
    assert rect is not None
    assert isinstance(rect, Rectangle)
    assert rect.name == 'Rect 1'
    assert rect.x == 5
    assert rect.y == 5
    assert rect.width == 300
    assert rect.height == 150
    assert rect.corner_width == 5
    assert rect.corner_height == 5


def test_create_polygon_widget():
    polygon = Polygon(name='Test Polygon', x=0, y=0, width=100, height=100)
    assert polygon is not None
    assert polygon.name == 'Test Polygon'

    polygon.line_width = 2
    polygon.line_color = Color((0, 0, 255))
    polygon.points.append(Point(x=0.0, y=0.0))
    polygon.points.append(Point(x=50.0, y=100.0))
    polygon.points.append(Point(x=100.0, y=0.0))

    assert polygon.line_width == 2
    assert polygon.line_color == Color((0, 0, 255))
    assert len(polygon.points) == 3
    assert polygon.points[0] == Point(x=0.0, y=0.0)
    assert polygon.points[1] == Point(x=50.0, y=100.0)
    assert polygon.points[2] == Point(x=100.0, y=0.0)

    assert str(polygon) == """<?xml version="1.0" ?>
<widget type="polygon" version="2.0.0">
  <name>Test Polygon</name>
  <x>0</x>
  <y>0</y>
  <width>100</width>
  <height>100</height>
  <line_width>2</line_width>
  <line_color>
    <color red="0" green="0" blue="255" alpha="255"/>
  </line_color>
  <points>
    <point x="0.0" y="0.0"/>
    <point x="50.0" y="100.0"/>
    <point x="100.0" y="0.0"/>
  </points>
</widget>
"""


def test_polygon_widget_from_xml():
    polygon_xml = """<widget type="polygon" version="2.0.0">
  <name>Polygon 1</name>
  <x>10</x>
  <y>10</y>
  <width>200</width>
  <height>200</height>
  <points>
    <point x="0.0" y="0.0"/>
    <point x="100.0" y="200.0"/>
    <point x="200.0" y="0.0"/>
  </points>
</widget>"""
    polygon = Polygon.from_element(fromstring(polygon_xml))
    assert polygon is not None
    assert isinstance(polygon, Polygon)
    assert polygon.name == 'Polygon 1'
    assert polygon.x == 10
    assert polygon.y == 10
    assert len(polygon.points) == 3
    assert polygon.points[0] == Point(x=0.0, y=0.0)
    assert polygon.points[1] == Point(x=100.0, y=200.0)
    assert polygon.points[2] == Point(x=200.0, y=0.0)


def test_create_polyline_widget():
    polyline = Polyline(name='Test Polyline', x=0, y=0, width=200, height=100)
    assert polyline is not None
    assert polyline.name == 'Test Polyline'

    polyline.line_width = 3
    polyline.line_color = Color((0, 255, 0))
    polyline.arrows = ArrowTypes.TO
    polyline.points.append(Point(x=0.0, y=50.0))
    polyline.points.append(Point(x=100.0, y=0.0))
    polyline.points.append(Point(x=200.0, y=50.0))

    assert polyline.line_width == 3
    assert polyline.line_color == Color((0, 255, 0))
    assert polyline.arrows == ArrowTypes.TO
    assert len(polyline.points) == 3

    assert str(polyline) == """<?xml version="1.0" ?>
<widget type="polyline" version="2.0.0">
  <name>Test Polyline</name>
  <x>0</x>
  <y>0</y>
  <width>200</width>
  <height>100</height>
  <line_width>3</line_width>
  <line_color>
    <color red="0" green="255" blue="0" alpha="255"/>
  </line_color>
  <arrows>To</arrows>
  <points>
    <point x="0.0" y="50.0"/>
    <point x="100.0" y="0.0"/>
    <point x="200.0" y="50.0"/>
  </points>
</widget>
"""


def test_polyline_widget_from_xml():
    polyline_xml = """<widget type="polyline" version="2.0.0">
  <name>Polyline 1</name>
  <x>5</x>
  <y>5</y>
  <width>100</width>
  <height>50</height>
  <arrows>Both</arrows>
  <points>
    <point x="0.0" y="0.0"/>
    <point x="100.0" y="50.0"/>
  </points>
</widget>"""
    polyline = Polyline.from_element(fromstring(polyline_xml))
    assert polyline is not None
    assert isinstance(polyline, Polyline)
    assert polyline.name == 'Polyline 1'
    assert polyline.x == 5
    assert polyline.y == 5
    assert polyline.arrows == ArrowTypes.BOTH
    assert len(polyline.points) == 2
    assert polyline.points[0] == Point(x=0.0, y=0.0)
    assert polyline.points[1] == Point(x=100.0, y=50.0)


def test_create_picture_widget():
    picture = Picture(name='Test Picture', file='/path/to/image.png', x=10, y=10, width=300, height=200)
    assert picture is not None
    assert picture.name == 'Test Picture'
    assert picture.file == Path('/path/to/image.png')
    assert picture.x == 10
    assert picture.y == 10
    assert picture.width == 300
    assert picture.height == 200

    picture.rotation = 90.0
    picture.stretch_to_fit = True

    assert picture.rotation == 90.0
    assert picture.stretch_to_fit == True

    assert str(picture) == """<?xml version="1.0" ?>
<widget type="picture" version="2.0.0">
  <name>Test Picture</name>
  <x>10</x>
  <y>10</y>
  <width>300</width>
  <height>200</height>
  <file>/path/to/image.png</file>
  <rotation>90.0</rotation>
  <stretch_to_fit>true</stretch_to_fit>
</widget>
"""


def test_picture_widget_from_xml():
    picture_xml = """<widget type="picture" version="2.0.0">
  <name>Picture 1</name>
  <x>0</x>
  <y>0</y>
  <width>400</width>
  <height>300</height>
  <file>my_image.png</file>
  <rotation>45.0</rotation>
</widget>"""
    picture = Picture.from_element(fromstring(picture_xml))
    assert picture is not None
    assert isinstance(picture, Picture)
    assert picture.name == 'Picture 1'
    assert picture.x == 0
    assert picture.y == 0
    assert picture.width == 400
    assert picture.height == 300
    assert picture.file == Path('my_image.png')
    assert picture.rotation == 45.0
