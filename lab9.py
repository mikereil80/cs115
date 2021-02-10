# mandelbrot.py
# Lab 9
#
# Name: Michael Reilly

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:

def mult(c,n):
    '''multiplies two numbers together by adding c n number of times to zero
by looping'''
    result=0
    for x in range(n):
        result+=c
        x+=1
    return result
def update(c,n):
    '''updates the value of z starting at 0 by z**2+c n number of times
by looping'''
    z=0
    for x in range(n):
        z=z**2+c
        x+=1
    return z
def inMSet(c,n):
    '''Returns False if the sequence Zn+1=Zn^2+c ever yields a z value
ehose magnitude is greater than 2. It should return True otherwise'''
    z=0
    for x in range(n):
        z=z**2+c
        x+=1
        if abs(z)>2:
            return False
    return True
def weWantThisPixel( col, row ):
    """ a function that returns True if we want
the pixel at col, row and False otherwise"""
    if col%10 == 0  and  row%10 == 0:
        return True
    else:
        return False
def test():
    """ a function to demonstrate how
to create and save a png image"""
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()
'''When change if col%10==0 and row%10==0: to if col%10==0 or row%10==0:
thiss causes the image to change from a set of individual dots to a set
of grid lines because it will work when as long as at least one of
row or col is a multiple of 10 regardless of where the other one is,
causing more points to work making the individual points look like a grid,
unlike when it is an and statement where many less points making an image
of individual points of pixels where both row and col are multiples of 10'''
def scale(pix, pixelMax, floatMin, floatMax):
    '''Returns the value of pix/pixmax within the range of
floatMin and floatMax'''
    if pix==0:
        return floatMin
    elif pix==pixelMax:
        return floatMax
    else:
        k=1.0*pix / pixelMax
        N=floatMax-floatMin
        L=k*N + floatMin
        return L
def mset():
    """ a function that creates the mandelbrot set png image"""
    width=300
    height=200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            x=scale(col, width, -2.0, 1.0)
            y=scale(row, height, -1.0, 1.0)
            c=x+y*1j
            n=25
            if inMSet( c, n ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()
