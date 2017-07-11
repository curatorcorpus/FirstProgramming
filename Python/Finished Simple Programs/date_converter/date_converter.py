# convert DD/MM/YYYY into word format
# enter a date in DD/MM/YYYY format

# problems that can be encountered: converting a numerial month into words
# and getting the correct suffix to the day (st, nd, rd, th)
# problems can be solved with judicious use of lists

#get input

def date_converter(numerical_date):
    """

    >>> date_converter("22/12/1995")
    '22nd December, 1995'
    >>> date_converter("14/11/1996")
    '14th November, 1996'
    >>> date_converter("05/06/1900")
    '5th June, 1900'
    >>> date_converter("01/01/1111")
    '1st January, 1111'
    >>> date_converter("02/02/2015")
    '2nd Feburary, 2015'
    >>> date_converter("31/12/2300")
    '31st December, 2300'
    >>> date_converter("23/10/2000")
    '23rd October, 2000'
    >>> date_converter("16/09/2006")
    '16th September, 2006'
    """
    #st = ["1", "21", "31"] #how to used the list st = ["1", "21", "31"] doesnt work
    final_date = ""
    zero = "0"
    first_number = numerical_date[:1]
    day = numerical_date[1:2]
    month = numerical_date[3:5]
    year = numerical_date[6:]
    # day
    for char in first_number:
        if char not in zero:
            final_date += char
    final_date1 = final_date

    for char in day:
        final_date1 += char
            
    if final_date1 == "1" or final_date1 == "21" or final_date1 == "31":
        final_date1 += "st" + " "
    elif final_date1 == "2" or final_date1 == "22": #multi if statements is a no no why?
        final_date1 += "nd" + " "
    elif final_date1 == "3" or final_date1 == "23":
         final_date1 += "rd" + " "
    else:
        final_date1 += "th" + " "
    final_date2 = final_date1

    if month == "01":
        final_date2 += "January" + ", "
    elif month == "02":
        final_date2 += "Feburary" + ", "
    elif month == "03":
        final_date2 += "March" + ", "
    elif month == "04":
        final_date2 += "April" + ", "
    elif month == "05":
        final_date2 += "May" + ", "            #put this into list
    elif month == "06":
        final_date2 += "June" + ", "            #apparently using if in this situation works
    elif month == "07":
        final_date2 += "July" + ", "
    elif month == "08":
        final_date2 += "August" + ", "
    elif month == "09":
        final_date2 += "September" + ", "
    elif month == "10":
        final_date2 += "October" + ", "
    elif month == "11":
        final_date2 += "November" + ", "
    elif month == "12":
        final_date2 += "December" + ", "
    #year
    final_date2 += year
    return final_date2

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
