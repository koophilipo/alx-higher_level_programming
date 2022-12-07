#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list:
        if len(my_list) > 0:
            new_list = my_list.copy()
            for i, val in enumerate(my_list):
                if val == search:
                    new_list.pop(i)
                    new_list.insert(i, replace)
            return (new_list)
    return (my_list)
