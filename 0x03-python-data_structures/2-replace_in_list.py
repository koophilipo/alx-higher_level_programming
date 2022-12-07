#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx >= 0:
        y = len(my_list)
        if idx < y:
            my_list.pop(idx)
            my_list.insert(idx, element)
    return (my_list)
