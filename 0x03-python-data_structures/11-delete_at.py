#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if my_list or idx < 0:
        if len(my_list) > 0 and idx < len(my_list):
            my_list.pop(idx)
    return (my_list)
