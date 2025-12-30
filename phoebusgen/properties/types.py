from enum import Enum
from dataclasses import dataclass, field
from xml.etree.ElementTree import Element
from abc import ABC
from collections.abc import MutableMapping, MutableSequence
from typing import Any, Callable, Generic, TypeVar, get_args

Primitive = int | float | str | bool

class Color(tuple):

    def __new__(cls, color: tuple[int, int, int] | tuple[int, int, int, int] | str):
        red = 0
        green = 0
        blue = 0
        alpha = 255
        if isinstance(color, tuple):
            if len(color) < 3:
                raise ValueError("Color tuple must be of length 3 (RGB) or 4 (RGBA)")
            red = color[0]
            green = color[1]
            blue = color[2]
            if len(color) == 3:
                alpha = 255
            else:
                alpha = color[3]
        elif isinstance(color, str) and color.startswith("#"):
            red = int(color[1:3], 16)
            green = int(color[3:5], 16)
            blue = int(color[5:7], 16)
        # TODO: support predefined colors
        # elif color in predefined_colors:
        #     color_attrib = predefined_colors[color]
        #     self.red = int(color_attrib['red'])
        #     self.green = int(color_attrib['green'])
        #     self.blue = int(color_attrib['blue'])
        #     self.alpha = int(color_attrib['alpha'])
        else:
            raise ValueError("Invalid color format! Must be RGB/RGBA tuple or HEX string.")
        
        color_tuple = (red, green, blue)
        if alpha != 255:
            color_tuple += (alpha,)
        return super().__new__(cls, tuple(color_tuple))

    def as_hex(self) -> str:
        if len(self) == 3:
            return "#{:02X}{:02X}{:02X}".format(self[0], self[1], self[2])
        elif len(self) == 4:
            return "#{:02X}{:02X}{:02X}{:02X}".format(self[0], self[1], self[2], self[3])
        else:
            raise ValueError("Color tuple must be of length 3 (RGB) or 4 (RGBA)")

class FontStyle(Enum):
    REGULAR = "REGULAR"
    ITALIC = "ITALIC"
    BOLD = "BOLD"
    BOLD_AND_ITALIC = "BOLD_ITALIC"




class HorizontalAlignment(Enum):
    LEFT = 0
    CENTER = 1
    RIGHT = 2

class VerticalAlignment(Enum):
    TOP = 0
    MIDDLE = 1
    BOTTOM = 2

class RotationStep(Enum):
    ZERO = 0
    NINETY = 1
    ONE_HUNDRED_EIGHTY = 2
    NEGATIVE_NINETY = 3

class ButtonMode(Enum):
    TOGGLE = 0
    PUSH = 1
    PUSH_INVERTED = 2

class InterpolationType(Enum):
    NONE = 0
    INTERPOLATE = 1
    AUTOMATIC = 2

class ColorMode(Enum):
    TYPE_CUSTOM = 0
    TYPE_MONO = 1
    TYPE_BAYER = 2
    TYPE_RGB1 = 3
    TYPE_RGB2 = 4
    TYPE_RGB3 = 5
    TYPE_YUV444 = 6
    TYPE_YUV422 = 7
    TYPE_YUV411 = 8
    TYPE_3BYTE_BGR = 9
    TYPE_4BYTE_ABGR = 10
    TYPE_4BYTE_ABGR_PRE = 11
    TYPE_BYTE_BINARY = 12
    TYPE_BYTE_GRAY = 13
    TYPE_BYTE_INDEXED = 14
    TYPE_INT_ARGB = 15
    TYPE_INT_ARGB_PRE = 16
    TYPE_INT_BGR = 17
    TYPE_INT_RGB = 18
    TYPE_USHORT_555_RGB = 19
    TYPE_USHORT_565_RGB = 20
    TYPE_USHORT_GRAY = 21

class GroupStyle(Enum):
    GROUP_BOX = 0
    TITLE_BAR = 1
    LINE = 2
    NONE = 3

class ResizeSetting(Enum):
    NO_RESIZE = 0
    SIZE_CONTENT_TO_FIT_WIDGET = 1
    SIZE_WIDGET_TO_MATCH_CONTENT = 2
    STRETCH_CONTENT_TO_FIT_WIDGET = 3
    CROP_CONTENT = 4

class FileComponent(Enum):
    FULL_PATH = 0
    DIRECTORY = 1
    NAME_AND_EXTENSION = 2
    BASE_NAME = 3

class TraceType(Enum):
    NONE = 0
    LINE = 1
    STEP = 2
    ERR_BARS = 3
    LINE_ERR_BARS = 4
    BARS = 5

class LineStyle(Enum):
    SOLID = 0
    DASHED = 1
    DOT = 2
    DASH_DOT = 3
    DASH_DOT_DOT = 4

class PointType(Enum):
    NONE = 0
    SQUARES = 1
    CIRCLES = 2
    DIAMONDS = 3
    X = 4
    TRIANGLES = 5

class ColorMap(Enum):
    VIRIDIS = "VIRIDIS"
    GRAYSCALE = "GRAY"
    JET = "JET"
    COLOR_SPECTRUM = "SPECTRUM"
    HOT = "HOT"
    COOL = "COOL"
    SHADED = "SHADED"
    MAGMA = "MAGMA"

class ArrowTypes(Enum):
    NONE = "None"
    FROM = "From"
    TO = "To"
    BOTH = "Both"

class TabDirection(Enum):
    HORIZONTAL = 0
    VERTICAL = 1

class OpenDisplayTarget(Enum):
    REPLACE = "replace"
    NEW_TAB = "tab"
    NEW_WINDOW = "window"

class ObservableDict(MutableMapping):
    def __init__(self, *args, **kwargs):
        self._dict = dict(*args, **kwargs)
        self._on_change_callback = None

    def _notify_change(self):
        if self._on_change_callback:
            self._on_change_callback(self)

    def __setitem__(self, key, value):
        self._dict[key] = value
        self._notify_change()

    def __len__(self):
        return len(self._dict)
    
    def __getitem__(self, key):
        return self._dict[key]

    def __iter__(self):
        return iter(self._dict)

    def __delitem__(self, key):
        del self._dict[key]
        self._notify_change()

    def clear(self):
        self._dict.clear()
        self._notify_change()

    def pop(self, key, default=None):
        result = self._dict.pop(key, default)
        self._notify_change()
        return result
    
    def update(self, *args, **kwargs):
        # A simple update notification; a more detailed one would iterate
        self._dict.update(*args, **kwargs)
        self._notify_change()

    def __repr__(self):
        return repr(self._dict)

    def __eq__(self, other):
        return self._dict.__eq__(other)


@dataclass
class ObservableDataclass:

    _on_change_callback: Callable[[Any], None] | None = field(init=False, default=None, repr=False)
    _attrib_fields: list[str] = field(init=False, default_factory=list, repr=False)

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)
        if name != "_on_change_callback" and self._on_change_callback:
            self._on_change_callback(self)

    @classmethod
    def fields(cls):
        fields = {}
        for field in cls.__dataclass_fields__:
            if not field.startswith("_"):
                fields[field] = cls.__dataclass_fields__[field]
        return fields

    def __eq__(self, other):
        for field in self.fields():
            if getattr(self, field) != getattr(other, field):
                return False
        return True

ValidListType = Primitive | Enum | ObservableDataclass
ValidListTypeT = TypeVar('ValidListTypeT', bound=ValidListType)

class ObservableList(MutableSequence, Generic[ValidListTypeT]):
    def __init__(self, *args, **kwargs):
        self._list = list(*args, **kwargs)
        self._on_change_callback = None


    def __getitem__(self, i):
        return self._list[i]

    def __len__(self):
        return len(self._list)

    def __delitem__(self, i):
        self._list.__delitem__(i)
        self._notify_change()

    def __setitem__(self, i, val):
        self._list.__setitem__(i, val)
        self._notify_change()

    def insert(self, index, value):
        self._list.insert(index, value)
        self._notify_change()

    def __repr__(self):
        return repr(self._list)

    def __eq__(self, value):
        return self._list.__eq__(value)

    # Other modifying methods like append, pop, extend are provided by MutableSequence 
    # and will call insert or __delitem__, triggering the callback implicitly.

    def _notify_change(self):
        if self._on_change_callback:
            self._on_change_callback(self)


@dataclass
class Font(ObservableDataclass):
    family: str = "Liberation Sans"
    size: int = 14
    style: FontStyle = FontStyle.REGULAR
    _attrib_fields: list[str] = field(init=False, default_factory=lambda: ["family", "size", "style"], repr=False)

@dataclass
class Script(ObservableDataclass):
    file_name: str = ""
    script_contents: str = ""
    pv_dict: ObservableDict = field(default_factory=ObservableDict)
    only_trigger_if_connected: bool = True
    embedded: bool = False

@dataclass
class Marker(ObservableDataclass):
    pv_name: str = ""
    color: Color = Color((255, 0, 0))
    interactive: bool = False

@dataclass
class Column(ObservableDataclass):
    name: str = ""
    width: int = 10
    editable: bool = True
    options: ObservableList[str] = field(default_factory=ObservableList[str])

@dataclass
class State(ObservableDataclass):
    value: int = 0
    label: str = ""
    color: Color = Color((0, 0, 0))


@dataclass
class ROI(ObservableDataclass):
    name: str = ""
    color: Color = Color((0, 255, 0))
    visible: bool = True
    interactive: bool = False
    x_pv: str = ""
    y_pv: str = ""
    width_pv: str = ""
    height_pv: str = ""
    file: str = ""

@dataclass
class Axis(ObservableDataclass):
    visible: bool = True
    title: str = ""
    minimum: float = 0.0
    maximum: float = 10.0
    on_right: bool = False
    auto_scale: bool = True
    log_scale: bool = False
    show_grid: bool = True
    title_font: Font = field(default_factory=Font)
    scale_font: Font = field(default_factory=Font)
    color: Color = Color((0, 0, 0))

@dataclass
class Trace:
    name: str
    x_pv: str = ""
    y_pv: str = ""
    error_pv: str = ""
    y_axis: int = 0
    trace_type: TraceType = TraceType.LINE
    color = Color((0, 0, 255))
    line_width: int = 1
    line_style: LineStyle = LineStyle.SOLID
    point_type: PointType = PointType.NONE
    point_size: int = 10
    visible: bool = True

@dataclass
class Tab(ObservableDataclass):
    name: str = ""
    file: str = ""
    macros: ObservableDict = field(default_factory=ObservableDict)
    group_name: str = ""


@dataclass
class Action(ObservableDataclass):
    description: str = ""

@dataclass
class OpenDisplayAction(Action):
    file: str = ""
    target: OpenDisplayTarget = OpenDisplayTarget.REPLACE
    macros: ObservableDict = field(default_factory=ObservableDict)

@dataclass
class WritePvAction(Action):
    pv_name: str = ""
    value: str = ""

@dataclass
class ExecuteAction(Action):
    script: Script = field(default_factory=lambda: Script())

@dataclass
class CommandAction(Action):
    command: str = ""

@dataclass
class OpenFileAction(Action):
    file: str = ""

@dataclass
class OpenWebpageAction(Action):
    url: str = ""

@dataclass
class RuleExpression(ObservableDataclass):
    bool_exp: str = ""
    value: str = ""

@dataclass
class Rule(ObservableDataclass):
    name: str = ""
    prop_id: str = ""
    exp: ObservableList[RuleExpression] = field(default_factory=ObservableList[RuleExpression])
    pv_name: ObservableList[str] = field(default_factory=ObservableList[str])
    output_as_expression: bool = False



