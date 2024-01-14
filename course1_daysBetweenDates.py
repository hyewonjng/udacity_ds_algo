def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def daysInMonth(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        else:
            return 30

def nextDay(year, month, day):
    # take care of Feb cases with a leap year
    if month == 2:
        if isLeapYear(year):
            if day < 29:
                return year, month, day+1
            else:
                return year, month+1, 1
        else:
            if day == 28:
                return year, month + 1, 1
            else:
                return year, month, day + 1
    # the rest of months
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 31:
            return year, month, day + 1
        if month == 12 and day == 31:
            return year+1, 1, 1
        if day == 31:
            return year, month+1, 1
    else:
        if day < 30:
            return year, month, day + 1
        if day == 30:
            return year, month+1, 1

        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False    

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
       
    # Throw an AssertionError if the input is not valid
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

# Testing code -- do not change
def codeTest(year1, month1, day1, year2, month2, day2, answer):
    try:
        result = daysBetweenDates(year1, month1, day1, year2, month2, day2)
        if result == answer and answer != "AssertionError":
            return "correct"
        else: 
            return "incorrect"
    
    except AssertionError:
        if answer == "AssertionError":
            return "correct AssertionError"
        else:
            return "incorrect AssertionError"
           

def mytest():
    assert codeTest(2012,1,1,2013,1,1,366) 
    assert codeTest(2013,1,1,2014,1,1,365)  
    assert codeTest(2013,1,24,2013,6,2,129)

    print("Tests finished")

mytest()