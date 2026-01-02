from .widget import WidgetType, Widget
from phoebusgen.properties import HasFile, HasUrl, HasShowToolbar

class ThreeDViewer(Widget, HasFile):
    """ ThreeDViewer Phoebus Widget """
    _widget_type: WidgetType | None = WidgetType.THREED_VIEWER
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
    _widget_type: WidgetType | None = WidgetType.WEBBROWSER
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
