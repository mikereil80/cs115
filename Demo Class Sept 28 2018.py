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
memo={} #dictionaary for use in fastLCS; keys are tuples (str1, str2)
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
