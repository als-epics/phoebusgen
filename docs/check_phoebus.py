import yaml
import sys
import argparse

# Used to parse phoebus.yaml and check what widgets use what properties

def print_structure():
    with open('phoebus.yaml') as f:
        dataMap = yaml.safe_load(f)
        for widget_type, widgets in dataMap.items():
            print(widget_type)
            for widget_name, widget_items in widgets.items():
                print("\t{}".format(widget_name))
                for subclass, subclass_types in widget_items.items():
                    print("\t\t{}".format(subclass))
                    for val in subclass_types:
                        print("\t\t\t{}".format(val))

def print_props(widget):
    with open('phoebus.yaml') as f:
        dataMap = yaml.safe_load(f)
        for widget_type, widgets in dataMap.items():
            for widget_name, widget_items in widgets.items():
                if widget_name.lower().replace(' ', '') == widget.lower().replace(' ', ''):
                    for subclass, subclass_types in widget_items.items():
                        for val in subclass_types:
                            print(val)

                    
def print_all_props():
    p = set()
    with open('phoebus.yaml') as f:
        dataMap = yaml.safe_load(f)
        for widget_type, widgets in dataMap.items():
            for widget_name, widget_items in widgets.items():
                for subclass, subclass_types in widget_items.items():
                    for val in subclass_types:
                        if type(val) != type({}):
                            p.add(val)
    for v in p:
        print(v)

def check_elem(elem_type, elem):
    widget_list = []
    with open('phoebus.yaml') as f:
        dataMap = yaml.safe_load(f)
        for widget_type, widgets in dataMap.items():
            for widget_name, widget_items in widgets.items():
                for subclass, subclass_types in widget_items.items():
                    if subclass.lower().replace(' ', '')  == elem_type.lower().replace(' ', ''):
                        if elem in subclass_types:
                            widget_list.append(widget_name)
                            print(widget_name)
                        #for val in subclass_types:
                        #    if val == elem:
                        #        print(widget_name)
    return widget_list

def check_elements(elem_type, elem):
    with open('phoebus.yaml') as f:
        dataMap = yaml.safe_load(f)
        for widget_type, widgets in dataMap.items():
            for widget_name, widget_items in widgets.items():
                found = True 
                for subclass, subclass_types in widget_items.items():
                    if subclass == elem_type:
                        for e in elem:
                            if e not in subclass_types:
                                found = False
                        if found:
                            print(widget_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='Used to find information about Phoebus widgets like what properties are available for that widget, \
            what widgets use a property, etc.')
    subparsers = parser.add_subparsers(dest='command')
    print_parser = subparsers.add_parser('print', help='Print either the entire Phoebus class structure, or print all properties')
    print_parser.add_argument('mode', choices=['structure', 'all'])

    widget_parser = subparsers.add_parser('widget', help='Takes 1 arg. Show all properties for a given widget')
    widget_parser.add_argument('widget_type', type=str, action='store')

    property_parser = subparsers.add_parser('property', help='Takes 2 args. Shows all widgets for a given property')
    property_parser.add_argument('widget_class', type=str, action='store', help='help for class')
    property_parser.add_argument('widget_property', type=str, action='store', help='help for property')

    args = parser.parse_args()

    if args.command == 'print':
        if args.mode == 'all':
            print_all_props()
        elif args.mode == 'structure':
            print_structure()
    elif args.command == 'widget':
        print_props(args.widget_type)
    elif args.command == 'property':
        check_elem(args.widget_class, args.widget_property)
    else:
        parser.print_help()
