from dataclasses import Field, dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, TypeVar, Union, TYPE_CHECKING

# SupportsIndex was added to typing in Python 3.8. Use the real type for the
# type checker, but fall back to int at runtime on 3.6/3.7.
if TYPE_CHECKING:
    from typing import SupportsIndex
else:
    try:
        from typing import SupportsIndex
    except ImportError:
        SupportsIndex = int

PropertyType = Union[
    int, float, str, bool,
    Tuple,
    Enum,
    'Color',
    'Font',
    'ObservableDict',
    'ObservableList',
    'ObservableDataclass',
    'Rule',
    'RuleExpression',
]

class Color(tuple):

    @classmethod
    def is_color(cls, value: Any) -> bool:
        if isinstance(value, cls):
            return True
        if isinstance(value, (tuple, list)) and all(isinstance(i, int) for i in value) and (len(value) == 3 or len(value) == 4):
            return all(0 <= i <= 255 for i in value)
        if isinstance(value, str) and value.startswith('#') and (len(value) == 7 or len(value) == 9):
            return True
        # TODO: validate predefined color names
        return False

    def __new__(cls, color: Optional[Union[Tuple[int, int, int], Tuple[int, int, int, int], str]] = None):
        if color is None:
            color = (0, 0, 0)
        red = 0
        green = 0
        blue = 0
        alpha = 255

        if isinstance(color, tuple):
            if len(color) < 3:
                raise ValueError('Color tuple must be of length 3 (RGB) or 4 (RGBA)')
            red = color[0]
            green = color[1]
            blue = color[2]
            if len(color) == 3:
                alpha = 255
            else:
                alpha = color[3]
        elif isinstance(color, str) and color.startswith('#'):
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
            raise ValueError('Invalid color format! Must be RGB/RGBA tuple or HEX string.')

        color_tuple = (red, green, blue)
        if alpha != 255:
            color_tuple += (alpha,)
        return super().__new__(cls, tuple(color_tuple))


    def as_hex(self) -> str:
        """Returns the color as a hex string in the format #RRGGBB or #RRGGBBAA."""
        if len(self) == 3:
            return '#{:02X}{:02X}{:02X}'.format(self[0], self[1], self[2])
        elif len(self) == 4:
            return '#{:02X}{:02X}{:02X}{:02X}'.format(self[0], self[1], self[2], self[3])
        else:
            raise ValueError('Color tuple must be of length 3 (RGB) or 4 (RGBA)')


    def __eq__(self, other: Any) -> bool:
        """Check equality with another Color instance or a compatible color representation."""
        if not isinstance(other, Color):
            try:
                other = Color(other)
            except ValueError:
                return False
        return tuple(self) == tuple(other)


ColorType = Union[Color, Tuple[int, int, int, int], Tuple[int, int, int], str]

class FontStyle(str, Enum):
    REGULAR = 'REGULAR'
    ITALIC = 'ITALIC'
    BOLD = 'BOLD'
    BOLD_AND_ITALIC = 'BOLD_ITALIC'

class HorizontalAlignment(int, Enum):
    LEFT = 0
    CENTER = 1
    RIGHT = 2

class VerticalAlignment(int, Enum):
    TOP = 0
    MIDDLE = 1
    BOTTOM = 2

class RotationStep(int, Enum):
    ZERO = 0
    NINETY = 1
    ONE_HUNDRED_EIGHTY = 2
    NEGATIVE_NINETY = 3

class ButtonMode(int, Enum):
    TOGGLE = 0
    PUSH = 1
    PUSH_INVERTED = 2

class InterpolationType(int, Enum):
    NONE = 0
    INTERPOLATE = 1
    AUTOMATIC = 2

class ColorMode(int, Enum):
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

class GroupStyle(int, Enum):
    GROUP_BOX = 0
    TITLE_BAR = 1
    LINE = 2
    NONE = 3

class LabelClass(str, Enum):
    DEFAULT = 'DEFAULT'
    TITLE = 'TITLE'
    COMMENT = 'COMMENT'
    SECTION = 'SECTION'
    LABEL = 'Label'
    LABEL_1 = 'Label_1'
    LABEL_2 = 'Label_2'


class ResizeBehavior(int, Enum):
    NO_RESIZE = 0
    SIZE_CONTENT_TO_FIT_WIDGET = 1
    SIZE_WIDGET_TO_MATCH_CONTENT = 2
    STRETCH_CONTENT_TO_FIT_WIDGET = 3
    CROP_CONTENT = 4

class FileComponent(int, Enum):
    FULL_PATH = 0
    DIRECTORY = 1
    NAME_AND_EXTENSION = 2
    BASE_NAME = 3

class TraceType(int, Enum):
    NONE = 0
    LINE = 1
    STEP = 2
    ERR_BARS = 3
    LINE_ERR_BARS = 4
    BARS = 5

class LineStyle(int, Enum):
    SOLID = 0
    DASHED = 1
    DOT = 2
    DASH_DOT = 3
    DASH_DOT_DOT = 4

class PointType(int, Enum):
    NONE = 0
    SQUARES = 1
    CIRCLES = 2
    DIAMONDS = 3
    X = 4
    TRIANGLES = 5

class ColorMap(str, Enum):
    VIRIDIS = 'VIRIDIS'
    GRAYSCALE = 'GRAY'
    JET = 'JET'
    COLOR_SPECTRUM = 'SPECTRUM'
    HOT = 'HOT'
    COOL = 'COOL'
    SHADED = 'SHADED'
    MAGMA = 'MAGMA'

class ArrowTypes(str, Enum):
    NONE = 'None'
    FROM = 'From'
    TO = 'To'
    BOTH = 'Both'

class OpenDisplayTarget(str, Enum):
    REPLACE = 'replace'
    NEW_TAB = 'tab'
    NEW_WINDOW = 'window'


class TabDirection(int, Enum):
    HORIZONTAL = 0
    VERTICAL = 1

class EmbeddedScriptType(str, Enum):
    PYTHON = 'EmbeddedPy'
    JAVASCRIPT = 'EmbeddedJS'

class Format(int, Enum):
    DEFAULT = 0
    DECIMAL = 1
    ENGINEERING = 2
    HEXADECIMAL = 3
    COMPACT = 4
    STRING = 5
    SEXAGESIMAL_HH_MM_SS = 6
    SEXAGESIMAL_HMS_24H_RAD = 7
    SEXAGESIMAL_DMS_360D_RAD = 8
    BINARY = 9


KT = TypeVar('KT')
VT = TypeVar('VT')

class ObservableDict(Dict[KT, VT]):

    _on_change_callback: Optional[Callable[['ObservableDict[KT, VT]'], None]] = None

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initializes the observable dictionary."""
        super().__init__(*args, **kwargs)

    def _notify_change(self) -> None:
        """Notify the callback function that the dictionary has changed."""
        if self._on_change_callback:
            self._on_change_callback(self)

    def __setitem__(self, key: KT, value: VT) -> None:
        """Update the value for the given key and notify the callback."""
        super().__setitem__(key, value)
        self._notify_change()

    def __delitem__(self, key: KT) -> None:
        """Delete the item with the given key and notify the callback."""
        super().__delitem__(key)
        self._notify_change()

    def clear(self) -> None:
        """Remove all items from the dictionary and notify the callback."""
        super().clear()
        self._notify_change()

    def pop(self, *args: Any) -> Any:
        """Remove the specified key and return the corresponding value, notifying the callback."""
        result = super().pop(*args)
        self._notify_change()
        return result

    def update(self, other: Any = (), **kwargs: Any) -> None:
        """Update the dictionary with the key/value pairs from other, overwriting existing keys, and notify the callback."""
        super().update(other, **kwargs)
        self._notify_change()

    def setdefault(self, key: KT, default: Any = None) -> VT:
        """Set the default value for the given key and notify the callback if the key was not present."""
        if key not in self:
            self[key] = default
        return self[key]

    def __ior__(self, other: Any) -> 'ObservableDict[KT, VT]':
        """Update the dictionary with the key/value pairs from other, overwriting existing keys, and notify the callback."""
        result = super().__ior__(other)
        self._notify_change()
        return result


@dataclass
class ObservableDataclass:

    _on_change_callback: Optional[Callable[[Any], None]] = field(init=False, default=None, repr=False, compare=False)
    _attrib_fields: List[str] = field(init=False, default_factory=list, repr=False)

    def __setattr__(self, name: str, value: Any) -> None:
        """Set the attribute and notify the callback if applicable."""
        super().__setattr__(name, value)
        if name != '_on_change_callback' and self._on_change_callback:
            self._on_change_callback(self)

    @classmethod
    def fields(cls) -> Dict[str, Field]:
        """Return a dictionary of the dataclass fields, excluding private fields."""
        fields: Dict[str, Field] = {}
        for dcls_field in cls.__dataclass_fields__:
            if not dcls_field.startswith('_'):
                fields[dcls_field] = cls.__dataclass_fields__[dcls_field]
        return fields

    def __eq__(self, other: object) -> bool:
        """Check equality with another ObservableDataclass instance based on the values of its fields."""
        if not isinstance(other, ObservableDataclass):
            return NotImplemented
        for dcls_field in self.fields():
            if getattr(self, dcls_field) != getattr(other, dcls_field):
                return False
        return True

ValidListType = Union[int, float, str, bool, Enum, ObservableDataclass]
ValidListTypeT = TypeVar('ValidListTypeT', bound=ValidListType)

class ObservableList(List[ValidListTypeT]):
    _on_change_callback: Optional[Callable[['ObservableList[ValidListTypeT]'], None]] = None

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize an observable list."""
        super().__init__(*args, **kwargs)

    def _notify_change(self) -> None:
        """Notify the callback function that the list has changed."""
        if self._on_change_callback:
            self._on_change_callback(self)

    def __setitem__(self, i: Any, val: Any) -> None:
        """Set the item at index i to val and notify the callback."""
        if hasattr(val, '_on_change_callback'):
            val._on_change_callback = lambda _self: self._notify_change()
        super().__setitem__(i, val)
        self._notify_change()

    def __delitem__(self, i: Any) -> None:
        """Delete the item at index i and notify the callback."""
        super().__delitem__(i)
        self._notify_change()

    def insert(self, index: SupportsIndex, value: ValidListTypeT) -> None:
        """Insert value before index and notify the callback."""
        if hasattr(value, '_on_change_callback'):
            value._on_change_callback = lambda _self: self._notify_change()
        super().insert(index, value)
        self._notify_change()

    def append(self, value: ValidListTypeT) -> None:
        """Append value to the end of the list and notify the callback."""
        if hasattr(value, '_on_change_callback'):
            value._on_change_callback = lambda _self: self._notify_change()
        super().append(value)
        self._notify_change()

    def extend(self, values: Iterable[ValidListTypeT]) -> None:
        """Extend the list with the given values and notify the callback."""
        for val in values:
            if hasattr(val, '_on_change_callback'):
                val._on_change_callback = lambda _self: self._notify_change()
        super().extend(values)
        self._notify_change()

    def pop(self, index: SupportsIndex = -1) -> ValidListTypeT:
        """Remove and return the item at the given index, notifying the callback."""
        result = super().pop(index)
        self._notify_change()
        return result

    def remove(self, value: ValidListTypeT) -> None:
        """Remove the first occurrence of value and notify the callback."""
        super().remove(value)
        self._notify_change()

    def clear(self) -> None:
        """Remove all items from the list and notify the callback."""
        super().clear()
        self._notify_change()

    def sort(self, *args: Any, **kwargs: Any) -> None:
        """Sort the list in place and notify the callback."""
        super().sort(*args, **kwargs)
        self._notify_change()

    def reverse(self) -> None:
        """Reverse the list in place and notify the callback."""
        super().reverse()
        self._notify_change()

    def __iadd__(self, values: Iterable[ValidListTypeT]) -> 'ObservableList[ValidListTypeT]':
        """Extend the list in place with the given values and notify the callback."""
        for val in values:
            if hasattr(val, '_on_change_callback'):
                val._on_change_callback = lambda _self: self._notify_change()
        result = super().__iadd__(values)
        self._notify_change()
        return result





@dataclass
class Font(ObservableDataclass):
    family: str = 'Liberation Sans'
    size: int = 14
    style: FontStyle = FontStyle.REGULAR
    _attrib_fields: List[str] = field(init=False, default_factory=lambda: ['family', 'size', 'style'], repr=False)


@dataclass
class Marker(ObservableDataclass):
    pv_name: str = ''
    color: Color = field(default_factory=lambda: Color((255, 0, 0)))
    interactive: bool = True

@dataclass
class Column(ObservableDataclass):
    name: str = ''
    width: int = 100
    editable: bool = True
    options: List[str] = field(default_factory=ObservableList[str])

@dataclass
class State(ObservableDataclass):
    value: int = 0
    label: str = ''
    color: ColorType = field(default_factory=Color)


@dataclass
class ROI(ObservableDataclass):
    name: str = ''
    color: ColorType = field(default_factory=lambda: Color((0, 255, 0)))
    visible: bool = True
    interactive: bool = True
    x_pv: str = ''
    y_pv: str = ''
    width_pv: str = ''
    height_pv: str = ''
    file: Optional[Path] = None

@dataclass
class ColorBar(ObservableDataclass):
    visible: bool = True
    bar_size: int = 40
    scale_font: Font = field(default_factory=Font)

@dataclass
class Axis(ObservableDataclass):
    visible: bool = True
    title: str = ''
    minimum: float = 0.0
    maximum: float = 10.0
    on_right: bool = False
    autoscale: bool = True
    log_scale: bool = False
    show_grid: bool = True
    title_font: Font = field(default_factory=Font)
    scale_font: Font = field(default_factory=Font)
    color: ColorType = field(default_factory=Color)

@dataclass
class Trace(ObservableDataclass):
    name: str
    x_pv: str = ''
    y_pv: str = ''
    error_pv: str = ''
    y_axis: int = 0
    trace_type: TraceType = TraceType.LINE
    color: ColorType = field(default_factory=lambda: Color((0, 0, 255)))
    line_width: int = 1
    line_style: LineStyle = LineStyle.SOLID
    point_type: PointType = PointType.NONE
    point_size: int = 10
    visible: bool = True

@dataclass
class NavTab(ObservableDataclass):
    name: str = ''
    file: Optional[Union[Path, str]] = None
    macros: Dict[str, str] = field(default_factory=ObservableDict)
    group_name: str = ''

@dataclass
class Script(ObservableDataclass):
    file: Optional[Union[Path, str]] = None
    pv_names: List[str] = field(default_factory=ObservableList[str])

@dataclass
class EmbeddedScript(Script):
    file: EmbeddedScriptType
    text: str = ''

@dataclass
class Action(ObservableDataclass):
    description: str = ''

@dataclass
class OpenDisplayAction(Action):
    file: Optional[Union[Path, str]] = None
    target: OpenDisplayTarget = OpenDisplayTarget.REPLACE
    macros: Dict[str, str] = field(default_factory=ObservableDict)

@dataclass
class WritePvAction(Action):
    pv_name: str = ''
    value: str = ''

@dataclass
class ExecuteAction(Action):
    script: Script = field(default_factory=Script)

@dataclass
class CommandAction(Action):
    command: str = ''

@dataclass
class OpenFileAction(Action):
    file: Optional[Union[Path, str]] = None

@dataclass
class OpenWebpageAction(Action):
    url: str = ''

@dataclass
class RuleExpression(ObservableDataclass):
    bool_exp: str = ''
    value: Optional[PropertyType] = None
    value_as_expression: bool = False


@dataclass
class Rule(ObservableDataclass):
    name: str = 'New Rule'
    prop_id: str = 'name'
    expressions: List[RuleExpression] = field(default_factory=ObservableList[RuleExpression])
    pv_names: Dict[str, bool] = field(default_factory=ObservableDict)
    out_exp: bool = False

@dataclass
class Instance(ObservableDataclass):
    macros: Dict[str, str] = field(default_factory=ObservableDict)


@dataclass
class Point(ObservableDataclass):
    x: float = 0.0
    y: float = 0.0
    _attrib_fields: List[str] = field(init=False, default_factory=lambda: ['x', 'y'], repr=False)

@dataclass
class LinearMeterColors(ObservableDataclass):
    """
    Linear meter widget combines all colors into special XML element, so needs to be its own dataclass
    """

    # Default colors taken from Phoebus LinearMeter widget
    foreground_color: ColorType = field(default_factory=lambda: Color((0, 0, 0)))
    background_color: ColorType = field(default_factory=lambda: Color((0, 0, 0, 0)))
    needle_color: ColorType = field(default_factory=lambda: Color((0, 0, 0)))
    knob_color: ColorType = field(default_factory=lambda: Color((0, 0, 0)))
    normal_status_color: ColorType = field(default_factory=lambda: Color((194, 198, 195)))
    minor_warning_color: ColorType = field(default_factory=lambda: Color((242, 148, 141)))
    major_warning_color: ColorType = field(default_factory=lambda: Color((240, 60, 46)))
    is_gradient_enabled: bool = False
    is_highlighting_of_active_regions_enabled: bool = True
