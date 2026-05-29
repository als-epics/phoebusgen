from ..properties.types import Color, HorizontalAlignment, VerticalAlignment

from .graphics import Label


Label._set_default_value('background_color', Color((255, 255, 255)))
Label._set_default_value('width', 100)
Label._set_default_value('height', 20)
Label._set_default_value('text', 'Label text')
Label._set_default_value('horizontal_alignment', )
