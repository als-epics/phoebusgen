from .property_helpers import PropertyBase, dynamic_property

@dynamic_property('x', int)
class HasX(PropertyBase):
    ...

@dynamic_property('y', int)
class HasY(PropertyBase):
    ...

@dynamic_property('width', int)
class HasWidth(PropertyBase):
    ...

@dynamic_property('height', int)
class HasHeight(PropertyBase):
    ...

class HasPosition(HasX, HasY, HasWidth, HasHeight):
    ...