from pathlib import Path
from typing import Optional, Union

from phoebusgen.v4.properties.display import HasShowToolbar
from phoebusgen.v4.properties.widget import HasFile, HasUrl

from .widget import Widget


class ThreeDViewer(Widget, HasFile):
    """ThreeDViewer Phoebus Widget"""

    width: int = 600
    height: int = 600

    def __init__(self, name: str = '', file: Optional[Union[Path, str]] = '', x: int = 0, y: int = 0, width: int = 600, height: int = 600) -> None:
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

    show_toolbar: bool = True
    width: int = 800
    height: int = 600

    def __init__(self, name: str = '', url: str = '', x: int = 0, y: int = 0, width: int = 800, height: int = 600) -> None:
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
