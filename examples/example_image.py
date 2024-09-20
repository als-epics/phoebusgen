"""Example
    Create ./example_image.bob with an image and properties.
"""

import phoebusgen
import phoebusgen.widget

my_screen = phoebusgen.screen.Screen('Image Example')
widgets = []

image1 = phoebusgen.widget.Image('Example Image 1', None, 10, 10, 500, 500)
image1.pv_name('sim://sinewave(10, 50, 10000, 0.5)')

# Add an x-axis
x_axis = phoebusgen.widget.ImageXAxis()
x_axis.minimum(-100)
x_axis.maximum(100)
image1.add_x_axis(x_axis)

# Add a y-axis
y_axis = phoebusgen.widget.ImageYAxis()
y_axis.minimum(-100)
y_axis.maximum(100)
image1.add_y_axis(y_axis)

# Color maps have predefined color sets
image1.predefined_color_map('JET')

# But you can also customize your own
# Parameters: value (order of colors), RGB
# All with values 0-255
color1 = phoebusgen.widget.ColorMapColor(0, 255, 100, 255)
color3 = phoebusgen.widget.ColorMapColor(100, 255, 0, 100)
color2 = phoebusgen.widget.ColorMapColor(255, 100, 0, 255)

image1.add_color_map(color1)
image1.add_color_map(color2)
image1.add_color_map(color3)

# add an interactive region of interest
roi1 = phoebusgen.widget.RegionOfInterest()
image1.add_roi(roi1)
roi1.x_pv('loc://roi_x(10)')
roi1.y_pv('loc://roi_y(10)')
roi1.width_pv('loc://roi_w(50)')
roi1.height_pv('loc://roi_h(10)')
roi1.interactive(True)
roi1.color(0, 0, 0)

widgets.append(image1)

my_screen.add_widget(widgets)
my_screen.write_screen('./example_image.bob')
