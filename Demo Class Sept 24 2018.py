from cs115 import *
def ED(first, second):
    '''Returns the edit distaance between the strings first and second'''
    print("ED("+first+","+second+")")
    if first=='':
        return len(second)
    elif second=='':
        return len(first)
    elif first[0]==second[0]:
        return ED(first[1:], second[1:])
    else:
        substitution =1+ED(first[1:], second[1:])
        deletion=1+ED(first[1:], second)
        insertion=1+ED(first, second[1:])
        return min(substitution, deletion, insertion)
def reverse(lst):
    def rev(lst, acc):
        if lst==[]:
            return acc
        else:
            return rev(lst[1:], [lst[0]]+acc)
    return rev(lst,[])
def makeAt(strs):
    '''Assuming strs is a list of non-empty strings,
    return the ones that begin with 'a' or 'A', but with that replaced by @.
    Use map, filter, lambda.'''
    startA=filter(lambda w: w[0]=='a' or w[0]=='A', strs)
    return map(lambda w: '@' +w[1:], startA)
