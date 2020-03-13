'''
Created on Sep 21, 2018

@author: sypat
'''

from cs115 import range, map, reduce, filter
import math

def coin_row(lst):
    if lst == []:
        return 0
    return max(lst[0] + coin_row(lst[2:]), coin_row(lst[1:]))

def coin_row_with_values(lst):
    if lst == []:
        return [0,[]]
    use_it = coin_row_with_values(lst[2:])
    new_sum = lst[0] + use_it[0]
    lose_it = coin_row_with_values(lst[1:])
    if new_sum > lose_it[0]:
        return [new_sum, [lst[0]] + use_it[1]]
    return lose_it

print(coin_row([]))
print(coin_row_with_values([]))
print(coin_row([5, 1, 2, 10, 6, 2]))
print(coin_row_with_values([5, 1, 2, 10, 6, 2]))
print(coin_row([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))
print(coin_row_with_values([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))

def distance(first, second):
    if first == '' or second == '':
        return len(first)
    if first[0] == second[0]:
        return distance(first[1:], second[1:])
    substitution = 1+ distance(first[1:], second[1:])
    insertion = distance(first, second[1:])
    deletion = 1 + distance(first[1:], second)
    return 1+ min(substitution, insertion, deletion)

print(distance('sam', 'am'))
print(distance('pot', 'spatty'))


