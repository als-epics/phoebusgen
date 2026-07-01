from pathlib import Path
from typing import Dict, List, Optional, Union

from phoebusgen.v4.properties.behavior import HasToolTip
from phoebusgen.v4.properties.display import HasTabActiveHeightDirection

from .property_helpers import PropertyBase
from .types import (
    FileComponent,
    Instance,
    NavTab,
    TabDirection,
)

class HasPVName(HasToolTip):
    pv_name: str = ''
    tool_tip: str = '$(pv_name)\n$(pv_value)'

class HasMacros(PropertyBase):
    macros: Dict[str, str]

class HasName(PropertyBase):
    name: str = ''

class HasFile(PropertyBase):
    file: Optional[Union[Path, str]] = None

class HasUrl(PropertyBase):
    url: str = ''

class HasBit(PropertyBase):
    bit: int = 0

class HasFileComponent(PropertyBase):
    file_component: FileComponent = FileComponent.FULL_PATH

class HasLabel(PropertyBase):
    label: str = ''

class HasNavTabs(HasTabActiveHeightDirection):
    tabs: List[NavTab]
    tab_spacing: int = 2
    tab_width: int = 100
    direction: TabDirection = TabDirection.VERTICAL # Navtabs use vertical tabs by default
    active_tab: int = 0 # NavTabs use 0-based indexing for active tab, while Tabs use 1-based indexing

class HasInstances(PropertyBase):
    instances: List[Instance]

class HasSymbols(PropertyBase):
    symbols: List[str]
