from xml.etree.ElementTree import Element, fromstring

from phoebusgen.v4.properties.types import ObservableList
from phoebusgen.v4.widgets.widget import HasWidgets
import pytest

from phoebusgen.v4.screen import Screen
from phoebusgen.v4.widgets.structure import NavigationTabs, Tabs, Tab
from phoebusgen.v4.properties.display import HasTabActiveHeightDirection
from phoebusgen.v4.properties.widget import HasName, HasNavTabs

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
