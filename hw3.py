'''
Created on __09/23/18_____________________
@author:   __Michael Reilly_____________________
Pledge:    __I pledge my honor that I have abided by the Stevens Honor System__

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here

from cs115 import *
def giveChange(amount, coins):
    '''Finds the minimum number of coins needed  to make a specific
    amount of money and returns that minimum number of coins
    as well as a list the coins that make up that least
    number of coins of change'''
    def change(amount, coins):
        '''Finds the least number of coins to get the amount of change'''
        if coins==[] and amount==0:
            return 0
        elif coins==[]:
            return float("inf")
        elif amount in coins:
            return 1
        def subchange(A, C):
            if A in C:
                return 1
            elif A==C[len(C)-1]:
                return 1
            elif A<C[len(C)-1]:
                return subchange(A, C[:len(C)-1])
            elif A>C[len(C)-1]:
                number=1+subchange(A-C[len(C)-1], C)
                return number
        if amount<coins[len(coins)-1]:
            return change(amount, coins[:len(coins)-1])
        if amount>coins[len(coins)-1]:
            lose=subchange(amount, coins[:len(coins)-1])
            use=subchange(amount, coins)
            return min(use, lose)
    def setchange(amount, coins):
        '''Gets the set of coins for the least amount of coins to get proper change'''
        if coins==[] and amount==0:
            return [0]
        elif coins==[]:
            return [float("inf")]
        elif amount in coins:
            return [amount]
        def subset(A, C):
            if A in C:
                return [A]
            elif A==C[len(C)-1]:
                return [C[len(C)-1]]
            elif A<C[len(C)-1]:
                return subset(A, C[:len(C)-1])
            elif A>C[len(C)-1]:
                return [C[len(C)-1]]+subset(A-C[len(C)-1], C)
        if amount<coins[len(coins)-1]:
            return setchange(amount, coins[:len(coins)-1])
        if amount>coins[len(coins)-1]:
            lose=subset(amount, coins[:len(coins)-1])
            use=subset(amount, coins)
            if len(use)>len(lose):
                return lose
            else:
                return use
    return [change(amount,coins)]+[setchange(amount,coins)]
        
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
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    def letterScore(letter, scorelist):
        '''Returns the score for an individual letter in scrabble'''
        if scorelist[0][0]==letter:
            return scorelist[0][1]
        else:
            return letterScore(letter, scorelist[1:])
    def wordScore(S, scorelist):
        '''Returns the score of a whole word in scrabble based on the letter scores'''
        if S=="":
            return 0
        else:
            n=letterScore(S[0], scorelist)
            return n + wordScore(S[1:], scorelist)
    if dct==[]:
        return []
    else:
        return [[dct[0]]+[wordScore(dct[0], scores)]]+wordsWithScore(dct[1:],scores)



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if n==0:
        return []
    else:
        return [L[0]]+take(n-1,L[1:])


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if n==0:
        return L
    else:
        return drop(n-1, L[1:])


