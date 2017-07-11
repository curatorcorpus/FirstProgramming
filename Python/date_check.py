# input: a date in the format of "dd/mm/yyyy"

# output: True if the date is valid, False otherwise

# Algorithm refinement:

# Level 1. check dd is valid day, mm is valid month etc



# Level 2. how do I check the month is valid?

#   - make sure month is between 1 and 12
#      - first split off the month part and convert to integer


# How do I check the day is valid?

#   - first check the day is between 1 and 31

#   - if the month is April (04) or June or Sept or Nov
#        then check the day is between 1 and 30

#   - if the month is Feb then
#        if it is a leap year, check day is between 1 and 29
#        else check day is between 1 and 28

def check_date(date_string):
    """
    >>> check_date("16/08/1970")
    True
    >>> check_date("01/01/2001")
    True
    >>> check_date("01/13/2001")
    False
    >>> check_date("32/01/2000")
    False
    >>> check_date("31/04/2000")
    False
    >>> check_date("29/02/2000")
    True
    >>> check_date("29/02/2001")
    False
    """

    # first split off the month part and convert to integer
    mth = int(date_string[3:5])

    # make sure month is between 1 and 12

    # following two ifs are equivalent
    # if not (mth >= 1 and mth <= 12) :
    if mth < 1 or mth > 12:
        return False

    # first split off the day part and convert to integer
    day = int(date_string[0:2])

    # first check the day is between 1 and 31
    if day <1 or day > 31:
        return False

    # if the month is April (04) or June or Sept or Nov
    #   then check the day is between 1 and 30

    if mth==4 or mth==6 or mth==9 or mth==11:
        if day>30:
            return False

    # if the month is Feb then
    #   if it is a leap year, check day is between 1 and 29
    #   else check day is between 1 and 28

    # first split off the year
    year = int(date_string[6:])
    if mth == 2:
        if year%4==0 and day>29:
            return False
        elif year%4!=0 and day>28:
            return False
        
    return True


if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)

