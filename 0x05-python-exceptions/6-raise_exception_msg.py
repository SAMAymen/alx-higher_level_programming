#!/usr/bin/python3

def raise_exception_msg(message=""):
    """Raise a NameError exception with the provided message.

    Args:
        message (str): The message to include with the exception.

    Raises:
        NameError: The exception with the provided message.
    """
    raise NameError(message)
