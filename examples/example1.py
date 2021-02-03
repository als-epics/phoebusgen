import phoebusgen


def make_screen():
    example_screen = phoebusgen.screen.Screen('Phoebusgen Example 1', './example1.bob')

    example_screen.width(1000)
    example_screen.height(1000)
    example_screen.macro('P', 'loc://example1')
    group = phoebusgen.widget.Group('Example Group', 0, 0, 500, 400)
    group.background_color(0, 0, 0, 50)
    #group.predefined_font('Header 3')
    for i in range(1, 11):
        label = phoebusgen.widget.Label('Label{}'.format(i), 'Here is a Label', 0, (i-1)*20, 120, 20)
        text_update = phoebusgen.widget.TextUpdate('TextUpdate{}'.format(i), '$(P):update1', 120, (i-1)*20, 120, 20)
        comment = phoebusgen.widget.Label('Comment1'.format(i), 'Label explanation', 240, (i-1)*20, 120, 20)
        #comment.predefined_font('Comment')
        comment.font_style_bold_italic()
        label.foreground_color(100, 0, 100)
        comment.predefined_foreground_color('Attention')
        group.add_widget([label, text_update, comment])

    example_screen.add_widget(group)
    example_screen.write_screen()


if __name__ == '__main__':
    make_screen()
