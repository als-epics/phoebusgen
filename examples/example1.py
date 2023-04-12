"""Example 1
    Create ./example1.bob with 3 widgets
"""

import phoebusgen

pv_prefix = 'loc://example1'
my_screen = phoebusgen.screen.Screen('Phoebusgen Example 1')
my_screen.macro('PV_PREFIX', pv_prefix)
my_screen.background_color(204, 255, 255)

widgets = []

# don't worry about width and height, we will use auto-size after setting font size
title = phoebusgen.widget.Label('TitleLabel', 'Example 1 Phoebusgen Title', 0, 0, 0, 0)
title.font_size(36)
title.auto_size()
widgets.append(title)

pv_name = pv_prefix + ':BOOL<VEnum>(0, "OFF", "ON")'

check_box = phoebusgen.widget.CheckBox('MyCheckBox', 'Boolean PV', pv_name, 0, 80, 190, 70)
check_box.font_style_bold()
check_box.font_size(24)
widgets.append(check_box)

led = phoebusgen.widget.LED('MyLED', pv_name, 230, 60, 140, 110)
led.off_color(255, 0, 0)
widgets.append(led)

# add all widgets to our screen
my_screen.add_widget(widgets)

# write to specified file
my_screen.write_screen('./example1.bob')
