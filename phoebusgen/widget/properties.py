from xml.etree.ElementTree import Element, SubElement


# TO DO : Add check if property is already available
# TO DO : Add way to specify defaults in a config file
class Property(object):
    def __init__(self, prop_type, val=None):
        self.element = Element(prop_type)
        if val is not None:
            self.element.text = str(val)


class Precision(Property):
    def __init__(self, val):
        super().__init__('precision', val)


class Font(Property):
    def __init__(self, family, style, size):
        super().__init__('font')
        if family is None:
            family ='Liberation Sans'
        if style is None:
            style = 'Regular'
        if size is None:
            size = 14
        SubElement(self.element, 'font', attrib={'family': family,
                                                 'style': style,
                                                 'size': str(size)})

