#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            count += 1
        print("\n", end='')
    except IndexError:
        print("\n", end='')
        return (count)
    else:
        return (count)
