#!/usr/bin/env python3

def no_c(my_string):
    if my_string:
        if len(my_string) > 0:
            s = ""
            for i in my_string:
                if i == 'c' or i == 'C':
                    pass
                else:
                    s += i
            return (s)
    return (my_string)
