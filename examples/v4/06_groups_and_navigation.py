"""Groups, nested widgets, and navigation discovery.

Containers (``Screen``, ``Group``, ``Tab``, ``TemplateInstance``) mix in
``HasWidgets``, so they have ``add_widget`` plus query helpers like
``get_widgets``, ``get_all_widgets``, ``get_widgets_by_type`` and
``get_widget_names``. A ``Screen`` can also report where it navigates to via
``get_linked_screens``.

Run with:  python 06_groups_and_navigation.py
"""

from phoebusgen.v4.screen import Screen
from phoebusgen.v4.widgets import Group, Label, TextUpdate, ActionButton
from phoebusgen.v4.properties.types import OpenDisplayAction, OpenDisplayTarget


def main() -> None:
    screen = Screen(name='Groups Demo')
    screen.width = 500
    screen.height = 400

    # A group is itself a widget that holds child widgets.
    readbacks = Group('readbacks', 10, 10, 240, 150)
    readbacks.add_widget([
        Label('rb_title', 'Readbacks', 5, 5, 200, 25),
        TextUpdate('rb1', 'SIM:01:A', 5, 35, 150, 25),
        TextUpdate('rb2', 'SIM:01:B', 5, 65, 150, 25),
    ])

    # Besides add_widget(), the ``widgets`` property can be used directly.
    # Append a single child in place...
    readbacks.widgets.append(TextUpdate('rb3', 'SIM:01:C', 5, 95, 150, 25))

    # ...or assign a whole new list (replaces the existing children).
    controls = Group('controls', 260, 10, 230, 150)
    controls.widgets = [
        Label('ctl_title', 'Controls', 5, 5, 200, 25),
        TextUpdate('sp1', 'SIM:01:SP', 5, 35, 150, 25),
    ]

    # A button that links to another screen (discoverable via navigation).
    nav = ActionButton('to_detail', 'Detail', '', 10, 180, 120, 30)
    nav.actions = [
        OpenDisplayAction(description='Detail', file='detail.bob',
                          target=OpenDisplayTarget.NEW_WINDOW, macros={'DEVICE': 'SIM:01'}),
    ]

    screen.add_widget([readbacks, controls, nav])

    # --- Query helpers ---
    print('Direct children:', [w.name for w in screen.get_widgets()])
    print('All widgets (recursive):', [w.name for w in screen.get_all_widgets()])
    print('All TextUpdates:', [w.name for w in screen.get_widgets_by_type(TextUpdate)])

    # --- Navigation discovery ---
    for transition in screen.get_linked_screens():
        print('Links to', transition.target, 'with macros', transition.macros)

    screen.write_screen('06_groups_and_navigation.bob')
    print('Wrote 06_groups_and_navigation.bob')


if __name__ == '__main__':
    main()
