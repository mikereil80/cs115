#Michael Reilly
#I pledge my honor that I  have abided by the Stevens Honor System

FullAdder={('0','0','0'):('0','0'), ('0','0','1'):('1','0'),
           ('0','1','0'):('1','0'), ('0','1','1'):('0','1'),
           ('1','0','0'):('1','0'), ('1','0','1'):('0','1'),
           ('1','1','0'):('0','1'), ('1','1','1'):('1','1')}
def numToBaseB(N, B):
    '''Takes a non-negative integer and returns a string representing
the number N in base B'''
    if N==0:
        return '0'
    def numBaser(N, B):
        '''Takes a non-negative integer and returns a string repesenting
the number in base B and returns an empty string if N==0'''
        if N==0:
            return ''
        elif N==1:
            return '1'
        else:
            return numBaser(N//B, B)+str(N%B)
    return numBaser(N,B)
def baseBToNum(S, B):
    '''Takes a string representing a number in Base B and
converts it to the number in base 10 representing the same number as S'''
    if S=='':
        return 0
    else:
        return int(S[0])*B**(len(S)-1)+baseBToNum(S[1:], B)
def baseToBase(B1, B2, SinB1):
    '''Converts a number representation in a string of B1
into that same number represented as a string in B2'''
    numB1=baseBToNum(SinB1, B1)
    SinB2=numToBaseB(numB1, B2)
    return SinB2
def add(S, T):
    '''Adds two binary strings together by converting both strings
into numbers adding them and then converting back'''
    numS=baseBToNum(S, 2)
    numT=baseBToNum(T, 2)
    numsum=numS+numT
    Sinsum=numToBaseB(numsum, 2)
    return Sinsum
def addB(S, T):
    '''Adds two binary strings together without using any base conversions
but instead through binary addition'''
    def adderB(S, T, carry):
        '''A helper function with a carry variable that
uses the FullAdder Dictionary to add two binary strings S and T together'''
        if S=='' and T=='':
            return ''
        elif S=='':
            twople=FullAdder[('0', T[len(T)-1], carry)]
            carry=twople[1]
            if len(T)==1:
                if carry=='1':
                    return carry+twople[0]
                else:
                    return twople[0]
            else:
                return adderB(S, T[:len(T)-1], carry)+twople[0]
        elif T=='':
            twople=FullAdder[(S[len(S)-1], '0', carry)]
            carry=twople[1]
            if len(S)==1:
                if carry=='1':
                    return carry+twople[0]
                else:
                    return twople[0]
            else:
                return adderB(S[:len(S)-1], T, carry)+twople[0]
        else:
            twople=FullAdder[(S[len(S)-1], T[len(T)-1], carry)]
            carry=twople[1]
            return adderB(S[:len(S)-1], T[:len(T)-1], carry)+twople[0]
    return adderB(S, T, '0')
    
