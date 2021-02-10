from cs115 import *

L1=['today','is','friday','right?']
L2=range(0,20)

def add(x,y):
    return x+y
def increment(k):
    '''returns a function that adds k to a number'''
    def f(n):
        return n+k
    return f
def inc_all(L,n):
    '''add n to every number in a given list of numbers'''
    return map(increment(n),L)

