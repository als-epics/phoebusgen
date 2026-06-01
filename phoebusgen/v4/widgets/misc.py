from pathlib import Path
from typing import Union

from phoebusgen.v4.properties.display import HasShowToolbar
from phoebusgen.v4.properties.widget import HasFile, HasUrl

from .widget import Widget


class ThreeDViewer(Widget, HasFile):
    """ThreeDViewer Phoebus Widget"""

    width: int = 600
    height: int = 600

    def __init__(self, name: str, file: Union[Path, str], x: int, y: int, width: int, height: int) -> None:
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
    """WebBrowser Phoebus Widget"""

    width: int = 800
    height: int = 600
    show_toolbar: bool = True

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
