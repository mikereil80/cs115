'''
Created on _10/14/18______________________
@author:   _Michael Reilly______________________
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
def numToBinary(n):
    '''Returns the binary number representation of integer n'''
    if n==0:
        return ''
    elif n==1:
        return '1'
    elif n==2:
        return '10'
    elif n%2==1:
        return numToBinary(n//2)+'1'
    else:
        return numToBinary(n//2)+'0'
def binaryToNum(s):
    '''Returns the decimal number representation of binary string s'''
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
def compress(S):
    '''Returns the run-length encoding of a string input'''
    if S=="":
        return S
    def counter(S, n, constant):
        '''Returns the number of 1s or 0s that occur consecutively
in the initial binary string'''
        if S=="":
            return numToBinary(n)
        elif S[0]==constant:
            n+=1
            return counter(S[1:], n, constant)
        else:
            return numToBinary(n)
    consecutive=counter(S, 0, S[0])
    if len(consecutive)<5:
        instance='0'*(5-len(consecutive))+consecutive
        start=binaryToNum(consecutive)
        if S[0]=='1' and len(S)==64:
            return '00000'+instance+compress(S[start:])
        else:
            return instance+compress(S[start:])
    elif binaryToNum(consecutive)>2**5-1:
        if S[0]=='1' and len(S)==64:
            return '00000'+'11111'+'00000'+compress(S[newnum:])
        else:
            return '11111'+'00000'+compress(S[2**5-1:])
    else:
        start=binaryToNum(consecutive)
        if S[0]=='1' and len(S)==64:
            return '00000'+consecutive+compress(S[start:])
        else:
            return consecutive+compress(S[start:])
def uncompress(C):
    '''Returns a 64 bit string from a run-length encoding string'''
    if C=="":
        return C
    def uncompressor(C, n):
        if C=="":
            return ""
        elif C[:10]=='1111100000':
            num=binaryToNum(C[:5])
            return n*num+uncompressor(C[10:], n)
        else:
            num=binaryToNum(C[:5])
            if n=='1':
                return n*num+uncompressor(C[5:], '0')
            else:
                return n*num+uncompressor(C[5:], '1')
    if C[:5]=='00000':
        return uncompressor(C[5:], '1')
    else:
        return uncompressor(C, '0')
    
def compression(S):
    '''Returns the ratio of the compressed size to the original size
of a string S'''
    return len(compress(S))/len(S)

'''The largest number of bits that the compress algorithm could use to encode
a 64-bit string/image is 5*64+5 which is 325 bits as if the 64-bit string starts
with a 1 and also is a checkerboard of 1010 etc it will print '00000' at the
beginning to indicate it starting with '1' as well as 64 sets of 5 bits
to represent each instance of a single '1' or '0' bit appearing in the
64-bit string'''

'''Tested the compression algorithm on all the test cases given by test_hw6.py
and got various compression ratios such as ones below 1 like .390625 and others
above 1 such as 5.0 which indicates that sometimes the compress function sometimes
outputs a string that is longer than the 64-bit string and other times
it outputs a string that is shorter than the 64-bit string'''

'''Professor Lai is wrong as it is impossible to write an algorithm that will
always output a shorter string that represents the image as there will always
a case where the data is changing back and forth that it will be impossible
for an algorithm like run-length-encoding to compress it to be smaller as there
is no readable pattern for the computer making it so the string after encoded
will become longer than the initial sstring. Thus Professor Lai must be lying
about his algorithm as there will always be exception cases that will cause the
encoding funcction to output a longer string than the initial one'''
