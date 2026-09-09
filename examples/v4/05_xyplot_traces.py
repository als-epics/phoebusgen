"""An XYPlot with traces and axes.

Plot widgets use dataclass-backed properties: ``x_axis`` is a single ``Axis``,
``y_axes`` is a list of ``Axis``, and ``traces`` is a list of ``Trace``. You
assign these objects directly to the properties.

Run with:  python 05_xyplot_traces.py
"""

from phoebusgen.v4.screen import Screen
from phoebusgen.v4.widgets import XYPlot
from phoebusgen.v4.properties.types import (
    Axis,
    Trace,
    TraceType,
    LineStyle,
    PointType,
    Color,
)


def main() -> None:
    screen = Screen(name='Plot Demo')
    screen.width = 700
    screen.height = 500

    plot = XYPlot('signals', 10, 10, 680, 480)
    plot.title = 'Signals'

    # A single X axis and one Y axis.
    plot.x_axis = Axis(title='Time (s)', minimum=0.0, maximum=100.0, autoscale=False)
    plot.y_axes = [
        Axis(title='Volts', minimum=-10.0, maximum=10.0, autoscale=False),
        Axis(title='Amps', minimum=0.0, maximum=5.0, on_right=True, autoscale=True),
    ]

    # Two traces, each bound to different PVs and Y axes.
    plot.traces = [
        Trace(name='Voltage', x_pv='SIM:T', y_pv='SIM:CH1', y_axis=0,
              trace_type=TraceType.LINE, color=Color((0, 0, 255)),
              line_width=2, line_style=LineStyle.SOLID, point_type=PointType.NONE),
        Trace(name='Current', x_pv='SIM:T', y_pv='SIM:CH2', y_axis=1,
              trace_type=TraceType.LINE, color=Color((255, 0, 0)),
              line_width=1, line_style=LineStyle.DASHED, point_type=PointType.CIRCLES,
              point_size=6),
    ]

    screen.add_widget(plot)
    screen.write_screen('05_xyplot_traces.bob')
    print(screen)
    print('Wrote 05_xyplot_traces.bob')


if __name__ == '__main__':
    main()
