#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if x == 100:
                print("FizzBuzz", end='\n')
        elif x % 3 == 0:
            print("Fizz", end=' ')
        elif x % 5 == 0:
            print("Buzz", end=' ')
        elif not (x % 3) and not (x % 5):
            print("FizzBuzz", end=' ')
        else:
            print(x, end=' ')
