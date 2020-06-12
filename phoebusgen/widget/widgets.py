from xml.etree.ElementTree import Element, SubElement, tostring
import widget
import properties as p


class Label(widget.Widget):
    def __init__(self, name, x, y, width, height, text):
        super().__init__('label', name, x, y, width, height)

        text_child = SubElement(self.root, 'text')
        text_child.text = text


class TextUpdate(widget.Widget):
    def __init__(self, name, pv_name, x, y, width, height):
        super().__init__('textupdate', name, x, y, width, height)
        p.PVName(self.root, pv_name)

    def add_precision(self, val):
        p.Precision(self.root, val)

    def add_font(self, family=None, style=None, size=None):
        p.Font(self.root, family, style, size)

    def add_horizontal_alignment(self, val):
        p.HorizontalAlignment(self.root, val)



if __name__ == '__main__':
    pass
