from cs115 import *

L = [1,2,3]   # this is a list
M = range(10) # this is also a list
s = 'this  is a literal string ACT' # this is a string

def cat(s,t):
    return s + t

def dbl(n):
    '''given a number n, returns 2 times n'''
    return 2 * n

def quad(n):
    '''given a number n, returns 4 times n'''
    answer = dbl(dbl(n))
    return answer

def howdy():
    """doesn't do anythingy"""
    return 7

def mult(x,y):
    return x*y

def evens(n):
    '''the first n even numbers, starting with 0'''
    return map(dbl, range(n))


