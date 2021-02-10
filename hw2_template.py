'''
Created on _9/18/18____________________________________________________________
@author:   _Michael Reilly_____________________________________________________
Pledge:    _"I pledge my honor that I have abided by the Stevens Honor System"_

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
    '''Returns the score associated with a letter in scrabble
    based on the scorelist'''
    if scorelist[0][0]==letter:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])
def wordScore(S, scorelist):
    '''Returns the score of a word in scrabble based on the scorelist'''
    if S=="":
        return 0
    else:
        n=letterScore(S[0], scorelist)
        return n + wordScore(S[1:], scorelist)
def letterstart(Rack, wordlist):
        if wordlist==[]:
            return []
        elif wordlist[0][0]==Rack[0]:
            return [wordlist[0]]+letterstart(Rack[0], wordlist[1:])
        else:
            return letterstart(Rack[0], wordlist[1:])
def possibleword(Rack, word):
    originalrack=Rack[:]
    if Rack==[] and word !=[]:
        return False
    elif Rack==[] and word==[]:
        return True
    elif Rack!=[] and word==[]:
        possibleword(Rack[1:], word)
    elif Rack[0]==word[0]:
        return possibleword(originalrack, word[1:])
    else:
        return possibleword(Rack[1:], word[0])
def explode(S):
    '''Makes a list out of the individual letters of a string.'''
    if S=="":
        return []
    if S==S[0]:
        return [S[0]]
    else:
        L=[""]
        L[0]=S[0]
        return L+explode(S[1:])
def ind(e,L):
    '''finds the first index where element e occurs in a list or string.
    If element e is not in the list returns the length of the list or the string.'''
    if L==[]:
        return 0
    if L=="":
        return 0
    if e==L[0]:
        return 0
    else:
        return 1+ind(e,L[1:])
def removeAll(e, L):
    '''removes all instances of element e from a list.
    Only removes element e if it is a top-level element in the list.'''
    if L==[]:
        return []
    elif e==L[0]:
        return removeAll(e,L[1:])
    else:
        return [L[0]]+removeAll(e,L[1:])
def removing(Rack, L):
    print(L)
    if L==[]:
        return []
    elif L[0]==[]:
        return removing(Rack, L[1:])
    elif Rack==[]:
        L.remove([0][0])
        return removing(Rack,L)
    elif Rack[0]==L[0][0]:
        if len(L)==1:
            return removing(Rack, L[1:])
        else:
            return [L[0][0]]+removing(Rack,L[0][1:])
    elif Rack[0]!=L[0][0] and Rack!=[]:
        return removing(Rack,L[0][1:])
def validword(Rack, M):
            if M==[]:
                return []
            elif len(M)<1:
                return []
            elif M[0][0] in Rack and len(M[0])>=1:
                if len(M[0])>1:
                    [Long]=[M[0]]
                    if len(Long[0])==1:
                        if doublecheck(Rack, Long)==True:
                            return [True]+validword(Rack, M[1:])
                        else:
                            return [False]+validword(Rack, M[1:])
                    else:
                        return validword(Rack, Long[1:])
                else:
                    return [True]+validword(Rack, M[1:])
            else:
                return [False] + validword(Rack, M[1:])
def doublecheck(Rack, char):
    if char==[]:
        return []
    elif char[0] in Rack:
        if len(char)==1:
            return True
        else:
            return doublecheck(Rack, char[1:])
    else:
        return False
def replace(L, wordlist):
    if L==[]:
        return []
    elif L[0]==True:
        return [wordlist[0]]+replace(L[1:],wordlist[1:])
    else:
        return replace(L[1:],wordlist[1:])
def scoreList(Rack):
    '''Uses a list of letters, and using the Dictionary and scrabbleScores list
    determines all words and their score that can be made from the
    available letters'''
    wordlist=Dictionary
    if Rack==[]:
        return []
    else:
        L=map(explode, wordlist)
        W=validword(Rack,L)
        R=replace(W, wordlist)
        V=removeAll(False, R)
        def scoring(W, scorelist):
            if W==[]:
                return []
            else:
                return [[W[0]]+[wordScore(W[0], scorelist)]]+scoring(W[1:], scorelist)
        return scoring(V, scrabbleScores)
def bestWord(Rack):
    L=scoreList(Rack)
    def highestnumber(L):
        print(L)
        if len(L)==1:
            return L
        elif L[0][1]>L[1][1]:
            return highestnumber([L[0]]+L[2:])
        elif L[0][1]==L[1][1]:
            return highestnumber(L[1:])
        else:
            return highestnumber(L[1:])
    H=highestnumber(L)
    return H
