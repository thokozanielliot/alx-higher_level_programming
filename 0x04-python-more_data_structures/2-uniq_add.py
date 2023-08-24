#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = list(set(my_list))
    x = 0
    for i in range(len(uniq_list)):
        x += uniq_list[i]
    return x
