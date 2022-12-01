#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        if x > i and i != 8:
            print("{:d}{:d}, ".format(i, x), end='')
        elif (i == 8 and x == 9):
            print("{:d}{:d}".format(i, x))
        x += 1
exit(0)
