import yaml
import sys

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
                    if subclass == elem_type:
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
    if len(sys.argv) == 2:
        print_structure()
        sys.exit(0)
    elif len(sys.argv) == 1:
        print_all_props()
        sys.exit(0)
    elif len(sys.argv) != 3:
        print("must specify <Class> <Property>!")
        print("Possible Classes: Graphics, Monitors, Controls, Plots, Structure, Miscellaneous")
        print("Property: can be single property or list of properties inside of class")
        sys.exit(2)
    arg_type = sys.argv[1]
    arg = sys.argv[2]
    arg = arg.split(',')
    if len(arg) == 1:
        check_elem(arg_type, arg[0])
    else:
        #l = []
        #for a in arg:
        #    l.append(check_elem(arg_type, arg))
        check_elements(arg_type, arg)


