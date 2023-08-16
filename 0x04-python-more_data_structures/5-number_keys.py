#!/usr/bin/python3
def number_keys(a_dictionary):
    num_keys = 0
    list1 = list(a_dictionary.keys())
    for i in range(len(list1)):
        num_keys += 1
    return num_keys