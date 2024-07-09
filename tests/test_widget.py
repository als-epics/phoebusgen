import sys
sys.path.insert(1, '../phoebusgen/widget/')
sys.path.insert(1, './phoebusgen/widget/')
import unittest
import widget


class TestWidgetClass(unittest.TestCase):
    def setUp(self):
        self.base_type = 'test_widget_type'
        self.base_name = 'Just Basic Widget Test'
        self.base_x = 10
        self.base_y = 12
        self.base_width = 14
        self.base_height = 15

    def create_basic_widget(self):
        return widget._Widget(self.base_type, self.base_name, self.base_x,
                               self.base_y, self.base_width, self.base_height)

    def test_basic_widget(self):
        widget_type = 'label'
        name = 'Label_1'
        x = 10
        y = 12
        width = 14
        height = 15
        w = widget._Widget(widget_type, name, x, y, width, height)
        self.assertEqual(w.root.tag, 'widget')
        self.assertEqual(w.root.attrib['type'], 'label')
        self.assertEqual(w.root.attrib['version'], '2.0.0')

        self.assertEqual(len(w.root), 5)
        for child in w.root:
            if child.tag == 'name':
                self.assertEqual(child.text, name)
            elif child.tag == 'x':
                self.assertEqual(child.text, str(x))
            elif child.tag == 'y':
                self.assertEqual(child.text, str(y))
            elif child.tag == 'width':
                self.assertEqual(child.text, str(width))
            elif child.tag == 'height':
                self.assertEqual(child.text, str(height))

    def test_visible(self):
        w = self.create_basic_widget()

        self.assertEqual(w.root.tag, 'widget')
        self.assertEqual(w.root.attrib['type'], 'test_widget_type')
        self.assertEqual(w.root.attrib['version'], '2.0.0')

        self.assertEqual(len(w.root), 5)
        for child in w.root:
            if child.tag == 'name':
                self.assertEqual(child.text, self.base_name)
            elif child.tag == 'x':
                self.assertEqual(child.text, str(self.base_x))
            elif child.tag == 'y':
                self.assertEqual(child.text, str(self.base_y))
            elif child.tag == 'width':
                self.assertEqual(child.text, str(self.base_width))
            elif child.tag == 'height':
                self.assertEqual(child.text, str(self.base_height))

        w.visible(False)
        self.assertEqual(len(w.root), 6)
        for child in w.root:
            if child.tag == 'visible':
                self.assertEqual(child.text, 'false')

        self.base_x = 10
        self.base_y = 12
        self.base_width = 14
        self.base_height = 15

    def test_name(self):
        w = self.create_basic_widget()

        self.assertEqual(w.root.tag, 'widget')
        self.assertEqual(w.root.attrib['type'], 'test_widget_type')
        self.assertEqual(w.root.attrib['version'], '2.0.0')

        self.assertEqual(len(w.root), 5)

        w.name('awesome new name')
        for child in w.root:
            if child.tag == 'name':
                self.assertEqual(child.text, 'awesome new name')

    def test_x_and_y(self):
        w = self.create_basic_widget()

        self.assertEqual(w.root.tag, 'widget')
        self.assertEqual(w.root.attrib['type'], 'test_widget_type')
        self.assertEqual(w.root.attrib['version'], '2.0.0')

        self.assertEqual(len(w.root), 5)

        w.x(24)
        for child in w.root:
            if child.tag == 'x':
                self.assertEqual(child.text, str(24))
        w.y(43)
        for child in w.root:
            if child.tag == 'y':
                self.assertEqual(child.text, str(43))

    def test_height_and_width(self):
        w = self.create_basic_widget()

        self.assertEqual(w.root.tag, 'widget')
        self.assertEqual(w.root.attrib['type'], 'test_widget_type')
        self.assertEqual(w.root.attrib['version'], '2.0.0')

        self.assertEqual(len(w.root), 5)

        w.height(12)
        for child in w.root:
            if child.tag == 'height':
                self.assertEqual(child.text, str(12))
        w.width(324)
        for child in w.root:
            if child.tag == 'width':
                self.assertEqual(child.text, str(324))

    def test_embedded_python_script(self):
        w = self.create_basic_widget()
        script = """# Embedded python script
from org.csstudio.display.builder.runtime.script import PVUtil, ScriptUtil
print 'Hello'
# widget.setPropertyValue('text', PVUtil.getString(pvs[0]))"""
        pvs = {'pv0': True, '$(pv_name)': False, 'pv2': True}
        w.embedded_python_script(script, pvs, False)
        self.assertEqual(len(w.root.findall('scripts')), 1)
        self.assertEqual(len(w.root.findall('scripts')[0].findall('script')), 1)
        self.assertEqual(len(w.root.findall('scripts')[0].findall('script')[0].findall('pv_name')), 3)
        pv_elements = w.root.findall('scripts')[0].findall('script')[0].findall('pv_name')
        for pv_element in pv_elements:
            self.assertEqual(pv_element.attrib['trigger'], str(pvs[pv_element.text]).lower())
        script_element = w.root.findall('scripts')[0].findall('script')[0]
        self.assertEqual(script_element.attrib['file'], 'EmbeddedPy')

    def test_embedded_javascript_script(self):
        w = self.create_basic_widget()
        script = """/* Embedded javascript */
importClass(org.csstudio.display.builder.runtime.script.PVUtil);
importClass(org.csstudio.display.builder.runtime.script.ScriptUtil);
logger = ScriptUtil.getLogger();
logger.info("Hello");
/* widget.setPropertyValue("text", PVUtil.getString(pvs[0])); */"""
        pvs = {'pv0': True, '$(pv_name)': False, 'pv2': True}
        w.embedded_javascript_script(script, pvs, True)
        self.assertEqual(len(w.root.findall('scripts')), 1)
        self.assertEqual(len(w.root.findall('scripts')[0].findall('script')), 1)
        self.assertEqual(len(w.root.findall('scripts')[0].findall('script')[0].findall('pv_name')), 3)
        pv_elements = w.root.findall('scripts')[0].findall('script')[0].findall('pv_name')
        for pv_element in pv_elements:
            self.assertEqual(pv_element.attrib['trigger'], str(pvs[pv_element.text]).lower())
        script_element = w.root.findall('scripts')[0].findall('script')[0]
        self.assertEqual(script_element.attrib['file'], 'EmbeddedJs')

    def test_external_script(self):
        w = self.create_basic_widget()
        pvs = {'pv0': True, '$(pv_name)': False}
        file_name = '/path/to/the/amazing/script.py'
        w.external_script(file_name, pvs, False)
        self.assertEqual(len(w.root.findall('scripts')), 1)
        self.assertEqual(len(w.root.findall('scripts')[0].findall('script')), 1)
        self.assertEqual(len(w.root.findall('scripts')[0].findall('script')[0].findall('pv_name')), 2)
        pv_elements = w.root.findall('scripts')[0].findall('script')[0].findall('pv_name')
        for pv_element in pv_elements:
            self.assertEqual(pv_element.attrib['trigger'], str(pvs[pv_element.text]).lower())
        script_element = w.root.findall('scripts')[0].findall('script')[0]
        self.assertEqual(script_element.attrib['file'], file_name)
        self.assertEqual(script_element.attrib['check_connections'], 'false')

    def test_multiple_scripts(self):
        w = self.create_basic_widget()
        pvs = {'pv0': True, '$(pv_name)': False}
        pvs2 = {'$(pv_name)': False}
        file_name = '/path/to/the/amazing/script.py'
        script = """/* Embedded javascript */
        importClass(org.csstudio.display.builder.runtime.script.PVUtil);
        importClass(org.csstudio.display.builder.runtime.script.ScriptUtil);
        logger = ScriptUtil.getLogger();
        logger.info("Hello");
        /* widget.setPropertyValue("text", PVUtil.getString(pvs[0])); */"""
        w.external_script(file_name, pvs, False)
        w.embedded_javascript_script(script, pvs2, True)
        self.assertEqual(len(w.root.findall('scripts')), 1)
        self.assertEqual(len(w.root.findall('scripts')[0].findall('script')), 2)

        script_element1 = w.root.findall('scripts')[0].findall('script')[0]
        self.assertEqual(script_element1.attrib['file'], file_name)
        self.assertEqual(script_element1.attrib['check_connections'], 'false')

        script_element2 = w.root.findall('scripts')[0].findall('script')[1]
        self.assertEqual(script_element2.attrib['file'], 'EmbeddedJs')

    def test_rule(self):
        w = self.create_basic_widget()
        pvs = {'pv0': True, '$(pv_name)': False}
        expressions = {'pv0 == pvStr1': 'test:analog'}
        rule_name = 'My Cool Cool Rule'
        w.rule(rule_name, 'pv_name', pvs, expressions, False)
        self.assertEqual(len(w.root.findall('rules')), 1)
        self.assertEqual(len(w.root.findall('rules')[0].findall('rule')), 1)

        rule_element = w.root.findall('rules')[0].findall('rule')[0]
        self.assertEqual(rule_element.attrib['name'], rule_name)
        self.assertEqual(rule_element.attrib['prop_id'], 'pv_name')
        self.assertEqual(rule_element.attrib['out_exp'], 'false')

        self.assertEqual(len(rule_element.findall('exp')), 1)
        expression_element = rule_element.findall('exp')[0]
        self.assertEqual(expression_element.attrib['bool_exp'], 'pv0 == pvStr1')
        self.assertEqual(expression_element.findall('value')[0].text, 'test:analog')

    def test_rule_integer_param(self):
        w = self.create_basic_widget()
        pvs = {'pv0': True, '$(pv_name)': False}
        expressions = {'pv0 == pvStr1': 'test:analog', 'pv1 == 0': 2}
        rule_name = 'My New Rule'
        w.rule(rule_name, 'pv_name', pvs, expressions, False)
        self.assertEqual(len(w.root.findall('rules')), 1)
        self.assertEqual(len(w.root.findall('rules')[0].findall('rule')), 1)

        rule_element = w.root.findall('rules')[0].findall('rule')[0]
        self.assertEqual(rule_element.attrib['name'], rule_name)
        self.assertEqual(rule_element.attrib['prop_id'], 'pv_name')
        self.assertEqual(rule_element.attrib['out_exp'], 'false')

        self.assertEqual(len(rule_element.findall('exp')), 2)
        expression_element = rule_element.findall('exp')[0]
        self.assertEqual(expression_element.attrib['bool_exp'], 'pv0 == pvStr1')
        self.assertEqual(expression_element.findall('value')[0].text, 'test:analog')
        expression_element_two = rule_element.findall('exp')[1]
        self.assertEqual(expression_element_two.attrib['bool_exp'], 'pv1 == 0')
        self.assertEqual(expression_element_two.findall('value')[0].text, '2')

    def test_rule_color_predefined(self):
        w = self.create_basic_widget()
        pvs = {'pv0': True, '$(pv_name)': False}
        color = {'pvStr0': 'OK'}
        rule_name = 'color rule again'
        w.rule(rule_name, 'color', pvs, color, False)

        rule_element = w.root.findall('rules')[0].findall('rule')[0]
        self.assertEqual(rule_element.attrib['name'], rule_name)
        self.assertEqual(rule_element.attrib['prop_id'], 'color')

    def test_rule_color(self):
        w = self.create_basic_widget()
        pvs = {'pv0': True, '$(pv_name)': False}
        color = {'pvStr0': (5, 10, 15, 20)}
        rule_name = 'color rule'
        w.rule(rule_name, 'color', pvs, color, False)

        rule_element = w.root.findall('rules')[0].findall('rule')[0]
        self.assertEqual(rule_element.attrib['name'], rule_name)
        self.assertEqual(rule_element.attrib['prop_id'], 'color')


class TestGenericWidget(unittest.TestCase):
    def setUp(self):
        self.base_type = 'test_widget_type'

    def create_basic_generic_widget(self):
        return widget._Generic(self.base_type)

    def test_basic_generic_widget(self):
        g = self.create_basic_generic_widget()
        self.assertEqual(g.root.tag, 'test_widget_type')

        self.assertEqual(len(g.root), 0)


if __name__ == '__main__':
    unittest.main()
