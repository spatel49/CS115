'''
Created on Sep 14, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Siddhanth Patel
username: spate144

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
    
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

def remove(letter, Rack):
    """Takes as input a single letter and removes it from the Rack"""
    if Rack == []:
        return []
    if letter==Rack[0]:
        return Rack[1:]
    return [Rack[0]] + remove(letter,Rack[1:])
    
print(remove('w', ['w','h','a','t']))

def isPossible(word, Rack):
    """Takes in a string as input and determines whether that word can be created using single
    letters from the Rack"""
    if word == '':
        return True
    if word[0] in Rack:
        return isPossible(word[1:], remove(word[0], Rack))
    return False

print (isPossible('one', ['t','w','o','q','n','e']))

def listOfwords(Dict, Rack):
    return filter(lambda word: isPossible(word, Rack), Dict)

def scoreList(Rack):
    """Takes as input a list of lower case letters and returns a list of all words in the global Dictionary
    that can be made from those letters and a score for each one"""
    return map(lambda word: [word, wordScore(word, scrabbleScores)], listOfwords(Dictionary, Rack))
print (scoreList(["a", "s", "m", "t", "p"]))
    
def bestWord(Rack):
    """Takes as input a list of lower case letters and returns the best word along with its
    corresponding score"""
    scorelist = scoreList(Rack)
    if scorelist == []:
        return ['',0]
    return reduce(lambda x,y: x if x[1] > y[1] else y, scorelist)

print(bestWord(["a", "s", "m", "t", "p"]))

 
