from pathlib import Path
from xml.etree.ElementTree import fromstring

from phoebusgen.v4.properties.types import (
    Axis,
    Color,
    ColorMap,
    InterpolationType,
    Marker,
    Trace,
    TraceType,
)
from phoebusgen.v4.widgets.plots import (
    DataBrowser,
    Image,
    StripChart,
    XYPlot,
)


def test_create_data_browser_widget():
    db = DataBrowser(name='Test DB', file='data.plt', x=10, y=10, width=600, height=400)
    assert db is not None
    assert db.name == 'Test DB'
    assert db.file == Path('data.plt')
    assert db.x == 10
    assert db.y == 10
    assert db.width == 600
    assert db.height == 400

    assert str(db) == """<?xml version="1.0" ?>
<widget type="databrowser" version="2.0.0">
  <name>Test DB</name>
  <x>10</x>
  <y>10</y>
  <width>600</width>
  <height>400</height>
  <file>data.plt</file>
</widget>
"""


def test_data_browser_from_xml():
    db_xml = """<widget type="databrowser" version="2.0.0">
  <name>DB 1</name>
  <x>0</x>
  <y>0</y>
  <width>800</width>
  <height>500</height>
  <file>history.plt</file>
</widget>"""
    db = DataBrowser.from_element(fromstring(db_xml))
    assert db is not None
    assert isinstance(db, DataBrowser)
    assert db.name == 'DB 1'
    assert db.file == Path('history.plt')
    assert db.width == 800
    assert db.height == 500


def test_create_image_widget():
    img = Image(name='Test Image', pv_name='CAM:IMAGE', x=10, y=10, width=400, height=300)
    assert img is not None
    assert img.name == 'Test Image'
    assert img.pv_name == 'CAM:IMAGE'

    img.color_map = ColorMap.VIRIDIS
    img.show_toolbar = True
    img.data_width = 640
    img.data_height = 480
    img.interpolation = InterpolationType.INTERPOLATE
    img.log_scale = True
    img.unsigned_data = True
    img.auto_scale = True
    img.minimum = 0.0
    img.maximum = 4095.0

    assert img.color_map == ColorMap.VIRIDIS
    assert img.show_toolbar
    assert img.data_width == 640
    assert img.data_height == 480
    assert img.interpolation == InterpolationType.INTERPOLATE
    assert img.log_scale
    assert img.unsigned_data
    assert img.auto_scale
    assert img.minimum == 0.0
    assert img.maximum == 4095.0

    assert str(img) == """<?xml version="1.0" ?>
<widget type="image" version="2.0.0">
  <name>Test Image</name>
  <x>10</x>
  <y>10</y>
  <width>400</width>
  <height>300</height>
  <pv_name>CAM:IMAGE</pv_name>
  <color_map>VIRIDIS</color_map>
  <show_toolbar>true</show_toolbar>
  <data_width>640</data_width>
  <data_height>480</data_height>
  <interpolation>1</interpolation>
  <log_scale>true</log_scale>
  <unsigned_data>true</unsigned_data>
  <auto_scale>true</auto_scale>
  <minimum>0.0</minimum>
  <maximum>4095.0</maximum>
</widget>
"""


def test_image_from_xml():
    img_xml = """<widget type="image" version="2.0.0">
  <name>Image 1</name>
  <x>0</x>
  <y>0</y>
  <width>640</width>
  <height>480</height>
  <pv_name>DET:DATA</pv_name>
  <data_width>1024</data_width>
  <data_height>768</data_height>
  <color_map>JET</color_map>
  <interpolation>2</interpolation>
  <unsigned_data>true</unsigned_data>
  <auto_scale>true</auto_scale>
  <minimum>10.0</minimum>
  <maximum>1000.0</maximum>
</widget>"""
    img = Image.from_element(fromstring(img_xml))
    assert img is not None
    assert isinstance(img, Image)
    assert img.name == 'Image 1'
    assert img.pv_name == 'DET:DATA'
    assert img.data_width == 1024
    assert img.data_height == 768
    assert img.color_map == ColorMap.JET
    assert img.interpolation == InterpolationType.AUTOMATIC
    assert img.unsigned_data
    assert img.auto_scale
    assert img.minimum == 10.0
    assert img.maximum == 1000.0


def test_create_strip_chart_widget():
    sc = StripChart(name='Test SC', x=10, y=10, width=500, height=300)
    assert sc is not None
    assert sc.name == 'Test SC'
    assert sc.x == 10
    assert sc.y == 10
    assert sc.width == 500
    assert sc.height == 300

    sc.title = 'Temperature History'
    sc.show_toolbar = True
    sc.show_legend = True
    sc.show_grid = True

    assert sc.title == 'Temperature History'
    assert sc.show_toolbar
    assert sc.show_legend
    assert sc.show_grid

    sc.traces.append(Trace(name='Trace 1', y_pv='TEMP:PV1'))
    sc.traces.append(Trace(name='Trace 2', y_pv='TEMP:PV2', color=Color((255, 0, 0))))

    assert len(sc.traces) == 2
    assert sc.traces[0].name == 'Trace 1'
    assert sc.traces[0].y_pv == 'TEMP:PV1'
    assert sc.traces[1].name == 'Trace 2'
    assert sc.traces[1].y_pv == 'TEMP:PV2'

    assert str(sc) == """<?xml version="1.0" ?>
<widget type="stripchart" version="2.1.0">
  <name>Test SC</name>
  <x>10</x>
  <y>10</y>
  <width>500</width>
  <height>300</height>
  <title>Temperature History</title>
  <show_toolbar>true</show_toolbar>
  <show_legend>true</show_legend>
  <show_grid>true</show_grid>
  <traces>
    <trace>
      <name>Trace 1</name>
      <x_pv/>
      <y_pv>TEMP:PV1</y_pv>
      <error_pv/>
      <y_axis>0</y_axis>
      <trace_type>1</trace_type>
      <color>
        <color red="0" green="0" blue="255" alpha="255"/>
      </color>
      <line_width>1</line_width>
      <line_style>0</line_style>
      <point_type>0</point_type>
      <point_size>10</point_size>
      <visible>true</visible>
    </trace>
    <trace>
      <name>Trace 2</name>
      <x_pv/>
      <y_pv>TEMP:PV2</y_pv>
      <error_pv/>
      <y_axis>0</y_axis>
      <trace_type>1</trace_type>
      <color>
        <color red="255" green="0" blue="0" alpha="255"/>
      </color>
      <line_width>1</line_width>
      <line_style>0</line_style>
      <point_type>0</point_type>
      <point_size>10</point_size>
      <visible>true</visible>
    </trace>
  </traces>
</widget>
"""


def test_strip_chart_from_xml():
    sc_xml = """<widget type="stripchart" version="2.0.0">
  <name>SC 1</name>
  <x>0</x>
  <y>0</y>
  <width>600</width>
  <height>350</height>
  <title>Signal Monitor</title>
  <show_toolbar>true</show_toolbar>
  <show_legend>true</show_legend>
</widget>"""
    sc = StripChart.from_element(fromstring(sc_xml))
    assert sc is not None
    assert isinstance(sc, StripChart)
    assert sc.name == 'SC 1'
    assert sc.width == 600
    assert sc.height == 350
    assert sc.title == 'Signal Monitor'
    assert sc.show_toolbar
    assert sc.show_legend


def test_create_xyplot_widget():
    plot = XYPlot(name='Test Plot', x=10, y=10, width=500, height=300)
    assert plot is not None
    assert plot.name == 'Test Plot'
    assert plot.x == 10
    assert plot.y == 10
    assert plot.width == 500
    assert plot.height == 300

    plot.title = 'X vs Y'
    plot.show_toolbar = True
    plot.show_legend = True

    plot.traces.append(Trace(name='Data', x_pv='X:PV', y_pv='Y:PV', trace_type=TraceType.LINE))

    assert plot.title == 'X vs Y'
    assert plot.show_toolbar
    assert plot.show_legend
    assert len(plot.traces) == 1
    assert plot.traces[0].name == 'Data'
    assert plot.traces[0].x_pv == 'X:PV'
    assert plot.traces[0].y_pv == 'Y:PV'

    assert str(plot) == """<?xml version="1.0" ?>
<widget type="xyplot" version="3.0.0">
  <name>Test Plot</name>
  <x>10</x>
  <y>10</y>
  <width>500</width>
  <height>300</height>
  <title>X vs Y</title>
  <show_toolbar>true</show_toolbar>
  <show_legend>true</show_legend>
  <traces>
    <trace>
      <name>Data</name>
      <x_pv>X:PV</x_pv>
      <y_pv>Y:PV</y_pv>
      <error_pv/>
      <y_axis>0</y_axis>
      <trace_type>1</trace_type>
      <color>
        <color red="0" green="0" blue="255" alpha="255"/>
      </color>
      <line_width>1</line_width>
      <line_style>0</line_style>
      <point_type>0</point_type>
      <point_size>10</point_size>
      <visible>true</visible>
    </trace>
  </traces>
</widget>
"""


def test_xyplot_from_xml():
    plot_xml = """<widget type="xyplot" version="2.0.0">
  <name>Plot 1</name>
  <x>0</x>
  <y>0</y>
  <width>800</width>
  <height>400</height>
  <title>Waveform</title>
  <show_toolbar>true</show_toolbar>
</widget>"""
    plot = XYPlot.from_element(fromstring(plot_xml))
    assert plot is not None
    assert isinstance(plot, XYPlot)
    assert plot.name == 'Plot 1'
    assert plot.width == 800
    assert plot.height == 400
    assert plot.title == 'Waveform'
    assert plot.show_toolbar


def test_xyplot_with_multiple_traces():
    plot = XYPlot(name='Multi Trace', x=0, y=0, width=600, height=400)
    plot.traces.append(Trace(name='Trace A', x_pv='X:A', y_pv='Y:A', color=Color((255, 0, 0))))
    plot.traces.append(Trace(name='Trace B', x_pv='X:B', y_pv='Y:B', color=Color((0, 255, 0))))

    assert len(plot.traces) == 2
    assert plot.traces[0].name == 'Trace A'
    assert plot.traces[0].color == Color((255, 0, 0))
    assert plot.traces[1].name == 'Trace B'
    assert plot.traces[1].color == Color((0, 255, 0))

    # Remove a trace
    del plot.traces[0]
    assert len(plot.traces) == 1
    assert plot.traces[0].name == 'Trace B'


def test_xyplot_with_y_axes_and_markers():
    plot = XYPlot(name='Full Plot', x=0, y=0, width=800, height=500)
    plot.title = 'Multi-Axis Plot'
    plot.show_toolbar = True
    plot.show_legend = True

    # Add two Y axes
    plot.y_axes.append(Axis(title='Temperature', minimum=0.0, maximum=100.0))
    plot.y_axes.append(Axis(title='Pressure', minimum=-10.0, maximum=10.0, on_right=True))

    assert len(plot.y_axes) == 2
    assert plot.y_axes[0].title == 'Temperature'
    assert plot.y_axes[0].minimum == 0.0
    assert plot.y_axes[0].maximum == 100.0
    assert not plot.y_axes[0].on_right
    assert plot.y_axes[1].title == 'Pressure'
    assert plot.y_axes[1].minimum == -10.0
    assert plot.y_axes[1].maximum == 10.0
    assert plot.y_axes[1].on_right

    # Add markers
    plot.markers.append(Marker(pv_name='MARK:THRESHOLD', color=Color((255, 0, 0)), interactive=False))
    plot.markers.append(Marker(pv_name='MARK:LIMIT', color=Color((0, 255, 0))))

    assert len(plot.markers) == 2
    assert plot.markers[0].pv_name == 'MARK:THRESHOLD'
    assert plot.markers[0].color == Color((255, 0, 0))
    assert  plot.markers[0].interactive is False
    assert plot.markers[1].pv_name == 'MARK:LIMIT'
    assert plot.markers[1].color == Color((0, 255, 0))
    assert plot.markers[1].interactive is True

    # Add traces referencing different y axes
    plot.traces.append(Trace(name='Temp Data', y_pv='TEMP:PV', y_axis=0))
    plot.traces.append(Trace(name='Press Data', y_pv='PRESS:PV', y_axis=1, color=Color((255, 0, 0))))

    assert str(plot) == """<?xml version="1.0" ?>
<widget type="xyplot" version="3.0.0">
  <name>Full Plot</name>
  <x>0</x>
  <y>0</y>
  <width>800</width>
  <height>500</height>
  <title>Multi-Axis Plot</title>
  <show_toolbar>true</show_toolbar>
  <show_legend>true</show_legend>
  <y_axes>
    <y_axis>
      <visible>true</visible>
      <title>Temperature</title>
      <minimum>0.0</minimum>
      <maximum>100.0</maximum>
      <on_right>false</on_right>
      <autoscale>true</autoscale>
      <log_scale>false</log_scale>
      <show_grid>true</show_grid>
      <title_font family="Liberation Sans" size="14" style="REGULAR"/>
      <scale_font family="Liberation Sans" size="14" style="REGULAR"/>
      <color>
        <color red="0" green="0" blue="0" alpha="255"/>
      </color>
    </y_axis>
    <y_axis>
      <visible>true</visible>
      <title>Pressure</title>
      <minimum>-10.0</minimum>
      <maximum>10.0</maximum>
      <on_right>true</on_right>
      <autoscale>true</autoscale>
      <log_scale>false</log_scale>
      <show_grid>true</show_grid>
      <title_font family="Liberation Sans" size="14" style="REGULAR"/>
      <scale_font family="Liberation Sans" size="14" style="REGULAR"/>
      <color>
        <color red="0" green="0" blue="0" alpha="255"/>
      </color>
    </y_axis>
  </y_axes>
  <markers>
    <marker>
      <pv_name>MARK:THRESHOLD</pv_name>
      <color>
        <color red="255" green="0" blue="0" alpha="255"/>
      </color>
      <interactive>false</interactive>
    </marker>
    <marker>
      <pv_name>MARK:LIMIT</pv_name>
      <color>
        <color red="0" green="255" blue="0" alpha="255"/>
      </color>
      <interactive>true</interactive>
    </marker>
  </markers>
  <traces>
    <trace>
      <name>Temp Data</name>
      <x_pv/>
      <y_pv>TEMP:PV</y_pv>
      <error_pv/>
      <y_axis>0</y_axis>
      <trace_type>1</trace_type>
      <color>
        <color red="0" green="0" blue="255" alpha="255"/>
      </color>
      <line_width>1</line_width>
      <line_style>0</line_style>
      <point_type>0</point_type>
      <point_size>10</point_size>
      <visible>true</visible>
    </trace>
    <trace>
      <name>Press Data</name>
      <x_pv/>
      <y_pv>PRESS:PV</y_pv>
      <error_pv/>
      <y_axis>1</y_axis>
      <trace_type>1</trace_type>
      <color>
        <color red="255" green="0" blue="0" alpha="255"/>
      </color>
      <line_width>1</line_width>
      <line_style>0</line_style>
      <point_type>0</point_type>
      <point_size>10</point_size>
      <visible>true</visible>
    </trace>
  </traces>
</widget>
"""


def test_xyplot_y_axes_and_markers_from_xml():
    plot_xml = """<widget type="xyplot" version="3.0.0">
  <name>Parsed Plot</name>
  <x>0</x>
  <y>0</y>
  <width>700</width>
  <height>450</height>
  <title>Parsed Title</title>
  <show_toolbar>true</show_toolbar>
  <show_legend>true</show_legend>
  <y_axes>
    <y_axis>
      <visible>true</visible>
      <title>Axis 1</title>
      <minimum>0.0</minimum>
      <maximum>50.0</maximum>
      <on_right>false</on_right>
      <autoscale>true</autoscale>
      <log_scale>false</log_scale>
      <show_grid>true</show_grid>
      <title_font family="Liberation Sans" size="14" style="REGULAR"/>
      <scale_font family="Liberation Sans" size="14" style="REGULAR"/>
      <color>
        <color red="0" green="0" blue="0" alpha="255"/>
      </color>
    </y_axis>
    <y_axis>
      <visible>true</visible>
      <title>Axis 2</title>
      <minimum>-5.0</minimum>
      <maximum>5.0</maximum>
      <on_right>true</on_right>
      <autoscale>false</autoscale>
      <log_scale>true</log_scale>
      <show_grid>false</show_grid>
      <title_font family="Liberation Sans" size="14" style="REGULAR"/>
      <scale_font family="Liberation Sans" size="14" style="REGULAR"/>
      <color>
        <color red="0" green="0" blue="0" alpha="255"/>
      </color>
    </y_axis>
  </y_axes>
  <markers>
    <marker>
      <pv_name>MARK:PV1</pv_name>
      <color>
        <color red="255" green="128" blue="0" alpha="255"/>
      </color>
      <interactive>true</interactive>
    </marker>
    <marker>
      <pv_name>MARK:PV2</pv_name>
      <color>
        <color red="0" green="0" blue="255" alpha="255"/>
      </color>
      <interactive>false</interactive>
    </marker>
  </markers>
  <traces>
    <trace>
      <name>Signal</name>
      <x_pv>X:SIG</x_pv>
      <y_pv>Y:SIG</y_pv>
      <error_pv/>
      <y_axis>0</y_axis>
      <trace_type>1</trace_type>
      <color>
        <color red="0" green="0" blue="255" alpha="255"/>
      </color>
      <line_width>1</line_width>
      <line_style>0</line_style>
      <point_type>0</point_type>
      <point_size>10</point_size>
      <visible>true</visible>
    </trace>
  </traces>
</widget>"""
    plot = XYPlot.from_element(fromstring(plot_xml))
    assert plot is not None
    assert isinstance(plot, XYPlot)
    assert plot.name == 'Parsed Plot'
    assert plot.title == 'Parsed Title'
    assert plot.show_toolbar
    assert plot.show_legend

    # Verify y_axes
    assert len(plot.y_axes) == 2
    assert plot.y_axes[0].title == 'Axis 1'
    assert plot.y_axes[0].minimum == 0.0
    assert plot.y_axes[0].maximum == 50.0
    assert not plot.y_axes[0].on_right
    assert plot.y_axes[0].autoscale
    assert not plot.y_axes[0].log_scale
    assert plot.y_axes[1].title == 'Axis 2'
    assert plot.y_axes[1].minimum == -5.0
    assert plot.y_axes[1].maximum == 5.0
    assert plot.y_axes[1].on_right
    assert not plot.y_axes[1].autoscale
    assert plot.y_axes[1].log_scale
    assert not plot.y_axes[1].show_grid

    # Verify markers
    assert len(plot.markers) == 2
    assert plot.markers[0].pv_name == 'MARK:PV1'
    assert plot.markers[0].color == Color((255, 128, 0))
    assert plot.markers[0].interactive
    assert plot.markers[1].pv_name == 'MARK:PV2'
    assert plot.markers[1].color == Color((0, 0, 255))
    assert not plot.markers[1].interactive

    # Verify traces
    assert len(plot.traces) == 1
    assert plot.traces[0].name == 'Signal'
    assert plot.traces[0].x_pv == 'X:SIG'
    assert plot.traces[0].y_pv == 'Y:SIG'
    assert plot.traces[0].y_axis == 0
