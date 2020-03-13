'''
Created on Sep 19, 2018
@author: Siddhanth Patel
username: spate144
I pledge my honor that I have abided by the Stevens Honor System.
'''

from cs115 import map, reduce, range, filter
import math
from math import inf

def knapsack(capacity, itemList):
    if capacity == 0:
        return [0, []]
    if itemList== []:
        return [0, []]
    lose_it = knapsack(capacity, itemList[1:])
    if capacity < itemList[0][0]:
        return lose_it
    use_it = knapsack(capacity-1, itemList[1:])
    if use_it[0] + itemList[0][1] > lose_it[0]:
        return [use_it[0] + itemList[0][1]] + [[itemList[0]] + use_it[1]]
    return [lose_it[0], lose_it[1]]

print(knapsack(5, [[2,500], [5,150], [1, 150], [1,400]]))

def functimes(lst):
    if lst == []:
        return None
    if len(lst) == 1:
        return lst[0]
    x = functimes(lst[1:])
    if x > lst[0]:
        return x
    return lst[0]

print(functimes([1,2,3,4,5,6,7]))


