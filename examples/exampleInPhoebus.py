import sys
import phoebusgen

pv_arg = sys.argv[1]

print('Received the following arg from phoebus: {}'.format(pv_arg))

my_screen = phoebusgen.screen.Screen('My Generated Screen', '/home/tford/als/hlc/phoebusgen/examples/generated.bob')

y = 0
for i in range(int(pv_arg)):
    idx = str(i)
    label = phoebusgen.widget.Label('label{}'.format(idx), 'Label {}'.format(idx), 0, y, 100, 20)
    my_screen.add_widget(label)
    y += 30

my_screen.write_screen()
