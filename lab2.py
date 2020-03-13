'''
Created on Sep 12, 2018
@author: Siddhanth Patel
username: spate144
I pledge my honor that I have abided by the Stevens Honor System.

'''
from cs115 import map, range, reduce


def length(lst):
    """Returns the length of the list."""
    if lst == []:
        return 0
    return 1 + length(lst[1:])

def dot(L, K):
    """Returns the dot product of lists L and K, in the form of: L = (x,y,z...) and K is (x,y,z...)"""
    if L == [] or K == []:
        return 0
    else:
        return L[0]*K[0] + dot(L[1:], K[1:])
    
def explode(s):
    """Takes a string and splits it into a list of strings, each with a length of 1"""
    if s == "":
        return []
    else:
        return [s[0]] + explode(s[1:])

def ind(e,L):
    """Returns the index at which e is found in list or string L"""
    if not L:
        return 0
    if L[0] == e:
        return 0
    else:
        return 1 + ind(e,L[1:])

def removeAll(e,L):
    """Takes in an element e, and removes it from list L. Only top level elements of L are removed"""
    if not L:
        return []
    if L[0] == e:
        return removeAll(e,L[1:])
    else:
        return [L[0]] + removeAll(e,L[1:])

def myFilter(f,L):
    """Takes two inputs, a function f that takes an input and returns either True or False, and a list L.
    Returns a new list, where the predicate returns True"""
    if L == []:
        return []
    if f(L[0]) == False:
        return myFilter(f,L[1:])
    else:
        return [L[0]] + myFilter(f,L[1:])

def deepReverse(L):
    """Takes a input a list of elements and returns the list in reverse order, including the lists in the list."""
    if L == []:
        return []
    if isinstance(L[0],list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]]
    
    
    