#powerset exercise and test helper
from cs115 import *
def powerset(L):
    '''The setof sub-lists of L. The sub-lists should be in same order
    as in L, but the order of sub-lists is arbitrary
    For example, powerset(["cat", "mouse", "mole"]) could
    return[[], ["cat"], ["mouse"], ["mole"], ["cat", "mouse"],
            {"cat", "mole"], ["mouse", "mole"], ["cat", "mouse", "mole"]'''
    if L==[]:
        return [[]]
    else:
        lose=powerset(L[1:])
        use=map(lambda M: [L[0]]+M, powerset(L[1:]))
        return lose+use
def isSubset(L,M):
    '''whther every elemnt of L is in M'''
    if L==[]:
        return true
    else:
        return L[0] in M and isSubset(L[1:],M)
def subset(target, L):
    '''whether some elements of L add up to exactly target,
    assuming target>=0 and all elements of L are non-negative numbers'''
    if target ==0:
        return True
    elif L==[]:
        return false
    elif L[0]>target:
        return subset(target, L[1:])
    else: # L[0]<=target
        lose= subset(target, L[1:])
        use= subset(target-L[0], L[1:])
        return use or lose
