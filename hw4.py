#Michael Reilly
#I pledge I have abided by the Stevens Honor System

from cs115 import *

def pascal_row(n):
    '''Returns a list of the the row n of the pascal triangle'''
    if n==0:
        return [1]
    elif n==1:
        return [1, 1]
    elif n<0:
        return []
    def list_add(K):
        '''Adds up the adjacent values of a list K and returns
a list of all those sums'''
        if K==[]:
            return []
        elif len(K)==1:
            return []
        else:
            return [K[0]+K[1]]+list_add(K[1:])     
    start=[1,1]
    L=[1]+list_add(start)+[1]
    def lister(L,n):
        '''Recursively re-calls list_add to an original list L
to keep incrementing it up until the final list respresenting
row n of pascal's triangle is returned'''
        if len(L)==n+1:
            return L
        else:
            M=[1]+list_add(L)+[1]
            return lister(M, n)
    return lister(L, n)
def pascal_triangle(n):
    '''Returns a list of sub-lists for all the rows of
pascal's triangle up to n'''
    if n==0:
        return [[1]]
    elif n<0:
        return []
    else:
        return pascal_triangle(n-1)+[pascal_row(n)]
def test_pascal_row():
    '''is a test function to make sure the pascal_row function
works as intended'''
    assert pascal_row(-1) == []
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]
    assert pascal_row(7) == [1, 7, 21, 35, 35, 21, 7, 1]
def test_pascal_triangle():
    '''is a test function to make sure the pascal_triangle function
works as intended'''
    assert pascal_triangle(-1) == []
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], \
                                  [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    
    
    
