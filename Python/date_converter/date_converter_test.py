def date_converter(numerical_date):
    final_date = ""
    #st = ["1", "21", "31"] #how to used the list st = ["1", "21", "31"] doesnt work
    day = numerical_date[:2]
    month = numerical_date[3:5]
    year = numerical_date[6:]
    # day
    if day == "1" or day == "21" or day == "31":
        final_date += day + "st" + " "
    if day == "2" or day == "22":
        final_date += day + "nd" + " "
    if day == "3" or day == "23":
        final_date += day + "rd" + " "
    if month == "01":
        final_date += "January" + " "
    if month == "02":
        final_date += "Feburary" + " "
    if month == "03":
        final_date += "March" + " "
    if month == "04":
        final_date += "April" + " "
    if month == "05":
        final_date += "May" + " "            #put this into list
    if month == "06":
        final_date += "June" + " "
    if month == "07":
        final_date += "July" + " "
    if month == "08":
        final_date += "August" + " "
    if month == "09":
        final_date += "September" + " "
    if month == "10":
        final_date += "October" + " "
    if month == "11":
        final_date += "November" + " "
    if month == "12":
        final_date += "December" + " "
    #year
    final_date += year

    return final-date
