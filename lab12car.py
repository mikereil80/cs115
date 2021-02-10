'''
CS 115, Lab 12, Inheritance

Author: Michael Reilly
Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 1 
' Implement missing sections of the Car class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Car(object):
    '''Write the constructor. It should take in four arguments:
       - make (a string, the company name, a.k.a. brand)
       - model (a string)
       - mpg (miles per gallon, a float)
       - tank_capacity (capacity of the gas tank in gallons, a float)
       These should all be assigned to corresponding private fields, i.e., with
       names that start with '__'.  Use the names in the 'str' method provided below.
       '''
    def __init__(self, brandname, modeltype, gallons, gastank):
        '''The constructor method for the car'''
        self.__make=brandname
        self.__model=modeltype
        self.__mpg=gallons
        self.__tank_capacity=gastank
        
    '''Write getters for make, model, mpg, and tank_capacity.'''
    def getMake(self):
        '''Returns the string of the make'''
        return self.__make
    
    def getModel(self):
        '''Returns the string of the model'''
        return self.__model

    def getMPG(self):
        '''Returns the float of the mpg'''
        return self.__mpg

    def getTank_Capacity(self):
        '''Return the float of the tank_capacity'''
        return self.__tank_capacity

    '''Write setters for mpg and tank_capacity.'''
    def setMPG(self, gallons):
        '''As a setter will change the value of the mpg in self'''
        self.__mpg=gallons

    def setTank_Capacity(self, gastank):
        '''As a setter will change the value of tank_capacity in self'''
        self.__tank_capacity=gastank

    '''Write a method called get_total_range.
       It returns the total distance the car can travel on a full tank of
       gas.'''
    def get_total_range(self):
        '''Returns the total distance the car can travel on a full tank of gas'''
        gallons=getMPG(self)
        gastank=getTank_Capacity(self)
        distance=int(gallons)*int(gastank)
        return distance



    def __str__(self):
        '''A string for printing information about a car.'''
        return self.__make + ' ' + self.__model + ', MPG: ' + str(self.__mpg) \
            + ', tank capacity: ' + str(self.__tank_capacity)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 2 
' Implement missing sections of the HybridCar class. 
' Make HybridCar be a subclass of Car.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class HybridCar():  
    '''Write the constructor. It should take in 6 arguments:
    - the first four are the same as in the Car constructor
    - battery_kWh (battery power in kilowatt-hours, a float)
    - miles_per_kWh (miles per kilowatt-hours, a float)
    The additional fields must be private.
    '''

    '''Implement the following method.'''
    def get_battery_range(self):
        '''Returns the total distance the car can travel on a fully charged
        battery.
        '''
 

    '''Override the method get_total_range.
    Returns the total distance the car can travel on a full tank of
    gas and a fully charged battery.
    Do not do any math here except a single +. To get credit, you must call
    the methods you have already written.
    '''

    def __str__(self):
        '''A string for printing information about a car.'''
        return super().__str__() + ', battery kWh: ' + \
            str(self.__battery_kWh) + ', miles/kWh: ' + \
            str(self.__miles_per_kWh)
