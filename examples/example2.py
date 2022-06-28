from phoebusgen import widget as w
from phoebusgen import screen as s
from phoebusgen import colors, fonts

widget_height = 20
widget_length = 120

def make_group(num_pvs):
    group = w.Group('Example Group', 0, 0, 400, 240)
    group.predefined_font(fonts.Header2)
    for i in range(1, num_pvs+1):
        y_position = (i-1)*widget_height
        pv_name = '$(P):update{}<VInteger>({})'.format(i, i*100)
        label = w.Label('Label{}'.format(i), 'Here is a Label', 0, y_position, widget_length, widget_height)
        text_update = w.TextUpdate('TextUpdate{}'.format(i), pv_name, widget_length, y_position, widget_length, widget_height)
        comment = w.Label('Comment{}'.format(i), 'Label explanation', widget_length*2, y_position, widget_length, widget_height)
        comment.predefined_font(fonts.Comment)
        comment.font_style_bold_italic()
        label.foreground_color(100, 0, 100)
        comment.predefined_foreground_color(colors.Attention)
        group.add_widget([label, text_update, comment])
    return group

def make_screen():
    example_screen = s.Screen('Phoebusgen Example 2', './example2.bob')
    example_screen.width(1000)
    example_screen.height(1000)
    example_screen.macro('P', 'loc://example3')
    example_screen.background_color(188, 188, 188)
    group = make_group(10)
    example_screen.add_widget(group)
    example_screen.write_screen()


if __name__ == '__main__':
    make_screen()
