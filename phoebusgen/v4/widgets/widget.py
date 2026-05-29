import re
from enum import Enum
from typing import List, Optional, Sequence, Type, TypeVar, Union
from xml.etree.ElementTree import Element

from phoebusgen.v4.properties.behavior import HasActionsRulesAndScripts, HasToolTip
from phoebusgen.v4.properties.display import HasVisible
from phoebusgen.v4.properties.position import HasPosition
from phoebusgen.v4.properties.property_helpers import PropertyBase
from phoebusgen.v4.properties.types import ObservableList
from phoebusgen.v4.properties.widget import HasName
from phoebusgen.v4.utils import PhoebusElement, prettify_xml

# Populated at runtime on import of phoebusgen.v4
widget_versions = {}


class WidgetType(str, Enum):
    """Enum of Phoebus Widget types."""

    # Graphics
    ARC = 'arc'
    ELLIPSE = 'ellipse'
    LABEL = 'label'
    PICTURE = 'picture'
    POLYGON = 'polygon'
    POLYLINE = 'polyline'
    RECTANGLE = 'rectangle'

    # Monitors
    BYTE_MONITOR = 'byte_monitor'
    LED = 'led'
    LEDMULTI_STATE = 'multi_state_led'
    METER = 'meter'
    PROGRESS_BAR = 'progressbar'
    LINEAR_METER = 'linearmeter'
    SYMBOL = 'symbol'
    TABLE = 'table'
    TANK = 'tank'
    TEXT_SYMBOL = 'text-symbol'
    TEXT_UPDATE = 'textupdate'
    THERMOMETER = 'thermometer'

    # Controls
    ACTION_BUTTON = 'action_button'
    BOOLEAN_BUTTON = 'bool_button'
    CHECK_BOX = 'checkbox'
    CHOICE_BUTTON = 'choice'
    COMBO_BOX = 'combo'
    FILE_SELECTOR = 'fileselector'
    RADIO_BUTTON = 'radio'
    SCALED_SLIDER = 'scaledslider'
    SCROLLBAR = 'scrollbar'
    SLIDE_BUTTON = 'slide_button'
    SPINNER = 'spinner'
    TEXT_ENTRY = 'textentry'
    THUMBWHEEL = 'thumbwheel'

    # Plots
    DATA_BROWSER = 'databrowser'
    IMAGE = 'image'
    STRIP_CHART = 'stripchart'
    XYPLOT = 'xyplot'

    # Structure
    ARRAY = 'array'
    TABS = 'tabs'
    EMBEDDED_DISPLAY = 'embedded'
    GROUP = 'group'
    NAVIGATION_TABS = 'navtabs'
    TEMPLATE_INSTANCE = 'template'

    # Miscellaneous
    THREE_DVIEWER = '3dviewer'
    WEB_BROWSER = 'webbrowser'


def _widget_type_from_class_name(class_name: str) -> WidgetType:
    """Convert a CamelCase class name to its corresponding WidgetType enum member.

    Inserts underscores between lowercase-uppercase boundaries and uppercases the result.
    e.g. 'TextUpdate' -> 'TEXT_UPDATE' -> WidgetType.TEXT_UPDATE

    :param class_name: CamelCase class name
    :return: Corresponding WidgetType enum member
    :raises KeyError: If no matching WidgetType member exists
    """

    enum_key = re.sub(r'([a-z])([A-Z])', r'\1_\2', class_name).upper()
    return WidgetType[enum_key]


WidgetT = TypeVar('WidgetT', bound='Widget')
PropertyT = TypeVar('PropertyT', bound=PropertyBase)


class HasParent:
    parent: Optional['HasWidgets'] = None

class Widget(PhoebusElement, HasParent, HasVisible, HasName, HasPosition, HasActionsRulesAndScripts, HasToolTip):
    """Base Class for all Phoebus widgets."""

    def __init__(self, name: str, x_pos: int, y_pos: int, width: int, height: int) -> None:
        """
        Base Class for all Phoebus widgets

        :param w_type: Widget type to be written into XML
        :param name: Widget name
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height:
        """

        root = Element('widget')
        PhoebusElement.__init__(self, root)

        if type(self) is Widget:
            raise ValueError('Widget is an abstract base class and cannot be instantiated directly!')

        # Use the name of the class to determine the widget type attribute in the XML. i.e. TextUpdate -> textupdate
        self._widget_type: WidgetType = _widget_type_from_class_name(type(self).__name__)

        self.root.attrib['type'] = self._widget_type.value
        if self._widget_type in widget_versions:
            self.root.attrib['version'] = widget_versions[self._widget_type.value]
        else:
            self.root.attrib['version'] = '2.0.0'

        self.name = name
        self.x = x_pos
        self.y = y_pos
        self.width = width
        self.height = height

    @classmethod
    def from_element(cls: Type[WidgetT], element: Element) -> WidgetT:
        """Convert an XML element into a Widget instance.

        Chooses the appropriate subclass based on the 'type' attribute of the element.

        :param cls: Description
        :param element: Description
        :type element: Element
        :return: Description
        :rtype: Widget
        """

        if element.tag != 'widget':
            raise ValueError(f"Expected 'widget' element, got '{element.tag}'")

        w_type = element.attrib.get('type', None)
        if w_type is None:
            raise ValueError('Widget type attribute missing!')

        if w_type not in [t.value for t in WidgetType]:
            raise ValueError(f"Widget type '{w_type}' is not a valid widget type!")


        # If using the Widget class directly, try to find the correct subclass based on the type attribute
        instance_cls = cls
        if instance_cls == Widget:
            for subcls in Widget.__subclasses__():
                try:
                    subcls_type = _widget_type_from_class_name(subcls.__name__)
                    if subcls_type.value == w_type:
                        instance_cls = subcls
                        break
                except (KeyError, ValueError):
                    continue

        expected_type = _widget_type_from_class_name(instance_cls.__name__)
        if w_type != expected_type.value:
            raise ValueError(f"Expected widget type '{expected_type.value}', got '{w_type}'")

        instance = instance_cls.__new__(instance_cls)
        instance.root = element
        return instance

    @property
    def version(self) -> str:
        """Get widget version from root widget.

        :return: Version string
        """
        return self.root.attrib.get('version', '2.0.0')

    @version.setter
    def version(self, version: str) -> None:
        """Change widget version in root widget.

        i.e. <widget type="textupdate" version="2.0.0">

        :param version: Version string
        """
        self.root.attrib['version'] = version

    def has_property(self, prop_name: str) -> bool:
        """Check if widget has a prop_name.

        :param prop_name: Property name to check for
        :return: True if property exists, False if not
        """
        return hasattr(self, prop_name)

    def has_property_class(self, prop_class: type) -> bool:
        """Check if widget has a property of type prop_class.

        :param prop_class: Property class to check for
        :return: True if property class exists, False if not
        """
        return isinstance(self, prop_class)

    def __str__(self):
        return prettify_xml(self.root)

    def __repr__(self):
        return prettify_xml(self.root)


class HasWidgets(PhoebusElement, PropertyBase):

    widgets: ObservableList[Widget]

    def __init__(self, widgets_tag_name: Optional[str] = None) -> None:
        """Interface for widgets that contain other widgets.

        :param widgets_tag_name: Optional tag name for the XML element that contains the child widgets. If not provided, defaults to 'widgets'.
        """

        self._override_property_tag_name('widgets', widgets_tag_name)


    def get_widgets_by_type(self, widget_type: Type[WidgetT]) -> List[WidgetT]:
        """Get a list of widgets contained within the container that are of type widget_type.

        :param widget_type: Widget type to filter by
        :return: List of Widget instances of type widget_type contained within the container
        :rtype: List[WidgetT]
        """

        return [w for w in self.widgets if isinstance(w, widget_type)]


    def get_widgets_by_property_class(self, prop_type: Type[PropertyT]) -> List[PropertyT]:
        """Get a list of widgets contained within the container that have a property of type prop_type.

        :param prop_type: Property type to filter by
        :return: List of Widget instances that have a property of type prop_type
        :rtype: List[PropertyT]
        """
        return [w for w in self.widgets if isinstance(w, prop_type)]


    def get_widgets_by_property(self, property_name: str) -> List[Widget]:
        """Get a list of widgets contained within the container that have a property named property_name.

        :param property_name: Name of property to filter by
        :return: List of Widget instances that have a property named property_name
        :rtype: List[Widget]
        """

        widgets_with_property = []
        for widget in self.widgets:
            if hasattr(widget, property_name):
                widgets_with_property.append(widget)
        return widgets_with_property


    # For BC, we keep the two below methods
    def add_widget(self, elem: Union[Widget, Sequence[Widget]]) -> None:
        """Add widget or list of widgets to screen.

        :param elem: <list/Phoebusgen.widget> List of Phoebusgen.widget's or a single widget to add
        """

        if isinstance(elem, Sequence):
            for e in elem:
                e.parent = self
                self.widgets.append(e)
        else:
            elem.parent = self
            self.widgets.append(elem)

    def get_widgets(self) -> List[Widget]:
        """Get a list of all widgets contained within the container.

        Widgets are returned in the order they appear in the XML,
        which is the order they are rendered in Phoebus (i.e. widgets later
        in the XML will be rendered on top of widgets earlier in the XML).

         :return: List of Widget instances for each widget element contained within the container
         :rtype: List[Widget]
         """

        return self.widgets


    def get_all_widgets(self) -> List[Widget]:
        """Get a list of all widgets contained within the container, including nested widgets.

        :return: List of all Widget instances contained within the container
        :rtype: List[Widget]
        """

        # Nest import to avoid circular import
        from .structure import Tabs

        all_widgets = []
        for widget in self.widgets:
            all_widgets.append(widget)
            if isinstance(widget, HasWidgets):
                all_widgets.extend(widget.get_all_widgets())
            elif isinstance(widget, Tabs):
                for tab in widget.tabs:
                    all_widgets.extend(tab.get_all_widgets())
        return all_widgets


    def remove_widget(self, widget: Widget) -> None:
        """Remove a widget from the container by reference.

        :param widget: The widget instance to remove
        """

        self.widgets = [w for w in self.widgets if w.root is not widget.root]


# Wrap the metaclass-generated widgets property to set parent on each widget
# when the list is read (e.g. from XML via from_element).
_widgets_prop = HasWidgets.widgets
_widgets_fget = _widgets_prop.fget
_widgets_fset = _widgets_prop.fset


def _widgets_getter_with_parent(self):
    widgets = _widgets_fget(self)
    for w in widgets:
        w.parent = self
    return widgets


HasWidgets.widgets = property(_widgets_getter_with_parent, _widgets_fset)
