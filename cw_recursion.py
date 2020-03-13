'''
Created on Sep 10, 2018

@author: sypat
'''
from cs115 import map, range, reduce


def factorial(n):
    if n == 0:
        return 1
    return n * factorial (n-1)

print (factorial(5))

def tower(n):
    """Computes 2^(2(2...)) using recursion"""
    if n == 0:
        return 1
    return 2 ** tower(n-1)

print(map(tower, range(5)))

def tower_reduce(n):
    """Computes 2^(2(2...)) using recursion"""
    def power(x,y):
        return y**x
    return reduce(power,[2]*n)

print(map(tower_reduce,range(1, 5)))

def length(lst):
    """Returns the length of the list."""
    if lst == []:
        return 0
    return 1 + length(lst[1:])

def length_str(s):
    """Returns the length of the string."""
    if s == "":
        return 0
    return 1 + length_str(s[1:])

def reverse(lst):
    """Takes as input a list of elements and returns the list in reverse order."""
    if lst == []:
        return []
    return reverse(lst[1:]) + [lst[0]]

print(reverse([1,2,4,5]))
    
def member(x,lst):
    """Returns True if x is contained in the list and false otherwise"""
    if lst == []:
        return False
    if x == lst[0]:
        return True
    return member(x, lst[1:])
    
print(member(4,[1,2,3,4,5]))

def mem(x,lst):
    if x != [x]:
        return False
    return True

print(mem(5,[1,2,3,4,5]))

def collapse(lst):
    """Collapses a list of possibly nested lists into a single list of values"""
    if lst == []:
        return []
    if isinstance(lst[0],list):
        return collapse(lst[0]) + collapse(lst[1:])
    return [lst[0]] + collapse(lst[1:])

print(collapse([1,[2,5], 5, [5,[5,3],6]]))

