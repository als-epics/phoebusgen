from .property_helpers import PropertyBase
from .types import FileComponent, NavTab, ObservableDict, ObservableList, Instance

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

class HasNavTabs(PropertyBase):
    tabs: ObservableList[NavTab]
    tab_spacing: int
    tab_width: int

class HasInstances(PropertyBase):
    instances: ObservableList[Instance]
