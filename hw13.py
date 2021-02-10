# Michael Reilly
# I pledge my honor that I have abided by the Stevens Honor System

class Board:
    '''The board which has a two-dimensional list of characters and a
set width and height'''
    def __init__(self, width=7, height=6):
        '''This is a constructor for Board objects that takes width and height
to create a board with said width and height'''
        self.width=width
        self.height=height
        self.board=self.createboard()
    def createrow(self):
        '''creates a single empty row for the board based on the width variable
of self'''
        row=[]
        for col in range(self.width):
            row+=[" "]
        return row
    def createboard(self):
        '''creates a  board of however many empty rows based on the height
variable of self'''
        B=[]
        for row in range(self.height):
            B+=[self.createrow()]
        return B
    def __str__(self):
        '''Returns the string representation of the board'''
        finstring=""
        for row in range(self.height):
            for col in range(self.width):
                if col==0:
                    finstring+="|"+self.board[row][col]+"|"
                else:
                    finstring+=self.board[row][col]+"|"
            finstring+="\n"
        finstring+="-"*((2*self.width)+1)+"\n"
        for col in range(self.width):
            if col==0:
                finstring+=" "+str(col)+" "
            else:
                finstring+=str(col)+" "
        return finstring
    def allowsMove(self, col):
        '''Returns True if a move can be made into the column c because there
is space available, if space is not available or col is not a valid column
than it returns False'''
        if col>self.width:
            return False
        else:
            for row in range(self.height):
                if self.board[row][col]==" ":
                    return True
            return False
    def addMove(self, col, ox):
        '''using an ox checker of either string "X" or "O" it first sees if
a move can be made to col and then puts the X or O into said column'''
        if self.allowsMove(col)==True:
            for row in reversed(range(self.height)):
                if self.board[row][col]==" ":
                    self.board[row][col]=ox
                    break

    def setBoard( self, moveString ):
        """ takes in a string of columns and places
alternating checkers in those columns,
starting with 'X'
For example, call b.setBoard('012345')
to see 'X's and 'O's alternate on the
bottom row, or b.setBoard('000000') to
see them alternate in the left column.
moveString must be a string of integers """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'
    def delMove(self, col):
        '''Removes the top checker from the column col.
If the column is empty then delMove should do nothing'''
        for row in range(self.height):
            if self.board[row][col]!=" ":
                self.board[row][col]=" "
                break
    def fullBoard(self):
        '''Returns False if the board of self is not completely full,
if it is completely full it returns True.'''
        for row in range(self.height):
            for col in range(self.width):
                currentspot=self.board[row][col]
                if currentspot==" ":
                    return False
        return True
    def winsFor(self, ox):
        '''Using the checker ox, returns True if the checker ox has won the boar,
else it returns False'''
        for row in range(self.height):
            for col in range(self.width):
                currentspot=self.board[row][col]
                if currentspot==ox:
                    if col<=self.width-4:
                        if currentspot==self.board[row][col+1] and \
                           currentspot==self.board[row][col+2] and \
                           currentspot==self.board[row][col+3]:
                            return True
                        elif row<=self.height-4 and \
                             currentspot==self.board[row+1][col+1] and \
                             currentspot==self.board[row+2][col+2] and \
                             currentspot==self.board[row+3][col+3]:
                            return True
                        elif row<=self.height-4 and \
                             currentspot==self.board[row+1][col] and \
                             currentspot==self.board[row+2][col] and \
                             currentspot==self.board[row+3][col]:
                            return True
                    else:
                        if row<=self.height-4 and \
                           currentspot==self.board[row+1][col-1] and \
                           currentspot==self.board[row+2][col-2] and \
                           currentspot==self.board[row+3][col-3]:
                            return True
                        elif row<=self.height-4 and \
                             currentspot==self.board[row+1][col] and \
                             currentspot==self.board[row+2][col] and \
                             currentspot==self.board[row+3][col]:
                            return True
        return False
    def hostGame(self):
        '''when calling a connect four board runs a loop allowing the
user to play the game'''
        print("Welcome to Connect Four")
        ox="X"
        while self.winsFor(ox)==False:
            print(self)
            column=int(input(ox+"'s choice: "))
            if self.allowsMove(column)==True:
                self.addMove(column, ox)
                if self.winsFor(ox)==True:
                    break
                elif self.fullBoard()==True:
                    break
                else:
                    if ox=="X":
                        ox="O"
                    else:
                        ox="X"
        if self.winsFor("X")==False and self.winsFor("O")==False:
            print("It's a tie!")
            print(self)
        else:
            print(ox+" wins -- Congratulations!")
            print(self) 
            
