'''
Created on Sep 09, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Siddhanth Patel
username: spate144

'''

import sys
from cs115 import map, reduce, filter

def factorial(n):
    """Takes value of n, and finds its factorial using cw_recursion"""
    if n == 0:
        return 1
    return n * factorial (n-1)

def add (x,y):
    """Takes values of x, y and adds them"""
    return x + y

def mean(L):
    """Takes a list as input and returns the average value in the list"""
    return reduce(add,L)/len(L)

def divides(n):
    """Takes value of n, and determines if it is divisible by k (leaves no remainders)"""
    def div(k):
        return n % k == 0
    return div

print(divides(6)(3))

def prime(n):
    """Takes a value of n and determines if it is prime number"""
    return sum(map(divides(n),range(2,n)))==0
print (prime(7))

def sieve(L):
    if L == []: 
        return []
    else: return [L[0]] + sieve(filter(lambda X: X % L[0] != 0, L[1:]))

def primes(n):
    return sieve(range(2, n+1))

print(primes(80))

    
    