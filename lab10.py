#
# life.py - Game of Life lab
#
# Name: Michael Reilly
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
#

import sys
import random

def createOneRow(width):
    '''returns one row of zeros of width "width"...
You might use this in your createBoard(width, height) function'''
    row=[]
    for col in range(width):
        row+=[0]
    return row
def createBoard(width, height):
    '''returns a 2d array with 'height' rows and 'width' cols'''
    A=[]
    for row in range(height):
        A+=[createOneRow(width)]
    return A
def printBoard( A ):
    '''This function prints the 2d list-of-lists
A without spaces(using sys.stdout.write)'''
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')
def diagonalize(width, height):
    '''creates an empty board and then modifies it
so that it has a diagonal strip of 'on' cells'''
    A=createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row==col:
                A[row][col]=1
            else:
                A[row][col]=0
    return A
def innerCells(w, h):
    '''creates an empty board and then modifies it so that
it has an outside strip of 0s surrounding the inner 1s'''
    A=createBoard(w, h)
    for row in range(h):
        for col in range(w):
            if row==0 or col==0 or row==h-1 or col==w-1:
                A[row][col]=0
            else:
                A[row][col]=1
    return A
def randomCells(w,h):
    '''creates an empty board and then modifies it so that
it has an outside strip or 0s on the edge and then all the
indexes within those borders being randomly assigned either
a 0 or a 1'''
    A=createBoard(w,h)
    for row in range(h):
        for col in range(w):
            if row==0 or col==0 or row==h-1 or col==w-1:
                A[row][col]=0
            else:
                A[row][col]=random.choice([0,1])
    return A
def copy(A):
    '''creates a copy of board A  called B using deep copying that
will not change if A is changes'''
    B=[]
    for row in range(len(A)):
        for col in range(len(A[0])):
            if col==0:
                B+=[[A[row][col]]]
            else:
                B[row]+=[A[row][col]]
    return B
def innerReverse(A):
    '''takes a board A and then creates a new generation
of the same shape and size. This new generation should be the 'opposite'
or A's cells everywhere except on the outer edge.
The outer edge of cells are always 0.'''
    B=[]
    for row in range(len(A)):
        for col in range(len(A[0])):
            if row==0 or col==0 or row==len(A)-1 or col==len(A[0])-1:
                if col==0:
                    B+=[[0]]
                else:
                    B[row]+=[0]
            else:
                if A[row][col]==1:
                    B[row]+=[0]
                else:
                    B[row]+=[1]
    return B
def next_life_generation(A):
    '''makes a copy of A and then advanced one generation of Conway's game
of life withing the *inner cells* of that copy.
The outer edge always stays 0.'''
    A2=copy(A)
    def countNeighbors(row, col, A):
        '''returns the number of neighbors a cell in the board A
at a particular row and col has'''
        count=0
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if r==row and c==col:
                    count+=0
                else:
                    if A[r][c]==1:
                        count+=1
                    else:
                        count+=0
        return count
    for row in range(len(A)):
        for col in range(len(A[0])):
            if row==0 or col==0 or row==len(A)-1 or col==len(A[0])-1:
                A2[row][col]=0
            else:
                neighbors=countNeighbors(row, col, A)
                if neighbors<2:
                    A2[row][col]=0
                elif neighbors>3:
                    A2[row][col]=0
                elif A[row][col]==0 and neighbors==3:
                    A2[row][col]=1
                else:
                    A2[row][col]=A[row][col]
    return A2
