#Michael Reilly
#I pledge my honor that I have abided by the Stevens Honor System
from cs115 import *

def change(amount, coins):
    '''Finds the minimum number of coins necessary to make
    a specific amount of money from a list of coins'''
    if coins==[] and amount==0:
        return 0
    elif coins==[]:
        return float("inf")
    if amount in coins:
        return 1
    def subchange(A, C):
        if A in C:
            return 1
        elif A==C[len(C)-1]:
            return 1
        elif A<C[len(C)-1]:
            return subchange(A, C[:len(C)-1])
        elif A>C[len(C)-1]:
            number=subchange(A-C[len(C)-1], C)+1
            return number
    if amount<coins[len(coins)-1]:
        return change(amount, coins[:len(coins)-1])
    if amount>coins[len(coins)-1]:
        lose=subchange(amount, coins[:len(coins)-1])
        use=subchange(amount, coins)
        return min(use, lose)
    
