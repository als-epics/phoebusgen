from .property_helpers import PropertyBase
from .types import FileComponent, Tab, ObservableDict, ObservableList, Instance, Direction

class HasMacros(PropertyBase):
    macros: ObservableDict

class HasName(PropertyBase):
    name: str

class HasFile(PropertyBase):
    file: str

class HasUrl(PropertyBase):
    url: str

class HasBit(PropertyBase):
    bit: int

class HasFileComponent(PropertyBase):
    file_component: FileComponent

class HasLabel(PropertyBase):
    label: str

class HasTabs(PropertyBase):
    tabs: ObservableList[Tab]
    tab_height: int
    tab_width: int
    tab_spacing: int
    active_tab: int
    direction: Direction

class HasInstances(PropertyBase):
    instances: ObservableList[Instance]
