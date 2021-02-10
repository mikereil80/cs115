from cs115 import *

def LCS(S1, S2):
    '''Length of longest common subsequence of two lists'''
    if S=="" or S2=="":
        return 0
    elif S1[0]==S2[0]:
        return 1+LCS(S1[1:], S2[1:])
    else:
        return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))
def coinNames(coinInfo):
    '''assume coinInfo is a non-empty list of pairs [value,name].
    Return the names, as a string. for example,
    coinName([[1,'penny'],[5,'nickel'],[10,'dime']]) should return
    'penny nickel dime'. '''
    return reduce(lambda st1, st2: st1+' ' +st2, map(lambda pair: pair[1], coinInfo))
def exp(n,k):
    '''n**k, assuming k>=0 and is a number'''
    if k==0:
        return 1
    else:
        return n*exp(n,k-1)
def expfast(n,k):
    if k==0:
        return 1
    elif k%2==0:
        t=expfast(n,k//2)
        return t*t
    else:
        return n*expfast(n,k-1)
def exptail(n,k):
    '''n**k, computed using tail recursion.'''
    def ext(accumulator, n, k):
        if k==0:
            return accumulator
        else:
            return ext(n*accumulator, n, k-1)
    return ext(1,n,k)
def reverse(L):
    if L==[]:
        return []
    else:
        return reverse(L[1:])+[L[0]]
def reversetail(L):
    def rev(accumulator, L):
        if L==[]:
            return accumulator
        else:
            return rev([L[0]]+accumulator, L[1:])
    return rev([],L)
