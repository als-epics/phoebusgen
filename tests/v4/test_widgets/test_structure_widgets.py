from pathlib import Path
from xml.etree.ElementTree import fromstring

from phoebusgen.v4.properties.types import (
    Instance,
    NavTab,
    ObservableDict,
)
from phoebusgen.v4.widgets import Label, Rectangle, TextUpdate
from phoebusgen.v4.widgets.structure import (
    Array,
    EmbeddedDisplay,
    Group,
    NavigationTabs,
    TemplateInstance,
)


def test_create_array_widget():
    arr = Array(name='Test Array', pv_name='ARR:PV', x=10, y=20, width=400, height=300)
    assert arr is not None
    assert arr.name == 'Test Array'
    assert arr.pv_name == 'ARR:PV'
    assert arr.x == 10
    assert arr.y == 20
    assert arr.width == 400
    assert arr.height == 300

    assert str(arr) == """<?xml version="1.0" ?>
<widget type="array" version="2.0.0">
  <name>Test Array</name>
  <x>10</x>
  <y>20</y>
  <width>400</width>
  <height>300</height>
  <pv_name>ARR:PV</pv_name>
</widget>
"""


def test_array_with_macros():
    arr = Array(name='Arr', pv_name='$(P):ARR', x=0, y=0, width=200, height=100)
    arr.macros['P'] = 'IOC1'
    arr.macros['R'] = 'Det1'

    assert dict(arr.macros) == {'P': 'IOC1', 'R': 'Det1'}

    assert str(arr) == """<?xml version="1.0" ?>
<widget type="array" version="2.0.0">
  <name>Arr</name>
  <x>0</x>
  <y>0</y>
  <width>200</width>
  <height>100</height>
  <pv_name>$(P):ARR</pv_name>
  <macros>
    <P>IOC1</P>
    <R>Det1</R>
  </macros>
</widget>
"""


def test_array_from_xml():
    arr_xml = """<widget type="array" version="2.0.0">
  <name>Arr1</name>
  <x>5</x>
  <y>10</y>
  <width>200</width>
  <height>150</height>
  <pv_name>SYS:ARR</pv_name>
  <macros>
    <P>IOC1</P>
  </macros>
</widget>"""
    arr = Array.from_element(fromstring(arr_xml))
    assert arr is not None
    assert isinstance(arr, Array)
    assert arr.name == 'Arr1'
    assert arr.pv_name == 'SYS:ARR'
    assert arr.x == 5
    assert arr.y == 10
    assert dict(arr.macros) == {'P': 'IOC1'}


def test_create_embedded_display_widget():
    ed = EmbeddedDisplay(name='Test Embed', file='panel.bob', x=10, y=20, width=300, height=200)
    assert ed is not None
    assert ed.name == 'Test Embed'
    assert ed.file == Path('panel.bob')
    assert ed.x == 10
    assert ed.y == 20

    assert str(ed) == """<?xml version="1.0" ?>
<widget type="embedded" version="2.0.0">
  <name>Test Embed</name>
  <x>10</x>
  <y>20</y>
  <width>300</width>
  <height>200</height>
  <file>panel.bob</file>
</widget>
"""


def test_embedded_display_with_macros():
    ed = EmbeddedDisplay(name='Embed', file='motor.bob', x=0, y=0, width=400, height=300)
    ed.macros['SYS'] = 'IOC1'
    ed.macros['DEV'] = 'Motor1'
    ed.macros['DESC'] = 'X Stage'

    assert dict(ed.macros) == {'SYS': 'IOC1', 'DEV': 'Motor1', 'DESC': 'X Stage'}

    assert str(ed) == """<?xml version="1.0" ?>
<widget type="embedded" version="2.0.0">
  <name>Embed</name>
  <x>0</x>
  <y>0</y>
  <width>400</width>
  <height>300</height>
  <file>motor.bob</file>
  <macros>
    <SYS>IOC1</SYS>
    <DEV>Motor1</DEV>
    <DESC>X Stage</DESC>
  </macros>
</widget>
"""


def test_embedded_display_from_xml():
    ed_xml = """<widget type="embedded" version="2.0.0">
  <name>Embed 1</name>
  <x>10</x>
  <y>20</y>
  <width>300</width>
  <height>200</height>
  <file>panel.bob</file>
  <macros>
    <SYS>IOC1</SYS>
    <DEV>Motor1</DEV>
  </macros>
</widget>"""
    ed = EmbeddedDisplay.from_element(fromstring(ed_xml))
    assert ed is not None
    assert isinstance(ed, EmbeddedDisplay)
    assert ed.name == 'Embed 1'
    assert ed.file == Path('panel.bob')
    assert ed.x == 10
    assert ed.y == 20
    assert dict(ed.macros) == {'SYS': 'IOC1', 'DEV': 'Motor1'}


def test_create_group_widget():
    grp = Group(name='Test Group', x=10, y=10, width=400, height=300)
    assert grp is not None
    assert grp.name == 'Test Group'
    assert grp.x == 10
    assert grp.y == 10
    assert grp.width == 400
    assert grp.height == 300

    assert str(grp) == """<?xml version="1.0" ?>
<widget type="group" version="3.0.0">
  <name>Test Group</name>
  <x>10</x>
  <y>10</y>
  <width>400</width>
  <height>300</height>
</widget>
"""


def test_group_add_widget():
    grp = Group(name='G', x=0, y=0, width=200, height=150)
    label = Label(name='L1', text='Hello', x=5, y=5, width=80, height=20)
    grp.widgets.append(label)

    assert len(grp.widgets) == 1
    assert grp.widgets[0].name == 'L1'

    assert str(grp) == """<?xml version="1.0" ?>
<widget type="group" version="3.0.0">
  <name>G</name>
  <x>0</x>
  <y>0</y>
  <width>200</width>
  <height>150</height>
  <widget type="label" version="2.0.0">
    <name>L1</name>
    <x>5</x>
    <y>5</y>
    <width>80</width>
    <height>20</height>
    <text>Hello</text>
  </widget>
</widget>
"""


def test_group_from_xml():
    grp_xml = """<widget type="group" version="3.0.0">
  <name>G1</name>
  <x>0</x>
  <y>0</y>
  <width>400</width>
  <height>300</height>
  <widget type="label" version="2.0.0">
    <name>L1</name>
    <x>0</x>
    <y>0</y>
    <width>100</width>
    <height>30</height>
    <text>Hello</text>
  </widget>
  <widget type="rectangle" version="2.0.0">
    <name>R1</name>
    <x>0</x>
    <y>40</y>
    <width>100</width>
    <height>50</height>
  </widget>
</widget>"""
    grp = Group.from_element(fromstring(grp_xml))
    assert grp is not None
    assert isinstance(grp, Group)
    assert grp.name == 'G1'
    assert grp.width == 400
    assert grp.height == 300


def test_create_navigation_tabs_widget():
    nav = NavigationTabs(name='Test Nav', x=10, y=10, width=500, height=400)
    assert nav is not None
    assert nav.name == 'Test Nav'
    assert nav.x == 10
    assert nav.y == 10
    assert nav.width == 500
    assert nav.height == 400

    nav.tabs.append(NavTab(name='Tab A', file='tab_a.bob'))
    nav.tabs.append(NavTab(name='Tab B', file='tab_b.bob', macros=ObservableDict({'SYS': 'IOC1'})))
    nav.tabs.append(NavTab(name='Tab C', file='tab_c.bob', macros=ObservableDict({'SYS': 'IOC2', 'DEV': 'Motor'})))

    assert len(nav.tabs) == 3
    assert nav.tabs[0].name == 'Tab A'
    assert nav.tabs[0].file == Path('tab_a.bob')
    assert nav.tabs[1].name == 'Tab B'
    assert nav.tabs[1].file == Path('tab_b.bob')
    assert dict(nav.tabs[1].macros) == {'SYS': 'IOC1'}
    assert nav.tabs[2].name == 'Tab C'
    assert dict(nav.tabs[2].macros) == {'SYS': 'IOC2', 'DEV': 'Motor'}

    assert str(nav) == """<?xml version="1.0" ?>
<widget type="navtabs" version="2.0.0">
  <name>Test Nav</name>
  <x>10</x>
  <y>10</y>
  <width>500</width>
  <height>400</height>
  <tabs>
    <tab>
      <name>Tab A</name>
      <file>tab_a.bob</file>
      <macros/>
      <group_name/>
    </tab>
    <tab>
      <name>Tab B</name>
      <file>tab_b.bob</file>
      <macros>
        <SYS>IOC1</SYS>
      </macros>
      <group_name/>
    </tab>
    <tab>
      <name>Tab C</name>
      <file>tab_c.bob</file>
      <macros>
        <SYS>IOC2</SYS>
        <DEV>Motor</DEV>
      </macros>
      <group_name/>
    </tab>
  </tabs>
</widget>
"""


def test_navigation_tabs_from_xml():
    nav_xml = """<widget type="navtabs" version="2.0.0">
  <name>Nav 1</name>
  <x>0</x>
  <y>0</y>
  <width>500</width>
  <height>400</height>
  <tabs>
    <tab>
      <name>Tab A</name>
      <file>a.bob</file>
      <macros/>
      <group_name/>
    </tab>
    <tab>
      <name>Tab B</name>
      <file>b.bob</file>
      <macros>
        <SYS>IOC1</SYS>
      </macros>
      <group_name/>
    </tab>
  </tabs>
</widget>"""
    nav = NavigationTabs.from_element(fromstring(nav_xml))
    assert nav is not None
    assert isinstance(nav, NavigationTabs)
    assert nav.name == 'Nav 1'
    assert nav.width == 500
    assert nav.height == 400
    assert len(nav.tabs) == 2
    assert nav.tabs[0].name == 'Tab A'
    assert nav.tabs[0].file == Path('a.bob')
    assert nav.tabs[1].name == 'Tab B'
    assert nav.tabs[1].file == Path('b.bob')
    assert dict(nav.tabs[1].macros) == {'SYS': 'IOC1'}


def test_create_template_instance_widget():
    tmpl = TemplateInstance(name='Test Template', file='template.bob', x=10, y=10, width=300, height=200)
    assert tmpl is not None
    assert tmpl.name == 'Test Template'
    assert tmpl.file == Path('template.bob')
    assert tmpl.x == 10
    assert tmpl.y == 10
    assert tmpl.width == 300
    assert tmpl.height == 200

    assert str(tmpl) == """<?xml version="1.0" ?>
<widget type="template" version="2.0.0">
  <name>Test Template</name>
  <x>10</x>
  <y>10</y>
  <width>300</width>
  <height>200</height>
  <file>template.bob</file>
</widget>
"""


def test_template_instance_with_instances_and_macros():
    tmpl = TemplateInstance(name='T', file='motor.bob', x=0, y=0, width=200, height=100)
    tmpl.instances.append(Instance(macros=ObservableDict({'P': 'IOC1', 'R': 'Motor1'})))
    tmpl.instances.append(Instance(macros=ObservableDict({'P': 'IOC2', 'R': 'Motor2'})))
    tmpl.instances.append(Instance(macros=ObservableDict({'P': 'IOC3', 'R': 'Motor3'})))

    assert len(tmpl.instances) == 3
    assert dict(tmpl.instances[0].macros) == {'P': 'IOC1', 'R': 'Motor1'}
    assert dict(tmpl.instances[1].macros) == {'P': 'IOC2', 'R': 'Motor2'}
    assert dict(tmpl.instances[2].macros) == {'P': 'IOC3', 'R': 'Motor3'}

    assert str(tmpl) == """<?xml version="1.0" ?>
<widget type="template" version="2.0.0">
  <name>T</name>
  <x>0</x>
  <y>0</y>
  <width>200</width>
  <height>100</height>
  <file>motor.bob</file>
  <instances>
    <instance>
      <macros>
        <P>IOC1</P>
        <R>Motor1</R>
      </macros>
    </instance>
    <instance>
      <macros>
        <P>IOC2</P>
        <R>Motor2</R>
      </macros>
    </instance>
    <instance>
      <macros>
        <P>IOC3</P>
        <R>Motor3</R>
      </macros>
    </instance>
  </instances>
</widget>
"""


def test_template_instance_add_and_remove_widgets():
    tmpl = TemplateInstance(name='T', file='t.bob', x=0, y=0, width=300, height=200)

    # Add several widgets
    tmpl.widgets.append(Label(name='L1', text='First', x=0, y=0, width=80, height=20))
    tmpl.widgets.append(Label(name='L2', text='Second', x=0, y=30, width=80, height=20))
    tmpl.widgets.append(Rectangle(name='R1', x=0, y=60, width=100, height=50))
    tmpl.widgets.append(TextUpdate(name='TU1', pv_name='PV:VAL', x=0, y=120, width=100, height=25))

    assert len(tmpl.widgets) == 4
    assert tmpl.widgets[0].name == 'L1'
    assert tmpl.widgets[1].name == 'L2'
    assert tmpl.widgets[2].name == 'R1'
    assert tmpl.widgets[3].name == 'TU1'

    # Remove middle widget
    del tmpl.widgets[1]
    assert len(tmpl.widgets) == 3
    assert tmpl.widgets[0].name == 'L1'
    assert tmpl.widgets[1].name == 'R1'
    assert tmpl.widgets[2].name == 'TU1'

    # Remove first widget
    del tmpl.widgets[0]
    assert len(tmpl.widgets) == 2
    assert tmpl.widgets[0].name == 'R1'
    assert tmpl.widgets[1].name == 'TU1'

    assert str(tmpl) == """<?xml version="1.0" ?>
<widget type="template" version="2.0.0">
  <name>T</name>
  <x>0</x>
  <y>0</y>
  <width>300</width>
  <height>200</height>
  <file>t.bob</file>
  <widgets>
    <widget type="rectangle" version="2.0.0">
      <name>R1</name>
      <x>0</x>
      <y>60</y>
      <width>100</width>
      <height>50</height>
    </widget>
    <widget type="textupdate" version="2.0.0">
      <name>TU1</name>
      <x>0</x>
      <y>120</y>
      <width>100</width>
      <height>25</height>
      <pv_name>PV:VAL</pv_name>
    </widget>
  </widgets>
</widget>
"""


def test_template_instance_from_xml():
    tmpl_xml = """<widget type="template" version="2.0.0">
  <name>T1</name>
  <x>0</x>
  <y>0</y>
  <width>200</width>
  <height>100</height>
  <file>template.bob</file>
  <instances>
    <instance>
      <macros>
        <P>IOC1</P>
        <R>Motor1</R>
      </macros>
    </instance>
    <instance>
      <macros>
        <P>IOC2</P>
        <R>Motor2</R>
      </macros>
    </instance>
  </instances>
  <widgets>
    <widget type="label" version="2.0.0">
      <name>L1</name>
      <x>0</x>
      <y>0</y>
      <width>50</width>
      <height>20</height>
      <text>Hi</text>
    </widget>
    <widget type="rectangle" version="2.0.0">
      <name>R1</name>
      <x>0</x>
      <y>30</y>
      <width>50</width>
      <height>20</height>
    </widget>
  </widgets>
</widget>"""
    tmpl = TemplateInstance.from_element(fromstring(tmpl_xml))
    assert tmpl is not None
    assert isinstance(tmpl, TemplateInstance)
    assert tmpl.name == 'T1'
    assert tmpl.file == Path('template.bob')

    # Verify instances with macros
    assert len(tmpl.instances) == 2
    assert dict(tmpl.instances[0].macros) == {'P': 'IOC1', 'R': 'Motor1'}
    assert dict(tmpl.instances[1].macros) == {'P': 'IOC2', 'R': 'Motor2'}

    # Verify child widgets
    assert len(tmpl.widgets) == 2
    assert tmpl.widgets[0].name == 'L1'
    assert isinstance(tmpl.widgets[0], Label)
    assert tmpl.widgets[1].name == 'R1'
    assert isinstance(tmpl.widgets[1], Rectangle)
