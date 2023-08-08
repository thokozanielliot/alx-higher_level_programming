#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3:
            print("{}".format("Fizz"), end=" ")
        elif i % 5:
            print("{}".format("Buzz"), end=" ")
        elif i % 5 and i % 3:
            print("{}".format("FizzBuzz"))
        else:
            print("{}".format(i))