from xml.etree.ElementTree import fromstring

from phoebusgen.v4.properties.types import NavTab, ObservableList, TabDirection
from phoebusgen.v4.widgets.widget import HasWidgets
import pytest

from phoebusgen.v4.widgets.structure import NavigationTabs, Tabs, Tab
from phoebusgen.v4.properties.widget import HasName

from phoebusgen.v4.widgets import Label, BooleanButton


def test_create_single_tab():
    tab = Tab('Test Tab')
    assert tab is not None

    assert tab.name == 'Test Tab'
    assert isinstance(tab, HasName)
    assert isinstance(tab, HasWidgets)
    assert len(tab.get_widgets()) == 0
    assert tab.root.tag == 'tab'
    label = Label(name='Test Label', text='Hello World', x=10, y=10, width=100, height=30)
    tab.add_widget(label)
    assert len(tab.get_widgets()) == 1
    assert tab.get_widgets()[0].name == 'Test Label'
    assert tab.get_widgets()[0].text == 'Hello World'
    assert str(tab) == """<?xml version="1.0" ?>
<tab>
  <name>Test Tab</name>
  <children>
    <widget type="label" version="2.0.0">
      <name>Test Label</name>
      <x>10</x>
      <y>10</y>
      <width>100</width>
      <height>30</height>
      <text>Hello World</text>
    </widget>
  </children>
</tab>
"""


def test_create_tabs_widget():
    tabs = Tabs(name='Test Tabs', x=10, y=10, width=300, height=200)
    assert tabs is not None
    assert tabs.name == 'Test Tabs'
    assert tabs.x == 10
    assert tabs.y == 10
    assert tabs.width == 300
    assert tabs.height == 200

    # Default direction, tab height, and active tab should be set
    assert tabs.direction == TabDirection.HORIZONTAL
    assert tabs.tab_height == 30
    assert tabs.active_tab == 1

    assert isinstance(tabs.tabs, ObservableList)
    assert len(tabs.tabs) == 0

    # Add a two tabs
    tabs.tabs.append(Tab('Tab 1'))
    tabs.tabs.append(Tab('Tab 2'))
    assert len(tabs.tabs) == 2
    assert all(isinstance(tab, Tab) for tab in tabs.tabs)
    assert tabs.tabs[0].name == 'Tab 1'
    assert tabs.tabs[1].name == 'Tab 2'

    # Now add widgets to the first tab
    label = Label(name='Test Label', text = 'Hello World', x=10, y=10, width=100, height=30)
    button = BooleanButton(name='Test Button', pv_name='Test:PV', x=10, y=50, width=100, height=30)
    tabs.tabs[0].widgets == []
    tabs.tabs[0].widgets.append(label)
    tabs.tabs[0].widgets.append(button)
    assert len(tabs.tabs[0].widgets) == 2
    assert tabs.tabs[0].widgets[0].name == 'Test Label'
    assert tabs.tabs[0].widgets[1].name == 'Test Button'

    # Add a widget to the second tab
    label2 = Label(name='Second Tab Label', text='Goodbye World', x=10, y=10, width=100, height=30)
    tabs.tabs[1].widgets.append(label2)
    assert len(tabs.tabs[1].widgets) == 1
    assert tabs.tabs[1].widgets[0].name == 'Second Tab Label'

    # Check created xml
    assert str(tabs) == """<?xml version="1.0" ?>
<widget type="tabs" version="2.0.0">
  <name>Test Tabs</name>
  <x>10</x>
  <y>10</y>
  <width>300</width>
  <height>200</height>
  <tabs>
    <tab>
      <children>
        <widget type="label" version="2.0.0">
          <name>Test Label</name>
          <x>10</x>
          <y>10</y>
          <width>100</width>
          <height>30</height>
          <text>Hello World</text>
        </widget>
        <widget type="bool_button" version="2.0.0">
          <name>Test Button</name>
          <x>10</x>
          <y>50</y>
          <width>100</width>
          <height>30</height>
          <pv_name>Test:PV</pv_name>
        </widget>
      </children>
      <name>Tab 1</name>
    </tab>
    <tab>
      <children>
        <widget type="label" version="2.0.0">
          <name>Second Tab Label</name>
          <x>10</x>
          <y>10</y>
          <width>100</width>
          <height>30</height>
          <text>Goodbye World</text>
        </widget>
      </children>
      <name>Tab 2</name>
    </tab>
  </tabs>
</widget>
"""

    # Now try removing a tab and a widget from one of the tabs
    del tabs.tabs[1]
    del tabs.tabs[0].widgets[1]

    # Also, let's change the tab direction, tab height from the defaults
    tabs.direction = TabDirection.VERTICAL
    tabs.tab_height = 40
    assert len(tabs.tabs) == 1
    assert tabs.tabs[0].name == 'Tab 1'
    assert len(tabs.tabs[0].widgets) == 1
    assert str(tabs) == """<?xml version="1.0" ?>
<widget type="tabs" version="2.0.0">
  <name>Test Tabs</name>
  <x>10</x>
  <y>10</y>
  <width>300</width>
  <height>200</height>
  <tabs>
    <tab>
      <children>
        <widget type="label" version="2.0.0">
          <name>Test Label</name>
          <x>10</x>
          <y>10</y>
          <width>100</width>
          <height>30</height>
          <text>Hello World</text>
        </widget>
      </children>
      <name>Tab 1</name>
    </tab>
  </tabs>
  <direction>1</direction>
  <tab_height>40</tab_height>
</widget>
"""


def test_tabs_widget_from_xml():

    tabs_xml = """<widget type="tabs" version="2.0.0">
  <name>Tabs</name>
  <tabs>
    <tab>
      <name>Tab 1</name>
      <children>
        <widget type="label" version="2.0.0">
          <name>Label</name>
          <x>78</x>
          <y>152</y>
        </widget>
      </children>
    </tab>
    <tab>
      <name>Tab 2</name>
      <children>
      </children>
    </tab>
  </tabs>
  <x>750</x>
  <y>720</y>
</widget>
"""
    tabs = Tabs.from_element(fromstring(tabs_xml))
    assert tabs is not None
    assert tabs.name == 'Tabs'
    assert tabs.x == 750
    assert tabs.y == 720
    assert len(tabs.tabs) == 2
    assert tabs.tabs[0].name == 'Tab 1'
    assert tabs.tabs[1].name == 'Tab 2'
    assert len(tabs.tabs[0].get_widgets()) == 1
    assert tabs.tabs[0].get_widgets()[0].name == 'Label'
    assert len(tabs.tabs[1].get_widgets()) == 0


def test_create_navtabs_widget():
    nav_tabs = NavigationTabs(name='Test Nav Tabs', x=10, y=10, width=300, height=200)
    assert nav_tabs is not None
    assert nav_tabs.name == 'Test Nav Tabs'
    assert nav_tabs.x == 10
    assert nav_tabs.y == 10
    assert nav_tabs.width == 300
    assert nav_tabs.height == 200

    # Check for defaults
    assert nav_tabs.direction == TabDirection.VERTICAL
    assert nav_tabs.tab_height == 30
    assert nav_tabs.active_tab == 0
    assert nav_tabs.tab_width == 100
    assert nav_tabs.tab_spacing == 2
    assert len(nav_tabs.tabs) == 0

    nav_tabs.tabs.append(NavTab(name='Nav Tab 1'))
    nav_tabs.tabs.append(NavTab(name='Nav Tab 2', file='sample.bob', macros={'Macro1': 'Value1'}, group_name='Group1'))
    assert len(nav_tabs.tabs) == 2
    assert nav_tabs.tabs[0].name == 'Nav Tab 1'
    assert nav_tabs.tabs[0].file == ''
    assert nav_tabs.tabs[0].macros == {}
    assert nav_tabs.tabs[0].group_name == ''
    assert nav_tabs.tabs[1].name == 'Nav Tab 2'
    assert nav_tabs.tabs[1].file == 'sample.bob'
    assert nav_tabs.tabs[1].macros == {'Macro1': 'Value1'}
    assert nav_tabs.tabs[1].group_name == 'Group1'

    assert (str(nav_tabs)) == """<?xml version="1.0" ?>
<widget type="navtabs" version="2.0.0">
  <name>Test Nav Tabs</name>
  <x>10</x>
  <y>10</y>
  <width>300</width>
  <height>200</height>
  <tabs>
    <tab>
      <name>Nav Tab 1</name>
      <file/>
      <macros/>
      <group_name/>
    </tab>
    <tab>
      <name>Nav Tab 2</name>
      <file>sample.bob</file>
      <macros>
        <Macro1>Value1</Macro1>
      </macros>
      <group_name>Group1</group_name>
    </tab>
  </tabs>
</widget>
"""

    # Now let's remove the first tab and change some properties
    del nav_tabs.tabs[0]
    nav_tabs.direction = TabDirection.HORIZONTAL
    nav_tabs.tab_height = 40
    nav_tabs.tab_spacing = 5
    nav_tabs.tab_width = 120
    assert len(nav_tabs.tabs) == 1
    assert nav_tabs.tabs[0].name == 'Nav Tab 2'
    assert nav_tabs.direction == TabDirection.HORIZONTAL
    assert nav_tabs.tab_height == 40
    assert nav_tabs.tab_spacing == 5
    assert nav_tabs.tab_width == 120
    assert (str(nav_tabs)) == """<?xml version="1.0" ?>
<widget type="navtabs" version="2.0.0">
  <name>Test Nav Tabs</name>
  <x>10</x>
  <y>10</y>
  <width>300</width>
  <height>200</height>
  <tabs>
    <tab>
      <name>Nav Tab 2</name>
      <file>sample.bob</file>
      <macros>
        <Macro1>Value1</Macro1>
      </macros>
      <group_name>Group1</group_name>
    </tab>
  </tabs>
  <direction>0</direction>
  <tab_height>40</tab_height>
  <tab_spacing>5</tab_spacing>
  <tab_width>120</tab_width>
</widget>
"""

def test_navtabs_widget_from_xml():
    nav_tabs_xml = """<widget type="navtabs" version="2.0.0">
      <name>Navigation Tabs</name>
      <tabs>
        <tab>
          <name>Tab 1</name>
          <file></file>
          <macros>
          </macros>
          <group_name></group_name>
        </tab>
        <tab>
          <name>Tab 2</name>
          <file>sample.bob</file>
          <macros>
            <Macro1>Value1</Macro1>
          </macros>
          <group_name>Group1</group_name>
        </tab>
      </tabs>
      <x>1450</x>
      <y>590</y>
      <width>350</width>
      <height>210</height>
      <direction>0</direction>
    </widget>
    """

    nav_tabs = NavigationTabs.from_element(fromstring(nav_tabs_xml))
    assert nav_tabs is not None
    assert nav_tabs.name == 'Navigation Tabs'
    assert nav_tabs.x == 1450
    assert nav_tabs.y == 590
    assert nav_tabs.width == 350
    assert nav_tabs.height == 210
    assert len(nav_tabs.tabs) == 2
    assert nav_tabs.tabs[0].name == 'Tab 1'
    assert nav_tabs.tabs[0].file == ''
    assert nav_tabs.tabs[0].macros == {}
    assert nav_tabs.tabs[0].group_name == ''
    assert nav_tabs.tabs[1].name == 'Tab 2'
    assert nav_tabs.tabs[1].file == 'sample.bob'
    assert nav_tabs.tabs[1].macros == {'Macro1': 'Value1'}
    assert nav_tabs.tabs[1].group_name == 'Group1'
    assert nav_tabs.direction == TabDirection.HORIZONTAL
    assert nav_tabs.tab_height == 30
    assert nav_tabs.tab_spacing == 2
    assert nav_tabs.tab_width == 100
