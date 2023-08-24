#1/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    _keys = list(new_dic.keys())
    for i in _keys:
        new_dic[i] *= 2
    return new_dic