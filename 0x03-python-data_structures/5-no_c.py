#!/usr/bin/python3
def no_c(my_string):
    dup = [c for c in my_string if c != 'c' and c != 'C']
    return ("".join(dup))
