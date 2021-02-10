from cs115 import *

def LCSX(S1,S2):
    if S1==""or S2=="":
        return 0
    elif S1[0]==S2[0]:
        return 1+LCSX(S1[1:], S2[1:])
    else:
        chopS1=LCSX(S1[1:], S2)
        chopS2=LCSX(S1, S2[1:])
        answer=max(chopS1, chopS2)
        return answer
memo={} #dictionary for use in fastLCS; keys are tuples (str1, str2)
def fastLCS(S1, S2):
    if (S1, S2) in memo:
        return memo[(S1, S2)]
    elif S1=="" or S2=="":
        memo[(S1, S2)]=0 #put (S1,S2):0 into table (remember this)
        return 0
    elif S1[0]==S2[0]:
        answer=1+fastLCS(S1[1:], S2[1:])
        memo[(S1, S2)]=answer #remember this
        return answer
    else:
        chopS1=fastLCS(S1[1:], S2)
        chopS2=fastLCS(S1, S2[1:])
        answer=max(chopS1, chopS2)
        memo[(S1, S2)]=answer #remember this
        return answer
def fastLCSalt(S1, S2):
    memo={}
    def fLCS(s1, S2):
        if (S1, S2) in memo:
            return memo[(S1, S2)]
        elif S1=="" or S2=="":
            memo[(S1, S2)]=0
            return 0
        elif S1[0]==S2[0]:
            answer=1+fLCS(S1[1:], S2[1:])
            memo[(S1, S2)]=answer
            return answer
        else:
            chopS1=fLCS(S1[1:], S2)
            chopS2=fLCS(S1, S2[1:])
            answer=max(chopS1, chopS2)
            memo[(S1, S2)]=answer
            return answer
    return fLCS(S1, S2)

def LCStrace(S1,S2):
    tabs=""
    def LCStracer(S1, S2):
        global tabs
        print(tabs+S1+S2)
        tabs+=" "
        if S1==""or S2=="":
            return 0
        elif S1[0]==S2[0]:
            return 1+LCSX(S1[1:], S2[1:])
        else:
            chopS1=LCSX(S1[1:], S2)
            chopS2=LCSX(S1, S2[1:])
            answer=max(chopS1, chopS2)
            return answer
    return LCStracer(S1, S2)
