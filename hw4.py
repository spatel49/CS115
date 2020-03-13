'''
Created on October 3, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Siddhanth Patel
username: spate144

'''

def pascal_row(n):
    """Returns a list of numbers from the nth row of a pascal's triangle"""
    def pascal_add(lst):
        """Returns the list of sums of adjacent numbers in a row of the pascal's triangle"""
        if len(lst) <= 1:
            return []
        return [lst[0] + lst[1]] + pascal_add(lst[1:])
    def pascal_helper(n, lst):
        """Uses cw_recursion to return a list of numbers from the nth row of a pascal's triangle"""
        if n == 0:
            return lst
        return pascal_helper(n - 1, [1] + pascal_add(lst) + [1])
    return pascal_helper(n, [1])

print(pascal_row(3))

def pascal_triangle(n):
    """Returns a list of lists, where each list corresponds to numbers in a row of pascal's triangle (from row 0 to row n)."""
    if n < 0:
        return []
    return pascal_triangle(n - 1) + [pascal_row(n)]

print(pascal_triangle(3))


