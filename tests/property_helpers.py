import os
from enum import Enum
from phoebusgen import _update_color_def, _update_font_def

class GenericTest(object):
    curr_path = os.path.dirname(__file__)
    predefined_colors = _update_color_def(curr_path + '/../phoebusgen/config/color.def')
    colors = Enum('colors', predefined_colors)

    predefined_fonts = _update_font_def(curr_path + '/../phoebusgen/config/font.def')
    fonts = Enum('fonts', predefined_fonts)

    def test_basics(self):
        self.assertEqual(self.element.get_element_value('name'), self.name)
        self.assertEqual(self.element.get_element_value('x'), str(self.x))
        self.assertEqual(self.element.get_element_value('y'), str(self.y))
        self.assertEqual(self.element.get_element_value('width'), str(self.width))
        self.assertEqual(self.element.get_element_value('height'), str(self.height))
        tool_tip = 'this is a test tooltip check it out!'
        self.element.tool_tip(tool_tip)
        self.assertEqual(self.element.get_element_value('tooltip'), tool_tip)
        self.assertEqual(self.element.root.attrib['type'], self.type)

    def test_against_file(self):
        curr_path = os.path.dirname(__file__)
        try:
            open(curr_path + '../files/widgets/{}.bob'.format(self.element.root.attrib['type']))
        except FileNotFoundError:
            print('File Not there!')
            return
        with open(curr_path + '/../files/widgets/{}.bob'.format(self.element.root.attrib['type'])) as f:
            xml = f.read()
            self.assertEqual(xml, self.element.prettify(self.element.root))

    def generic_element_test(self, tag_name, value):
        element = self.element.find_element(tag_name)
        self.assertFalse(isinstance(element, list))
        self.assertIsNotNone(element)
        if value is None:
            self.assertIsNone(element.text)
        else:
            if isinstance(value, bool):
                self.assertEqual(element.text, str(value).lower())
            else:
                self.assertEqual(element.text, str(value))
        self.element.remove_element(tag_name)
        self.assertIsNone(self.element.find_element(tag_name))

    def null_test(self, tag_name):
        self.assertIsNone(self.element.root.find(tag_name))

    # for some properties (actions, macros, you can have multiple children. Pass True to do_not_remove for these
    def child_element_test(self, parent_tag, tag_name, value, attrib, do_not_remove=False):
        parent = self.element.find_element(parent_tag)
        self.assertIsNotNone(parent)
        child = parent.find(tag_name)
        self.assertIsNotNone(child)
        if value is None:
            self.assertIsNone(child.text)
        elif len(parent) == 1:
            self.assertEqual(child.text, str(value))
        else:
            item_lst = []
            for child in parent:
                item_lst.append(child.text)
            index = item_lst.index(value)
            self.assertEqual(str(value) in item_lst, True)
            self.assertEqual(parent[index].text, str(value))
        self.assertEqual(child.attrib, attrib)
        if not do_not_remove:
            self.element.remove_element(parent_tag)
            self.assertIsNone(self.element.find_element(parent_tag))

class InternalTest(object):
    curr_path = os.path.dirname(__file__)
    predefined_colors = _update_color_def(curr_path + '/../phoebusgen/config/color.def')
    colors = Enum('colors', predefined_colors)

    def null_test(self, tag_name):
        self.assertIsNone(self.element.root.find(tag_name))

    def generic_element_test(self, tag_name, value):
        element = self.element.find_element(tag_name)
        self.assertFalse(isinstance(element, list))
        self.assertIsNotNone(element)
        if value is None:
            self.assertIsNone(element.text)
        else:
            if isinstance(value, bool):
                self.assertEqual(element.text, str(value).lower())
            else:
                self.assertEqual(element.text, str(value))
        self.element.remove_element(tag_name)
        self.assertIsNone(self.element.find_element(tag_name))

    def child_element_test(self, parent_tag, tag_name, value, attrib, do_not_remove=False):
        parent = self.element.find_element(parent_tag)
        self.assertIsNotNone(parent)
        child = parent.find(tag_name)
        self.assertIsNotNone(child)
        if value is None:
            self.assertIsNone(child.text)
        elif len(parent) == 1:
            self.assertEqual(child.text, str(value))
        else:
            item_lst = []
            for child in parent:
                item_lst.append(child.text)
            index = item_lst.index(value)
            self.assertEqual(str(value) in item_lst, True)
            self.assertEqual(parent[index].text, str(value))
        self.assertEqual(child.attrib, attrib)
        if not do_not_remove:
            self.element.remove_element(parent_tag)
            self.assertIsNone(self.element.find_element(parent_tag))

class TestPVName(GenericTest):
    def test_pv_name(self):
        self.assertEqual(self.element.find_element('pv_name').text, self.pv_name)

class TestPVNameInternal(InternalTest):
    def test_pv_name(self):
        pv_name = 'test'
        self.element.pv_name(pv_name)
        self.assertEqual(self.element.find_element('pv_name').text, pv_name)

class TestText(GenericTest):
    def test_text(self):
        self.assertEqual(self.element.find_element('text').text, self.text)

class TestFont(GenericTest):
    font_element_name = 'font'
    default_font_family = 'Liberation Sans'
    default_font_style = 'REGULAR'
    default_font_size = '14'

    def test_predefined_font(self):
        self.element.predefined_font(self.fonts.Comment)
        self.child_element_test(self.font_element_name, 'font', None, {'name': 'Comment', 'family': 'Liberation Sans', 'size': '14', 'style': 'ITALIC'})

    def test_predefined_font2(self):
        self.element.predefined_font(self.fonts.Header1)
        self.child_element_test(self.font_element_name, 'font', None, {'name': 'Header 1', 'family': 'Liberation Sans', 'size': '22', 'style': 'BOLD'})

    def test_font_family(self):
        value = 'Liberation Serif'
        self.element.font_family(value)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_font_family2(self):
        value = 'Noto Sans Sinhala'
        self.element.font_family(value)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_font_size(self):
        value = 72.0
        self.element.font_size(value)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': str(int(value)), 'style': self.default_font_style})

    def test_font_size_wrong(self):
        value = 'tset'
        self.element.font_size(value)
        self.null_test(self.font_element_name)

    def test_multiple_fonts(self):
        size_val = 26
        self.element.font_size(size_val)
        self.element.font_style_bold_italic()
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': str(int(size_val)), 'style': 'BOLD_ITALIC'})

    def test_change_font_attributes(self):
        value = 'Liberation Serif'
        self.element.font_family(value)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})
        value = 'Cantarell'
        self.element.font_family(value)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_font_style_regular(self):
        self.element.font_style_regular()
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'REGULAR'})

    def test_font_style_bold(self):
        self.element.font_style_bold()
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'BOLD'})

    def test_font_style_bold_italic(self):
        self.element.font_style_bold_italic()
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'BOLD_ITALIC'})

    def test_font_style_italic(self):
        self.element.font_style_italic()
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'ITALIC'})

    def test_defaults(self):
        self.element.font_family(self.default_font_family)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': self.default_font_style})

class TestTitleFont(GenericTest):
    font_element_name = 'title_font'
    default_font_family = 'Liberation Sans'
    default_font_style = 'REGULAR'
    default_font_size = '14'

    def test_title_predefined_font(self):
        self.element.predefined_title_font(self.fonts.Comment)
        self.child_element_test(self.font_element_name, 'font', None, {'name': 'Comment', 'family': 'Liberation Sans', 'size': '14', 'style': 'ITALIC'})

    def test_title_predefined_font2(self):
        self.element.predefined_title_font(self.fonts.Header1)
        self.child_element_test(self.font_element_name, 'font', None, {'name': 'Header 1', 'family': 'Liberation Sans', 'size': '22', 'style': 'BOLD'})

    def test_title_font_family(self):
        value = 'Liberation Serif'
        self.element.title_font_family(value)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_title_font_family2(self):
        value = 'Noto Sans Sinhala'
        self.element.title_font_family(value)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_title_font_size(self):
        value = 72.0
        self.element.title_font_size(value)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': str(int(value)), 'style': self.default_font_style})

    def test_title_font_size_wrong(self):
        value = 'tset'
        self.element.title_font_size(value)
        self.null_test(self.font_element_name)

    def test_title_multiple_fonts(self):
        size_val = 26
        self.element.title_font_size(size_val)
        self.element.title_font_style_bold_italic()
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': str(int(size_val)), 'style': 'BOLD_ITALIC'})

    def test_title_change_font_attributes(self):
        value = 'Liberation Serif'
        self.element.title_font_family(value)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})
        value = 'Cantarell'
        self.element.title_font_family(value)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_title_font_style_regular(self):
        self.element.title_font_style_regular()
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'REGULAR'})

    def test_title_font_style_bold(self):
        self.element.title_font_style_bold()
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'BOLD'})

    def test_title_font_style_bold_italic(self):
        self.element.title_font_style_bold_italic()
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'BOLD_ITALIC'})

    def test_title_font_style_italic(self):
        self.element.title_font_style_italic()
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'ITALIC'})

    def test_title_defaults(self):
        self.element.title_font_family(self.default_font_family)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': self.default_font_style})

class TestTitleFontInternal(InternalTest):
    font_element_name = 'title_font'
    default_font_family = 'Liberation Sans'
    default_font_style = 'REGULAR'
    default_font_size = '14'

    def test_title_predefined_font(self):
        self.element.predefined_title_font('Comment')
        self.child_element_test(self.font_element_name, 'font', None, {'name': 'Comment', 'family': 'Liberation Sans', 'size': '14', 'style': 'ITALIC'})

    def test_title_predefined_font2(self):
        self.element.predefined_title_font('Header1')
        self.child_element_test(self.font_element_name, 'font', None, {'name': 'Header 1', 'family': 'Liberation Sans', 'size': '22', 'style': 'BOLD'})

    def test_title_font_family(self):
        value = 'Liberation Serif'
        self.element.title_font_family(value)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_title_font_family2(self):
        value = 'Noto Sans Sinhala'
        self.element.title_font_family(value)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_title_font_size(self):
        value = 72.0
        self.element.title_font_size(value)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': str(int(value)), 'style': self.default_font_style})

    def test_title_font_size_wrong(self):
        value = 'tset'
        self.element.title_font_size(value)
        self.null_test(self.font_element_name)

    def test_title_multiple_fonts(self):
        size_val = 26
        self.element.title_font_size(size_val)
        self.element.title_font_style_bold_italic()
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': str(int(size_val)), 'style': 'BOLD_ITALIC'})

    def test_title_change_font_attributes(self):
        value = 'Liberation Serif'
        self.element.title_font_family(value)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})
        value = 'Cantarell'
        self.element.title_font_family(value)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_title_font_style_regular(self):
        self.element.title_font_style_regular()
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'REGULAR'})

    def test_title_font_style_bold(self):
        self.element.title_font_style_bold()
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'BOLD'})

    def test_title_font_style_bold_italic(self):
        self.element.title_font_style_bold_italic()
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'BOLD_ITALIC'})

    def test_title_font_style_italic(self):
        self.element.title_font_style_italic()
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'ITALIC'})

    def test_title_defaults(self):
        self.element.title_font_family(self.default_font_family)
        self.child_element_test(self.font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': self.default_font_style})


class TestLabelFont(GenericTest):
    label_font_element_name = 'label_font'
    default_font_family = 'Liberation Sans'
    default_font_style = 'REGULAR'
    default_font_size = '14'

    def test_label_predefined_font(self):
        self.element.predefined_label_font(self.fonts.Comment)
        print(self.element)
        self.child_element_test(self.label_font_element_name, 'font', None, {'name': 'Comment', 'family': 'Liberation Sans', 'size': '14', 'style': 'ITALIC'})

    def test_label_predefined_font2(self):
        self.element.predefined_label_font(self.fonts.Header1)
        print(self.element)
        self.child_element_test(self.label_font_element_name, 'font', None, {'name': 'Header 1', 'family': 'Liberation Sans', 'size': '22', 'style': 'BOLD'})

    def test_label_font_family(self):
        value = 'Liberation Serif'
        self.element.label_font_family(value)
        print(self.element)
        self.child_element_test(self.label_font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_label_font_family2(self):
        value = 'Noto Sans Sinhala'
        self.element.label_font_family(value)
        self.child_element_test(self.label_font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_label_font_size(self):
        value = 72.0
        self.element.label_font_size(value)
        self.child_element_test(self.label_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': str(int(value)), 'style': self.default_font_style})

    def test_label_font_size_wrong(self):
        value = 'tset'
        self.element.label_font_size(value)
        self.null_test(self.label_font_element_name)

    def test_label_multiple_fonts(self):
        size_val = 26
        self.element.label_font_size(size_val)
        self.element.label_font_style_bold_italic()
        self.child_element_test(self.label_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': str(int(size_val)), 'style': 'BOLD_ITALIC'})

    def test_label_change_font_attributes(self):
        value = 'Liberation Serif'
        self.element.label_font_family(value)
        self.child_element_test(self.label_font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})
        value = 'Cantarell'
        self.element.label_font_family(value)
        self.child_element_test(self.label_font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_label_font_style_regular(self):
        self.element.label_font_style_regular()
        self.child_element_test(self.label_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'REGULAR'})

    def test_label_font_style_bold(self):
        self.element.label_font_style_bold()
        self.child_element_test(self.label_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'BOLD'})

    def test_label_font_style_bold_italic(self):
        self.element.label_font_style_bold_italic()
        self.child_element_test(self.label_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'BOLD_ITALIC'})

    def test_label_font_style_italic(self):
        self.element.label_font_style_italic()
        self.child_element_test(self.label_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'ITALIC'})

    def test_label_defaults(self):
        self.element.label_font_family(self.default_font_family)
        self.child_element_test(self.label_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': self.default_font_style})


class TestScaleFont(GenericTest):
    scale_font_element_name = 'scale_font'
    default_font_family = 'Liberation Sans'
    default_font_style = 'REGULAR'
    default_font_size = '14'

    def test_scale_predefined_font(self):
        self.element.predefined_scale_font(self.fonts.Comment)
        self.child_element_test(self.scale_font_element_name, 'font', None, {'name': 'Comment', 'family': 'Liberation Sans', 'size': '14', 'style': 'ITALIC'})

    def test_scale_predefined_font2(self):
        self.element.predefined_scale_font(self.fonts.Header1)
        self.child_element_test(self.scale_font_element_name, 'font', None, {'name': 'Header 1', 'family': 'Liberation Sans', 'size': '22', 'style': 'BOLD'})

    def test_scale_font_family(self):
        value = 'Liberation Serif'
        self.element.scale_font_family(value)
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_scale_font_family2(self):
        value = 'Noto Sans Sinhala'
        self.element.scale_font_family(value)
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_scale_font_size(self):
        value = 72.0
        self.element.scale_font_size(value)
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': str(int(value)), 'style': self.default_font_style})

    def test_scale_font_size_wrong(self):
        value = 'tset'
        self.element.scale_font_size(value)
        self.null_test(self.scale_font_element_name)

    def test_scale_multiple_fonts(self):
        size_val = 26
        self.element.scale_font_size(size_val)
        self.element.scale_font_style_bold_italic()
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': str(int(size_val)), 'style': 'BOLD_ITALIC'})

    def test_scale_change_font_attributes(self):
        value = 'Liberation Serif'
        self.element.scale_font_family(value)
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})
        value = 'Cantarell'
        self.element.scale_font_family(value)
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_scale_font_style_regular(self):
        self.element.scale_font_style_regular()
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'REGULAR'})

    def test_scale_font_style_bold(self):
        self.element.scale_font_style_bold()
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'BOLD'})

    def test_scale_font_style_bold_italic(self):
        self.element.scale_font_style_bold_italic()
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'BOLD_ITALIC'})

    def test_scale_font_style_italic(self):
        self.element.scale_font_style_italic()
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'ITALIC'})

    def test_scale_defaults(self):
        self.element.scale_font_family(self.default_font_family)
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': self.default_font_style})

class TestScaleFontInternal(InternalTest):
    scale_font_element_name = 'scale_font'
    default_font_family = 'Liberation Sans'
    default_font_style = 'REGULAR'
    default_font_size = '14'

    def test_scale_predefined_font(self):
        self.element.predefined_scale_font('Comment')
        self.child_element_test(self.scale_font_element_name, 'font', None, {'name': 'Comment', 'family': 'Liberation Sans', 'size': '14', 'style': 'ITALIC'})

    def test_scale_predefined_font2(self):
        self.element.predefined_scale_font('Header1')
        self.child_element_test(self.scale_font_element_name, 'font', None, {'name': 'Header 1', 'family': 'Liberation Sans', 'size': '22', 'style': 'BOLD'})

    def test_scale_font_family(self):
        value = 'Liberation Serif'
        self.element.scale_font_family(value)
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_scale_font_family2(self):
        value = 'Noto Sans Sinhala'
        self.element.scale_font_family(value)
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_scale_font_size(self):
        value = 72.0
        self.element.scale_font_size(value)
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': str(int(value)), 'style': self.default_font_style})

    def test_scale_font_size_wrong(self):
        value = 'tset'
        self.element.scale_font_size(value)
        self.null_test(self.scale_font_element_name)

    def test_scale_multiple_fonts(self):
        size_val = 26
        self.element.scale_font_size(size_val)
        self.element.scale_font_style_bold_italic()
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': str(int(size_val)), 'style': 'BOLD_ITALIC'})

    def test_scale_change_font_attributes(self):
        value = 'Liberation Serif'
        self.element.scale_font_family(value)
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})
        value = 'Cantarell'
        self.element.scale_font_family(value)
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': value, 'size': self.default_font_size, 'style': self.default_font_style})

    def test_scale_font_style_regular(self):
        self.element.scale_font_style_regular()
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'REGULAR'})

    def test_scale_font_style_bold(self):
        self.element.scale_font_style_bold()
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'BOLD'})

    def test_scale_font_style_bold_italic(self):
        self.element.scale_font_style_bold_italic()
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'BOLD_ITALIC'})

    def test_scale_font_style_italic(self):
        self.element.scale_font_style_italic()
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': 'ITALIC'})

    def test_scale_defaults(self):
        self.element.scale_font_family(self.default_font_family)
        self.child_element_test(self.scale_font_element_name, 'font', None,
                                {'family': self.default_font_family, 'size': self.default_font_size, 'style': self.default_font_style})

class TestForegroundColor(GenericTest):
    def test_predefined_foreground_color(self):
        tag_name = 'foreground_color'
        self.element.predefined_foreground_color(self.colors.Background)
        self.child_element_test(tag_name, 'color', None, {'name': 'Background', 'red': '255', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})

    def test_foreground_color(self):
        tag_name = 'foreground_color'
        self.element.foreground_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '255'})


class TestBackgroundColor(GenericTest):
    def test_predefined_background_color(self):
        tag_name = 'background_color'
        self.element.predefined_background_color(self.colors.MINOR)
        self.child_element_test(tag_name, 'color', None, {'name': 'MINOR', 'red': '255', 'green': '128', 'blue': '0', 'alpha': '255'})

    def test_background_color(self):
        tag_name = 'background_color'
        self.element.background_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10', 'blue': '15', 'alpha': '255'})


class TestTransparent(GenericTest):
    def test_transparent(self):
        tag_name = 'transparent'
        value = True
        self.element.transparent(value)
        self.generic_element_test(tag_name, value)


class TestFormat(GenericTest):
    def test_format(self):
        tag_name = 'format'
        value = 'Engineering'
        xml_value = '3'
        self.element.format(value)
        self.generic_element_test(tag_name, xml_value)


class TestPrecision(GenericTest):
    def test_precision(self):
        tag_name = 'precision'
        value = 25.3
        real_value = '25'
        self.element.precision(value)
        self.generic_element_test(tag_name, real_value)


class TestShowUnits(GenericTest):
    def test_show_units(self):
        tag_name = 'show_units'
        value = False
        self.element.show_units(value)
        self.generic_element_test(tag_name, value)


class TestHorizontalAlignment(GenericTest):
    def test_horizontal_alignment(self):
        tag_name = 'horizontal_alignment'
        xml_value = 1
        self.element.horizontal_alignment_center()
        self.generic_element_test(tag_name, xml_value)

    def test_horizontal_alignment_left(self):
        tag_name = 'horizontal_alignment'
        xml_value = 0
        self.element.horizontal_alignment_right()
        self.element.horizontal_alignment_left()
        self.generic_element_test(tag_name, xml_value)

    def test_horizontal_alignment_right(self):
        tag_name = 'horizontal_alignment'
        xml_value = 2
        self.element.horizontal_alignment_right()
        self.generic_element_test(tag_name, xml_value)

class TestVerticalAlignment(GenericTest):
    def test_vertical_alignment_1(self):
        tag_name = 'vertical_alignment'
        xml_value = 1
        self.element.vertical_alignment_middle()
        self.generic_element_test(tag_name, xml_value)

    def test_vertical_alignment_0(self):
        tag_name = 'vertical_alignment'
        xml_value = 0
        self.element.vertical_alignment_top()
        self.generic_element_test(tag_name, xml_value)

    def test_vertical_alignment_2(self):
        tag_name = 'vertical_alignment'
        xml_value = 2
        self.element.vertical_alignment_bottom()
        self.generic_element_test(tag_name, xml_value)

class TestWrapWords(GenericTest):
    def test_wrap_words(self):
        tag_name = 'wrap_words'
        value = False
        self.element.wrap_words(value)
        self.generic_element_test(tag_name, value)


class TestRotationStep(GenericTest):
    def test_rotation_step(self):
        tag_name = 'rotation_step'
        xml_value = 2
        self.element.rotation_step_180()
        self.generic_element_test(tag_name, xml_value)

    def test_rotation_step_0(self):
        tag_name = 'rotation_step'
        xml_value = 0
        self.element.rotation_step_180()
        self.element.rotation_step_0()
        self.generic_element_test(tag_name, xml_value)

    def test_rotation_step_90(self):
        tag_name = 'rotation_step'
        xml_value = 1
        self.element.rotation_step_90()
        self.generic_element_test(tag_name, xml_value)

    def test_rotation_step_minus_90(self):
        tag_name = 'rotation_step'
        xml_value = 3
        self.element.rotation_step_negative_90()
        self.generic_element_test(tag_name, xml_value)

class TestBorder(GenericTest):
    def test_border_width(self):
        tag_name = 'border_width'
        value = 2
        self.element.border_width(value)
        self.generic_element_test(tag_name, value)

    def test_border_color(self):
        tag_name = 'border_color'
        self.element.border_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10', 'blue': '15', 'alpha': '255'})

    def test_predefined_border_color(self):
        tag_name = 'border_color'
        self.element.predefined_border_color(self.colors.Attention)
        self.child_element_test(tag_name, 'color', None, {'name': 'Attention', 'red': '255', 'green': '160',
                                                          'blue': '0', 'alpha': '255'})


class TestMacro(GenericTest):
    def test_macro(self):
        self.element.macro('test', 'mac1')
        self.child_element_test('macros', 'test', 'mac1', {}, True)
        self.element.macro('test2', 'mac2')
        self.child_element_test('macros', 'test', 'mac1', {}, True)
        self.child_element_test('macros', 'test2', 'mac2', {}, True)
        print(self.element)


class TestBit(GenericTest):
    tag_name = 'bit'

    def test_bit_with_number(self):
        value = 234
        self.element.bit(value)
        self.generic_element_test(self.tag_name, value)

    def test_default_bit(self):
        self.element.bit()
        self.generic_element_test(self.tag_name, -1)


class TestAutoSize(GenericTest):

    def test_auto_size(self):
        tag_name = 'auto_size'
        val = False
        self.element.auto_size(val)
        self.generic_element_test(tag_name, val)

    def test_auto_size_default(self):
        tag_name = 'auto_size'
        self.element.auto_size()
        self.generic_element_test(tag_name, True)


class TestMultiLine(GenericTest):
    def test_multi_line(self):
        tag_name = 'multi_line'
        val = True
        self.element.multi_line(val)
        self.generic_element_test(tag_name, val)


class TestSquare(GenericTest):
    def test_square(self):
        tag_name = 'square'
        val = True
        self.element.square(val)
        self.generic_element_test(tag_name, val)


class TestLabelsFromPV(GenericTest):
    def test_labels_from_pv(self):
        tag_name = 'labels_from_pv'
        val = True
        self.element.labels_from_pv(val)
        self.generic_element_test(tag_name, val)


class TestAlarmBorder(GenericTest):
    def test_alarm_border(self):
        tag_name = 'border_alarm_sensitive'
        val = True
        self.element.alarm_border(val)
        self.generic_element_test(tag_name, val)


class TestEnabled(GenericTest):
    def test_enabled(self):
        tag_name = 'enabled'
        val = False
        self.element.enabled(val)
        self.generic_element_test(tag_name, val)


class TestLineWidth(GenericTest):
    tag_name = 'line_width'

    def test_line_width(self):
        val = 5
        self.element.line_width(val)
        self.generic_element_test(self.tag_name, val)

    def test_line_width_wrong(self):
        val = 'asdfs'
        self.element.line_width(val)
        self.null_test(self.tag_name)

class TestLineWidthInternal(InternalTest):
    tag_name = 'line_width'

    def test_line_width(self):
        val = 5
        self.element.line_width(val)
        self.generic_element_test(self.tag_name, val)

    def test_line_width_wrong(self):
        val = 'asdfs'
        self.element.line_width(val)
        self.null_test(self.tag_name)


class TestCorner(GenericTest):
    def test_corner_width(self):
        tag_name = 'corner_width'
        val = 5
        self.element.corner_width(val)
        self.generic_element_test(tag_name, val)

    def test_corner_width_string(self):
        tag_name = 'corner_width'
        val = 'asdjflksdjf'
        self.element.corner_width(val)
        self.null_test(tag_name)

    def test_corner_height(self):
        tag_name = 'corner_height'
        val = 5
        self.element.corner_height(val)
        self.generic_element_test(tag_name, val)

    def test_corner_height_string(self):
        tag_name = 'corner_height'
        val = 'asdjflksdjf'
        self.element.corner_height(val)
        self.null_test(tag_name)


class TestAngle(GenericTest):
    def test_angle_start(self):
        tag_name = 'start_angle'
        val = 32
        self.element.angle_start(val)
        self.generic_element_test(tag_name, val)

    def test_angle_size(self):
        tag_name = 'total_angle'
        val = 92
        self.element.angle_size(val)
        self.generic_element_test(tag_name, val)


class TestConfirmation(GenericTest):
    dialog_tag = 'show_confirm_dialog'
    message_tag = 'confirm_message'
    password_tag = 'password'
    message = 'Are you sure?'

    def test_confirmation_no_password(self):
        self.element.confirmation_dialog(self.message)
        self.generic_element_test(self.message_tag, self.message)
        self.generic_element_test(self.dialog_tag, True)
        self.null_test(self.password_tag)
        self.null_test(self.password_tag)

    def test_confirmation_with_password(self):
        password = '1234569999'
        self.element.confirmation_dialog(self.message, password)
        self.generic_element_test(self.message_tag, self.message)
        self.generic_element_test(self.dialog_tag, True)
        self.generic_element_test(self.password_tag, password)

    def test_turn_off_confirmation(self):
        password = 235893
        self.element.confirmation_dialog(self.message, password)
        self.generic_element_test(self.message_tag, self.message)
        self.generic_element_test(self.dialog_tag, True)
        self.generic_element_test(self.password_tag, password)
        self.element.confirmation_dialog(self.message, password)
        self.element.disable_confirmation_dialog()
        self.generic_element_test(self.password_tag, password)
        self.generic_element_test(self.message_tag, self.message)
        self.generic_element_test(self.dialog_tag, False)

class TestLineColor(GenericTest):
    def test_predefined_line_color(self):
        tag_name = 'line_color'
        self.element.predefined_line_color(self.colors.Background)
        self.child_element_test(tag_name, 'color', None, {'name': 'Background', 'red': '255', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})

    def test_line_color(self):
        tag_name = 'line_color'
        self.element.line_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '255'})

    def test_predefined_line_color_group(self):
        tag_name = 'line_color'
        self.element.version('2.0.0')
        self.element.predefined_line_color(self.colors.Background)
        if self.type == 'group':
            self.assertIsNone(self.element.root.find('line_color'))
        else:
            self.child_element_test(tag_name, 'color', None, {'name': 'Background', 'red': '255', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})

    def test_line_color_group(self):
        tag_name = 'line_color'
        self.element.version('2.0.0')
        self.element.line_color(5, 10, 15)
        if self.type == 'group':
            self.assertIsNone(self.element.root.find('line_color'))
        else:
            self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '255'})

    def test_predefined_line_color_group2(self):
        tag_name = 'line_color'
        self.element.version('3.1.2')
        self.element.predefined_line_color(self.colors.Background)
        self.child_element_test(tag_name, 'color', None, {'name': 'Background', 'red': '255', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})

    def test_line_color_group2(self):
        tag_name = 'line_color'
        self.element.version('3.1.2')
        self.element.line_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '255'})

class TestOffColor(GenericTest):
    def test_predefined_off_color(self):
        tag_name = 'off_color'
        self.element.predefined_off_color(self.colors.Background)
        self.child_element_test(tag_name, 'color', None, {'name': 'Background', 'red': '255', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})

    def test_predefined_off_color2(self):
        tag_name = 'off_color'
        self.element.predefined_off_color('Background')
        self.child_element_test(tag_name, 'color', None, {'name': 'Background', 'red': '255', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})

    def test_predefined_off_color3(self):
        tag_name = 'off_color'
        self.element.predefined_off_color({'name': 'Background', 'red': '255', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})
        self.child_element_test(tag_name, 'color', None, {'name': 'Background', 'red': '255', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})

    def test_off_color(self):
        tag_name = 'off_color'
        self.element.off_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '255'})

class TestOff(TestOffColor):
    def test_off_label(self):
        tag_name = 'off_label'
        value = 'This is off!'
        self.element.off_label(value)
        self.generic_element_test(tag_name, value)

class TestOnColor(GenericTest):
    def test_predefined_on_color(self):
        tag_name = 'on_color'
        self.element.predefined_on_color(self.colors.Background)
        self.child_element_test(tag_name, 'color', None, {'name': 'Background', 'red': '255', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})

    def test_on_color(self):
        tag_name = 'on_color'
        self.element.on_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '255'})

class TestOn(TestOnColor):
    def test_on_label(self):
        tag_name = 'on_label'
        value = 'This is on!'
        self.element.on_label(value)
        self.generic_element_test(tag_name, value)

class TestStretchToFit(GenericTest):
    def test_stretch_to_fit1(self):
        tag_name = 'stretch_image'
        val = False
        self.element.stretch_to_fit(val)
        self.generic_element_test(tag_name, val)

    def test_stretch_to_fit2(self):
        tag_name = 'stretch_image'
        val = 'false'
        self.element.stretch_to_fit(val)
        self.generic_element_test(tag_name, False)

    def test_stretch_to_fit3(self):
        tag_name = 'stretch_image'
        val = True
        self.element.stretch_to_fit(val)
        self.generic_element_test(tag_name, val)

    def test_stretch_to_fit4(self):
        tag_name = 'stretch_image'
        val = 1
        self.element.stretch_to_fit(val)
        self.generic_element_test(tag_name, True)


class TestFile(GenericTest):
    # file is a constructor param for widgets (similar to x or pv_name)
    # so we don't have to add it here, just test that it made it
    def test_file(self):
        tag_name = 'file'
        self.generic_element_test(tag_name, self.file)

class TestFileInternal(InternalTest):
    # ROI-specific test -> ROI object does not have a file parameter in its constructor
    def test_file(self):
        tag_name = 'file'
        self.element.file(tag_name)
        self.generic_element_test(tag_name, 'file')


class TestRotation(GenericTest):
    tag_name = 'rotation'

    def test_rotation1(self):
        val = 24
        self.element.rotation(val)
        self.generic_element_test(self.tag_name, val)

    def test_rotation2(self):
        val = -12.2
        self.element.rotation(val)
        self.generic_element_test(self.tag_name, val)

    def test_rotation3(self):
        val = 142.2
        self.element.rotation(val)
        self.generic_element_test(self.tag_name, val)

    def test_rotation4(self):
        val = 'sadfdsf'
        self.element.rotation(val)
        self.null_test(self.tag_name)


class TestResizeBehavior(GenericTest):
    tag_name = 'resize'
    def test_no_resize(self):
        self.element.no_resize()
        self.generic_element_test(self.tag_name, 0)

    def test_size_content_to_fit_widget(self):
        self.element.size_content_to_fit_widget()
        self.generic_element_test(self.tag_name, 1)

    def test_size_widget_to_match_content(self):
        self.element.size_widget_to_match_content()
        self.generic_element_test(self.tag_name, 2)


    def test_stretch_content_to_fit_widget(self):
        self.element.stretch_content_to_fit_widget()
        self.generic_element_test(self.tag_name, 3)

    def test_crop_content(self):
        self.element.crop_content()
        self.generic_element_test(self.tag_name, 4)


class TestGroupName(GenericTest):
    # we should be able to add property multiple times, with only the latest being added to xml
    def test_add_twice(self):
        tag_name = 'group_name'
        val = 'test2'
        self.element.group_name('test')
        self.element.group_name(val)
        self.generic_element_test(tag_name, val)

class TestStyle(GenericTest):
    def test_add_elem_twice(self):
        self.element.style_group_box()
        self.generic_element_test('style', 0)

    def test_title_bar(self):
        self.element.style_title_bar()
        self.generic_element_test('style', 1)

    def test_line(self):
        self.element.style_line()
        self.generic_element_test('style', 2)

    def test_no_style(self):
        self.element.no_style()
        self.generic_element_test('style', 3)


class TestLabel(GenericTest):
    def test_label(self):
        tag_name = 'label'
        self.generic_element_test(tag_name, self.label)

class TestItemsFromPV(GenericTest):
    def test_on(self):
        tag_name = 'items_from_pv'
        self.element.items_from_pv(True)
        self.generic_element_test(tag_name, True)

    def test_off(self):
        tag_name = 'items_from_pv'
        self.element.items_from_pv(False)
        self.generic_element_test(tag_name, False)

class TestItems(GenericTest):
    def test_add_item(self):
        tag_name = 'items'
        val = 'Item Number Uno'
        self.element.item(val)
        self.child_element_test(tag_name, 'item', val, {}, True)
        val2 = 'Item Number Dos'
        self.element.item(val2)
        self.child_element_test(tag_name, 'item', val, {}, True)
        self.child_element_test(tag_name, 'item', val2, {}, True)

class TestActions(GenericTest):
    def action_test(self, action_type, desc, action_args, macros=None):
        parent_element = self.element.find_element('actions')
        self.assertTrue(len(parent_element) > 0)
        for parent in parent_element:
            if parent.attrib == {'type': action_type}:
                description = parent.find('description')
                self.assertEqual(description.text, desc)
                for key, value in action_args.items():
                    elem = parent.find(key)
                    self.assertIsNotNone(elem)
                    self.assertEqual(elem.text, value)
                if macros is not None:
                    macro_parent = parent.find('macros')
                    self.assertIsNotNone(macro_parent)
                    for k, v in macros.items():
                        mac = macro_parent.find(k)
                        self.assertIsNotNone(mac)
                        self.assertEqual(v, mac.text)

    def script_test(self, script_file, desc, script=None):
        parent_element = self.element.find_element('actions')
        self.assertTrue(len(parent_element) > 0)
        foundIt = False
        for parent in parent_element:
            if parent.attrib == {'type': 'execute'}:
                foundIt = True
                description = parent.find('description')
                self.assertEqual(description.text, desc)
                script_element = parent.find('script')
                self.assertIsNotNone(script_element)
                self.assertEqual(script_file, script_element.attrib['file'])
                if script_file == 'EmbeddedPy' or script_file == 'EmbeddedJs':
                    text_element = script_element.find('text')
                    self.assertIsNotNone(text_element)
                    self.assertEqual(text_element.text, script)
        self.assertTrue(foundIt);

    def test_execute_as_one(self):
        tag_name = 'actions'
        self.element.action_execute_as_one(True)
        file = 'test.bob'
        target = 'TaB'
        self.element.action_open_display(file, target)
        self.child_element_test(tag_name, 'action', None, {'type': 'open_display'})

    def test_execute_as_one_str(self):
        tag_name = 'actions'
        self.element.action_execute_as_one('True')
        file = 'test.bob'
        target = 'TaB'
        self.element.action_open_display(file, target)
        self.child_element_test(tag_name, 'action', None, {'type': 'open_display'})

    def test_execute_as_one_str_wrong(self):
        tag_name = 'actions'
        self.element.action_execute_as_one('abc')
        file = 'test.bob'
        target = 'TaB'
        self.element.action_open_display(file, target)
        self.child_element_test(tag_name, 'action', None, {'type': 'open_display'})

    def test_execute_as_one_int(self):
        tag_name = 'actions'
        self.element.action_execute_as_one(1)
        file = 'test.bob'
        target = 'TaB'
        self.element.action_open_display(file, target)
        self.child_element_test(tag_name, 'action', None, {'type': 'open_display'})

    def test_open_display(self):
        file = 'test.bob'
        target = 'TaB'
        self.element.action_open_display(file, target)
        self.action_test('open_display', 'Open Display', {'file': file, 'target': 'tab'})

    def test_open_display2(self):
        file = 'test.bob'
        target = 'winDow'
        self.element.action_open_display(file, target)
        self.action_test('open_display', 'Open Display', {'file': file, 'target': 'window'})

    def test_open_display3(self):
        file = 'test.bob'
        target = 'replace'
        self.element.action_open_display(file, target)
        self.action_test('open_display', 'Open Display', {'file': file, 'target': 'replace'})

    def test_open_display_desc(self):
        file = 'test.bob'
        target = 'replace'
        desc = 'my description'
        self.element.action_open_display(file, target, desc)
        self.action_test('open_display', desc, {'file': file, 'target': 'replace'})

    def test_open_display_macros(self):
        file = 'test.bob'
        target = 'replace'
        macro_dict = {'TestMac': '1', 'MOD': 'Mod1'}
        self.element.action_open_display(file, target, macros=macro_dict)
        self.action_test('open_display', 'Open Display', {'file': file, 'target': 'replace'}, macro_dict)

    def test_open_display_macros_wrong_type(self):
        file = 'test.bob'
        target = 'replace'
        macro_str = 'TestMac'
        self.assertIsNone(self.element.action_open_display(file, target, macros=macro_str))

    def test_open_display_macros_and_desc(self):
        file = 'test.bob'
        target = 'replace'
        desc = 'test test test'
        self.element.action_open_display(file, target, desc, {'BPM': 'BPMA'})
        self.action_test('open_display', desc, {'file': file, 'target': 'replace'}, {'BPM': 'BPMA'})

    def test_open_display_wrong_target(self):
        file = 'test.bob'
        target = 'hello'
        self.assertIsNone(self.element.action_open_display(file, target))

    def test_write_pv(self):
        pv = 'TEST:PV'
        value = 235
        description = 'This is my action'
        self.element.action_write_pv(pv, value, description)
        self.action_test('write_pv', description, {'pv_name': pv, 'value': str(value), 'description': description})

    def test_write_pv_no_desc(self):
        pv = 'TEST:PV'
        value = 235
        self.element.action_write_pv(pv, value)
        self.action_test('write_pv', 'Write PV', {'pv_name': pv, 'value': str(value), 'description': 'Write PV'})

    def test_execute_command(self):
        command = '/bin/bash /home/test.sh'
        description = 'test description'
        self.element.action_execute_command(command, description)
        self.action_test('command', description, {'command': command})

    def test_execute_command_no_desc(self):
        command = '/bin/bash /home/test.sh'
        self.element.action_execute_command(command)
        self.action_test('command', 'Execute Command', {'command': command})

    def test_open_file(self):
        file_name = '/home/my-file.pdf'
        self.element.action_open_file(file_name)
        self.action_test('open_file', 'Open File', {'file': file_name})
        file = 'test.bob'
        target = 'replace'
        self.element.action_open_display(file, target)
        self.action_test('open_display', 'Open Display', {'file': file, 'target': 'replace'})

    def test_open_webpage(self):
        url = 'https://tynanford.com'
        self.element.action_open_webpage(url)
        self.action_test('open_webpage', 'Open Webpage', {'url': url})

    def test_execute_python_script(self):
        script = '''# Embedded python script
from org.csstudio.display.builder.runtime.script import PVUtil, ScriptUtil
print 'Hello'
# widget.setPropertyValue('text', PVUtil.getString(pvs[0]))

PVUtil.writePV("loc://test", 5, 1000)
        '''
        self.element.action_execute_python_script(script)
        self.action_test('execute', 'Execute Script', {'script': None})
        self.script_test('EmbeddedPy', 'Execute Script', script)

    def test_execute_javascript_script(self):
        script = '''/* Embedded javascript */
importClass(org.csstudio.display.builder.runtime.script.PVUtil);
importClass(org.csstudio.display.builder.runtime.script.ScriptUtil);
logger = ScriptUtil.getLogger();
logger.info("Hello");
/* widget.setPropertyValue("text", PVUtil.getString(pvs[0])); */
        '''
        self.element.action_execute_javascript_script(script)
        self.action_test('execute', 'Execute Script', {'script': None})
        self.script_test('EmbeddedJs', 'Execute Script', script)

    def test_execute_external_script(self):
        file_name = 'test.py'
        self.element.action_execute_external_script(file_name)
        self.action_test('execute', 'Execute Script', {'script': None})
        self.script_test(file_name, 'Execute Script')

class TestHorizontal(GenericTest):
    def test_default(self):
        tag_name = 'horizontal'
        self.element.horizontal(True)
        self.generic_element_test(tag_name, True)

    def test_off(self):
        tag_name = 'horizontal'
        self.element.horizontal(False)
        self.generic_element_test(tag_name, False)


class TestFillColor(GenericTest):
    def test_predefined_fill_color(self):
        tag_name = 'fill_color'
        self.element.predefined_fill_color(self.colors.INVALID)
        self.child_element_test(tag_name, 'color', None, {'name': 'INVALID', 'red': '255', 'green': '0',
                                                          'blue': '255', 'alpha': '255'})

    def test_fill_color(self):
        tag_name = 'fill_color'
        self.element.fill_color(5, 10, 15, 12)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '12'})

class TestLimitsFromPV(GenericTest):
    def test_limits_off(self):
        tag_name = 'limits_from_pv'
        self.element.limits_from_pv(True)
        self.generic_element_test(tag_name, True)

    def test_limits_off2(self):
        tag_name = 'limits_from_pv'
        self.element.limits_from_pv(False)
        self.generic_element_test(tag_name, False)

    def test_limits_off3(self):
        tag_name = 'limits_from_pv'
        self.element.limits_from_pv(False)
        self.element.limits_from_pv(True)
        self.generic_element_test(tag_name, True)

    def test_limits_off4(self):
        tag_name = 'limits_from_pv'
        self.element.limits_from_pv('tsetsst')
        self.null_test(tag_name)

class TestMinMax(GenericTest):
    def test_min_float(self):
        tag_name = 'minimum'
        val = 2.5
        self.element.minimum(val)
        self.generic_element_test(tag_name, val)

    def test_min_string(self):
        tag_name = 'minimum'
        self.element.minimum('asfdsf')
        self.null_test(tag_name)

    def test_max_float(self):
        tag_name = 'maximum'
        val = -24.2
        self.element.maximum(val)
        self.generic_element_test(tag_name, val)

class TestMinMaxInternal(InternalTest):
    def test_min_float(self):
        tag_name = 'minimum'
        val = 2.5
        self.element.minimum(val)
        self.generic_element_test(tag_name, val)

    def test_min_string(self):
        tag_name = 'minimum'
        self.element.minimum('asfdsf')
        self.null_test(tag_name)

    def test_max_float(self):
        tag_name = 'maximum'
        val = -24.2
        self.element.maximum(val)
        self.generic_element_test(tag_name, val)

class TestEmptyColor(GenericTest):
    def test_predefined_empty_color(self):
        tag_name = 'empty_color'
        self.element.predefined_empty_color(self.colors.INVALID)
        self.child_element_test(tag_name, 'color', None, {'name': 'INVALID', 'red': '255', 'green': '0',
                                                          'blue': '255', 'alpha': '255'})

    def test_empty_color(self):
        tag_name = 'empty_color'
        self.element.empty_color(5, 10, 15, 12)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '12'})

class TestScaleVisible(GenericTest):
    def test_scale_visible(self):
        tag_name = 'scale_visible'
        self.element.scale_visible('false')
        self.generic_element_test(tag_name, False)

class TestUrl(GenericTest):
    def test_url(self):
        tag_name = 'url'
        self.generic_element_test(tag_name, self.url)
        val = 'https://als.lbl.gov'
        self.element.url(val)
        self.generic_element_test(tag_name, val)

class TestShowToolbar(GenericTest):
    def test_show_toolbar(self):
        tag_name = 'show_toolbar'
        val = False
        self.element.show_toolbar(val)
        self.generic_element_test(tag_name, val)

    def test_show_toolbar_true(self):
        tag_name = 'show_toolbar'
        val = True
        self.element.show_toolbar(val)
        self.generic_element_test(tag_name, val)

    def test_show_toolbar_wrong(self):
        tag_name = 'show_toolbar'
        val = 'slkajfl'
        self.element.show_toolbar(val)
        self.null_test(tag_name)

    def test_show_toolbar_wrong_2(self):
        tag_name = 'show_toolbar'
        val = 'tRue'
        self.element.show_toolbar(val)
        self.generic_element_test(tag_name, True)

class TestButtonsOnLeft(GenericTest):
    def test_buttons_on_left(self):
        tag_name = 'buttons_on_left'
        val = 'fAlse'
        self.element.buttons_on_left(val)
        self.generic_element_test(tag_name, False)

    def test_buttons_on_left_true(self):
        tag_name = 'buttons_on_left'
        val = True
        self.element.buttons_on_left(val)
        self.generic_element_test(tag_name, val)

    def test_buttons_on_left_int(self):
        tag_name = 'buttons_on_left'
        val = 1
        self.element.buttons_on_left(val)
        self.generic_element_test(tag_name, True)

class TestIncrement(GenericTest):
    def test_increment(self):
        tag_name = 'increment'
        val = 12.2
        self.element.increment(val)
        self.generic_element_test(tag_name, val)

    def test_increment2(self):
        tag_name = 'increment'
        val = 2
        self.element.increment(val)
        self.generic_element_test(tag_name, val)

    def test_increment_wrong(self):
        tag_name = 'increment'
        val = 'testjlksj'
        self.element.increment(val)
        self.null_test(tag_name)

class TestFileComponent(GenericTest):
    def test_file_component(self):
        tag_name = 'component'
        self.element.file_component_full_path()
        self.generic_element_test(tag_name, 0)

    def test_component_directory(self):
        tag_name = 'component'
        self.element.file_component_directory()
        self.generic_element_test(tag_name, 1)

    def test_component_name_and_extension(self):
        tag_name = 'component'
        self.element.file_component_name_and_extension()
        self.generic_element_test(tag_name, 2)

    def test_component_base_name(self):
        tag_name = 'component'
        self.element.file_component_base_name()
        self.generic_element_test(tag_name, 3)

    def test_multiple_changes(self):
        tag_name = 'component'
        self.element.file_component_base_name()
        self.generic_element_test(tag_name, 3)
        self.element.file_component_full_path()
        self.generic_element_test(tag_name, 0)

class TestEditable(GenericTest):
    def test_editable_true(self):
        tag_name = 'editable'
        self.element.editable(True)
        self.generic_element_test(tag_name, True)

    def test_editable_false(self):
        tag_name = 'editable'
        self.element.editable('faLse')
        self.generic_element_test(tag_name, False)

class TestSelectedColor(GenericTest):
    def test_selected_color(self):
        tag_name = 'selected_color'
        self.element.predefined_selected_color(self.colors.OK)
        self.child_element_test(tag_name, 'color', None, {'name': 'OK', 'red': '0', 'green': '255',
                                                          'blue': '0', 'alpha': '255'})

    def test_selected_color_2(self):
        tag_name = 'selected_color'
        self.element.selected_color(5, 10, 15, 232)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '232'})

    def test_selected_color_wrong(self):
        self.element.selected_color(-2, 10, 15, 232)
        self.null_test('color')

class TestDeselectedColor(GenericTest):
    def test_deselected_color(self):
        tag_name = 'deselected_color'
        self.element.predefined_deselected_color(self.colors.OK)
        self.child_element_test(tag_name, 'color', None, {'name': 'OK', 'red': '0', 'green': '255',
                                                          'blue': '0', 'alpha': '255'})

    def test_deselected_color_2(self):
        tag_name = 'deselected_color'
        self.element.deselected_color(5, 10, 15, 232)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '232'})

    def test_deselected_color_wrong(self):
        self.element.deselected_color(-2, 10, 15, 232)
        self.null_test('color')

class TestMode(GenericTest):
    def test_toggle(self):
        self.element.mode_toggle()
        self.generic_element_test('mode', 0)

    def test_push(self):
        self.element.mode_push()
        self.generic_element_test('mode', 1)

    def test_push_inverted(self):
        self.element.mode_push_inverted()
        self.generic_element_test('mode', 2)

    def test_twice(self):
        self.element.mode_push_inverted()
        self.generic_element_test('mode', 2)
        self.element.mode_toggle()
        self.generic_element_test('mode', 0)
        self.element.mode_toggle()
        self.element.remove_element('mode')
        self.null_test('mode')

class TestOffImage(TestOff):
    def test_image_file(self):
        tag_name = 'off_image'
        val = './test/image.png'
        self.element.off_image(val)
        self.generic_element_test(tag_name, val)

class TestOnImage(TestOn):
    def test_on_image_file(self):
        tag_name = 'on_image'
        val = './test/image.png'
        self.element.on_image(val)
        self.generic_element_test(tag_name, val)

class TestShowLED(GenericTest):
    def test_show_led(self):
        tag_name = 'show_led'
        self.element.show_led(False)
        self.generic_element_test(tag_name, False)

class TestNeedleColor(GenericTest):
    def test_predefined_needle_color(self):
        tag_name = 'needle_color'
        self.element.predefined_needle_color(self.colors.Write_Background)
        self.child_element_test(tag_name, 'color', None, {'name': 'Write_Background', 'red': '128', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})

    def test_needle_color(self):
        tag_name = 'needle_color'
        self.element.needle_color(5, 10, 15, 12)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '12'})

class TestKnobColor(GenericTest):
    def test_predefined_knob_color(self):
        tag_name = 'knob_color'
        self.element.predefined_knob_color(self.colors.MINOR)
        self.child_element_test(tag_name, 'color', None, {'name': 'MINOR', 'red': '255', 'green': '128',
                                                          'blue': '0', 'alpha': '255'})

    def test_knob_color(self):
        tag_name = 'knob_color'
        self.element.knob_color(5, 0, 255)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '0',
                                                          'blue': '255', 'alpha': '255'})

    def test_knob_color_wrong(self):
        self.element.knob_color('sdfsd', 0, 255)
        self.null_test('color')

class TestShowValue(GenericTest):
    def test_show_value_false(self):
        tag_name = 'show_value'
        self.element.show_value(False)
        self.generic_element_test(tag_name, False)

class TestShowLimits(GenericTest):
    def test_show_limits_true(self):
        tag_name = 'show_limits'
        self.element.show_limits(True)
        self.generic_element_test(tag_name, True)

    def test_show_limits_wrong(self):
        tag_name = 'show_limits'
        self.element.show_limits('atsddfj')
        self.null_test(tag_name)

class TestShowValueTip(GenericTest):
    def test_show_value_tip_true(self):
        tag_name = 'show_value_tip'
        self.element.show_value_tip(True)
        self.generic_element_test(tag_name, True)

    def test_show_value_tip_false(self):
        tag_name = 'show_value_tip'
        self.element.show_value_tip(True)
        self.element.show_value_tip(False)
        self.generic_element_test(tag_name, False)

class TestBarLength(GenericTest):
    def test_bar_length(self):
        tag_name = 'bar_length'
        val = 2.5
        self.element.bar_length(val)
        self.generic_element_test(tag_name, val)

    def test_bar_length2(self):
        tag_name = 'bar_length'
        val = 1.0
        self.element.bar_length(val)
        self.generic_element_test(tag_name, val)

class TestSelectionValuePV(GenericTest):
    def test_selection_value_pv(self):
        tag_name = 'selection_value_pv'
        val = '$(P):MY:COOL:PV'
        self.element.selection_value_pv(val)
        self.generic_element_test(tag_name, val)

class TestPoints(GenericTest):
    def test_points(self):
        self.element.point(2, 5)
        self.child_element_test('points', 'point', None, {'x': '2', 'y': '5'})

    def test_points_wrong(self):
        self.element.point('2', 5)
        self.null_test('points')

    def test_points_wrong_again(self):
        self.element.point(2, '5')
        self.null_test('points')

    def test_multiple_points(self):
        self.element.point(2, 5)
        self.child_element_test('points', 'point', None, {'x': '2', 'y': '5'}, True)
        self.element.point(8, 9)
        self.assertEqual(len(self.element.find_element('points').findall('point')), 2)

class TestArrow(GenericTest):
    def test_arrow_length(self):
        tag_name = 'arrow_length'
        val = 5
        self.element.arrow_length(val)
        self.generic_element_test(tag_name, val)

    def test_arrow_length_wrong(self):
        tag_name = 'arrow_length'
        val = 'asdfsdf'
        self.element.arrow_length(val)
        self.null_test(tag_name)

    def test_arrows_from(self):
        tag_name = 'arrows'
        self.element.arrows_from()
        self.generic_element_test(tag_name, 1)

    def test_arrows_to(self):
        tag_name = 'arrows'
        self.element.arrows_to()
        self.generic_element_test(tag_name, 2)

    def test_arrows_both(self):
        tag_name = 'arrows'
        self.element.arrows_both()
        self.generic_element_test(tag_name, 3)

    def test_arrows_none(self):
        tag_name = 'arrows'
        self.element.arrows_none()
        self.generic_element_test(tag_name, 0)

class TestLineStyle(GenericTest):
    def test_line_style_solid(self):
        self.element.line_style_solid()
        self.generic_element_test('line_style', 0)

    def test_line_style_dashed(self):
        self.element.line_style_dashed()
        self.generic_element_test('line_style', 1)

    def test_line_style_dot(self):
        self.element.line_style_dot()
        self.generic_element_test('line_style', 2)

    def test_line_style_dash_dot(self):
        self.element.line_style_dash_dot()
        self.generic_element_test('line_style', 3)

    def test_line_style_dash_dot_dot(self):
        self.element.line_style_dash_dot_dot()
        self.generic_element_test('line_style', 4)

class TestLineStyleInternal(InternalTest):
    def test_line_style_solid(self):
        self.element.line_style_solid()
        self.generic_element_test('line_style', 0)

    def test_line_style_dashed(self):
        self.element.line_style_dashed()
        self.generic_element_test('line_style', 1)

    def test_line_style_dot(self):
        self.element.line_style_dot()
        self.generic_element_test('line_style', 2)

    def test_line_style_dash_dot(self):
        self.element.line_style_dash_dot()
        self.generic_element_test('line_style', 3)

    def test_line_style_dash_dot_dot(self):
        self.element.line_style_dash_dot_dot()
        self.generic_element_test('line_style', 4)


class TestActiveTab(GenericTest):
    def test_active_tab(self):
        tag_name = 'active_tab'
        val = 4
        self.element.active_tab(val)
        self.generic_element_test(tag_name, val)

    def test_tab_wrong(self):
        tag_name = 'active_tab'
        val = 'tab1TryString'
        self.element.active_tab(val)
        self.null_test(tag_name)

class TestTabHeight(GenericTest):
    def test_tab_height(self):
        tag_name = 'tab_height'
        val = 23
        self.element.tab_height(val)
        self.generic_element_test(tag_name, val)

    def test_tab_wrong(self):
        tag_name = 'tab_height'
        val = 'lkasjdfls'
        self.element.tab_height(val)
        self.null_test(tag_name)

class TestDirection(GenericTest):
    def test_horizontal(self):
        self.element.tab_direction_horizontal()
        self.generic_element_test('direction', 0)

    def test_vertical(self):
        self.element.tab_direction_vertical()
        self.generic_element_test('direction', 1)

    def test_both(self):
        self.element.tab_direction_vertical()
        self.generic_element_test('direction', 1)
        self.element.tab_direction_horizontal()
        self.generic_element_test('direction', 0)

class TestStartBit(GenericTest):
    def test_start_bits(self):
        tag_name = 'startBit'
        val = 2
        self.element.start_bit(val)
        self.generic_element_test(tag_name, val)

class TestNumBits(GenericTest):
    def test_num_bits(self):
        tag_name = 'numBits'
        val = 32
        self.element.num_bits(val)
        self.generic_element_test(tag_name, val)

class TestReverseBits(GenericTest):
    def test_reverse_bits_default(self):
        tag_name = 'bitReverse'
        self.element.reverse_bits()
        self.generic_element_test(tag_name, True)

    def test_reverse_bits_false(self):
        tag_name = 'bitReverse'
        self.element.reverse_bits(False)
        self.generic_element_test(tag_name, False)

    def test_reverse_bits_true(self):
        tag_name = 'bitReverse'
        self.element.reverse_bits(True)
        self.generic_element_test(tag_name, True)

    def test_reverse_wrong(self):
        tag_name = 'bitReverse'
        self.element.reverse_bits('tets')
        self.null_test(tag_name)

class TestTabWidth(GenericTest):
    def test_tab_width(self):
        tag_name = 'tab_width'
        val = 235.5
        self.element.tab_width(val)
        self.generic_element_test(tag_name, int(val))

    def test_tab_width_wrong(self):
        tag_name = 'tab_width'
        val = 'lkasjdfls'
        self.element.tab_width(val)
        self.null_test(tag_name)

class TestTabSpacing(GenericTest):
    def test_tab_spacing(self):
        tag_name = 'tab_spacing'
        val = 2.5
        self.element.tab_spacing(val)
        self.generic_element_test(tag_name, int(val))

    def test_tab_spacing_2(self):
        tag_name = 'tab_spacing'
        val = 23
        self.element.tab_spacing(val)
        self.generic_element_test(tag_name, val)

class TestLabels(GenericTest):
    def test_label_single_string(self):
        label_name = 'testLabel1'
        self.element.labels(label_name)
        self.child_element_test('labels', 'text', label_name, {})

    def test_label_list(self):
        label_names = ['testLabel1', 'label2', 'label5']
        self.element.labels(label_names)
        self.assertEqual(len(self.element.find_element('labels').findall('text')), len(label_names))

    def test_label_wrong(self):
        label_name = 112358
        self.element.labels(label_name)
        self.assertFalse(self.element.find_element('labels'))

class TestArrayIndex(GenericTest):
    def test_array_index(self):
        tag_name = 'array_index'
        val = 2
        self.element.array_index(val)
        self.generic_element_test(tag_name, val)

class TestSymbols(GenericTest):
    def test_symbols_single_string(self):
        label_name = 'testLabel1'
        self.element.symbols(label_name)
        self.child_element_test('symbols', 'symbol', label_name, {})

    def test_symbols_two_strings(self):
        label_name = 'testLabel1'
        label_name2 = 'testLabel2'
        self.element.symbols(label_name)
        self.element.symbols(label_name2)
        self.child_element_test('symbols', 'symbol', label_name, {}, True)
        self.child_element_test('symbols', 'symbol', label_name2, {}, True)

    def test_symbols_list(self):
        label_names = ['testLabel1', 'file:/test.png', 'label5']
        self.element.symbols(label_names)
        self.assertEqual(len(self.element.find_element('symbols').findall('symbol')), len(label_names))

    def test_symbols_list_string(self):
        label_names = ['testLabel1', 'file:/test.png', 'label5']
        label_name = 'testLabel2'
        self.element.symbols(label_names)
        self.assertEqual(len(self.element.find_element('symbols').findall('symbol')), len(label_names))
        self.element.symbols(label_name)
        self.child_element_test('symbols', 'symbol', label_name, {}, True)

    def test_symbols_wrong(self):
        label_name = 123456789
        self.element.symbols(label_name)
        self.assertFalse(self.element.find_element('symbols'))

class TestInitialIndex(GenericTest):
    def test_initial_index_index(self):
        tag_name = 'initial_index'
        val = 2
        self.element.initial_index(val)
        self.generic_element_test(tag_name, val)


class TestShowIndex(GenericTest):
    def test_show_index_default(self):
        tag_name = 'show_index'
        self.element.show_index()
        self.generic_element_test(tag_name, True)

    def test_show_index_false(self):
        tag_name = 'show_index'
        self.element.show_index(False)
        self.generic_element_test(tag_name, False)

    def test_show_index_true(self):
        tag_name = 'show_index'
        self.element.show_index(True)
        self.generic_element_test(tag_name, True)

    def test_show_index_wrong(self):
        tag_name = 'show_index'
        self.element.show_index('tets')
        self.null_test(tag_name)

class TestPreserveRatio(GenericTest):
    def test_preserve_ratio_default(self):
        tag_name = 'preserve_ratio'
        self.element.preserve_ratio()
        self.generic_element_test(tag_name, True)

    def test_preserve_ratio_false(self):
        tag_name = 'preserve_ratio'
        self.element.preserve_ratio(False)
        self.generic_element_test(tag_name, False)

    def test_preserve_ratio_true(self):
        tag_name = 'preserve_ratio'
        self.element.preserve_ratio(True)
        self.generic_element_test(tag_name, True)

    def test_preserve_ratio_wrong(self):
        tag_name = 'preserve_ratio'
        self.element.preserve_ratio('tets')
        self.null_test(tag_name)

class TestShowScale(GenericTest):
    def test_show_scale_default(self):
        tag_name = 'show_scale'
        self.element.show_scale()
        self.generic_element_test(tag_name, True)

    def test_show_scale_false(self):
        tag_name = 'show_scale'
        self.element.show_scale(False)
        self.generic_element_test(tag_name, False)

    def test_show_scale_true(self):
        tag_name = 'show_scale'
        self.element.show_scale(True)
        self.generic_element_test(tag_name, True)

class TestShowMinorTicks(GenericTest):
    def test_show_minor_ticks_default(self):
        tag_name = 'show_minor_ticks'
        self.element.show_minor_ticks()
        self.generic_element_test(tag_name, True)

    def test_show_minor_ticks_false(self):
        tag_name = 'show_minor_ticks'
        self.element.show_minor_ticks(False)
        self.generic_element_test(tag_name, False)

    def test_show_minor_ticks_true(self):
        tag_name = 'show_minor_ticks'
        self.element.show_minor_ticks(True)
        self.generic_element_test(tag_name, True)

class TestMajorTicksPixelDist(GenericTest):
    def test_major_tick_step_hint(self):
        tag_name = 'major_tick_step_hint'
        val = 2352
        self.element.major_ticks_pixel_dist(val)
        self.generic_element_test(tag_name, val)

class TestScaleFormat(GenericTest):
    def test_scale_format(self):
        tag_name = 'scale_format'
        val = '# .###'
        self.element.scale_format(val)
        self.generic_element_test(tag_name, val)

class TestLevelsAndShow(GenericTest):
    def test_level_hihi(self):
        tag_name = 'level_hihi'
        val = 200.23
        self.element.level_hihi(val)
        self.generic_element_test(tag_name, val)

    def test_level_hihi_int(self):
        tag_name = 'level_hihi'
        val = 200
        self.element.level_hihi(val)
        self.generic_element_test(tag_name, val)

    def test_level_high(self):
        tag_name = 'level_high'
        val = 2.23
        self.element.level_high(val)
        self.generic_element_test(tag_name, val)

    def test_level_lolo(self):
        tag_name = 'level_lolo'
        val = 500.23
        self.element.level_lolo(val)
        self.generic_element_test(tag_name, val)

    def test_level_lolo_int(self):
        tag_name = 'level_lolo'
        val = 100
        self.element.level_lolo(val)
        self.generic_element_test(tag_name, val)

    def test_level_low(self):
        tag_name = 'level_low'
        val = 500.23
        self.element.level_low(val)
        self.generic_element_test(tag_name, val)

    def test_level_low_int(self):
        tag_name = 'level_low'
        val = 100
        self.element.level_low(val)
        self.generic_element_test(tag_name, val)

    def test_show_hihi_default(self):
        tag_name = 'show_hihi'
        self.element.show_hihi()
        self.generic_element_test(tag_name, True)

    def test_show_high_default(self):
        tag_name = 'show_high'
        self.element.show_high()
        self.generic_element_test(tag_name, True)

    def test_show_low_default(self):
        tag_name = 'show_low'
        self.element.show_low()
        self.generic_element_test(tag_name, True)

    def test_show_lolo_default(self):
        tag_name = 'show_lolo'
        self.element.show_lolo()
        self.generic_element_test(tag_name, True)

    def test_show_hihi_true(self):
        tag_name = 'show_hihi'
        self.element.show_hihi(True)
        self.generic_element_test(tag_name, True)

    def test_show_high_true(self):
        tag_name = 'show_high'
        self.element.show_high(True)
        self.generic_element_test(tag_name, True)

    def test_show_low_true(self):
        tag_name = 'show_low'
        self.element.show_low(True)
        self.generic_element_test(tag_name, True)

    def test_show_lolo_true(self):
        tag_name = 'show_lolo'
        self.element.show_lolo(True)
        self.generic_element_test(tag_name, True)

    def test_show_hihi_false(self):
        tag_name = 'show_hihi'
        self.element.show_hihi(False)
        self.generic_element_test(tag_name, False)

    def test_show_high_false(self):
        tag_name = 'show_high'
        self.element.show_high(False)
        self.generic_element_test(tag_name, False)

    def test_show_low_false(self):
        tag_name = 'show_low'
        self.element.show_low(False)
        self.generic_element_test(tag_name, False)

    def test_show_lolo_false(self):
        tag_name = 'show_lolo'
        self.element.show_lolo(False)
        self.generic_element_test(tag_name, False)

class TestStates(GenericTest):
    def test_state(self):
        self.element.state(1, 'Test', 223, 242, 12)
        self.element.state_predefined_color(0, 'INVALID STATE', self.colors.INVALID)
        self.assertEqual(len(self.element.find_element('states').findall('state')), 2)

class TestFallback(GenericTest):
    def test_fallback_label(self):
        tag_name = 'fallback_label'
        val = 'MyLabel'
        self.element.fallback_label(val)
        self.generic_element_test(tag_name, val)

    def test_predefined_fallback_color(self):
        tag_name = 'fallback_color'
        self.element.predefined_fallback_color(self.colors.Background)
        self.child_element_test(tag_name, 'color', None, {'name': 'Background', 'red': '255', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})

    def test_fallback_color(self):
        tag_name = 'fallback_color'
        self.element.fallback_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '255'})

class TestSelectRows(GenericTest):
    def test_select_rows_default(self):
        tag_name = 'row_selection_mode'
        self.element.select_rows()
        self.generic_element_test(tag_name, True)

    def test_select_rows_false(self):
        tag_name = 'row_selection_mode'
        self.element.select_rows(False)
        self.generic_element_test(tag_name, False)

    def test_select_rows_true(self):
        tag_name = 'row_selection_mode'
        self.element.select_rows(True)
        self.generic_element_test(tag_name, True)

class TestSelectionPV(GenericTest):
    def test_selection_pv(self):
        tag_name = 'selection_pv'
        val = 'Selection:PV:Test'
        self.element.selection_pv(val)
        self.generic_element_test(tag_name, val)

class TestColumns(GenericTest):
    # add more testing!
    def test_columns(self):
        self.element.column('col1', 123, False, ['opt532', 'option35'])
        self.element.column('col2', 123, True, 'optionStr')
        self.assertEqual(len(self.element.find_element('columns').findall('column')), 2)

    def test_columns_options_wrong(self):
        self.element.column('col1', 123, False, ['opt532', 'option35'])
        self.element.column('col2', 123, True, 123)
        self.assertEqual(len(self.element.find_element('columns').findall('column')), 2)

    def test_columns_options_none(self):
        self.element.column('col1', 123, False, ['opt532', 'option35'])
        self.element.column('col2', 123, True, None)
        self.assertEqual(len(self.element.find_element('columns').findall('column')), 2)


class TestTabs(GenericTest):
    def test_tab(self):
        self.element.tab('tab1')
        self.assertEqual(len(self.element.root.find('tabs').findall('tab')), 1)
        self.assertEqual(self.element.root.find('tabs').findall('tab')[0].find('name').text, 'tab1')

    def test_add_widget(self):
        self.element.tab('tab1')
        self.assertEqual(len(self.element.root.find('tabs').findall('tab')), 1)
        self.element.add_widget('tab1', self.widget)
        self.assertEqual(self.element.root.find('tabs').find('tab').find('children')[0].find('name').text, 'testGroup')

    def test_add_widget_none(self):
        self.element.add_widget('tab1', self.widget)
        self.assertIsNone(self.element.root.find('tabs'))

    def test_add_widget_not_found(self):
        self.element.tab('tab1')
        self.assertEqual(len(self.element.root.find('tabs').findall('tab')), 1)
        self.element.add_widget('tab2', self.widget)
        self.assertNotEqual(self.element.root.find('tabs').find('tab').find('name').text, 'tab2')


class TestNavTabs(GenericTest):
    def test_nav_tab(self):
        self.element.tab('TabElement2', './tab2.bob', 'TabGroupName', {'MAC1': 'MacV'})
        self.assertIsNotNone(self.element.root.find('tabs'))
        self.assertIsNotNone(self.element.root.find('tabs').find('tab'))
        self.assertEqual(self.element.root.find('tabs').find('tab').find('name').text, 'TabElement2')
        self.assertEqual(self.element.root.find('tabs').find('tab').find('file').text, './tab2.bob')
        self.assertEqual(self.element.root.find('tabs').find('tab').find('group_name').text, 'TabGroupName')
        self.assertIsNotNone(self.element.root.find('tabs').find('tab').find('macros'))
        self.assertEqual(self.element.root.find('tabs').find('tab').find('macros').find('MAC1').text, 'MacV')
        self.element.tab('TabElement', './tab.bob', 'TabGroupName')
        self.assertEqual(len(self.element.root.find('tabs').findall('tab')), 2)

    def test_nav_tab_macros_wrong(self):
        self.element.tab('TabElement2', './tab2.bob', 'TabGroupName', 'macro')
        self.assertIsNotNone(self.element.root.find('tabs'))
        self.assertIsNotNone(self.element.root.find('tabs').find('tab'))
        self.assertEqual(self.element.root.find('tabs').find('tab').find('name').text, 'TabElement2')
        self.assertEqual(self.element.root.find('tabs').find('tab').find('file').text, './tab2.bob')
        self.assertEqual(self.element.root.find('tabs').find('tab').find('group_name').text, 'TabGroupName')
        self.assertIsNotNone(self.element.root.find('tabs').find('tab').find('macros'))
        self.assertIsNone(self.element.root.find('tabs').find('tab').find('macros').find('MAC1'))
        self.element.tab('TabElement', './tab.bob', 'TabGroupName')
        self.assertEqual(len(self.element.root.find('tabs').findall('tab')), 2)

class TestTitle(GenericTest):
    def test_title(self):
        tag_name = 'title'
        val = 'MyChart Title'
        self.element.title(val)
        self.generic_element_test(tag_name, val)

class TestTitleInternal(InternalTest):
    def test_title(self):
        tag_name = 'title'
        val = 'MyChart Title'
        self.element.title(val)
        self.generic_element_test(tag_name, val)

class TestAutoScale(GenericTest):
    def test_auto_scale_false(self):
        tag_name = 'autoscale'
        self.element.auto_scale(False)
        self.generic_element_test(tag_name, False)

    def test_auto_scale_true(self):
        tag_name = 'autoscale'
        self.element.auto_scale(True)
        self.generic_element_test(tag_name, True)

class TestAutoScaleInternal(InternalTest):
    def test_auto_scale_false(self):
        tag_name = 'autoscale'
        self.element.auto_scale(False)
        self.generic_element_test(tag_name, False)

    def test_auto_scale_true(self):
        tag_name = 'autoscale'
        self.element.auto_scale(True)
        self.generic_element_test(tag_name, True)

class TestDataHeightAndWidth(GenericTest):
    def test_data_height(self):
        tag_name = 'data_height'
        val = 23
        self.element.data_height(val)
        self.generic_element_test(tag_name, val)

    def test_data_width(self):
        tag_name = 'data_width'
        val = 964
        self.element.data_width(val)
        self.generic_element_test(tag_name, val)

class TestLogScale(GenericTest):
    def test_log_scale_default(self):
        tag_name = 'log_scale'
        self.element.log_scale()
        self.generic_element_test(tag_name, True)

    def test_log_scale_false(self):
        tag_name = 'log_scale'
        self.element.log_scale(False)
        self.generic_element_test(tag_name, False)

    def test_log_scale_true(self):
        tag_name = 'log_scale'
        self.element.log_scale(True)
        self.generic_element_test(tag_name, True)

class TestLogScaleInternal(InternalTest):
    def test_log_scale_default(self):
        tag_name = 'log_scale'
        self.element.log_scale()
        self.generic_element_test(tag_name, True)

    def test_log_scale_false(self):
        tag_name = 'log_scale'
        self.element.log_scale(False)
        self.generic_element_test(tag_name, False)

    def test_log_scale_true(self):
        tag_name = 'log_scale'
        self.element.log_scale(True)
        self.generic_element_test(tag_name, True)

class TestUnsignedData(GenericTest):
    def test_unsigned_default(self):
        tag_name = 'unsigned'
        self.element.unsigned_data()
        self.generic_element_test(tag_name, True)

    def test_unsigned_false(self):
        tag_name = 'unsigned'
        self.element.unsigned_data(False)
        self.generic_element_test(tag_name, False)

    def test_unsigned_true(self):
        tag_name = 'unsigned'
        self.element.unsigned_data(True)
        self.generic_element_test(tag_name, True)

class TestShowGrid(GenericTest):
    def test_show_grid_default(self):
        tag_name = 'show_grid'
        self.element.show_grid()
        self.generic_element_test(tag_name, True)

    def test_show_grid_false(self):
        tag_name = 'show_grid'
        self.element.show_grid(False)
        self.generic_element_test(tag_name, False)

    def test_show_grid_true(self):
        tag_name = 'show_grid'
        self.element.show_grid(True)
        self.generic_element_test(tag_name, True)

class TestShowGridInternal(InternalTest):
    def test_show_grid_default(self):
        tag_name = 'show_grid'
        self.element.show_grid()
        self.generic_element_test(tag_name, True)

    def test_show_grid_false(self):
        tag_name = 'show_grid'
        self.element.show_grid(False)
        self.generic_element_test(tag_name, False)

    def test_show_grid_true(self):
        tag_name = 'show_grid'
        self.element.show_grid(True)
        self.generic_element_test(tag_name, True)

class TestShowLegend(GenericTest):
    def test_show_legend_default(self):
        tag_name = 'show_legend'
        self.element.show_legend()
        self.generic_element_test(tag_name, True)

    def test_show_legend_false(self):
        tag_name = 'show_legend'
        self.element.show_legend(False)
        self.generic_element_test(tag_name, False)

    def test_sshow_legend_true(self):
        tag_name = 'show_legend'
        self.element.show_legend(True)
        self.generic_element_test(tag_name, True)

class TestTimeRange(GenericTest):
    def test_time_range(self):
        tag_name = 'time_range'
        val = '5 minutes'
        self.element.time_range(val)
        self.generic_element_test(tag_name, val)

class TestGridColor(GenericTest):
    def test_predefined_grid_color(self):
        tag_name = 'grid_color'
        self.element.predefined_grid_color(self.colors.Background)
        self.child_element_test(tag_name, 'color', None, {'name': 'Background', 'red': '255', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})

    def test_grid_color(self):
        tag_name = 'grid_color'
        self.element.grid_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '255'})

class TestCursor(GenericTest):
    def test_cursor_info_pv(self):
        tag_name = 'cursor_info_pv'
        val = 'Cursor:INFO:PV:Test'
        self.element.cursor_info_pv(val)
        self.generic_element_test(tag_name, val)

    def test_cursor_x_pv(self):
        tag_name = 'x_pv'
        val = 'Cursor:X:PV:Test'
        self.element.cursor_x_pv(val)
        self.generic_element_test(tag_name, val)

    def test_cursor_y_pv(self):
        tag_name = 'y_pv'
        val = 'Cursor:Y:PV:Test'
        self.element.cursor_y_pv(val)
        self.generic_element_test(tag_name, val)

    def test_cursor_crosshair_default(self):
        tag_name = 'cursor_crosshair'
        default_val = True
        self.element.cursor_crosshair()
        self.generic_element_test(tag_name, default_val)

    def test_cursor_crosshair_on(self):
        tag_name = 'cursor_crosshair'
        val = True
        self.element.cursor_crosshair(val)
        self.generic_element_test(tag_name, val)

    def test_cursor_crosshair_off(self):
        tag_name = 'cursor_crosshair'
        val = False
        self.element.cursor_crosshair(val)
        self.generic_element_test(tag_name, val)

class TestInterpolation(GenericTest):
    def test_interpolation_none(self):
        self.element.interpolation_none()
        self.generic_element_test('interpolation', 0)

    def test_interpolation_interpolate(self):
        self.element.interpolation_interpolate()
        self.generic_element_test('interpolation', 1)

    def test_interpolation_automatic(self):
        self.element.interpolation_automatic()
        self.generic_element_test('interpolation', 2)

    def test_interpolation_twice(self):
        self.element.interpolation_none()
        self.generic_element_test('interpolation', 0)
        self.element.interpolation_interpolate()
        self.generic_element_test('interpolation', 1)
        self.element.interpolation_automatic()
        self.element.remove_element('interpolation')
        self.null_test('interpolation')

class TestTraces(InternalTest):
    def test_add_trace(self):
        trace = self.trace1
        self.element.add_trace(trace)
        self.child_element_test('traces', 'trace', None, {}, True)

    def test_add_two_traces(self):
        trace = self.trace1
        trace2 = self.trace2
        self.element.add_trace(trace)
        self.element.add_trace(trace2)
        trace_tags = self.element.root.find('traces').findall('trace')
        self.assertEqual(len(trace_tags), 2)

    def test_add_same_trace(self):
        trace = self.trace1
        self.element.add_trace(trace)
        self.element.add_trace(trace)
        trace_tags = self.element.root.find('traces').findall('trace')
        self.assertEqual(len(trace_tags), 1)

    def test_remove_trace(self):
        trace = self.trace1
        self.element.add_trace(trace)
        self.element.remove_trace(trace)
        traces_tag = self.element.root.find('traces')
        trace_tags = traces_tag.findall('trace')
        self.assertEqual(len(trace_tags), 0)
        self.assertEqual(len(traces_tag), 0)

    def test_remove_two_traces(self):
        trace = self.trace1
        trace2 = self.trace2
        self.element.add_trace(trace)
        self.element.add_trace(trace2)
        self.element.remove_trace(trace)
        self.element.remove_trace(trace2)
        traces_tag = self.element.root.find('traces')
        trace_tags = traces_tag.findall('trace')
        self.assertEqual(len(trace_tags), 0)
        self.assertEqual(len(traces_tag), 0)

    def test_remove_same_trace(self):
        trace = self.trace1
        self.element.add_trace(trace)
        self.element.remove_trace(trace)
        self.element.remove_trace(trace)
        traces_tag = self.element.root.find('traces')
        self.assertEqual(traces_tag, None)

    def test_remove_none(self):
        trace = self.trace1
        self.element.remove_trace(trace)
        traces_tag = self.element.root.find('traces')
        self.assertEqual(traces_tag, None)

    def test_add_mismatch_trace_type(self):
        trace = self.trace_wrong
        self.element.add_trace(trace)
        traces_tag = self.element.root.find('traces')
        self.assertEqual(traces_tag, None)

class TestName(InternalTest):
    # name
    def test_name(self):
        name = 'test name'
        self.element.name(name)
        self.generic_element_test('name', name)

class TestXPV(InternalTest):
    # x_pv
    def test_x_pv(self):
        xpv = 'x pv value'
        self.element.x_pv(xpv)
        self.generic_element_test('x_pv', xpv)

class TestYPV(InternalTest):
    # y_pv
    def test_y_pv(self):
        ypv = 'y pv value'
        self.element.y_pv(ypv)
        self.generic_element_test('y_pv', ypv)

class TestErrPV(InternalTest):
    # err_pv
    def test_err_pv(self):
        errpv = 'error pv value'
        self.element.err_pv(errpv)
        self.generic_element_test('err_pv', errpv)

class TestYAxis(InternalTest):
    # axis (y-axis)
    def test_axis(self):
        axis = 2
        self.element.axis(axis)
        self.generic_element_test('axis', axis)

    def test_axis_wrong(self):
        axis = 'True'
        self.element.axis(axis)
        self.null_test('axis')

class TestPointSize(InternalTest):
    def test_point_size(self):
        size = 7
        self.element.point_size(size)
        self.generic_element_test('point_size', 7)

    def test_point_size_wrong(self):
        size = 'string'
        self.element.point_size(size)
        self.null_test('point_size')

class TestTraceType(InternalTest):
    def test_trace_type_none(self):
        self.element.trace_type_none()
        self.generic_element_test('trace_type', 0)

    def test_trace_type_line(self):
        self.element.trace_type_line()
        self.generic_element_test('trace_type', 1)

    def test_trace_type_step(self):
        self.element.trace_type_step()
        self.generic_element_test('trace_type', 2)

    def test_trace_type_error_bars(self):
        self.element.trace_type_error_bars()
        self.generic_element_test('trace_type', 3)

    def test_trace_type_line_error_bars(self):
        self.element.trace_type_line_error_bars()
        self.generic_element_test('trace_type', 4)

    def test_trace_type_bars(self):
        self.element.trace_type_bars()
        self.generic_element_test('trace_type', 5)

class TestPointType(InternalTest):
    def test_point_type_none(self):
        self.element.point_type_none()
        self.generic_element_test('point_type', 0)

    def test_point_type_squares(self):
        self.element.point_type_squares()
        self.generic_element_test('point_type', 1)

    def test_point_type_circles(self):
        self.element.point_type_circles()
        self.generic_element_test('point_type', 2)

    def test_point_type_diamonds(self):
        self.element.point_type_diamonds()
        self.generic_element_test('point_type', 3)

    def test_point_type_x(self):
        self.element.point_type_x()
        self.generic_element_test('point_type', 4)

    def test_point_type_triangles(self):
        self.element.point_type_triangles()
        self.generic_element_test('point_type', 5)

class TestColor(InternalTest):
    def test_color(self):
        tag_name = 'color'
        self.element.color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '255'})

    def test_color_alpha(self):
        tag_name = 'color'
        self.element.color(5, 10, 15, 20)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '20'})

    def test_color_wrong(self):
        self.element.color('string', False, 9)
        self.null_test('color')

    def test_predefined_color(self):
        tag_name = 'color'
        self.element.predefined_color(self.colors.Write_Background)
        self.child_element_test(tag_name, 'color', None, {'name': 'Write_Background', 'red': '128', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})

class TestYAxes(InternalTest):
    def test_add_y_axis(self):
        yaxis = self.yaxis1
        self.element.add_y_axis(yaxis)
        self.child_element_test('y_axes', 'y_axis', None, {}, True)

    def test_add_two_y_axes(self):
        yaxis = self.yaxis1
        yaxis2 = self.yaxis2
        self.element.add_y_axis(yaxis2)
        self.element.add_y_axis(yaxis)
        yaxis_tags = self.element.root.find('y_axes').findall('y_axis')
        self.assertEqual(len(yaxis_tags), 2)

    def test_add_same_y_axis(self):
        yaxis = self.yaxis1
        self.element.add_y_axis(yaxis)
        self.element.add_y_axis(yaxis)
        yaxis_tags = self.element.root.find('y_axes').findall('y_axis')
        self.assertEqual(len(yaxis_tags), 1)

    def test_remove_y_axis(self):
        yaxis = self.yaxis1
        self.element.add_y_axis(yaxis)
        self.element.remove_y_axis(yaxis)
        yaxes_tag = self.element.root.find('y_axes')
        yaxis_tags = yaxes_tag.findall('y_axis')
        self.assertEqual(len(yaxis_tags), 0)
        self.assertEqual(len(yaxes_tag), 0)

    def test_remove_two_y_axes(self):
        yaxis = self.yaxis1
        yaxis2 = self.yaxis2
        self.element.add_y_axis(yaxis)
        self.element.add_y_axis(yaxis2)
        self.element.remove_y_axis(yaxis)
        self.element.remove_y_axis(yaxis2)
        yaxes_tag = self.element.root.find('y_axes')
        yaxis_tags = yaxes_tag.findall('y_axis')
        self.assertEqual(len(yaxis_tags), 0)
        self.assertEqual(len(yaxes_tag), 0)

    def test_remove_same_y_axis(self):
        yaxis = self.yaxis1
        self.element.add_y_axis(yaxis)
        self.element.remove_y_axis(yaxis)
        self.element.remove_y_axis(yaxis)
        yaxes_tag = self.element.root.find('y_axes')
        self.assertEqual(yaxes_tag, None)

    def test_remove_no_axes(self):
        yaxis = self.yaxis1
        self.element.remove_y_axis(yaxis)
        yaxes_tag = self.element.root.find('y_axes')
        self.assertEqual(yaxes_tag, None)

    def test_add_mismatch_type(self):
        yaxis = self.yaxis_wrong
        self.element.add_y_axis(yaxis)
        yaxes_tag = self.element.root.find('y_axes')
        self.assertEqual(yaxes_tag, None)

class TestYAxisSingle(InternalTest):
    def test_add_yaxis(self):
        yaxis1 = self.yaxis1
        self.element.add_y_axis(yaxis1)
        self.generic_element_test('y_axis', None)

    def test_add_two_x_axes(self):
        yaxis1 = self.yaxis1
        yaxis2 = self.yaxis2
        self.element.add_y_axis(yaxis1)
        self.element.add_y_axis(yaxis2)
        y_axes = self.element.root.findall('y_axis')
        self.assertEqual(len(y_axes), 1)

    def test_add_same_y_axis(self):
        yaxis = self.yaxis1
        self.element.add_y_axis(yaxis)
        self.element.add_y_axis(yaxis)
        y_axes = self.element.root.findall('y_axis')
        self.assertEqual(len(y_axes), 1)

    def test_remove_y_axis(self):
        yaxis = self.yaxis1
        self.element.add_y_axis(yaxis)
        self.element.remove_y_axis(yaxis)
        y_axes = self.element.root.findall('y_axis')
        self.assertEqual(len(y_axes), 0)

    def test_remove_same_y_axis(self):
        yaxis = self.yaxis1
        self.element.add_y_axis(yaxis)
        self.element.remove_y_axis(yaxis)
        self.element.remove_y_axis(yaxis)
        y_axes = self.element.root.find('y_axis')
        self.assertEqual(y_axes, None)

    def test_remove_nonexistent_yaxis(self):
        yaxis = self.yaxis1
        self.element.remove_y_axis(yaxis)
        y_axes = self.element.root.find('y_axis')
        self.assertEqual(y_axes, None)

class TestMarkers(InternalTest):
    def test_add_marker(self):
        marker = self.marker1
        self.element.add_marker(marker)
        self.child_element_test('marker', 'marker', None, {}, True)

    def test_add_two_markers(self):
        marker = self.marker1
        marker2 = self.marker2
        self.element.add_marker(marker2)
        self.element.add_marker(marker)
        marker_tags = self.element.root.find('marker').findall('marker')
        self.assertEqual(len(marker_tags), 2)

    def test_add_same_marker(self):
        marker = self.marker1
        self.element.add_marker(marker)
        self.element.add_marker(marker)
        marker_tags = self.element.root.find('marker').findall('marker')
        self.assertEqual(len(marker_tags), 1)

    def test_remove_marker(self):
        marker = self.marker1
        self.element.add_marker(marker)
        self.element.remove_marker(marker)
        outer_tag = self.element.root.find('marker')
        marker_tags = outer_tag.findall('marker')
        self.assertEqual(len(marker_tags), 0)
        self.assertEqual(len(outer_tag), 0)

    def test_remove_two_markers(self):
        marker = self.marker1
        marker2 = self.marker2
        self.element.add_marker(marker)
        self.element.add_marker(marker2)
        self.element.remove_marker(marker)
        self.element.remove_marker(marker2)
        outer_tag = self.element.root.find('marker')
        marker_tags = outer_tag.findall('marker')
        self.assertEqual(len(marker_tags), 0)
        self.assertEqual(len(outer_tag), 0)

    def test_remove_same_marker(self):
        marker = self.marker1
        self.element.add_marker(marker)
        self.element.remove_marker(marker)
        self.element.remove_marker(marker)
        outer_tag = self.element.root.find('marker')
        self.assertEqual(outer_tag, None)

    def test_remove_no_markers(self):
        marker = self.marker1
        self.element.remove_marker(marker)
        outer_tag = self.element.root.find('marker')
        self.assertEqual(outer_tag, None)

class TestOnRight(InternalTest):
    def test_on_right(self):
        self.element.on_right(True)
        self.generic_element_test('on_right', True)

    def test_on_left(self):
        self.element.on_right(False)
        self.generic_element_test('on_right', False)

    def test_on_right_wrong(self):
        self.element.on_right('Not a boolean')
        self.null_test('on_right')

class TestInteractive(InternalTest):
    def test_interactive(self):
        self.element.interactive(True)
        self.generic_element_test('interactive', True)

    def test_interactive_wrong(self):
        self.element.interactive('Not true')
        self.null_test('interactive')

class TestXAxes(InternalTest):
    def test_add_xaxis(self):
        xaxis1 = self.xaxis1
        self.element.add_x_axis(xaxis1)
        self.generic_element_test('x_axis', None)

    def test_add_two_x_axes(self):
        xaxis1 = self.xaxis1
        xaxis2 = self.xaxis2
        self.element.add_x_axis(xaxis1)
        self.element.add_x_axis(xaxis2)
        x_axes = self.element.root.findall('x_axis')
        self.assertEqual(len(x_axes), 1)

    def test_add_same_x_axis(self):
        xaxis = self.xaxis1
        self.element.add_x_axis(xaxis)
        self.element.add_x_axis(xaxis)
        x_axes = self.element.root.findall('x_axis')
        self.assertEqual(len(x_axes), 1)

    def test_remove_x_axis(self):
        xaxis = self.xaxis1
        self.element.add_x_axis(xaxis)
        self.element.remove_x_axis(xaxis)
        x_axes = self.element.root.findall('x_axis')
        self.assertEqual(len(x_axes), 0)

    def test_remove_same_x_axis(self):
        xaxis = self.xaxis1
        self.element.add_x_axis(xaxis)
        self.element.remove_x_axis(xaxis)
        self.element.remove_x_axis(xaxis)
        x_axes = self.element.root.find('x_axis')
        self.assertEqual(x_axes, None)

    def test_remove_nonexistent(self):
        xaxis = self.xaxis1
        self.element.remove_x_axis(xaxis)
        x_axes = self.element.root.find('x_axis')
        self.assertEqual(x_axes, None)

class TestColorMode(GenericTest):
    def test_color_mode_custom(self):
        self.element.color_mode_CUSTOM()
        self.generic_element_test('color_mode', 0)

    def test_color_mode_mono(self):
        self.element.color_mode_MONO()
        self.generic_element_test('color_mode', 1)

    def test_color_mode_bayer(self):
        self.element.color_mode_BAYER()
        self.generic_element_test('color_mode', 2)

    def test_color_mode_rgb1(self):
        self.element.color_mode_RGB1()
        self.generic_element_test('color_mode', 3)

    def test_color_mode_rgb2(self):
        self.element.color_mode_RGB2()
        self.generic_element_test('color_mode', 4)

    def test_color_mode_rgb3(self):
        self.element.color_mode_RGB3()
        self.generic_element_test('color_mode', 5)

    def test_color_mode_yuv444(self):
        self.element.color_mode_YUV444()
        self.generic_element_test('color_mode', 6)

    def test_color_mode_yuv422(self):
        self.element.color_mode_YUV422()
        self.generic_element_test('color_mode', 7)

    def test_color_mode_yuv411(self):
        self.element.color_mode_YUV411()
        self.generic_element_test('color_mode', 8)

    def test_color_mode_3byte_bgr(self):
        self.element.color_mode_3BYTE_BGR()
        self.generic_element_test('color_mode', 9)

    def test_color_mode_4byte_abgr(self):
        self.element.color_mode_4BYTE_ABGR()
        self.generic_element_test('color_mode', 10)

    def test_color_mode_4byte_abgr_pre(self):
        self.element.color_mode_4BYTE_ABGR_PRE()
        self.generic_element_test('color_mode', 11)

    def test_color_mode_byte_binary(self):
        self.element.color_mode_BYTE_BINARY()
        self.generic_element_test('color_mode', 12)

    def test_color_mode_byte_gray(self):
        self.element.color_mode_BYTE_GRAY()
        self.generic_element_test('color_mode', 13)

    def test_color_mode_byte_indexed(self):
        self.element.color_mode_BYTE_INDEXED()
        self.generic_element_test('color_mode', 14)

    def test_color_mode_int_argb(self):
        self.element.color_mode_INT_ARGB()
        self.generic_element_test('color_mode', 15)

    def test_color_mode_int_argb_pre(self):
        self.element.color_mode_INT_ARGB_PRE()
        self.generic_element_test('color_mode', 16)

    def test_color_mode_int_bgr(self):
        self.element.color_mode_INT_BGR()
        self.generic_element_test('color_mode', 17)

    def test_color_mode_int_rgb(self):
        self.element.color_mode_INT_RGB()
        self.generic_element_test('color_mode', 18)

    def test_color_mode_ushort_555_rgb(self):
        self.element.color_mode_USHORT_555_RGB()
        self.generic_element_test('color_mode', 19)

    def test_color_mode_ushort_565_rgb(self):
        self.element.color_mode_USHORT_565_RGB()
        self.generic_element_test('color_mode', 20)

    def test_color_mode_ushort_gray(self):
        self.element.color_mode_USHORT_GRAY()
        self.generic_element_test('color_mode', 21)

class TestWidthPV(InternalTest):
    def test_width_pv(self):
        pv = 'this is a width'
        self.element.width_pv(pv)
        self.generic_element_test('width_pv', pv)

class TestHeightPV(InternalTest):
    def test_height_pv(self):
        pv = 'this is a height'
        self.element.height_pv(pv)
        self.generic_element_test('height_pv', pv)

class TestRegionsOfInterest(InternalTest):
    def test_add_roi(self):
        roi = self.roi1
        self.element.add_roi(roi)
        self.child_element_test('rois', 'roi', None, {}, True)

    def test_add_two_rois(self):
        roi = self.roi1
        roi2 = self.roi2
        self.element.add_roi(roi2)
        self.element.add_roi(roi)
        roi_tag = self.element.root.find('rois').findall('roi')
        self.assertEqual(len(roi_tag), 2)

    def test_add_same_roi(self):
        roi = self.roi1
        self.element.add_roi(roi)
        self.element.add_roi(roi)
        roi_tag = self.element.root.find('rois').findall('roi')
        self.assertEqual(len(roi_tag), 1)

    def test_remove_roi(self):
        roi = self.roi1
        self.element.add_roi(roi)
        self.element.remove_roi(roi)
        rois_tag = self.element.root.find('rois')
        roi_tag = rois_tag.findall('roi')
        self.assertEqual(len(roi_tag), 0)
        self.assertEqual(len(rois_tag), 0)

    def test_remove_two_rois(self):
        roi = self.roi1
        roi2 = self.roi2
        self.element.add_roi(roi)
        self.element.add_roi(roi2)
        self.element.remove_roi(roi)
        self.element.remove_roi(roi2)
        rois_tag = self.element.root.find('rois')
        roi_tag = rois_tag.findall('roi')
        self.assertEqual(len(roi_tag), 0)
        self.assertEqual(len(rois_tag), 0)

    def test_remove_same_roi(self):
        roi = self.roi1
        self.element.add_roi(roi)
        self.element.remove_roi(roi)
        self.element.remove_roi(roi)
        rois_tag = self.element.root.find('rois')
        self.assertEqual(rois_tag, None)

    def test_remove_no_rois(self):
        roi = self.roi1
        self.element.remove_roi(roi)
        rois_tag = self.element.root.find('rois')
        self.assertEqual(rois_tag, None)

class TestColorBarSize(InternalTest):
    def test_bar_size(self):
        tag_name = 'bar_size'
        value = 6
        self.element.bar_size(value)
        self.generic_element_test(tag_name, value)

class TestColorBar(InternalTest):
    def test_add_color_bar(self):
        bar1 = self.bar1
        self.element.add_color_bar(bar1)
        self.generic_element_test('color_bar', None)

    def test_add_two_color_bars(self):
        bar1 = self.bar1
        bar2 = self.bar2
        self.element.add_color_bar(bar1)
        self.element.add_color_bar(bar2)
        color_bars = self.element.root.findall('color_bar')
        self.assertEqual(len(color_bars), 1)

    def test_add_same_color_bar(self):
        bar1 = self.bar1
        self.element.add_color_bar(bar1)
        self.element.add_color_bar(bar1)
        color_bars = self.element.root.findall('color_bar')
        self.assertEqual(len(color_bars), 1)

    def test_remove_color_bar(self):
        bar1 = self.bar1
        self.element.add_color_bar(bar1)
        self.element.remove_color_bar(bar1)
        color_bars = self.element.root.findall('color_bar')
        self.assertEqual(len(color_bars), 0)

    def test_remove_same_color_bar(self):
        bar1 = self.bar1
        self.element.add_color_bar(bar1)
        self.element.remove_color_bar(bar1)
        self.element.remove_color_bar(bar1)
        color_bars = self.element.root.find('color_bar')
        self.assertEqual(color_bars, None)

    def test_remove_nonexistent_color_bar(self):
        bar1 = self.bar1
        self.element.remove_color_bar(bar1)
        color_bars = self.element.root.find('color_bar')
        self.assertEqual(color_bars, None)

class TestColorMap(InternalTest):
    def test_predefined_color_map(self):
        self.element.predefined_color_map('JET')
        color_map = self.element.root.find('color_map')
        self.assertEqual(color_map.find('name').text, 'JET')

    def test_two_predefined_color_map(self):
        self.element.predefined_color_map('JET')
        self.element.predefined_color_map('GRAY')
        color_map = self.element.root.find('color_map')
        self.assertEqual(color_map.find('name').text, 'GRAY')
        self.assertEqual(len(color_map.findall('name')), 1)

    def test_predefined_color_map_wrong(self):
        self.element.predefined_color_map('TEST')
        self.assertEqual(self.element.root.find('color_map'), None)

    def test_add_color_map(self):
        map1 = self.map1
        self.element.add_color_map(map1)
        self.generic_element_test('color_map', None)

    def test_add_two_color_maps(self):
        map1 = self.map1
        map2 = self.map2
        self.element.add_color_map(map1)
        self.element.add_color_map(map2)
        color_map = self.element.root.find('color_map')
        section = color_map.findall('section')
        self.assertEqual(len(section), 2)

    def test_add_same_color_map(self):
        map1 = self.map1
        self.element.add_color_map(map1)
        self.element.add_color_map(map1)
        color_map = self.element.root.find('color_map')
        section = color_map.findall('section')
        self.assertEqual(len(section), 1)

    def test_add_color_map_before_predefined(self):
        map1 = self.map1
        self.element.add_color_map(map1)
        self.element.predefined_color_map('MAGMA')
        color_map = self.element.root.find('color_map')
        self.assertFalse(color_map.findall('section'))
        self.assertTrue(color_map.findall('name'))

    def test_add_color_map_after_predefined(self):
        self.element.predefined_color_map('MAGMA')
        map1 = self.map1
        self.element.add_color_map(map1)
        color_map = self.element.root.find('color_map')
        self.assertTrue(color_map.findall('section'))
        self.assertFalse(color_map.findall('name'))

    def test_remove_color_map(self):
        map1 = self.map1
        self.element.add_color_map(map1)
        self.element.remove_color_map(map1)
        color_map = self.element.root.findall('color_map')
        self.assertEqual(len(color_map), 0)

    def test_remove_another_color_map(self):
        map1 = self.map1
        map2 = self.map2
        self.element.add_color_map(map1)
        self.element.add_color_map(map2)
        self.element.remove_color_map(map1)
        color_map = self.element.root.find('color_map')
        self.assertEqual(len(color_map.findall('section')), 1)

    def test_remove_three_color_maps(self):
        map1 = self.map1
        map2 = self.map2
        map3 = self.map3
        self.element.add_color_map(map1)
        self.element.add_color_map(map2)
        self.element.add_color_map(map3)
        self.element.remove_color_map(map1)
        color_map = self.element.root.find('color_map')
        self.assertEqual(len(color_map.findall('section')), 2)

    def test_remove_same_color_map(self):
        map1 = self.map1
        self.element.add_color_map(map1)
        self.element.remove_color_map(map1)
        self.element.remove_color_map(map1)
        color_map = self.element.root.find('color_map')
        self.assertEqual(color_map, None)

    def test_remove_color_nonexistent(self):
        map1 = self.map1
        map2 = self.map2
        self.element.add_color_map(map1)
        self.element.remove_color_map(map2)
        color_map = self.element.root.find('color_map')
        self.assertTrue(map2 not in color_map.findall('section'))

    def test_remove_nonexistent_color_map(self):
        map1 = self.map1
        self.element.remove_color_map(map1)
        color_map = self.element.root.find('color_map')
        self.assertEqual(color_map, None)

class TestStructure(GenericTest):
    def test_add_widget_structure(self):
        obj = self.widget_obj
        self.element.add_widget(obj)
        self.assertEqual(self.element.root.find('widget').attrib['type'], 'xyplot')


    def test_add_widget_structure_list(self):
        lst = self.widget_list
        self.element.add_widget(lst)
        self.assertEqual(self.element.root.findall('widget')[0].attrib['type'], 'label')
        self.assertEqual(self.element.root.findall('widget')[1].attrib['type'], 'xyplot')
