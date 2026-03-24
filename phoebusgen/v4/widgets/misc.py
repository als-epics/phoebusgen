from .widget import WidgetType, Widget
from phoebusgen.v4.properties.display import HasShowToolbar
from phoebusgen.v4.properties.widget import HasFile, HasUrl

class ThreeDViewer(Widget, HasFile):
    """ ThreeDViewer Phoebus Widget """
    _widget_type: WidgetType | None = WidgetType.THREE_DVIEWER
    def __init__(self, name: str, file: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create ThreeDViewer Widget

        :param name: Widget name
        :param file: File path
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.file = file

class WebBrowser(Widget, HasUrl, HasShowToolbar):
    """ WebBrowser Phoebus Widget """
    _widget_type: WidgetType | None = WidgetType.WEB_BROWSER
    def __init__(self, name: str, url: str, x: int, y: int, width: int, height: int) -> None:
        """
        Create WebBrowser Widget

        :param name: Widget name
        :param url: URL
        :param x: X position
        :param y: Y position
        :param width: Widget width
        :param height: Widget height
        """
        Widget.__init__(self, name, x, y, width, height)
        self.url = url
