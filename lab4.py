#Michael Reilly
#I pledge my honor that I have abided by the Stevens Honor System

from cs115 import *

def knapsack(capacity, itemList):
    '''Returns the max value possible for the items in a list
that fit within the set capacity of a backpack'''
    if itemList==[]:
        return [0,[]]
    elif capacity==0:
        return [0,[]]
    elif itemList[0][0]>capacity:
        return knapsack(capacity, itemList[1:])
    else:
        use=knapsack(capacity-itemList[0][0], itemList[1:])
        lose=knapsack(capacity, itemList[1:])
        use[0] += itemList[0][1]
        use[1]=[itemList[0]]+use[1]
        if lose[0] > use[0]:
            return lose
        else:
            # 1) add the value of the item we used to the knapsack's value
            
            # 2) add the item itself to the knapsack's list of items
            
            return use
