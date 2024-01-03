#!/usr/bin/python3

def safe_print_list(input_list=[], x=0):
    """Print a specified number of elements from a list.

    Args:
        input_list (list): The list containing elements to be printed.
        x (int): The number of elements from input_list to be printed.

    Returns:
        int: The actual x of elements that were printed.
    """
    printed_x = 0
    for i in range(x):
        try:
            print("{}".format(input_list[i]), end="")
            printed_x += 1
        except IndexError:
            break
    print("")
    return printed_x
