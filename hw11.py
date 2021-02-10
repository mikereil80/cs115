# nim template DNaumann (2018), for assignment nim_hw11.txt

#Michael Reilly
#I pledge my honor that I have abided by the Stevens Honor System

# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)


def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    print("We're going to play Nim. You'd better play optimally or I'll win.")
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:

            # TODO print a message telling the user they won
            print("You played optimally, congrats")
            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:

            # TODO print a message telling the user the computer won
            print("I win ... AGAIN")
            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles

    while True:
        try:
            num_piles=int(input("How many piles do you want to play with? "))
            num=0
            while True:
                try:
                    piles+=[int(input("How many in pile "+str(num)+"? "))]
                    num+=1
                    if num==num_piles:
                        break
                except:
                    continue
            break
        except:
            continue
        
        

        
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles

    for num in range(0, num_piles):
        print("pile "+str(num)+" = "+str(piles[num])+"\n")
    


def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles
    
    while True:
        try:
            pile=int(input("Which pile? "))
            if 0<=pile<num_piles and piles[pile]!=0:
                break
            else:
                continue
        except:
            continue
    return pile


def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles
    
    while True:
        try:
            remove=int(input("How many? "))
            if 1<=remove<=piles[pnum]:
                break
            else:
                continue
        except:
            continue
    return remove

    
def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles

    def nim_sum_piles(number, pilelist):
        '''returns the nim-sum of the piles using a for loop'''
        currentsum=0
        nimsum=0
        for index in range(0,number):
            if index==0:
                currentsum=pilelist[index]
            else:
                currentsum=currentsum^pilelist[index]
        nimsum=currentsum
        return nimsum
    return nim_sum_piles(num_piles, piles)
        


def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles

    nimsum=game_nim_sum()
    def best_play(number, pilelist, sumnim):
        '''returns the optimal play in a tuple using the nim-sum
found from game_nim_sum'''
        for index in range(0, number):
            for number in pilelist:
                if pilelist[index]!=0:
                    pilesum=pilelist[index]^sumnim
                    if pilelist[index]>pilesum:
                        difference=pilelist[index]-pilesum
                        return (index, difference)
                    elif pilelist[index]==pilesum and index==number-1:
                        for i in range(0, number):
                            if pilelist[i]!=0:
                                return (i, 1)
    return best_play(num_piles, piles, nimsum)

    


def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles

    print("My turn ... prepare to be dazzled!!!")
    play=opt_play()
    piles[play[0]]=piles[play[0]]-play[1]
    print("I remove "+str(play[1])+" from pile "+str(play[0]))
    

    


#   start playing automatically
if __name__ == "__main__" : play_nim()
