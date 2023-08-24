#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num, deno = 0, 0
    for i in my_list:
        num += i[0] * i[1]
        deno += i[1]
    return num/deno
