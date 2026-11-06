from pathlib import Path
from xml.etree.ElementTree import SubElement

from phoebusgen.v4.widgets import ThreeDViewer, WebBrowser


def test_threedviewer_file_property() -> None:
    w = ThreeDViewer('3DViewer1', file='/path/to/model.obj', x=5, y=5, width=400, height=300)
    assert hasattr(w, 'file')
    assert isinstance(w.file, Path)
    assert w.file == Path('/path/to/model.obj')
    w.file = '/new/path/to/model.obj'
    assert w.file == Path('/new/path/to/model.obj')
    file_elem = w.root.find('file')
    assert file_elem is not None
    assert file_elem.text == '/new/path/to/model.obj'

def test_webbrowser_url_property() -> None:
    w = WebBrowser('WebBrowser1', url='https://example.com', x=10, y=10, width=800, height=600)
    assert hasattr(w, 'url')
    assert isinstance(w.url, str)
    assert w.url == 'https://example.com'
    w.url = 'https://newexample.com'
    assert w.url == 'https://newexample.com'
    url_elem = w.root.find('url')
    assert url_elem is not None
    assert url_elem.text == 'https://newexample.com'

def test_threedviewer_from_xml(widget_xml_factory) -> None:
    root = widget_xml_factory(ThreeDViewer)
    SubElement(root, 'file').text = '/path/to/model.obj'
    w = ThreeDViewer.from_element(root)
    assert isinstance(w, ThreeDViewer)
    assert w.file == Path('/path/to/model.obj')

def test_webbrowser_from_xml(widget_xml_factory) -> None:
    root = widget_xml_factory(WebBrowser)
    SubElement(root, 'url').text = 'https://example.com'
    w = WebBrowser.from_element(root)
    assert isinstance(w, WebBrowser)
    assert w.url == 'https://example.com'
