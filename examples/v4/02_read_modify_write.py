"""Read an existing screen, modify it, and write it back.

Pass ``f_name`` to the ``Screen`` constructor to parse an existing .bob file
back into a ``Screen`` object::

    screen = Screen(f_name='existing.bob')

To keep it self-contained, this example first writes a small screen, then
reopens it, edits it, and writes the result to a new file.

Run with:  python 02_read_modify_write.py
"""

from phoebusgen.v4.screen import Screen
from phoebusgen.v4.widgets import Label, TextUpdate
from phoebusgen.v4.properties.types import Color


def make_original(path: str) -> None:
    """Create a starting screen so this example can run standalone."""
    screen = Screen(name='Original')
    screen.width = 400
    screen.height = 200
    screen.add_widget([
        Label('heading', 'Original Heading', 10, 10, 200, 30),
        Label('subheading', 'Subtitle', 10, 45, 200, 25),
        TextUpdate('rbv', 'SIM:01:VAL_RBV', 10, 80, 150, 25),
    ])
    screen.write_screen(path)


def modify(in_path: str, out_path: str) -> None:
    # Parsing an existing file back into a Screen object.
    screen = Screen(f_name=in_path)

    # Reading properties off the parsed screen.
    print('Loaded screen name:', screen.name)
    print('Size:', screen.width, 'x', screen.height)
    print('Widget names:', sorted(screen.get_widget_names()))

    # Modify the screen-level properties.
    screen.name = 'Modified'
    screen.background_color = Color((230, 245, 255))

    # Edit every Label: recolor and nudge it to the right.
    for label in screen.get_widgets_by_type(Label):
        label.foreground_color = Color((180, 0, 0))
        label.x = label.x + 5

    # Retarget the readback PV to a different device.
    for tu in screen.get_widgets_by_type(TextUpdate):
        tu.pv_name = tu.pv_name.replace('SIM:01', 'SIM:02')

    # Write the edited screen back out to a new file.
    # Note, if opened with `overwrite=True`, calling `write_screen()` with
    # no arguments will overwrite the original file. Here we write to a new file.
    screen.write_screen(out_path)


if __name__ == '__main__':
    make_original('02_original.bob')
    modify('02_original.bob', '02_modified.bob')
    print('Wrote 02_modified.bob')
