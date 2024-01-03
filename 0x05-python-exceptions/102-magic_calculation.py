#!/usr/bin/python3

def magic_calculation(a, b):
    """
    Perform a custom magic calculation based on the provided values.

    Args:
        a (int or float): The first value.
        b (int or float): The second value.

    Returns:
        int or float: The result of the magic calculation.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except Exception:
            result = b + a
            break
    return result
