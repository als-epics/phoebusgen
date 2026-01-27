from phoebusgen.properties import HasMacros, HasName, HasFile, HasUrl, HasBit, HasLabel, HasFileComponent, FileComponent, HasTabs, Tab
import pytest
import re


@pytest.mark.parametrize("property_cls, initial_value, new_value", [
    (HasName, "", "NewName"),
    (HasFile, "", "new/file/path.bob"),
    (HasUrl, "", "http://new.url"),
    (HasBit, 0, 1),
    (HasLabel, "", "New Label"),
])
def test_widget_primitive_properties(property_cls, initial_value, new_value, property_factory):
    prop = property_factory(property_cls)
    prop_name = re.sub(r"([a-z])([A-Z])", r"\1_\2", property_cls.__name__[3:]).lower()

    assert getattr(prop, prop_name) == initial_value
    setattr(prop, prop_name, new_value)
    assert getattr(prop, prop_name) == new_value

    assert prop.root.find(prop_name) is not None
    assert prop.root.find(prop_name).text == str(new_value)


def test_file_component_property(property_factory):
    prop = property_factory(HasFileComponent)
    assert prop.file_component == FileComponent.FULL_PATH
    prop.file_component = FileComponent.DIRECTORY
    assert prop.file_component == FileComponent.DIRECTORY
    assert prop.root.find("file_component") is not None
    assert prop.root.find("file_component").text == str(FileComponent.DIRECTORY.value)


def test_macros_property(property_factory):
    prop = property_factory(HasMacros)
    assert prop.macros == {}
    prop.macros["TestMacro"] = "TestValue"
    assert prop.macros == {"TestMacro": "TestValue"}
    prop.macros = {"macro1": "value1", "macro2": "value2"}
    assert prop.macros == {'macro1': 'value1', 'macro2': 'value2'}
    assert prop.root.find('macros') is not None


def test_tabs_property(property_factory):
    prop = property_factory(HasTabs)
    assert prop.tabs == []

    prop.tabs.append(Tab(name="Tab1", file="tab1.bob"))
    assert len(prop.tabs) == 1
    assert prop.root.find("tabs") is not None
    assert len(prop.root.find("tabs").findall("tab")) == 1
    tab_elem = prop.root.find("tabs").findall("tab")[0]
    assert tab_elem.find("name").text == "Tab1"
    assert tab_elem.find("file").text == "tab1.bob"
    prop.tabs = [Tab(name="Tab2"), Tab(name="Tab3", file="tab3.bob")]
    assert len(prop.tabs) == 2
    assert len(prop.root.find("tabs").findall("tab")) == 2

