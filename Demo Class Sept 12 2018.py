from cs115 import *
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def div(k):
    '''Checks whether 42 is evenly divisible by an integer k.'''
    return 42%k==0
def divides(n):
    def div(k):
        return n%k==0
    return div
def f(n):
    if n==0:
        return []
    else:
        return [42]+f(n-1)
def divisibles(n,L):
    '''assume L is a list of integers; return a list of the ones divisible by n'''
    if L==[]:
        return []
    elif divides(L[0])(n):
            return [L[0]]+divisibles(n,L[1:])
    else: return divisibles(n,L[1:])
def test_divisibles():
    print(divisibles(3,[1,6,4,9])==[6,9])
def make_len(n):
    '''Assume n is a non negative integer.
    Return a function.
    That function applies to strings.
    It concatenates * characters to the given string,
    to make its length at least n.'''
    def pad_it(word):
        x=len(word)
        return word+((n-len(word))* '*')
    return pad_it
def pad(words):
    '''Assume words is a non-empty list of strings.
    Let n be the length of the longest.
    Return a list of the same strings except with enough
    * characters appended to make each one length n'''
    m=max(map(len,words))
    return map(make_len(m),words)
def test_pad():
    '''Test for pad. Correct tests print True'''
