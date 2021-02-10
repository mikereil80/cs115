#demo during class 9/5/18
from cs115 import *
def add(x,y):
    '''add integers together'''
    return x+y
def mult(x,y):
    '''multiply integers together'''
    print("hello there")
    '''don't really need print'''
    return x*y
def f(L):
    '''assume L is a list of numbers; return its ssum'''
    return reduce(add,L)
M=range(0,9)
def fact(N):
    '''find the factorial of a number'''
    return reduce (mult, range(1,N+1))
def span(L):
    '''assuming L is a list of numbers, return diff of max and min of L'''
    m=reduce(min,L)
    n=reduce(max,L)
    return n-m
def gauss(N):
    '''returns the sum of 1 to N'''
    return reduce (add, range(1,N+1))
def square(N):
    '''find the square of a number'''
    return mult(N,N)
def sumOfSquares(N):
    '''returnss the sum 1 to N^2'''
    return reduce (add, map (square, range(1,N+1)))
