"""Example
    Create ./example_xyplot.bob with 3 plots with properties.
"""


import phoebusgen
import phoebusgen.widget

my_screen = phoebusgen.screen.Screen('XYPlot Example')
widgets = []


#XYPlot 1: An XYPlot with two y-axes and multiple traces.

xy_plot1 = phoebusgen.widget.XYPlot('Example Plot 1', 10, 10, 500, 500)
xy_plot1.title('Example Plot 1')

# Although this y-axis exists by default, adding the widget allows access to
# the methods associated with y-axes
yaxis1 = phoebusgen.widget.XYPlotYAxis()
yaxis1.title('Y Axis 1')
xy_plot1.add_y_axis(yaxis1)

# This is a second y-axis.
yaxis2 = phoebusgen.widget.XYPlotYAxis()
yaxis2.title('Y Axis 2')
yaxis2.on_right(True)
xy_plot1.add_y_axis(yaxis2)

# Traces are associated with the first y-axis by default
trace1 = phoebusgen.widget.XYPlotTrace()
# traces can have both an x and y PV
trace1.x_pv('sim://sawtooth(3, 0, 50, 0.2, 25, 75)')
trace1.y_pv('sim://sinewave(1, 50, 100, 0.1, 10, 50)')
xy_plot1.add_trace(trace1)

# This trace is based on the second y-axis
trace2 = phoebusgen.widget.XYPlotTrace()
trace2.y_pv('sim://gaussianwave(10, 4, 100, 1)')
yaxis2.auto_scale(True)  # scales y-axis based on trace
trace2.axis(1)
xy_plot1.add_trace(trace2)

widgets.append(xy_plot1)


# XYPlot 2: An XYPlot that uses trace methods.

xy_plot2 = phoebusgen.widget.XYPlot('Example Plot 2', 520, 10, 500, 500)
xy_plot2.title('Example Plot 2')

trace3 = phoebusgen.widget.XYPlotTrace()
trace3.y_pv('sim://noisewave(25, 50, 0.5)')
xy_plot2.add_trace(trace3)

# Traces have many styles
trace3.line_style_dot()

# Their width and points can also be changed
trace3.point_type_triangles()
trace3.line_width(2)

# Traces can also be given custom colors
trace3.color(255, 100, 255, 255) # alpha value is optional
widgets.append(xy_plot2)


# XYPlot 3: A stylized XY Plot

xy_plot3 = phoebusgen.widget.XYPlot('Example Plot 3', 1040, 10, 500, 500)
xy_plot3.title('Example Plot 3')
xy_plot3.title_font_family('Lato')
xy_plot3.title_font_style_bold_italic()
xy_plot3.title_font_size(24)

trace4 = phoebusgen.widget.XYPlotTrace()
trace4.y_pv('sim://sinewave(0, 100, 110, 0, 0, 100)')
trace4.x_pv('sim://sinewave(1, 100, 110, 0.1, 0, 100)')
xy_plot3.add_trace(trace4)

widgets.append(xy_plot3)

my_screen.add_widget(widgets)
my_screen.write_screen('./example_xyplot.bob')
