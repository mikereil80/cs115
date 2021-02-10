#Michael Reilly
#"I pledge my honor that I have abided by the Stevens Honor System"
from cs115 import *
def dot(L, K):
    '''Finds the dot product of two lists.'''
    if L == []:
        return 0.0
    if K == []:
        return 0.0
    else:
        return L[0]*K[0]+dot(L[1:],K[1:])
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
    if e==L[0]:
        return removeAll(e,L[1:])
    else:
        return [L[0]]+removeAll(e,L[1:])
def myFilter(f, L):
    '''Makes a list of all elements of a list that make predicate f true.'''
    if L==[]:
        return []
    if f(L[0])==False:
        return myFilter(f, L[1:])
    else:
        return [L[0]]+myFilter(f,L[1:])
def even(X):
    if X%2==0:
        return True
    else:
        return False
def deepReverse(L):
    '''Completely reverse a list.
    Also reverses all instances of a list within the original list.'''
    M=[]
    if len(L)-1>=0:
        if isinstance(L[len(L)-1], list):
            if isinstance(L[len(L)-2], list):
                return [(deepReverse(L[len(L)-1]))]+[deepReverse(L[len(L)-2])]+[L[0]]
            else:
                return [(deepReverse(L[len(L)-1]))]+[L[0]]
    if L==[]:
        return []
    else:
        if len(L)-1>=0:
            return [L[len(L)-1]]+(deepReverse(L[:(len(L)-1)]))
