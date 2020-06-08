from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom




class Screen(object):
    def __init__(self, name, f_name=None):
        self.f_name = f_name
        self.root = Element('display', version='2.0.0')
        name_child = SubElement(self.root, 'name')
        name_child.text = name

        print (self.prettify(self.root))

    def write(self, elem):
        rough_string = tostring(elem, 'utf-8')
        reparse_xml = minidom.parseString(rough_string)
        if self.f_name == None:
            return False
        else:
            with open(self.f_name, 'w') as f:
                reparse_xml.writexml(f, indent="  ", addindent="  ", newl="\n", encoding="UTF-8")
            return True

    def prettify(self, elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = tostring(elem, 'utf-8')
        reparse_xml = minidom.parseString(rough_string)
        return reparse_xml.toprettyxml(indent="  ", newl="\n")




if __name__ == '__main__':
    s = Screen('DisplayTest')
