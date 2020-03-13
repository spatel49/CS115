'''lab1
Created on Sep 5, 2018
@author: Siddhanth Patel
username: spate144
I pledge my honor that I have abided by the Stevens Honor System.
'''
from cs115 import map, reduce
import math

def inverse(n):
    """Returns the inverse of n"""
    return 1/n

def add(x,y):
    """Returns the sum of x and y."""
    return x + y

def factorial(n):
    """Returns the factorial of n, except 0"""
    return n * factorial(n-1)

def e(n):
    """Returns approximations of the value of e, by adding the inverse of n factorial."""
    mylist = range (1,n+1)
    newlist = map(math.factorial, mylist)
    return reduce(add, map(inverse, newlist)) + 1
               
def error(n):
    """Returns the error of the approximations of the value of e"""
    return abs(math.e - e(n))