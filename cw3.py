'''
Created on Sep 10, 2018

@author: sypat
'''
from cs115 import range, map, reduce, filter
import math

def superSpecial (x):
    if x <42:
            return "Small number"
    elif x==42 or x % 42 == 0 :
        return "Nice"
    elif 41 <= x <= 43:
        return "So close!"
    else:
        return "Yuck"
print(superSpecial(42))

def my_map(f, lst):
    """Returns a new list where the function f has been applied to every element in the original list"""
    if lst == []:
        return []
    return [f(list[0])] + my_map(f, lst[1:])

def power(x,y):
    """Returns x^y."""
    if y==0:
        return 1
    return x * power (x,y-1)

def power_tail(x,y):
    """Computers x^y using tail cw_recursion."""
    def power_tail_helper(x, y, accum):
        if y==0:
            return accum
        return power_tail_helper(x, y-1, x * accum)
    return power_tail_helper(x, y, 1)

def my_reduce(f, lst):
    """Reduces the list to a single value as a dictated by the predicate f"""
    def my_reduce_helper(f, lst, accum):
        if lst == []:
            return accum
        return my_reduce_helper(f, lst[1:], f(accum, lst[0]))
    
    if lst == []:
        raise TypeError('my_reduce() of empty sequence with no inital value') 
    return my_reduce_helper(f, lst[1:], lst[0])

def add(x,y):
    return x+y
print(my_reduce(add, range(11)))

"""
def sqr(x):
    return x*x
print(my_map(sqr,[1,2,3]))"""

def prime(n):
    """Returns whether or not an integer is prime"""
    possible_divisors = range(2, int(math.sqrt(n)) + 1)
    divisors = filter(lambda x: n % x == 0, possible_divisors)
    return len(divisors) == 0

print(prime(2))

def primes(n):
    def sieve(lst):
        if lst == []:
            return []
        return [lst[0]] + sieve(filter(lambda x: x % lst[0] != 0, lst[1:]))    
    return sieve(range(2,n+1))

print(primes(10))


def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib (n-2)

print(fib(5))

def subset(target, lst):
    if target == 0:
        return True
    if lst == []:
        return False
    return subset(target - lst[0], lst[1:]) or subset(target, lst[1:])

"""Determines whether or not it is possible to create target sum using the values in the
     list. Values in the list can be positive, negative, or 0."""
     
print(subset(10,[1,9,1]))

def powerset(lst):
    """Returns the power set of the list, that is, the set of all subsets of
    the list."""
    if lst == []:
        return [[]]
    lose_it = powerset(lst[1:])
    use_it = map(lambda subset: [lst[0]] + subset, lose_it)
    return lose_it + use_it

print(powerset(range(2)))

print(powerset([1,2,3]))

def subset_with_values(target, lst):
    """Determines whether or not it is possible to create the target sum using values in the list. Values in the list
    can be positive, negative, or zero. The function returns a tuple of exactly two items. The first is a Boolean that indicates
    True if the sum is possible and False if it's not.
    The second element in the tuple is a list of all the values that add up to make the target sum."""
    if target == 0:
        return (True, [])
    if lst == []:
        return (False, [])
    use_it = subset_with_values(target - lst[0], lst[1:])
    if use_it[0] == True:
        return (True, [lst[0]] + use_it[1]) 
    return subset_with_values(target, lst[1:])

print(subset_with_values(5,[3,1,2]))

def LCS(s1, s2):
    """Returns the length of the longest common subsequence in strings s1 and s2"""
    if s1 == '' or s2 == '':
        return 0
    if s1[0] == s2[0]:
        return 1 + LCS(s1[1:], s2[1:])
    return max(LCS(s1, s2[1:]), LCS(s1[1:], s2))

print(LCS('spot', 'pots'))

def LCS_with_values(s1, s2):
    if s1 == '' or s2 == '':
        return [0, '']
    if s1[0] == s2[0]:
        result = LCS_with_values(s1[1:], s2[1:])
        return [1+ result[0], s1[0] + result[1]]
    useS1 = LCS_with_values(s1, s2[1:])
    useS2 = LCS_with_values(s1[1:], s2)
    if useS1[0] > useS2[0]:
        return useS1
    return useS2

print(LCS_with_values('spot', 'pots'))

def change(amount, coins):
    """Takes in input as amount and returns the minimum number of coins needed to create the amount"""
    if amount == 0:
        return 0
    if coins == []:
        return float('inf')
    if amount < coins[0]:
        return change(amount, coins[1:])
    use_it = 1 + change(amount - coins[0], coins)
    lose_it = change(amount, coins[1:])
    return min(use_it, lose_it)

print(change(48, [1, 7, 24, 42]))


def coin_row(lst):
    if lst == []:
        return 0
    return max(lst[0] + coin_row(lst[2:]), coin_row(lst[1:]))

print(coin_row([]))
#print(coin_row_with_values([]))
print(coin_row([5, 1, 2, 10, 6, 2]))
#print(coin_row_with_values([5, 1, 2, 10, 6, 2]))
print(coin_row([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))
#print(coin_row_with_values([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))