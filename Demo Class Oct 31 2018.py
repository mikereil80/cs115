def printBoard(board):
    if debug:
        print('debugging')
    row=0
    column=0
    for row in range(3):
        if row!=2:
            printRow(board, row)
            print('------------')
        else:
            printRow(board, row)
        for column in range(3):
            print(board[row][column])
            column+=1
            if column!=2:
                print('|')
            elif column==3:
                row+=1
                column=0
                if row!=2:
                    print('-------------')
                if row==3:
                    break
def boardFull(board):
    if debug:
        print('debugging')
    full=True #all seen so far are non-blank
    for row in range(3):
        for col in range(3):
            full=full and board[row][col]!=''
    return full
#complex numbers are built into python
