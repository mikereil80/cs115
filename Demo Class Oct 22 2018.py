# two-part exercise

from cs115 import map

'''
Part 0
Here is a memoized version of edit distance.
Your task: make it trace the calls to fastED_help, indented
according to recursion depth.  Hint: add a parameter to fastED_help.
'''
def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    def fastED_help(first, second, memo, indents):
        print(' '*indents+'fastED_help('+first+', '+second+')')
        if (first, second) in memo:
            return memo[(first, second)]
        elif first == '':
            result = len(second)
        elif second == '':
            result = len(first)
        elif first[0] == second[0]:
            result = fastED_help(first[1:], second[1:], memo, indents+1)
        else:
            substitution = 1 + fastED_help(first[1:], second[1:], memo, indents+1)
            deletion = 1 + fastED_help(first[1:], second, memo, indents+1)
            insertion = 1 + fastED_help(first, second[1:], memo, indents+1)
            result = min(substitution, deletion, insertion)
        memo[(first, second)] = result
        return result    
    return fastED_help(first, second, {}, 0)



'''
Part 1
Complete the following function.  You may use the functions
numToBinary and increment from lab 6, provided below.
Start by sketching your design in psuedo-code.
'''

def numToTC(N):
    '''Assume N is an integer.
    If N can be represented in 8 bits using two's complement, return
    that representation as a string of exactly 8 bits.  
    Otherwise return the string 'Error'.
    '''
    if N>127:
        return 'Error'
    elif N<-128:
        return 'Error'
    def string_switcher(S):
        '''Returns a binary string of inverted digits of the original binary string'''
        if S=='':
            return S
        elif S[0]=='1':
            return '0'+string_switcher(S[1:])
        else:
            return '1'+string_switcher(S[1:])
    bstring=numToBinary(N)
    if len(bstring)<8:
        bits='0'*(8-len(bstring))+bstring
        Str=string_switcher(bits)
        istring=increment(Str)
        return istring
    else:
        Str=string_switcher(bstring)
        istring=increment(Str)
        return istring

'''
Examples:
   NumToTc(1) ---> '00000001'
   NumToTc(-128) ---> '10000000'
   NumToTc(200) ---> 'Error'
'''


def numToBinary(N):
    '''Assuming N is a non-negative integer, return its base 2
    representation as a string of bits.'''
    if N == 0:
        return ''
    if isOdd(N):
        return numToBinary(N//2) + '1'
    else:
        return numToBinary(N//2) + '0'

def increment(s):
    '''Assuming s is a string of 8 bits, return the binary representation 
    of the next larger number takes an 8 bit string of 1's and 0's and 
    returns the next largest number in base 2'''
    num = binaryToNum(s) + 1
    if num == 256:
        return '00000000'
    zeros = (len(s)-len(numToBinary(num))) * '0'
    return zeros + numToBinary(num)

def binaryToNum(s):
    '''Assuming s is a string of bits, interpret it as an unsigned binary
    number and return that number (as a python integer).
    '''
    def binaryToNumHelp(s, index):
        if s == '':
            return 0
        elif s[0] == '0':
            index -= 1
            return 0 + binaryToNumHelp(s[1:], index)
        else:
            index -= 1
            return 2**index + binaryToNumHelp(s[1:], index)
    return binaryToNumHelp(s, len(s))

def isOdd(n):
    '''returns whether a number is odd or not'''
    if n % 2 == 0:
        return False
    else:
        return True
