'''
Created on Sep 14, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Siddhanth Patel
username: spate144

CS115 - Hw 3
'''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from cs115 import map, reduce, filter

def giveChange(amount, coins):
    if amount == 0:
        return [0,[]]
    if coins == [] or amount <0:
        return [float('inf') , []]
    if amount < coins[0]:
        return giveChange(amount, coins[1:])
    use_it= giveChange(amount - coins[0], coins)
    lose_it= giveChange(amount, coins[1:])
    if use_it[0] < lose_it[0]:
        return [1 + use_it[0], use_it[1] + [coins[0]]]
    return lose_it
    
print(giveChange(100, [1, 7, 24, 42]))

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(letter, scorelist):
    """Takes as input a single letter and finds the score associated with that letter from 
    the ScrabbleScores List"""
    if scorelist == []:
        return 0
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    return letterScore(letter,scorelist[1:])

print(letterScore("f", scrabbleScores))

def wordScore(S, scoreList):
    """Takes as input a string S and returns the total score of all the letters in that string
    according to the scrabbleScores list"""
    if S == '':
        return 0
    return letterScore(S[0], scoreList) + wordScore(S[1:],scoreList)

print(wordScore("spam", scrabbleScores))

def wordsWithScore(dct, scores):
    ''''List of words in dct, with their Scrabble score.Assume dct is a list of words and scores is a list of [letter,number]
     pairs. Return the dictionary annotated so each word is paired with its
     value. For example, wordsWithScore(Dictionary, scrabbleScores) should
     return [['a', 1], ['am', 4], ['at', 2] ...etc... ]'''
    if dct == []:
        return []
    return [[dct[0], wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)
 
print(wordsWithScore(Dictionary,scrabbleScores))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use cw_recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if n == 0:
        return []
    if L==[]:
        return []
    return [L[0]] + take(n-1, L[1:])

print(take(3,[1,2,3,4,5]))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use cw_recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if n == 0:
        return L
    if L==[]:
        return []
    return drop(n-1, L[1:])

print(drop(5,[1,2,3,4,5,6,7,8]))