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
- Progress Bar
  - `phoebusgen.widget.ProgressBar(name, pv_name, x, y, width, height)`
- Tank 
  - `phoebusgen.widget.Tank(name, pv_name, x, y, width, height)`
- Text Update
  - `phoebusgen.widget.TextUpdate(name, pv_name, x, y, width, height)`
- Thermometer 
  - `phoebusgen.widget.Thermometer(name, pv_name, x, y, width, height)`

## Controls

- Action Button
  - `phoebusgen.widget.ActionButton(name, text, pv_name, x, y, width, height)`
- Check Box
  - `phoebusgen.widget.CheckBox(name, label, pv_name, x, y, width, height)`
- Radio Button 
  - `phoebusgen.widget.RadioButton(name, pv_name, x, y, width, height)`
- Slide Button 
  - `phoebusgen.widget.SlideButton(name, label, pv_name, x, y, width, height)`
- Text Entry
  - `phoebusgen.widget.TextEntry(name, pv_name, x, y, width, height)`

## Plots

## Structure

- Array
  - `phoebusgen.widget.Array(name, pv_name, x, y, width, height)
- Embedded Display
  - `phoebusgen.widget.EmbeddedDisplay(name, file, x, y, width, height)`
- Group
  - `phoebusgen.widget.Group(name, x, y, width, height)`


## Miscellaneous
- Web Browser
  - `phoebusgen.widget.WebBrowser(name, url, x, y, width, height`
- 3D Viewer
  - `phoebusgen.widget.ThreeDViewer(name, file, x, y, width, height`

