#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for i, val in enumerate(reversed(my_list)):
        print("{}".format(val))
