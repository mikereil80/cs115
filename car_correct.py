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
    def __init__(self, make, model, mpg, tank_capacity):
        '''The constructor method for the Car Class'''
        self.__make=make
        self.__model=model
        self.__mpg=mpg
        self.__tank_capacity=tank_capacity
        
    '''Write getters for make, model, mpg, and tank_capacity.'''
    @property
    def make(self):
        '''Returns the string of the make'''
        return self.__make
    
    @property
    def model(self):
        '''Returns the string of the model'''
        return self.__model
    
    @property
    def mpg(self):
        '''Returns the float of the mpg'''
        return self.__mpg
    
    @property
    def tank_capacity(self):
        '''Returns the float of the tank_capacity'''
        return self.__tank_capacity

    '''Write setters for mpg and tank_capacity.'''
    @mpg.setter
    def mpg(self, mpg):
        '''As a setter will change the value of the mpg in self'''
        self.__mpg=mpg
        
    @tank_capacity.setter
    def tank_capacity(self, tank_capacity):
        '''As a setter will change the value of tank_capacity in self'''
        self.__tank_capacity=tank_capacity

    '''Write a method called get_total_range.
       It returns the total distance the car can travel on a full tank of
       gas.'''
    def get_total_range(self):
        '''Returns the total distance the car can travel on a full tank of gas'''
        gallons=self.mpg
        gastank=self.tank_capacity
        distance=gallons*gastank
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
class HybridCar(Car):  
    '''Write the constructor. It should take in 6 arguments:
    - the first four are the same as in the Car constructor
    - battery_kWh (battery power in kilowatt-hours, a float)
    - miles_per_kWh (miles per kilowatt-hours, a float)
    The additional fields must be private.
    '''
    def __init__(self, make, model, mpg, tank_capacity, battery_kWh, miles_per_kWh):
        '''The constructor method for the HybridCar class'''
        Car.__init__(self, make, model, mpg, tank_capacity)
        self.__battery_kWh=battery_kWh
        self.__miles_per_kWh=miles_per_kWh
        
    @property
    def battery_kWh(self):
        '''Returns the float of the battery_kWh'''
        return self.__battery_kWh
    
    @property
    def miles_per_kWh(self):
        '''Returns the float of the miles_per_kWh'''
        return self.__miles_per_kWh

    '''Implement the following method.'''
    def get_battery_range(self):
        '''Returns the total distance the car can travel on a fully charged
        battery.
        '''
        batterypower=self.battery_kWh
        miles=self.miles_per_kWh
        distance=batterypower*miles
        return distance
 

    '''Override the method get_total_range.
    Returns the total distance the car can travel on a full tank of
    gas and a fully charged battery.
    Do not do any math here except a single +. To get credit, you must call
    the methods you have already written.
    '''
    def get_total_range(self):
        '''Returns the total distance the car can travel on a full tank of gas
and a fully charged battery'''
        gasdistance=Car.get_total_range(self)
        batterydistance=self.get_battery_range()
        return gasdistance+batterydistance

    def __str__(self):
        '''A string for printing information about a car.'''
        return super().__str__() + ', battery kWh: ' + \
            str(self.__battery_kWh) + ', miles/kWh: ' + \
            str(self.__miles_per_kWh)
