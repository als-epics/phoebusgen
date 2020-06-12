from xml.etree.ElementTree import Element, SubElement


# TO DO : Add check if property is already available
# TO DO : Add way to specify defaults in a config file
class Property(object):
    def __init__(self, prop_type, root_element, val=None):
        self.element = Element(prop_type)
        if val is not None:
            self.element.text = str(val)
        root_element.append(self.element)


class PVName(Property):
    def __init__(self, root_element, name):
        super().__init__('pv_name', root_element, name)


class Precision(Property):
    def __init__(self, root_element, val):
        super().__init__('precision', root_element, val)


# When true, there shouldn't be any element
class ShowUnits(Property):
    def __init__(self, root_element, show=True):
        super().__init__('show_units', root_element, show)


class HorizontalAlignment(Property):
    def __init__(self, root_element, val):
        if val.lower() == 'left':
            v = 0
        elif val.lower() == 'center':
            v = 1
        elif val.lower() == 'right':
            v = 2
        else:
            raise Exception('Wrong input to horizontal alightment: {}'.format(val))
        super().__init__('horizontal_alignment', root_element, v)


class Font(Property):
    def __init__(self, root_element, family, style, size):
        super().__init__('font', root_element)
        if family is None:
            family ='Liberation Sans'
        if style is None:
            style = 'Regular'
        if size is None:
            size = 14
        SubElement(self.element, 'font', attrib={'family': family,
                                                 'style': style,
                                                 'size': str(size)})

