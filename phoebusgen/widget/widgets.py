from xml.etree.ElementTree import Element, SubElement, tostring
import widget
import properties as p


class Label(widget.Widget):
    def __init__(self, name, x, y, width, height, text):
        super().__init__('label', name, x, y, width, height)

        text_child = SubElement(self.root, 'text')
        text_child.text = text


class TextUpdate(widget.Widget):
    def __init__(self, name, x, y, width, height):
        super().__init__('textupdate', name, x, y, width, height)

    def add_precision(self, val):
        prop = p.Precision(val)
        self.root.append(prop.element)

    def add_font(self, family=None, style=None, size=None):
        prop = p.Font(family, style, size)
        self.root.append(prop.element)



if __name__ == '__main__':
    pass
