'''
Created on Sep 19, 2018
@author: Siddhanth Patel
username: spate144
I pledge my honor that I have abided by the Stevens Honor System.
'''

from cs115 import map, reduce, range, filter
import math
from math import inf

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
