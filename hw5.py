'''
Created on __10/8/18_____________________
@author:   __Michael Reilly______________
Pledge:    I pledge on my honor that I have abided by the Stevens Honor System

CS115 - Hw 5
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

def sv_tree(trunk_length, levels):
    '''Returns a drawing of a stick figure tree using turtle graphics'''
    turtle.forward(trunk_length)
    if levels==1:
        turtle.backward(trunk_length)
    else:
        turtle.right(45)
        sv_tree(trunk_length/2, levels-1)
        turtle.left(90)
        sv_tree(trunk_length/2, levels-1)
        turtle.right(45)
        turtle.backward(trunk_length)

memo_lucas={}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if (n-1,n-2) in memo_lucas:
        return memo_lucas[(n-1,n-2)]
    elif n==0:
        return 2
    elif n==1:
        return 1
    else:
        answer=fast_lucas(n-1)+fast_lucas(n-2)
        memo_lucas[(n-1,n-2)]=answer
        return answer

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def change(amount, coins):
        '''Finds the least number of coins to get the amount of change'''
        if coins==[] and amount==0:
            return 0
        elif coins==[]:
            return float("inf")
        elif amount in coins:
            return 1
        def subchange(A, C):
            '''Is a helper function for change that returns the number of coins
needed to make the amount with the list of coins given'''
            if A in C:
                return 1
            elif A==C[len(C)-1]:
                return 1
            elif A<C[len(C)-1]:
                return subchange(A, C[:len(C)-1])
            elif A>C[len(C)-1]:
                number=1+subchange(A-C[len(C)-1], C)
                return number
        if amount<coins[len(coins)-1]:
            return change(amount, coins[:len(coins)-1])
        if amount>coins[len(coins)-1]:
            lose=subchange(amount, coins[:len(coins)-1])
            use=subchange(amount, coins)
            return min(use, lose)
    def fast_change_helper(amount, coins, memo):
        '''Helper function that memos the answers of change to speed up
the process of finding the amount of coins needed for large numbers'''
        answer=change(amount, coins)
        memo[(coins)]=answer
        return answer
    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)
