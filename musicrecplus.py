#Michael Reilly
#I pledge my honor that I have abided by the Stevens Honor System

PREF_FILE="musicrecplus.txt"

def loadUsers(fileName):
    ''' Reads in a file of stored users' preferences
        stored in the file 'fileName'.
        Returns a dictionary containing a mapping
        of user names to a list preferred artists
    '''
    try:
        file = open(fileName, 'r')
        userDict = {}
        for line in file:
            # Read and parse a single line
            [userName, bands] = line.strip().split(":")
            bandList = bands.split(",") #make list of artists
            bandList.sort()
            userDict[userName] = bandList #store in dictionary
        file.close()
        return userDict
    except:
        newfile=open(fileName, 'w')
        userDict={}
        file.close()
        return userDict
    
         
def getPreferences(userName, userMap):
    ''' Returns a list of the uesr's preferred artists.

        If the system already knows about the user,
        it gets the preferences out of the userMap
        dictionary and then asks the user if she has
        additional preferences.  If the user is new,
        it simply asks the user for her preferences. '''
    newPref = ""
    if userName in userMap:
        prefs = userMap[userName]
        for artist in prefs:
            print(artist)
        newPref = input("Enter an artist that you like (Enter to finish):") #Enter new preference
    else:
        prefs = []
        newPref = input("Enter an artist that you like (Enter to finish):") #Enter new preference
        
    while newPref != "":
        prefs.append(newPref.strip().title())
        newPref = input("Enter an artist that you like (Enter to finish):")
        
    # Always keep the lists in sorted order for ease of comparison
    prefs.sort()
    return prefs


def getRecommendations(currUser, prefs, userMap):
    ''' Gets recommendations for a user (currUser) based
        on the users in userMap (a dictionary)
        and the user's preferences in pref (a list).
        Returns a list of recommended artists.  '''
    bestUser = findBestUser(currUser, prefs, userMap)
    if bestUser==None:
        return []
    else:
        recommendations = drop(prefs, userMap[bestUser])
        return set(recommendations)

def findBestUser(currUser, prefs, userMap):
    ''' Find the user whose tastes are closest to the current
        user.  Return the best user's name (a string) '''
    users = userMap.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        if user[-1] != '$':
            if userMap[user]!=userMap[currUser]:
                score = numMatches(prefs, userMap[user])
                if score > bestScore and currUser != user:
                    bestScore = score
                    bestUser = user
    return bestUser

def drop(list1, list2):
    ''' Return a new list that contains only the elements in
        list2 that were NOT in list1. '''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
            
    return list3

def numMatches( list1, list2 ):
    ''' return the number of elements that match between
        two sorted lists '''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def saveUserPreferences(userName, prefs, userMap, fileName):
    ''' Writes all of the user preferences to the file.
        Returns nothing. '''
    userMap[userName] = prefs #put user preferences in dictionary
    #sorted? maybe, should check this one
    file = open(fileName, "w")
    for user in userMap:
        toSave = str(user) + ":" + ",".join(userMap[user]) + "\n"
        file.write(toSave)
    file.close()

def print_recs(list1):
    '''prints the recommendation in one per line'''
    if len(list1)==0:
        print("No recommendations available at this time")
    else:
        for rec in list1:
            print(str(rec))

def best_artists(userMap):
    '''Finds the artist or artists that are the mot popular,
aka: occur the most within the dictionary.'''
    valuelist=values(userMap)
    count=1
    maxcount=0
    bestartist=[]
    for i in range(0, len(valuelist)):
        if i==len(valuelist)-1 and valuelist[i]==valuelist[i-1]:
            count+=1
            if count>maxcount:
                maxcount=count
                bestartist=[valuelist[i]]
            elif count==maxcount:
                bestartist+=[valuelist[i]]
        elif valuelist[i]==valuelist[i-1]:
            count+=1
        else:
            if count>maxcount:
                maxcount=count
                bestartist=[valuelist[i-1]]
            elif count==maxcount:
                bestartist+=[valuelist[i-1]]
                count=1
    return bestartist

def print_bestartists(list1):
    '''Prints the list of best artists one per line'''
    if len(list1)==0:
        print("Sorry, no artists found")
    else:
        for artist in list1:
            print(str(artist))

def how_artist(userMap):
    '''Finds how popular the most popular artist or artists are,
aka: how often they occur in the dictionary'''
    valuelist=values(userMap)
    if len(valuelist)==0:
        print("Sorry, no artists found")
    else:
        count=1
        maxcount=0
        for i in range(0, len(valuelist)):
            if i==len(valuelist)-1 and valuelist[i]==valuelist[i-1]:
                count+=1
                if count>maxcount:
                    maxcount=count
            elif valuelist[i]==valuelist[i-1]:
                count+=1
            else:
                if count>maxcount:
                    maxcount=count
        print(maxcount)
        
def most_likes(userMap):
    '''Finds who had the most liked artist in the dictionary,
aka: who has the most preferences'''
    itemlist=items(userMap)
    maxlength=1
    name=[]
    for i in itemlist:
        if len(i[1])>maxlength:
            maxlength=len(i[1])
            name=[i[0]]
        elif len(i[1])==maxlength:
            name+=[i[0]]
    return name

def print_likes(list1):
    '''prints the users with the most likes'''
    if len(list1)==0:
        print("Sorry, no user found")
    else:
        for likes in list1:
            print(str(likes))
    
def menu(userName, userMap):
    '''The menu for inputs of the user such as r to Get recommendations'''
    while True:
        print("e - Enter preferences" + "\n" + "r - Get recommendations" + "\n" +
          "p - Show most popular artists" + "\n" + "h - How popular is the most popular" + "\n" +
          "m - Which user has the most likes" + "\n" + "q - Save and quit")
        choice=input()
        if choice=='e':
            prefs=getPreferences(userName, userMap)
        elif choice=='r':
            recs=getRecommendations(userName, userMap[userName], userMap)
            print_recs(recs)
        elif choice=='p':
            bestartist=best_artists(userMap)
            print_bestartists(bestartist)
        elif choice=='h':
            howpopular=how_artist(userMap)
        elif choice=='m':
            mostlikes=most_likes(userMap)
            print_likes(mostlikes)
        elif choice=='q':
            try:
                saveUserPreferences(userName, userMap[userName], userMap, PREF_FILE)
                break
            except:
                break

def values(userMap):
    '''returns the values available for use if $ is not at the end of the key'''
    users=userMap.keys()
    valuelist=[]
    for user in users:
        if user[-1] != "$":
            valuelist+=userMap[user]
            valuelist.sort()
    return valuelist

def items(userMap):
    '''returns the items available for use if $ is not at the end of the key'''
    users=userMap.keys()
    itemslist=[]
    for user in users:
        if user[-1] != "$":
            itemslist+=[(user, userMap[user])]
            itemslist.sort()
    return itemslist

def main():
    ''' The main function that starts up the menu after inputting username'''
    userMap = loadUsers(PREF_FILE)
    #returns dict(username: preferences)

    userName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    if userName not in userMap:
        newPref=getPreferences(userName, userMap)
        savedPref=saveUserPreferences(userName, newPref, userMap, PREF_FILE)
    menu(userName, userMap)
    

if __name__ == "__main__": main()
