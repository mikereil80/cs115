'''
Created on _11/26/18______________________
@author:   _Michael Reilly______________________
Pledge:    _I pledge my honor that I have abided by the Stevens Honor System__

CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
as the calling object (self).'''
        dnew=Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
whether or not they are the in the same place in memory.'''
        return self.year==d2.year and self.month==d2.month and \
               self.day==d2.day

    def tomorrow(self):
        '''Returns the next day after the current self date,
takes into account if it is a leap year'''
        if self.month==12 and self.day==31:
            self.day=1
            self.month=1
            self.year+=1
        elif self.isLeapYear()==True and self.month==2 and self.day==28:
            self.day+=1
        elif self.isLeapYear()==True and self.month==2 and self.day==29:
            self.day=1
            self.month+=1
        elif DAYS_IN_MONTH[self.month]==self.day and self.month!=12:
            self.day=1
            self.month+=1
        else:
            self.day+=1

    def yesterday(self):
        '''Returns the day before the curent self date,
takes into account if it is a leap year'''
        if self.month==1 and self.day==1:
            self.month=12
            self.day=31
            self.year-=1
        elif self.isLeapYear()==True and self.month==3 and self.day==1:
            self.day=29
            self.month-=1
        elif self.day==1:
            self.month-=1
            self.day=DAYS_IN_MONTH[self.month]
        else:
            self.day-=1

    def addNDays(self, N):
        '''prints every date from the starting self date to the day N days
after the original self date, also changes self to be the final date printed
after N number of days'''
        for count in range(0,N):
            print(self)
            self.tomorrow()
            if count==N-1:
                print(self)

    def subNDays(self, N):
        '''prints every date from the starting self date to the day N days
before the original self date, also changes self to be the final date printed
after N number of days'''
        for count in range(0, N):
            print(self)
            self.yesterday()
            if count==N-1:
                print(self)

    def isBefore(self, d2):
        '''Returns True is the calling object date is before the date of d2,
otherwise returns False'''
        if self.year<d2.year:
            return True
        elif self.year>d2.year:
            return False
        else:
            if self.month<d2.month:
                return True
            elif self.month>d2.month:
                return False
            else:
                if self.day<d2.day:
                    return True
                else:
                    return False
    
    def isAfter(self,d2):
        '''Returns True if the calling object date is after the date of d2,
otherwise returns False'''
        if self.year<d2.year:
            return False
        elif self.year>d2.year:
            return True
        else:
            if self.month<d2.month:
                return False
            elif self.month>d2.month:
                return True
            else:
                if self.day>d2.day:
                    return True
                else:
                    return False

    def diff(self, d2):
        '''Returns an integer representing the number of days between
self and d2'''
        day1=self.copy()
        day2=d2.copy()
        count=0
        if day1.isBefore(day2):
            while day1.isBefore(day2):
                day1.tomorrow()
                count-=1
            return count
        elif day1.isAfter(day2):
            while day1.isAfter(day2):
                day1.yesterday()
                count+=1
            return count
        else:
            return count

    def dow(self):
        '''Returns a string of the day of the week based on the original
date of Monday, November 26, 2018'''
        day1=self.copy()
        knowndate=Date(11,26,2018)
        difference=knowndate.diff(day1)
        if difference==0:
            return "Monday"
        elif difference%7==0:
            return "Monday"
        elif difference%7==1:
            return "Sunday"
        elif difference%7==2:
            return "Saturday"
        elif difference%7==3:
            return "Friday"
        elif difference%7==4:
            return "Thursday"
        elif difference%7==5:
            return "Wednesday"
        elif difference%7==6:
            return "Tuesday"
