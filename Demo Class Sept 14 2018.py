from cs115 import *
def divides(n):
    def div(k):
        return n%k==0
    return div
def divisibles(n, L):
    '''assume L is a list of integers;
    return a list of the ones divisible by n'''
    if L==[]:
        return []
    elif divides(L[0])(n):
        return [L[0]]+divisibles(n, L[1:])
    else:
       return divisibles(n, L[1:])
def reverse(L):
    if L==[]:
        return []
    else:
        return reverse(L[1:])+[L[0]]
def mymap(f,L): #same as map(f,L)
    if L==[]:
        return []
    else:
        return [f(L[0])] +mymap(f, L[1:])
def myreduce(op,L):
    if L==[]:
        return None
    elif len(L)==1:
        return L[0]
    else:
        return op(L[0], myreduce(op,L[1:]))
def prime(n):
    possibleDivisorss=range(2,n)
    divisors=filter(lambda X: n%X==0, possibleDivisors)
    return len(divisors)==0
def sieve(L):
    '''Eratosthenes; assume L is a list of naturals'''
    if L==[]:
        return []
    else:
        return [L[0]] + sieve(filter(lambda x: x%L[0]!=0,L[1:]))
def primes(n):
    '''The primes up to n'''
    return sieve(range(2,n+1))
