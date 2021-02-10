#Lab 1
#Michael Reilly
#"I pledge my honor that I have abided by the Stevens honor system"
from cs115 import map
import math
def inverse(n):
    '''gets the inverse of integer n'''
    return 1/n
def e(n):
    '''estimates e based of integer n using the 1+1/1!+1/2!... 1/n! estimation'''
    return sum(map(inverse, map(math.factorial, range(0,n+1))))
def error(n):
    '''finds the error between the guess for e in our code and the actual value of e'''
    return abs((math.e)-e(n))
