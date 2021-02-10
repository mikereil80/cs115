from cs115 import *
def LCS(S1, S2):
    if S1=="" or S2=="":
        return 0
    else:
        if S1[0]==S2[0]:
            return 1+LCS(S1[1:],S2[1:])
        else:
            return max(LCS(S1, S2[1:]),LCS(S1[1:],S2))
def knapsack(n, L):
    if L==[]:
        return 0
    elif n==0:
        return 0
    else:
        if n<L[0][0]:
            return knapsack(n,L[1:])
        else:
            return max(L[0][1]+knapsack(n-L[0][1], L[1:]),  L[L[len(L)-1][1]+knapsack(n-L[len(L)-1][0], L[:len(L)-1]))
