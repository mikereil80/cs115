#Michael Reilly

from cs115 import *

def intersect(L, M):
    '''Returns the values in list M that are also in list L'''
    return filter(lambda x: x in M, L)
def intersectSorted(L,M):
    '''Returns the values in list M that are also in list L, sorted'''
    res=[]
    i=0 #index for L
    j=0 #index for M
    while i<len(L) and j<len(M):
        assert res==intersect(L[:i], M[:j])
        if L[i]==M[j]:
            res=res+[L[i]]
            i+=1
            j+=1
        elif L[i]<M[j]:
            i+=1
        else:
            j+=1
    return res
def ncommon(L,M):
    '''Returns the number common values between the two lists'''
    res=0
    i=0 #index for L
    j=0 #index for M
    while i<len(L) and j<len(M):
        assert res==len(intersect(L[:i], M[:j]))
        if L[i]==M[j]:
            res+=1
            i+=1
            j+=1
        elif L[i]<M[j]:
            i+=1
        else:
            j+=1
    return res
def swapx(a,b):
    '''A FAILED SWAP!!! DO NOT DO'''
    temp=a
    a=b
    b=temp
def swap(aList, i, j):
    '''swaps the values of aList[i] and aList[j]'''
    temp=aList[i]
    aList[i]=aList[j]
    aList[j]=temp
def sortx(L):
    if L[1]<L[2]:
        swap(L[1], L[2])
#Different sorts:
#Insertion Sort - find where L[i] belongs after inserting j in by shifting all after j over 1, n^2
#Selection Sort - find min in L[i:] swap with L[i], must know all sorted values are less than the values past i, all values after sort are greater than L[:i],
#Quick Sort
#
