from xml.etree.ElementTree import fromstring

from phoebusgen.v4.properties.types import (
    Color,
    Format,
    State,
)
from phoebusgen.v4.widgets import (
    LED,
    ByteMonitor,
    LEDMultiState,
    LinearMeter,
    Meter,
    ProgressBar,
    Symbol,
    Table,
    Tank,
    TextSymbol,
    TextUpdate,
    Thermometer,
)


def test_create_text_update_widget():
    tu = TextUpdate(name='Test TU', pv_name='TEST:PV', x=10, y=20, width=200, height=30)
    assert tu is not None
    assert tu.name == 'Test TU'
    assert tu.pv_name == 'TEST:PV'
    assert tu.x == 10
    assert tu.y == 20
    assert tu.width == 200
    assert tu.height == 30

    assert str(tu) == """<?xml version="1.0" ?>
<widget type="textupdate" version="2.0.0">
  <name>Test TU</name>
  <x>10</x>
  <y>20</y>
  <width>200</width>
  <height>30</height>
  <pv_name>TEST:PV</pv_name>
</widget>
"""


def test_text_update_with_properties():
    tu = TextUpdate(name='Formatted TU', pv_name='SIG:VALUE', x=0, y=0, width=150, height=25)
    tu.format = Format.DECIMAL
    tu.precision = 3
    tu.show_units = True
    tu.foreground_color = Color((0, 0, 0))
    tu.background_color = Color((240, 240, 240))

    assert tu.format == Format.DECIMAL
    assert tu.precision == 3
    assert tu.show_units == True
    assert tu.foreground_color == Color((0, 0, 0))
    assert tu.background_color == Color((240, 240, 240))

    assert str(tu) == """<?xml version="1.0" ?>
<widget type="textupdate" version="2.0.0">
  <name>Formatted TU</name>
  <x>0</x>
  <y>0</y>
  <width>150</width>
  <height>25</height>
  <pv_name>SIG:VALUE</pv_name>
  <format>1</format>
  <precision>3</precision>
  <show_units>true</show_units>
  <foreground_color>
    <color red="0" green="0" blue="0" alpha="255"/>
  </foreground_color>
  <background_color>
    <color red="240" green="240" blue="240" alpha="255"/>
  </background_color>
</widget>
"""


def test_text_update_from_xml():
    tu_xml = """<widget type="textupdate" version="2.0.0">
  <name>TU From XML</name>
  <x>5</x>
  <y>15</y>
  <width>100</width>
  <height>20</height>
  <pv_name>MY:PV</pv_name>
  <precision>2</precision>
  <show_units>true</show_units>
</widget>"""
    tu = TextUpdate.from_element(fromstring(tu_xml))
    assert tu is not None
    assert isinstance(tu, TextUpdate)
    assert tu.name == 'TU From XML'
    assert tu.x == 5
    assert tu.y == 15
    assert tu.width == 100
    assert tu.height == 20
    assert tu.pv_name == 'MY:PV'
    assert tu.precision == 2
    assert tu.show_units == True
    assert tu.format == Format.DECIMAL  # Default format


def test_create_led_widget():
    led = LED(name='Test LED', pv_name='TEST:STATUS', x=10, y=10, width=20, height=20)
    assert led is not None
    assert led.name == 'Test LED'
    assert led.pv_name == 'TEST:STATUS'
    assert led.x == 10
    assert led.y == 10
    assert led.width == 20
    assert led.height == 20

    led.on_color = Color((0, 255, 0))
    led.off_color = Color((255, 0, 0))
    led.square = True

    assert led.on_color == Color((0, 255, 0))
    assert led.off_color == Color((255, 0, 0))
    assert led.square == True

    assert str(led) == """<?xml version="1.0" ?>
<widget type="led" version="2.0.0">
  <name>Test LED</name>
  <x>10</x>
  <y>10</y>
  <width>20</width>
  <height>20</height>
  <pv_name>TEST:STATUS</pv_name>
  <on_color>
    <color red="0" green="255" blue="0" alpha="255"/>
  </on_color>
  <off_color>
    <color red="255" green="0" blue="0" alpha="255"/>
  </off_color>
  <square>true</square>
</widget>
"""


def test_led_from_xml():
    led_xml = """<widget type="led" version="2.0.0">
  <name>LED 1</name>
  <x>20</x>
  <y>30</y>
  <width>25</width>
  <height>25</height>
  <pv_name>SIG:STATUS</pv_name>
  <square>true</square>
</widget>"""
    led = LED.from_element(fromstring(led_xml))
    assert led is not None
    assert isinstance(led, LED)
    assert led.name == 'LED 1'
    assert led.x == 20
    assert led.y == 30
    assert led.width == 25
    assert led.height == 25
    assert led.pv_name == 'SIG:STATUS'
    assert led.square == True


def test_create_led_multistate_widget():
    led = LEDMultiState(name='Multi LED', pv_name='TEST:STATE', x=5, y=5, width=30, height=30)
    assert led is not None
    assert led.name == 'Multi LED'
    assert led.pv_name == 'TEST:STATE'

    led.states.append(State(value=0, label='Off', color=Color((128, 128, 128))))
    led.states.append(State(value=1, label='On', color=Color((0, 255, 0))))

    assert len(led.states) == 2
    assert led.states[0].value == 0
    assert led.states[0].label == 'Off'
    assert led.states[1].value == 1
    assert led.states[1].label == 'On'

    assert str(led) == """<?xml version="1.0" ?>
<widget type="multi_state_led" version="2.0.0">
  <name>Multi LED</name>
  <x>5</x>
  <y>5</y>
  <width>30</width>
  <height>30</height>
  <pv_name>TEST:STATE</pv_name>
  <states>
    <state>
      <value>0</value>
      <label>Off</label>
      <color>
        <color red="128" green="128" blue="128" alpha="255"/>
      </color>
    </state>
    <state>
      <value>1</value>
      <label>On</label>
      <color>
        <color red="0" green="255" blue="0" alpha="255"/>
      </color>
    </state>
  </states>
</widget>
"""


def test_led_multistate_from_xml():
    led_xml = """<widget type="multi_state_led" version="2.0.0">
  <name>MS LED</name>
  <x>10</x>
  <y>10</y>
  <width>20</width>
  <height>20</height>
  <pv_name>STATE:PV</pv_name>
  <states>
    <state>
      <value>0</value>
      <label>Idle</label>
      <color>
        <color red="200" green="200" blue="200"/>
      </color>
    </state>
  </states>
</widget>"""
    led = LEDMultiState.from_element(fromstring(led_xml))
    assert led is not None
    assert isinstance(led, LEDMultiState)
    assert led.name == 'MS LED'
    assert led.pv_name == 'STATE:PV'
    assert len(led.states) == 1
    assert led.states[0].value == 0
    assert led.states[0].label == 'Idle'


def test_create_byte_monitor_widget():
    bm = ByteMonitor(name='Test BM', pv_name='TEST:BYTE', x=10, y=10, width=200, height=30)
    assert bm is not None
    assert bm.name == 'Test BM'
    assert bm.pv_name == 'TEST:BYTE'
    assert bm.x == 10
    assert bm.y == 10

    bm.start_bit = 0
    bm.num_bits = 8
    bm.horizontal = True

    assert bm.start_bit == 0
    assert bm.num_bits == 8
    assert bm.horizontal == True

    assert str(bm) == """<?xml version="1.0" ?>
<widget type="byte_monitor" version="2.0.0">
  <name>Test BM</name>
  <x>10</x>
  <y>10</y>
  <width>200</width>
  <height>30</height>
  <pv_name>TEST:BYTE</pv_name>
  <start_bit>0</start_bit>
  <num_bits>8</num_bits>
  <horizontal>true</horizontal>
</widget>
"""


def test_byte_monitor_from_xml():
    bm_xml = """<widget type="byte_monitor" version="2.0.0">
  <name>BM 1</name>
  <x>5</x>
  <y>5</y>
  <width>160</width>
  <height>20</height>
  <pv_name>SYS:BITS</pv_name>
  <num_bits>16</num_bits>
  <start_bit>0</start_bit>
</widget>"""
    bm = ByteMonitor.from_element(fromstring(bm_xml))
    assert bm is not None
    assert isinstance(bm, ByteMonitor)
    assert bm.name == 'BM 1'
    assert bm.pv_name == 'SYS:BITS'
    assert bm.num_bits == 16
    assert bm.start_bit == 0


def test_create_meter_widget():
    meter = Meter(name='Test Meter', pv_name='TEST:TEMP', x=10, y=10, width=200, height=200)
    assert meter is not None
    assert meter.name == 'Test Meter'
    assert meter.pv_name == 'TEST:TEMP'

    meter.show_value = True
    meter.show_units = True
    meter.show_limits = True
    meter.limits_from_pv = True

    assert meter.show_value == True
    assert meter.show_units == True
    assert meter.show_limits == True
    assert meter.limits_from_pv == True

    assert str(meter) == """<?xml version="1.0" ?>
<widget type="meter" version="3.0.0">
  <name>Test Meter</name>
  <x>10</x>
  <y>10</y>
  <width>200</width>
  <height>200</height>
  <pv_name>TEST:TEMP</pv_name>
  <show_value>true</show_value>
  <show_units>true</show_units>
  <show_limits>true</show_limits>
  <limits_from_pv>true</limits_from_pv>
</widget>
"""


def test_meter_from_xml():
    meter_xml = """<widget type="meter" version="2.0.0">
  <name>Meter 1</name>
  <x>0</x>
  <y>0</y>
  <width>250</width>
  <height>250</height>
  <pv_name>MOTOR:POS</pv_name>
  <show_value>true</show_value>
  <limits_from_pv>true</limits_from_pv>
</widget>"""
    meter = Meter.from_element(fromstring(meter_xml))
    assert meter is not None
    assert isinstance(meter, Meter)
    assert meter.name == 'Meter 1'
    assert meter.pv_name == 'MOTOR:POS'
    assert meter.show_value == True
    assert meter.limits_from_pv == True


def test_create_progress_bar_widget():
    pb = ProgressBar(name='Test PB', pv_name='TEST:PROGRESS', x=10, y=10, width=200, height=30)
    assert pb is not None
    assert pb.name == 'Test PB'
    assert pb.pv_name == 'TEST:PROGRESS'

    pb.horizontal = True
    pb.fill_color = Color((0, 128, 255))
    pb.limits_from_pv = True

    assert pb.horizontal == True
    assert pb.fill_color == Color((0, 128, 255))
    assert pb.limits_from_pv == True

    assert str(pb) == """<?xml version="1.0" ?>
<widget type="progressbar" version="2.0.0">
  <name>Test PB</name>
  <x>10</x>
  <y>10</y>
  <width>200</width>
  <height>30</height>
  <pv_name>TEST:PROGRESS</pv_name>
  <horizontal>true</horizontal>
  <fill_color>
    <color red="0" green="128" blue="255" alpha="255"/>
  </fill_color>
  <limits_from_pv>true</limits_from_pv>
</widget>
"""


def test_progress_bar_from_xml():
    pb_xml = """<widget type="progressbar" version="2.0.0">
  <name>PB 1</name>
  <x>5</x>
  <y>5</y>
  <width>300</width>
  <height>25</height>
  <pv_name>FILL:LEVEL</pv_name>
  <horizontal>true</horizontal>
  <limits_from_pv>true</limits_from_pv>
</widget>"""
    pb = ProgressBar.from_element(fromstring(pb_xml))
    assert pb is not None
    assert isinstance(pb, ProgressBar)
    assert pb.name == 'PB 1'
    assert pb.pv_name == 'FILL:LEVEL'
    assert pb.horizontal == True
    assert pb.limits_from_pv == True


def test_create_tank_widget():
    tank = Tank(name='Test Tank', pv_name='TEST:LEVEL', x=10, y=10, width=100, height=200)
    assert tank is not None
    assert tank.name == 'Test Tank'
    assert tank.pv_name == 'TEST:LEVEL'

    tank.fill_color = Color((0, 0, 255))
    tank.empty_color = Color((200, 200, 200))
    tank.scale_visible = True
    tank.limits_from_pv = True

    assert tank.fill_color == Color((0, 0, 255))
    assert tank.empty_color == Color((200, 200, 200))
    assert tank.scale_visible == True
    assert tank.limits_from_pv == True

    assert str(tank) == """<?xml version="1.0" ?>
<widget type="tank" version="2.0.0">
  <name>Test Tank</name>
  <x>10</x>
  <y>10</y>
  <width>100</width>
  <height>200</height>
  <pv_name>TEST:LEVEL</pv_name>
  <fill_color>
    <color red="0" green="0" blue="255" alpha="255"/>
  </fill_color>
  <empty_color>
    <color red="200" green="200" blue="200" alpha="255"/>
  </empty_color>
  <scale_visible>true</scale_visible>
  <limits_from_pv>true</limits_from_pv>
</widget>
"""


def test_tank_from_xml():
    tank_xml = """<widget type="tank" version="2.0.0">
  <name>Tank 1</name>
  <x>0</x>
  <y>0</y>
  <width>80</width>
  <height>150</height>
  <pv_name>WATER:LEVEL</pv_name>
  <scale_visible>true</scale_visible>
</widget>"""
    tank = Tank.from_element(fromstring(tank_xml))
    assert tank is not None
    assert isinstance(tank, Tank)
    assert tank.name == 'Tank 1'
    assert tank.pv_name == 'WATER:LEVEL'
    assert tank.scale_visible == True


def test_create_thermometer_widget():
    thermo = Thermometer(name='Test Thermo', pv_name='TEST:TEMP', x=10, y=10, width=50, height=200)
    assert thermo is not None
    assert thermo.name == 'Test Thermo'
    assert thermo.pv_name == 'TEST:TEMP'

    thermo.fill_color = Color((255, 0, 0))
    thermo.limits_from_pv = True

    assert thermo.fill_color == Color((255, 0, 0))
    assert thermo.limits_from_pv == True

    assert str(thermo) == """<?xml version="1.0" ?>
<widget type="thermometer" version="2.0.0">
  <name>Test Thermo</name>
  <x>10</x>
  <y>10</y>
  <width>50</width>
  <height>200</height>
  <pv_name>TEST:TEMP</pv_name>
  <fill_color>
    <color red="255" green="0" blue="0" alpha="255"/>
  </fill_color>
  <limits_from_pv>true</limits_from_pv>
</widget>
"""


def test_thermometer_from_xml():
    thermo_xml = """<widget type="thermometer" version="2.0.0">
  <name>Thermo 1</name>
  <x>5</x>
  <y>5</y>
  <width>40</width>
  <height>180</height>
  <pv_name>CRYO:TEMP</pv_name>
  <limits_from_pv>true</limits_from_pv>
</widget>"""
    thermo = Thermometer.from_element(fromstring(thermo_xml))
    assert thermo is not None
    assert isinstance(thermo, Thermometer)
    assert thermo.name == 'Thermo 1'
    assert thermo.pv_name == 'CRYO:TEMP'
    assert thermo.limits_from_pv == True


def test_create_symbol_widget():
    sym = Symbol(name='Test Symbol', pv_name='TEST:STATE', x=10, y=10, width=100, height=100)
    assert sym is not None
    assert sym.name == 'Test Symbol'
    assert sym.pv_name == 'TEST:STATE'

    sym.initial_index = 0
    sym.show_index = True
    sym.symbols.append('icon_off.png')
    sym.symbols.append('icon_on.png')

    assert sym.initial_index == 0
    assert sym.show_index == True
    assert len(sym.symbols) == 2

    assert str(sym) == """<?xml version="1.0" ?>
<widget type="symbol" version="2.0.0">
  <name>Test Symbol</name>
  <x>10</x>
  <y>10</y>
  <width>100</width>
  <height>100</height>
  <pv_name>TEST:STATE</pv_name>
  <initial_index>0</initial_index>
  <show_index>true</show_index>
  <symbols>
    <symbol>icon_off.png</symbol>
    <symbol>icon_on.png</symbol>
  </symbols>
</widget>
"""


def test_symbol_from_xml():
    sym_xml = """<widget type="symbol" version="2.0.0">
  <name>Symbol 1</name>
  <x>0</x>
  <y>0</y>
  <width>64</width>
  <height>64</height>
  <pv_name>DEVICE:STATE</pv_name>
  <symbols>
    <symbol>state0.png</symbol>
    <symbol>state1.png</symbol>
    <symbol>state2.png</symbol>
  </symbols>
</widget>"""
    sym = Symbol.from_element(fromstring(sym_xml))
    assert sym is not None
    assert isinstance(sym, Symbol)
    assert sym.name == 'Symbol 1'
    assert sym.pv_name == 'DEVICE:STATE'
    assert len(sym.symbols) == 3
    assert sym.symbols[0] == 'state0.png'
    assert sym.symbols[1] == 'state1.png'
    assert sym.symbols[2] == 'state2.png'


def test_create_table_widget():
    table = Table(name='Test Table', pv_name='TEST:TABLE', x=10, y=10, width=400, height=200)
    assert table is not None
    assert table.name == 'Test Table'
    assert table.pv_name == 'TEST:TABLE'

    table.editable = True
    table.show_toolbar = True

    assert table.editable == True
    assert table.show_toolbar == True

    assert str(table) == """<?xml version="1.0" ?>
<widget type="table" version="2.0.0">
  <name>Test Table</name>
  <x>10</x>
  <y>10</y>
  <width>400</width>
  <height>200</height>
  <pv_name>TEST:TABLE</pv_name>
  <editable>true</editable>
  <show_toolbar>true</show_toolbar>
</widget>
"""


def test_table_from_xml():
    table_xml = """<widget type="table" version="2.0.0">
  <name>Table 1</name>
  <x>0</x>
  <y>0</y>
  <width>500</width>
  <height>300</height>
  <pv_name>DATA:TABLE</pv_name>
  <editable>true</editable>
</widget>"""
    table = Table.from_element(fromstring(table_xml))
    assert table is not None
    assert isinstance(table, Table)
    assert table.name == 'Table 1'
    assert table.pv_name == 'DATA:TABLE'
    assert table.editable == True


def test_create_text_symbol_widget():
    ts = TextSymbol(name='Test TS', pv_name='TEST:IDX', x=10, y=10, width=100, height=30)
    assert ts is not None
    assert ts.name == 'Test TS'
    assert ts.pv_name == 'TEST:IDX'

    ts.symbols.append('Idle')
    ts.symbols.append('Running')
    ts.symbols.append('Error')

    assert len(ts.symbols) == 3
    assert ts.symbols[0] == 'Idle'
    assert ts.symbols[1] == 'Running'
    assert ts.symbols[2] == 'Error'

    assert str(ts) == """<?xml version="1.0" ?>
<widget type="text-symbol" version="2.0.0">
  <name>Test TS</name>
  <x>10</x>
  <y>10</y>
  <width>100</width>
  <height>30</height>
  <pv_name>TEST:IDX</pv_name>
  <symbols>
    <symbol>Idle</symbol>
    <symbol>Running</symbol>
    <symbol>Error</symbol>
  </symbols>
</widget>
"""


def test_text_symbol_from_xml():
    ts_xml = """<widget type="text-symbol" version="2.0.0">
  <name>TS 1</name>
  <x>5</x>
  <y>5</y>
  <width>120</width>
  <height>25</height>
  <pv_name>MODE:PV</pv_name>
  <symbols>
    <symbol>Off</symbol>
    <symbol>On</symbol>
  </symbols>
</widget>"""
    ts = TextSymbol.from_element(fromstring(ts_xml))
    assert ts is not None
    assert isinstance(ts, TextSymbol)
    assert ts.name == 'TS 1'
    assert ts.pv_name == 'MODE:PV'
    assert len(ts.symbols) == 2
    assert ts.symbols[0] == 'Off'
    assert ts.symbols[1] == 'On'


def test_create_linear_meter_widget():
    lm = LinearMeter(name='Test LM', pv_name='TEST:VALUE', x=10, y=10, width=300, height=80)
    assert lm is not None
    assert lm.name == 'Test LM'
    assert lm.pv_name == 'TEST:VALUE'

    lm.show_value = True
    lm.show_units = True
    lm.limits_from_pv = True
    lm.horizontal = True

    assert lm.show_value == True
    assert lm.show_units == True
    assert lm.limits_from_pv == True
    assert lm.horizontal == True

    assert str(lm) == """<?xml version="1.0" ?>
<widget type="linearmeter" version="2.0.0">
  <name>Test LM</name>
  <x>10</x>
  <y>10</y>
  <width>300</width>
  <height>80</height>
  <pv_name>TEST:VALUE</pv_name>
  <show_value>true</show_value>
  <show_units>true</show_units>
  <limits_from_pv>true</limits_from_pv>
  <horizontal>true</horizontal>
</widget>
"""


def test_linear_meter_from_xml():
    lm_xml = """<widget type="linearmeter" version="2.0.0">
  <name>LM 1</name>
  <x>0</x>
  <y>0</y>
  <width>250</width>
  <height>60</height>
  <pv_name>BEAM:CURRENT</pv_name>
  <horizontal>true</horizontal>
  <limits_from_pv>true</limits_from_pv>
</widget>"""
    lm = LinearMeter.from_element(fromstring(lm_xml))
    assert lm is not None
    assert isinstance(lm, LinearMeter)
    assert lm.name == 'LM 1'
    assert lm.pv_name == 'BEAM:CURRENT'
    assert lm.horizontal == True
    assert lm.limits_from_pv == True
