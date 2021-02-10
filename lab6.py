'''
Created on __10/10/18_____________________
@author:   __Michael Reilly_____________________
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    '''42=2^5+2^3+2^1'''
    if n%2==0:
        return False
    else:
        return True

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    elif n==1:
        return '1'
    elif n==2:
        return '10'
    elif isOdd(n)==True:
        return numToBinary(n//2)+'1'
    else:
        return numToBinary(n//2)+'0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=="":
        return 0
    elif s=="0":
        return 0
    elif s=="1":
        return 1
    elif s[0]=="1" and s != "1":
        return 2**(len(s)-1)+binaryToNum(s[1:])
    else:
        return binaryToNum(s[1:])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s=='':
        return '00000001'
    elif s=='11111111':
        return '00000000'
    elif s[0]=='0':
        return increment(s[1:])
    else:
        n=binaryToNum(s)+1
        return '0'*(8-len(numToBinary(n)))+numToBinary(n)

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n==0:
        print(s)
    else:
        print(s)
        return count(increment(s),n-1)
    

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    elif n==1:
        return '1'
    elif n==2:
        return '2'
    elif n==3:
        return '10'
    elif n%3==0:
        return numToTernary(n//3)+'0'
    elif n%3==1:
        return numToTernary(n//3)+'1'
    else:
        return numToTernary(n//3)+'2'

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s=="":
        return 0
    elif s=="0":
        return 0
    elif s=="1":
        return 1
    elif s=="2":
        return 2
    elif s[0]=="2" and s != "2":
        return 2*3**(len(s)-1)+ternaryToNum(s[1:])
    elif s[0]=="1" and s != "1":
        return 3**(len(s)-1)+ternaryToNum(s[1:])
    else:
        return ternaryToNum(s[1:])
