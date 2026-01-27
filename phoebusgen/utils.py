from xml.etree.ElementTree import tostring
from xml.dom import minidom

def prettify_xml(elem):
    """Return a pretty-printed XML string for the Element.
        From: https://pymotw.com/3/xml.etree.ElementTree/create.html
    """
    rough_string = tostring(elem, 'utf-8')
    reparse_xml = minidom.parseString(rough_string)
    return reparse_xml.toprettyxml(indent='  ', newl='\n')


