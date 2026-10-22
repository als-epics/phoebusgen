"""Build a screen from scratch and write it to a .bob file.

In v4 every widget property is a normal Python attribute, so you set things
with plain ``=`` assignment.

Run with:  python 01_create_screen.py
"""

from phoebusgen.v4.screen import Screen
from phoebusgen.v4.widgets import Label, Rectangle, TextEntry, TextUpdate, ActionButton
from phoebusgen.v4.properties.types import (
    Color,
    Font,
    FontStyle,
    OpenDisplayAction,
    OpenDisplayTarget,
)


def build_screen() -> Screen:
    # A screen with no f_name yet - we set the output file when we write.
    screen = Screen(name='Demo Screen')
    screen.width = 640
    screen.height = 480
    screen.background_color = Color((240, 240, 240))
    # Macros are exposed as a plain dict property.
    screen.macros = {'DEVICE': 'SIM:01'}

    # --- Title label ---
    title = Label('title', 'Device Overview', 10, 10, 320, 30)
    title.font = Font(size=20, style=FontStyle.BOLD)
    title.foreground_color = Color('#003366')  # hex strings are accepted too

    # --- A panel behind the readbacks ---
    panel = Rectangle('panel', 10, 50, 320, 130)
    panel.background_color = Color((255, 255, 255))
    panel.line_color = Color((0, 0, 0))
    panel.line_width = 1

    # --- Readback + setpoint. Macros can be used inside PV names. ---
    readback = TextUpdate('readback', '$(DEVICE):VAL_RBV', 20, 70, 150, 25)
    setpoint = TextEntry('setpoint', '$(DEVICE):VAL', 20, 105, 150, 25)

    # --- A button that opens a detail screen in a new tab ---
    detail_button = ActionButton('detail', 'Open Detail', '', 20, 140, 140, 30)
    detail_button.actions = [
        OpenDisplayAction(
            description='Detail',
            file='detail.bob',
            target=OpenDisplayTarget.NEW_TAB,
            macros={'DEVICE': '$(DEVICE)'},
        ),
    ]

    # add_widget accepts a single widget or a list of them.
    screen.add_widget([title, panel, readback, setpoint, detail_button])
    return screen


if __name__ == '__main__':
    screen = build_screen()
    screen.write_screen('01_create_screen.bob')
    print(screen)
    print('Wrote 01_create_screen.bob')
