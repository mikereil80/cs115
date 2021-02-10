#variables are mutable
#list values, and numbers, are immutable

#examples of function call/return
def f(x):
    x=x-1
    return g(x)+1
def g(x):
    return x*2
def h(x):
    if x%2==1:
        return f(x)+x
    else:
        return f(f(x))
def factorial(n):
    '''Recursive Factorial'''
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def towen(n):
    """exponential towe of 2s of height n"""
    if n==0:
        return 1
    else:
        return 2** tower(n-1)
#recursion on lists
#Ingredients: L[0] (the first element),
#L[1:] (the rest, L==[] (check for empty)
def mylen(L):
    """len(L), assuming L s a list"""
    if L==[]:
        return 0
    else:
        return 1+mylen(L[1:])
def mysum(L):
    """sum(L), assuming L is a list of numbers"""
    if L==[]:
        return 0
    else:
        return L[0]+mysum(L[1:])
def reverse(L):
    """returnss a new list tthat is the reverse of L"""
    return None
