#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if i == 50 or i == 99:
            my_string.pop(i)
            new_str = my_string

