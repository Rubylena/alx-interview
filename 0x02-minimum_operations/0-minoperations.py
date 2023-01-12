#!/usr/bin/python3

"""
    Method that determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
        A function that calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
        args: n: Number of characters to be displayed
        return:
               number of min operations
    """

    atStart = 1
    counter = 0
    empty = 0

    # the start of every iteration through the file for each operations
    while atStart < n:
        # what remains after each iteration(atStart)
        remainder = n - atStart
        # remainder divided by number of iterations(atStart)
        if (remainder % atStart == 0):
            empty = atStart
            atStart += empty
            counter += 2
        else:
            atStart += empty
            counter += 1
    return counter
