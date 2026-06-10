""" phoebusgen.widgets Module

This module contains Python class representations of each widget. Widgets can be created
by calling the widget class constructor, i.e. phoebusgen.widget.TextUpdate(...) or
phoebusgen.widget.ScaledSlider(...). Once the class is created and assigned to a Python
variable, additional methods to change widget properties are available.

Example:
    >>> import phoebusgen
    >>> text_update_widget = phoebusgen.widgets.TextUpdate('test widget', 'TEST:PV', 10, 20, 20, 50)
    >>> text_update_widget.predefined_foreground_color(phoebusgen.colors.OK)
    >>> text_update_widget.font_style_bold()
    >>> print(text_update_widget)
    <?xml version="1.0" ?>
    <widget type="textupdate" version="2.0.0">
      <name>test widget</name>
      <x>10</x>
      <y>20</y>
      <width>20</width>
      <height>50</height>
      <pv_name>TEST:PV</pv_name>
      <foreground_color>
        <color name="OK" red="0" green="255" blue="0" alpha="255"/>
      </foreground_color>
      <font>
        <font family="Liberation Sans" size="14" style="BOLD"/>
      </font>
    </widget>
"""

from .controls import (
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
from .graphics import (
    Arc,
    Ellipse,
    Label,
    Picture,
    Polygon,
    Polyline,
    Rectangle,
)
from .misc import ThreeDViewer, WebBrowser
from .monitors import (
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
from .plots import (
    DataBrowser,
    Image,
    StripChart,
    XYPlot,
)
from .structure import (
    Array,
    EmbeddedDisplay,
    Group,
    NavigationTabs,
    Tab,
    Tabs,
    TemplateInstance,
)
from .widget import HasWidgets, Widget, WidgetType, widget_versions

# from .plots import (
#     XYPlot,
#     Image,
#     StripChart,
#     DataBrowser
# )

__all__ = [
    # Widget Base Classes
    'WidgetType',
    'Widget',

    'HasWidgets',
    'widget_versions',
    # Graphics widgets
    'Arc',
    'Ellipse',
    'Polygon',
    'Polyline',
    'Rectangle',
    'Label',
    'Picture',
    # Misc widgets
    'WebBrowser',
    'ThreeDViewer',
    # Monitor widgets
    'ByteMonitor',
    'LED',
    'LEDMultiState',
    'Meter',
    'ProgressBar',
    'Symbol',
    'Table',
    'Tank',
    'TextSymbol',
    'TextUpdate',
    'Thermometer',
    'LinearMeter',
    # Control widgets
    'ActionButton',
    'CheckBox',
    'ComboBox',
    'RadioButton',
    'ScaledSlider',
    'TextEntry',
    'ChoiceButton',
    'BooleanButton',
    'FileSelector',
    'Spinner',
    'Scrollbar',
    'SlideButton',
    'Thumbwheel',
    # Structure widgets
    'Tab',
    'Tabs',
    'Group',
    'NavigationTabs',
    'Array',
    'EmbeddedDisplay',
    'TemplateInstance',
    # Plot widgets
    'XYPlot',
    'Image',
    'StripChart',
    'DataBrowser'
]
