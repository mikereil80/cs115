#Michael Reilly
#"I pledge my honor that I have abided by the Stevens Honor System."

from cs115 import reduce, map

def mult(x,y):
    """Returns the product of x and y"""
    return x*y
def factorial(n):
    """Returns the factorial up to the number n"""
    return reduce(mult, range(1,n+1))
def add(x,y):
    """Return the sum of x and y"""
    return x+y
def mean(L):
    """Returns the mean of a list of numbers"""
    return (reduce(add, L))/(len(L))
def div(k):
    """Returns a boolean seeing if number k is a factor of 42"""
    return 42%k==0
def divides(n):
    """Returns a a boolean seeing if div(k) is a factor of n"""
    def div(k):
        return n%k==0
    return div
def prime(n):
    """Finds if a number is a prime number or not"""
    L=map(divides(n),range(2,n))
    return sum(L)== 0
    
