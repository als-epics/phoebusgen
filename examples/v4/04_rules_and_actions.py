"""Adding rules and actions to widgets.

Widgets that mix in ``HasActionsRulesAndScripts`` have ``actions`` and ``rules``
list properties. This example adds a couple of rules (color and visibility
driven by PV expressions) and a few action types on a button.

Run with:  python 04_rules_and_actions.py
"""

from phoebusgen.v4.screen import Screen
from phoebusgen.v4.widgets import Label, ActionButton
from phoebusgen.v4.properties.types import (
    Color,
    Rule,
    RuleExpression,
    OpenDisplayAction,
    OpenDisplayTarget,
    WritePvAction,
    OpenWebpageAction,
)


def main() -> None:
    screen = Screen(name='Rules and Actions')
    screen.width = 500
    screen.height = 300

    # --- A label whose color is driven by a rule ---
    status = Label('status', 'Status', 10, 10, 200, 30)
    color_rule = Rule(
        name='Color By Value',
        prop_id='foreground_color',            # property the rule drives
        expressions=[
            RuleExpression(bool_exp='pv0 > 5', value=Color((255, 0, 0)), value_as_expression=False),
            RuleExpression(bool_exp='true', value=Color((0, 160, 0)), value_as_expression=False),
        ],
        pv_names={'SIM:01:VAL': True},         # {pv_name: trigger}
        out_exp=False,
    )
    status.rules = [color_rule]

    # --- A label that is hidden when a PV is zero ---
    warning = Label('warning', 'ALARM', 10, 50, 200, 30)
    warning.foreground_color = Color((200, 0, 0))
    warning.rules = [
        Rule(
            name='Visible When Nonzero',
            prop_id='visible',
            expressions=[RuleExpression(bool_exp='pv0 != 0', value=True, value_as_expression=False)],
            pv_names={'SIM:01:ALARM': True},
            out_exp=False,
        ),
    ]

    # --- A button carrying several kinds of action ---
    button = ActionButton('multi', 'Actions', '', 10, 90, 150, 30)
    button.actions = [
        OpenDisplayAction(description='Open detail', file='detail.bob',
                          target=OpenDisplayTarget.NEW_TAB, macros={'DEVICE': 'SIM:01'}),
        WritePvAction(description='Reset', pv_name='SIM:01:RESET', value='1'),
        OpenWebpageAction(description='Docs', url='https://control-system-studio.readthedocs.io'),
    ]

    print(button.actions)

    # --- We can modify the actions list in place, too ---
    button.actions.append(WritePvAction(description='Clear', pv_name='SIM:01:CLEAR', value='1'))
    del button.actions[1]  # remove the Reset action
    print(button.actions)

    screen.add_widget([status, warning, button])
    screen.write_screen('04_rules_and_actions.bob')
    print(screen)
    print('Wrote 04_rules_and_actions.bob')


if __name__ == '__main__':
    main()
