#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number
print("Last digit of {} is".format(number), end=' ')
if number < 0:
    x *= (-1)
x %= 10
if number < 0:
    x *= (-1)
if x < 6 and x != 0:
    print("{} and is less than 6 and not 0".format(x))
elif x > 5:
    print("{} and is greater than 5".format(x))
elif x == 0:
    print("{} and is 0".format(x))
exit(0)
