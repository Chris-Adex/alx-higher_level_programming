#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Function that adds two numbers, converting floats to integers.

    Args:
        a: First number to be added.
        b: Second number to be added.

    Returns:
        The sum of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
