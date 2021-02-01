# phoebusgen.widget Objects

This is a brief overview of the constructors for each widget and the methods available to add more properties.

## Graphics

### Arc
  - `phoebusgen.widget.Arc(name, x, y, width, height)`
    - `.angle_start(angle_start)`
    - `.angle_size(angle_size)`
    - `.macro(name, value)`
    - `.line_width(width)`
    - `.predefined_line_color(color_name)`
    - `.line_color(red, green, blue, alpha=255)`
    - `.predefined_background_color(color_name)`
    - `.background_color(red, green, blue, alpha=255)`
    - `.transparent(True/False)`

### Ellipse
  - `phoebusgen.widget.Ellipse(name, x, y, width, height)`
### Label
  - `phoebusgen.widget.Label(name, text, x, y, width, height)`
### Picture
  - `phoebusgen.widget.Picture(name, file, x, y, width, height)`
### Rectangle
  - `phoebusgen.widget.Rectangle(name, x, y, width, height)`

## Monitors

- LED
  - `phoebusgen.widget.LED(name, pv_name, x, y, width, height)`
- Text Update
  - `phoebusgen.widget.TextUpdate(name, pv_name, x, y, width, height)`

## Controls

- Action Button
  - `phoebusgen.widget.ActionButton(name, text, pv_name, x, y, width, height)`
- Text Entry
  - `phoebusgen.widget.TextEntry(name, pv_name, x, y, width, height)`

## Plots

## Structure

- Embedded Display
  - `phoebusgen.widget.EmbeddedDisplay(name, file, x, y, width, height)`
- Group
  - `phoebusgen.widget.Group(name, x, y, width, height)`


## Miscellaneous

