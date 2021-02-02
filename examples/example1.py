import phoebusgen


def make_screen():
    example_screen = phoebusgen.screen.Screen('Phoebusgen Example 1', './example1.bob')

    example_screen.width(400)
    example_screen.height(400)
    example_screen.macro('P', 'loc://example1')

    example_screen.write_screen()


if __name__ == '__main__':
    make_screen()