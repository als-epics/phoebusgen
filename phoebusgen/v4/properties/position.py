from .property_helpers import PropertyBase

class HasPosition(PropertyBase):
    x: int = 0
    y: int = 0
    width: int
    height: int
