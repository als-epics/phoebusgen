from pathlib import Path
from xml.etree.ElementTree import fromstring

from phoebusgen.v4.properties.types import (
    ButtonMode,
    Color,
    CommandAction,
    Format,
    OpenDisplayAction,
    OpenDisplayTarget,
    OpenFileAction,
    OpenWebpageAction,
    WritePvAction,
)
from phoebusgen.v4.widgets import (
    ActionButton,
    BooleanButton,
    CheckBox,
    ChoiceButton,
    ComboBox,
    FileSelector,
    RadioButton,
    ScaledSlider,
    Scrollbar,
    SlideButton,
    Spinner,
    TextEntry,
    Thumbwheel,
)


def test_create_action_button_widget():
    btn = ActionButton(name='Test Button', text='Click Me', pv_name='TEST:PV', x=10, y=10, width=100, height=30)
    assert btn is not None
    assert btn.name == 'Test Button'
    assert btn.text == 'Click Me'
    assert btn.pv_name == 'TEST:PV'
    assert btn.x == 10
    assert btn.y == 10
    assert btn.width == 100
    assert btn.height == 30

    assert btn == """<?xml version="1.0" ?>
<widget type="action_button" version="3.0.0">
  <name>Test Button</name>
  <x>10</x>
  <y>10</y>
  <width>100</width>
  <height>30</height>
  <pv_name>TEST:PV</pv_name>
  <text>Click Me</text>
</widget>
"""


def test_action_button_with_actions():
    btn = ActionButton(name='Multi Action', text='Actions', pv_name='', x=0, y=0, width=120, height=30)

    # Add various action types
    btn.actions.append(OpenDisplayAction(
        description='Open Screen',
        file='screen.bob',
        target=OpenDisplayTarget.NEW_TAB,
    ))
    btn.actions.append(WritePvAction(description='Write Value', pv_name='MY:PV', value='1'))
    btn.actions.append(CommandAction(description='Run cmd', command='ls -la'))
    btn.actions.append(OpenWebpageAction(description='Open Site', url='https://example.com'))
    btn.actions.append(OpenFileAction(description='Open File', file='/tmp/test.txt'))

    assert len(btn.actions) == 5
    assert isinstance(btn.actions[0], OpenDisplayAction)
    assert btn.actions[0].file == Path('screen.bob')
    assert btn.actions[0].target == OpenDisplayTarget.NEW_TAB
    assert isinstance(btn.actions[1], WritePvAction)
    assert btn.actions[1].pv_name == 'MY:PV'
    assert btn.actions[1].value == '1'
    assert isinstance(btn.actions[2], CommandAction)
    assert btn.actions[2].command == 'ls -la'
    assert isinstance(btn.actions[3], OpenWebpageAction)
    assert btn.actions[3].url == 'https://example.com'
    assert isinstance(btn.actions[4], OpenFileAction)
    assert btn.actions[4].file == Path('/tmp/test.txt')

    assert btn == """<?xml version="1.0" ?>
<widget type="action_button" version="3.0.0">
  <name>Multi Action</name>
  <x>0</x>
  <y>0</y>
  <width>120</width>
  <height>30</height>
  <pv_name/>
  <text>Actions</text>
  <actions>
    <action type="open_display">
      <description>Open Screen</description>
      <file>screen.bob</file>
      <target>tab</target>
      <macros/>
    </action>
    <action type="write_pv">
      <description>Write Value</description>
      <pv_name>MY:PV</pv_name>
      <value>1</value>
    </action>
    <action type="command">
      <description>Run cmd</description>
      <command>ls -la</command>
    </action>
    <action type="open_webpage">
      <description>Open Site</description>
      <url>https://example.com</url>
    </action>
    <action type="open_file">
      <description>Open File</description>
      <file>/tmp/test.txt</file>
    </action>
  </actions>
</widget>
"""

    # Remove actions and verify
    del btn.actions[4]
    del btn.actions[3]
    del btn.actions[2]
    assert len(btn.actions) == 2
    assert isinstance(btn.actions[0], OpenDisplayAction)
    assert isinstance(btn.actions[1], WritePvAction)

    # Remove remaining actions
    del btn.actions[0]
    assert len(btn.actions) == 1
    assert btn.actions[0].description == 'Write Value'

    assert btn == """<?xml version="1.0" ?>
<widget type="action_button" version="3.0.0">
  <name>Multi Action</name>
  <x>0</x>
  <y>0</y>
  <width>120</width>
  <height>30</height>
  <pv_name/>
  <text>Actions</text>
  <actions>
    <action type="write_pv">
      <description>Write Value</description>
      <pv_name>MY:PV</pv_name>
      <value>1</value>
    </action>
  </actions>
</widget>
"""


def test_action_button_with_confirmation():
    btn = ActionButton(name='Danger Btn', text='Delete', pv_name='SYS:DEL', x=0, y=0, width=100, height=30)
    btn.show_confirm_dialog = True
    btn.confirm_message = 'Are you sure?'

    assert btn.show_confirm_dialog
    assert btn.confirm_message == 'Are you sure?'

    assert btn == """<?xml version="1.0" ?>
<widget type="action_button" version="3.0.0">
  <name>Danger Btn</name>
  <x>0</x>
  <y>0</y>
  <width>100</width>
  <height>30</height>
  <pv_name>SYS:DEL</pv_name>
  <text>Delete</text>
  <show_confirm_dialog>true</show_confirm_dialog>
  <confirm_message>Are you sure?</confirm_message>
</widget>
"""


def test_action_button_from_xml():
    btn_xml = """<widget type="action_button" version="3.0.0">
  <name>Btn 1</name>
  <x>5</x>
  <y>5</y>
  <width>120</width>
  <height>35</height>
  <pv_name>SYS:CMD</pv_name>
  <text>Execute</text>
  <actions>
    <action type="write_pv">
      <description>Set Value</description>
      <pv_name>TARGET:PV</pv_name>
      <value>42</value>
    </action>
  </actions>
</widget>"""
    btn = ActionButton.from_element(fromstring(btn_xml))
    assert btn is not None
    assert isinstance(btn, ActionButton)
    assert btn.name == 'Btn 1'
    assert btn.pv_name == 'SYS:CMD'
    assert btn.text == 'Execute'
    assert btn.x == 5
    assert btn.y == 5
    assert len(btn.actions) == 1
    assert isinstance(btn.actions[0], WritePvAction)
    assert btn.actions[0].pv_name == 'TARGET:PV'
    assert btn.actions[0].value == '42'


def test_create_boolean_button_widget():
    btn = BooleanButton(name='Test Bool', pv_name='TEST:TOGGLE', x=10, y=10, width=80, height=40)
    assert btn is not None
    assert btn.name == 'Test Bool'
    assert btn.pv_name == 'TEST:TOGGLE'

    btn.mode = ButtonMode.PUSH
    btn.show_led = True
    btn.on_image = 'on_icon.png'
    btn.off_image = 'off_icon.png'

    assert btn.mode == ButtonMode.PUSH
    assert btn.show_led
    assert btn.on_image == Path('on_icon.png')
    assert btn.off_image == Path('off_icon.png')

    assert btn == """<?xml version="1.0" ?>
<widget type="bool_button" version="2.0.0">
  <name>Test Bool</name>
  <x>10</x>
  <y>10</y>
  <width>80</width>
  <height>40</height>
  <pv_name>TEST:TOGGLE</pv_name>
  <mode>1</mode>
  <show_led>true</show_led>
  <on_image>on_icon.png</on_image>
  <off_image>off_icon.png</off_image>
</widget>
"""


def test_boolean_button_from_xml():
    btn_xml = """<widget type="bool_button" version="2.0.0">
  <name>Bool 1</name>
  <x>0</x>
  <y>0</y>
  <width>100</width>
  <height>30</height>
  <pv_name>MOTOR:ON</pv_name>
  <mode>0</mode>
  <on_image>motor_on.png</on_image>
  <off_image>motor_off.png</off_image>
</widget>"""
    btn = BooleanButton.from_element(fromstring(btn_xml))
    assert btn is not None
    assert isinstance(btn, BooleanButton)
    assert btn.name == 'Bool 1'
    assert btn.pv_name == 'MOTOR:ON'
    assert btn.mode == ButtonMode.TOGGLE
    assert btn.on_image == Path('motor_on.png')
    assert btn.off_image == Path('motor_off.png')


def test_create_checkbox_widget():
    cb = CheckBox(name='Test CB', label='Enable', pv_name='TEST:ENABLE', x=10, y=10, width=100, height=20)
    assert cb is not None
    assert cb.name == 'Test CB'
    assert cb.label == 'Enable'
    assert cb.pv_name == 'TEST:ENABLE'

    cb.auto_size = True
    cb.foreground_color = Color((50, 50, 50))

    assert cb.auto_size
    assert cb.foreground_color == Color((50, 50, 50))

    assert cb == """<?xml version="1.0" ?>
<widget type="checkbox" version="2.0.0">
  <name>Test CB</name>
  <x>10</x>
  <y>10</y>
  <width>100</width>
  <height>20</height>
  <pv_name>TEST:ENABLE</pv_name>
  <label>Enable</label>
  <auto_size>true</auto_size>
  <foreground_color>
    <color red="50" green="50" blue="50" alpha="255"/>
  </foreground_color>
</widget>
"""


def test_checkbox_from_xml():
    cb_xml = """<widget type="checkbox" version="2.0.0">
  <name>CB 1</name>
  <x>5</x>
  <y>5</y>
  <width>80</width>
  <height>20</height>
  <pv_name>FLAG:PV</pv_name>
  <label>Active</label>
</widget>"""
    cb = CheckBox.from_element(fromstring(cb_xml))
    assert cb is not None
    assert isinstance(cb, CheckBox)
    assert cb.name == 'CB 1'
    assert cb.pv_name == 'FLAG:PV'
    assert cb.label == 'Active'


def test_create_choice_button_widget():
    choice = ChoiceButton(name='Test Choice', pv_name='TEST:SEL', x=10, y=10, width=200, height=30)
    assert choice is not None
    assert choice.name == 'Test Choice'
    assert choice.pv_name == 'TEST:SEL'

    choice.items.append('Option A')
    choice.items.append('Option B')
    choice.items.append('Option C')
    choice.items_from_pv = False
    choice.selected_color = Color((0, 100, 200))

    assert len(choice.items) == 3
    assert not choice.items_from_pv
    assert choice.selected_color == Color((0, 100, 200))

    assert choice == """<?xml version="1.0" ?>
<widget type="choice" version="2.0.0">
  <name>Test Choice</name>
  <x>10</x>
  <y>10</y>
  <width>200</width>
  <height>30</height>
  <pv_name>TEST:SEL</pv_name>
  <items>
    <item>Option A</item>
    <item>Option B</item>
    <item>Option C</item>
  </items>
  <items_from_pv>false</items_from_pv>
  <selected_color>
    <color red="0" green="100" blue="200" alpha="255"/>
  </selected_color>
</widget>
"""


def test_choice_button_from_xml():
    choice_xml = """<widget type="choice" version="2.0.0">
  <name>Choice 1</name>
  <x>0</x>
  <y>0</y>
  <width>150</width>
  <height>25</height>
  <pv_name>MODE:PV</pv_name>
  <items>
    <item>Manual</item>
    <item>Auto</item>
  </items>
</widget>"""
    choice = ChoiceButton.from_element(fromstring(choice_xml))
    assert choice is not None
    assert isinstance(choice, ChoiceButton)
    assert choice.name == 'Choice 1'
    assert choice.pv_name == 'MODE:PV'
    assert len(choice.items) == 2
    assert choice.items[0] == 'Manual'
    assert choice.items[1] == 'Auto'


def test_create_combo_box_widget():
    combo = ComboBox(name='Test Combo', pv_name='TEST:SEL', x=10, y=10, width=150, height=25)
    assert combo is not None
    assert combo.name == 'Test Combo'
    assert combo.pv_name == 'TEST:SEL'

    combo.items.append('Item 1')
    combo.items.append('Item 2')
    combo.editable = True

    assert len(combo.items) == 2
    assert combo.editable

    assert combo == """<?xml version="1.0" ?>
<widget type="combo" version="2.0.0">
  <name>Test Combo</name>
  <x>10</x>
  <y>10</y>
  <width>150</width>
  <height>25</height>
  <pv_name>TEST:SEL</pv_name>
  <items>
    <item>Item 1</item>
    <item>Item 2</item>
  </items>
  <editable>true</editable>
</widget>
"""


def test_combo_box_from_xml():
    combo_xml = """<widget type="combo" version="2.0.0">
  <name>Combo 1</name>
  <x>0</x>
  <y>0</y>
  <width>120</width>
  <height>25</height>
  <pv_name>SEL:PV</pv_name>
  <items_from_pv>true</items_from_pv>
</widget>"""
    combo = ComboBox.from_element(fromstring(combo_xml))
    assert combo is not None
    assert isinstance(combo, ComboBox)
    assert combo.name == 'Combo 1'
    assert combo.pv_name == 'SEL:PV'
    assert combo.items_from_pv


def test_create_file_selector_widget():
    fs = FileSelector(name='Test FS', pv_name='TEST:FILE', x=10, y=10, width=200, height=30)
    assert fs is not None
    assert fs.name == 'Test FS'
    assert fs.pv_name == 'TEST:FILE'

    assert fs == """<?xml version="1.0" ?>
<widget type="fileselector" version="2.0.0">
  <name>Test FS</name>
  <x>10</x>
  <y>10</y>
  <width>200</width>
  <height>30</height>
  <pv_name>TEST:FILE</pv_name>
</widget>
"""


def test_file_selector_from_xml():
    fs_xml = """<widget type="fileselector" version="2.0.0">
  <name>FS 1</name>
  <x>5</x>
  <y>5</y>
  <width>250</width>
  <height>30</height>
  <pv_name>PATH:PV</pv_name>
</widget>"""
    fs = FileSelector.from_element(fromstring(fs_xml))
    assert fs is not None
    assert isinstance(fs, FileSelector)
    assert fs.name == 'FS 1'
    assert fs.pv_name == 'PATH:PV'


def test_create_radio_button_widget():
    radio = RadioButton(name='Test Radio', pv_name='TEST:SEL', x=10, y=10, width=100, height=80)
    assert radio is not None
    assert radio.name == 'Test Radio'
    assert radio.pv_name == 'TEST:SEL'

    radio.items.append('Choice 1')
    radio.items.append('Choice 2')
    radio.items.append('Choice 3')
    radio.items_from_pv = False

    assert len(radio.items) == 3
    assert not radio.items_from_pv

    assert radio == """<?xml version="1.0" ?>
<widget type="radio" version="2.0.0">
  <name>Test Radio</name>
  <x>10</x>
  <y>10</y>
  <width>100</width>
  <height>80</height>
  <pv_name>TEST:SEL</pv_name>
  <items>
    <item>Choice 1</item>
    <item>Choice 2</item>
    <item>Choice 3</item>
  </items>
  <items_from_pv>false</items_from_pv>
</widget>
"""


def test_radio_button_from_xml():
    radio_xml = """<widget type="radio" version="2.0.0">
  <name>Radio 1</name>
  <x>0</x>
  <y>0</y>
  <width>120</width>
  <height>60</height>
  <pv_name>OPT:PV</pv_name>
  <items>
    <item>Low</item>
    <item>High</item>
  </items>
</widget>"""
    radio = RadioButton.from_element(fromstring(radio_xml))
    assert radio is not None
    assert isinstance(radio, RadioButton)
    assert radio.name == 'Radio 1'
    assert radio.pv_name == 'OPT:PV'
    assert len(radio.items) == 2
    assert radio.items[0] == 'Low'
    assert radio.items[1] == 'High'


def test_create_scaled_slider_widget():
    slider = ScaledSlider(name='Test Slider', pv_name='TEST:SETPOINT', x=10, y=10, width=300, height=50)
    assert slider is not None
    assert slider.name == 'Test Slider'
    assert slider.pv_name == 'TEST:SETPOINT'

    slider.show_scale = True
    slider.limits_from_pv = True
    slider.increment = 0.1
    slider.level_high = 80.0
    slider.level_hihi = 90.0
    slider.level_low = 20.0
    slider.level_lolo = 10.0
    slider.show_high = True
    slider.show_hihi = True
    slider.show_low = True
    slider.show_lolo = True

    assert slider.show_scale
    assert slider.limits_from_pv
    assert slider.increment == 0.1
    assert slider.level_high == 80.0
    assert slider.level_hihi == 90.0
    assert slider.level_low == 20.0
    assert slider.level_lolo == 10.0

    assert slider == """<?xml version="1.0" ?>
<widget type="scaledslider" version="2.0.0">
  <name>Test Slider</name>
  <x>10</x>
  <y>10</y>
  <width>300</width>
  <height>50</height>
  <pv_name>TEST:SETPOINT</pv_name>
  <show_scale>true</show_scale>
  <limits_from_pv>true</limits_from_pv>
  <increment>0.1</increment>
  <level_high>80.0</level_high>
  <level_hihi>90.0</level_hihi>
  <level_low>20.0</level_low>
  <level_lolo>10.0</level_lolo>
  <show_high>true</show_high>
  <show_hihi>true</show_hihi>
  <show_low>true</show_low>
  <show_lolo>true</show_lolo>
</widget>
"""


def test_scaled_slider_from_xml():
    slider_xml = """<widget type="scaledslider" version="2.0.0">
  <name>Slider 1</name>
  <x>0</x>
  <y>0</y>
  <width>250</width>
  <height>40</height>
  <pv_name>MOTOR:SP</pv_name>
  <limits_from_pv>true</limits_from_pv>
  <show_scale>true</show_scale>
</widget>"""
    slider = ScaledSlider.from_element(fromstring(slider_xml))
    assert slider is not None
    assert isinstance(slider, ScaledSlider)
    assert slider.name == 'Slider 1'
    assert slider.pv_name == 'MOTOR:SP'
    assert slider.limits_from_pv
    assert slider.show_scale


def test_create_scrollbar_widget():
    sb = Scrollbar(name='Test SB', pv_name='TEST:POS', x=10, y=10, width=200, height=20)
    assert sb is not None
    assert sb.name == 'Test SB'
    assert sb.pv_name == 'TEST:POS'

    sb.minimum = 0.0
    sb.maximum = 100.0
    sb.bar_length = 10.0

    assert sb.minimum == 0.0
    assert sb.maximum == 100.0
    assert sb.bar_length == 10.0

    assert sb == """<?xml version="1.0" ?>
<widget type="scrollbar" version="2.0.0">
  <name>Test SB</name>
  <x>10</x>
  <y>10</y>
  <width>200</width>
  <height>20</height>
  <pv_name>TEST:POS</pv_name>
  <minimum>0.0</minimum>
  <maximum>100.0</maximum>
  <bar_length>10.0</bar_length>
</widget>
"""


def test_scrollbar_from_xml():
    sb_xml = """<widget type="scrollbar" version="2.0.0">
  <name>SB 1</name>
  <x>5</x>
  <y>5</y>
  <width>180</width>
  <height>20</height>
  <pv_name>SCROLL:PV</pv_name>
  <minimum>0.0</minimum>
  <maximum>50.0</maximum>
</widget>"""
    sb = Scrollbar.from_element(fromstring(sb_xml))
    assert sb is not None
    assert isinstance(sb, Scrollbar)
    assert sb.name == 'SB 1'
    assert sb.pv_name == 'SCROLL:PV'
    assert sb.minimum == 0.0
    assert sb.maximum == 50.0


def test_create_slide_button_widget():
    slide = SlideButton(name='Test Slide', label='Power', pv_name='TEST:PWR', x=10, y=10, width=80, height=30)
    assert slide is not None
    assert slide.name == 'Test Slide'
    assert slide.label == 'Power'
    assert slide.pv_name == 'TEST:PWR'

    slide.on_color = Color((0, 255, 0))
    slide.off_color = Color((255, 0, 0))

    assert slide.on_color == Color((0, 255, 0))
    assert slide.off_color == Color((255, 0, 0))

    assert slide == """<?xml version="1.0" ?>
<widget type="slide_button" version="2.0.0">
  <name>Test Slide</name>
  <x>10</x>
  <y>10</y>
  <width>80</width>
  <height>30</height>
  <pv_name>TEST:PWR</pv_name>
  <label>Power</label>
  <on_color>
    <color red="0" green="255" blue="0" alpha="255"/>
  </on_color>
  <off_color>
    <color red="255" green="0" blue="0" alpha="255"/>
  </off_color>
</widget>
"""


def test_slide_button_from_xml():
    slide_xml = """<widget type="slide_button" version="2.0.0">
  <name>Slide 1</name>
  <x>0</x>
  <y>0</y>
  <width>60</width>
  <height>25</height>
  <pv_name>SW:ON</pv_name>
  <label>Switch</label>
</widget>"""
    slide = SlideButton.from_element(fromstring(slide_xml))
    assert slide is not None
    assert isinstance(slide, SlideButton)
    assert slide.name == 'Slide 1'
    assert slide.pv_name == 'SW:ON'
    assert slide.label == 'Switch'


def test_create_spinner_widget():
    spinner = Spinner(name='Test Spinner', pv_name='TEST:VAL', x=10, y=10, width=100, height=30)
    assert spinner is not None
    assert spinner.name == 'Test Spinner'
    assert spinner.pv_name == 'TEST:VAL'

    spinner.minimum = 0.0
    spinner.maximum = 100.0
    spinner.increment = 1.0
    spinner.limits_from_pv = True
    spinner.buttons_on_left = True

    assert spinner.minimum == 0.0
    assert spinner.maximum == 100.0
    assert spinner.increment == 1.0
    assert spinner.limits_from_pv
    assert spinner.buttons_on_left

    assert spinner == """<?xml version="1.0" ?>
<widget type="spinner" version="2.0.0">
  <name>Test Spinner</name>
  <x>10</x>
  <y>10</y>
  <width>100</width>
  <height>30</height>
  <pv_name>TEST:VAL</pv_name>
  <minimum>0.0</minimum>
  <maximum>100.0</maximum>
  <increment>1.0</increment>
  <limits_from_pv>true</limits_from_pv>
  <buttons_on_left>true</buttons_on_left>
</widget>
"""


def test_spinner_from_xml():
    spinner_xml = """<widget type="spinner" version="2.0.0">
  <name>Spinner 1</name>
  <x>0</x>
  <y>0</y>
  <width>80</width>
  <height>25</height>
  <pv_name>COUNT:PV</pv_name>
  <minimum>0.0</minimum>
  <maximum>10.0</maximum>
  <increment>0.5</increment>
</widget>"""
    spinner = Spinner.from_element(fromstring(spinner_xml))
    assert spinner is not None
    assert isinstance(spinner, Spinner)
    assert spinner.name == 'Spinner 1'
    assert spinner.pv_name == 'COUNT:PV'
    assert spinner.minimum == 0.0
    assert spinner.maximum == 10.0
    assert spinner.increment == 0.5


def test_create_text_entry_widget():
    te = TextEntry(name='Test TE', pv_name='TEST:INPUT', x=10, y=10, width=200, height=25)
    assert te is not None
    assert te.name == 'Test TE'
    assert te.pv_name == 'TEST:INPUT'

    te.multi_line = True
    te.wrap_words = True
    te.format = Format.DECIMAL
    te.precision = 3
    te.show_units = True

    assert te.multi_line
    assert te.wrap_words
    assert te.format == Format.DECIMAL
    assert te.precision == 3
    assert te.show_units

    assert te == """<?xml version="1.0" ?>
<widget type="textentry" version="2.0.0">
  <name>Test TE</name>
  <x>10</x>
  <y>10</y>
  <width>200</width>
  <height>25</height>
  <pv_name>TEST:INPUT</pv_name>
  <multi_line>true</multi_line>
  <wrap_words>true</wrap_words>
  <format>1</format>
  <precision>3</precision>
  <show_units>true</show_units>
</widget>
"""


def test_text_entry_from_xml():
    te_xml = """<widget type="textentry" version="2.0.0">
  <name>TE 1</name>
  <x>5</x>
  <y>5</y>
  <width>150</width>
  <height>25</height>
  <pv_name>ENTRY:PV</pv_name>
  <multi_line>true</multi_line>
</widget>"""
    te = TextEntry.from_element(fromstring(te_xml))
    assert te is not None
    assert isinstance(te, TextEntry)
    assert te.name == 'TE 1'
    assert te.pv_name == 'ENTRY:PV'
    assert te.multi_line


def test_create_thumbwheel_widget():
    tw = Thumbwheel(name='Test TW', pv_name='TEST:SET', x=10, y=10, width=150, height=40)
    assert tw is not None
    assert tw.name == 'Test TW'
    assert tw.pv_name == 'TEST:SET'

    assert tw == """<?xml version="1.0" ?>
<widget type="thumbwheel" version="2.0.0">
  <name>Test TW</name>
  <x>10</x>
  <y>10</y>
  <width>150</width>
  <height>40</height>
  <pv_name>TEST:SET</pv_name>
</widget>
"""


def test_thumbwheel_from_xml():
    tw_xml = """<widget type="thumbwheel" version="2.0.0">
  <name>TW 1</name>
  <x>0</x>
  <y>0</y>
  <width>120</width>
  <height>35</height>
  <pv_name>DIAL:PV</pv_name>
</widget>"""
    tw = Thumbwheel.from_element(fromstring(tw_xml))
    assert tw is not None
    assert isinstance(tw, Thumbwheel)
    assert tw.name == 'TW 1'
    assert tw.pv_name == 'DIAL:PV'
