import phoebusgen.widget._widget as _w
import phoebusgen.widget._property_stubs as _p


class Label(_w.Widget, _p.Text, _p.Font, _p.ForegroundColor, _p.BackgroundColor, _p.Transparent, _p.HorizontalAlignment,
            _p.VerticalAlignment, _p.RotationStep, _p.WrapWords, _p.AutoSize, _p.Border):
    def __init__(self, name, text, x, y, width, height):
        _w.Widget.__init__(self, 'label', name, x, y, width, height)

        self.text(text)


class TextUpdate(_w.Widget, _p.PVName, _p.Font, _p.ForegroundColor, _p.BackgroundColor, _p.Transparent,
                 _p.Format, _p.Precision, _p.ShowUnits, _p.HorizontalAlignment, _p.VerticalAlignment, _p.WrapWords,
                 _p.RotationStep, _p.Border):
    def __init__(self, name, pv_name, x, y, width, height):
        _w.Widget.__init__(self, 'textupdate', name, x, y, width, height)
        self.pv_name(pv_name)


if __name__ == '__main__':
    pass
