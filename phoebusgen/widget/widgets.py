from xml.etree.ElementTree import Element, SubElement, tostring
import widget


class Label(widget.Widget):
    def __init__(self, name, x, y, width, height, text):
        super().__init__('label', name, x, y, width, height)

        text_child = SubElement(self.root, 'text')
        text_child.text = text


class TextUpdate(widget.Widget):
    def __init__(self, name, pv_name, x, y, width, height):
        super().__init__('textupdate', name, x, y, width, height)
        self.prop_factory.add_pv_name(pv_name)

    def add_precision(self, val):
        self.prop_factory.add_precision(val)

    def add_font(self, family=None, style=None, size=None):
        self.prop_factory.add_font(family, style, size)

    def add_horizontal_alignment(self, val):
        self.prop_factory.add_horizontal_alignment(val)

    def add_predefined_foreground_color(self, name):
        self.prop_factory.add_foreground_color(name, None, None, None, None)

    def add_foreground_color(self, red, green, blue, alpha=255):
        self.prop_factory.add_foreground_color(None, red, green, blue, alpha)



if __name__ == '__main__':
    pass
