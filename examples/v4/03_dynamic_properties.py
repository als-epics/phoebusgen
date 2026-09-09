"""Working with widget properties.

Every widget property is a type-annotated Python attribute. This means you can set
it with plain ``=`` assignment, and read it back as a python type (either a primitive
like ``int`` or ``str``, or a more complex object like ``Color`` or ``Font``).

Run with:  python 03_dynamic_properties.py
"""

from phoebusgen.v4.widgets import TextUpdate
from phoebusgen.v4.properties.types import Color, Font, FontStyle


def main() -> None:
    widget = TextUpdate('demo', 'SIM:01:VAL', 10, 20, 120, 30)

    # --- Plain attribute get/set ---
    widget.x = 15
    widget.width = 200
    widget.foreground_color = Color((0, 128, 0))
    widget.background_color = '#FFFFFF'          # hex string accepted
    widget.font = Font(family='Liberation Sans', size=16, style=FontStyle.BOLD)

    # --- Reading a property returns a proper python object, rather than just a string ---
    color = widget.foreground_color
    print('foreground_color ->', 'type', type(color), 'value', color, 'as hex:', color.as_hex())
    print('font ->', 'type', type(widget.font), 'value', widget.font)

    # Color equality is flexible - compares against tuples and hex strings.
    assert widget.foreground_color == (0, 128, 0)
    assert widget.background_color == '#FFFFFF'

    # --- Mutating a nested value updates the widget's XML automatically ---
    font = widget.font
    font.size = 18
    print('font after size change ->', widget.font)

    # --- Introspection helpers ---
    print('has "pv_name"? ', widget.has_property('pv_name'))
    print('type of "x": ', widget.get_property_type_by_name('x'))
    print('type of "foreground_color": ', widget.get_property_type_by_name('foreground_color'))
    print('all property names:', sorted(widget.get_property_names()))

    print(widget)


if __name__ == '__main__':
    main()
