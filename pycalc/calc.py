"""
    A simple calculator will calculate the sum of the 2 numbers.
"""

from __future__ import print_function

def add2nums(strA, strB):
    """
        This function calculates the sum of the 2 numbers.

        Parameters: string input A, string input B
        Return: Return sum of two number A and B if both numbers are valid.
                Otherwise, Return "Invalid input!" string
    """
    numA = 0.0
    numB = 0.0
    try:
        numA = float(strA)
        numB = float(strB)
    except ValueError:
        return "Invalid input!"
    return numA + numB

if __name__ == '__main__':
    """
        Test cases: for testing different cases
    """
    testCases = [ [" ", " "], [" 1 ", " "], ["/", " 2.5 "], [" 1.5 ", "  2.5 "],  ]
    for t in testCases:
        res = add2nums(t[0], t[1])
        print('{} = {}'.format(t, res))
