#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    x = len(argv) - 1
    if x == 1:
        print("{} argument:".format(x))
    elif x == 0:
        print("{} arguments.".format(x))
    else:
        print("{} arguments:".format(x))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
