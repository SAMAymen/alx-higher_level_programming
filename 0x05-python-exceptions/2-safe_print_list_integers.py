#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first 'x' elements from a list that are integers.

    Args:
        my_list (list): The list containing elements to print from.
        x (int): The number of elements from my_list to print.

    Returns:
        int: The number of integer elements that were successfully printed.
    """
    printed_x = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed_x += 1
        except (ValueError, TypeError):
            continue
    print("")
    return printed_x
