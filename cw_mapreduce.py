'''
Created on Sep 5, 2018

@author: sypat
'''
from cs115 import map, reduce

def add(x,y):
    """Returns the sum of x and y."""
    return x + y

def sqr(x):
    """Returns the square of x"""
    return x * x

def mult(x,y):
    return x * y


def span(lst):
    return reduce(max, lst) - reduce(min, lst)

    
def gauss(n):
    """Takes as input a positive integer n and returns the sum
    1 + 2 + 3 + ... + n"""
    return reduce(add, range(1, n+1))

def sum_of_squares(n):
    """Takes as input a positive integer n and returns the sum
    1^2 + 2^2 + 3^2 + ... n^2"""
    return reduce(add,map(sqr,range(1, n+1)))
