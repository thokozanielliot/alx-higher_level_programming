#!/usr/bin/python3
def pow(a, b):
    if b != 0:
        return a * pow(a, b -1)
    else:
        return 1
