from pathlib import Path
from typing import Optional

from phoebusgen.v4.properties.display import HasTabActiveHeightDirection

from .property_helpers import PropertyBase
from .types import FileComponent, NavTab, ObservableDict, ObservableList, Instance, TabDirection

class HasMacros(PropertyBase):
    macros: ObservableDict

class HasName(PropertyBase):
    name: str = ''

class HasFile(PropertyBase):
    file: Optional[Path] = None

class HasUrl(PropertyBase):
    url: str = ''

class HasBit(PropertyBase):
    bit: int = 0

class HasFileComponent(PropertyBase):
    file_component: FileComponent = FileComponent.FULL_PATH

class HasLabel(PropertyBase):
    label: str = ''

class HasNavTabs(HasTabActiveHeightDirection):
    tabs: ObservableList[NavTab]
    tab_spacing: int = 2
    tab_width: int = 100
    direction: TabDirection = TabDirection.VERTICAL # Navtabs use vertical tabs by default
    active_tab: int = 0 # NavTabs use 0-based indexing for active tab, while Tabs use 1-based indexing

class HasInstances(PropertyBase):
    instances: ObservableList[Instance]
