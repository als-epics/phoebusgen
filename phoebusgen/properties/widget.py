from .property_helpers import PropertyBase, dynamic_property
from .types import FileComponent, Tab, Action, ObservableDict, ObservableList, Script
from xml.etree.ElementTree import SubElement

@dynamic_property("macros", ObservableDict)
class HasMacros(PropertyBase):
    ...

@dynamic_property("name", str)
class HasName(PropertyBase):
    ...

@dynamic_property("file", str)
class HasFile(PropertyBase):
    ...

@dynamic_property("url", str)
class HasUrl(PropertyBase):
    ...

@dynamic_property("bit", int)
class HasBit(PropertyBase):
    ...

@dynamic_property("file_component", FileComponent)
class HasFileComponent(PropertyBase):
    ...

@dynamic_property("label", str)
class HasLabel(PropertyBase):
    ...

@dynamic_property("tabs", ObservableList[Tab])
class HasTabs(PropertyBase):
    ...

