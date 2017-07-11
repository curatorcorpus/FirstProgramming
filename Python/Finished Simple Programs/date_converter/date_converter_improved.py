def date_converter(date):
    word = ""
    space = " "
    date_list = date.split("/")
    month_names = ["January","Feburary","March","April","May","June",
                   "July","August","September","October","November",
                   "December"]

    day = date_list[0]
    integer_day = int(day)
    if integer_day == 1 or integer_day == 21 or integer_day == 31:
        word += str(integer_day) + "st" + space
    elif integer_day == 2 or integer_day == 22:
        word += str(integer_day) + "nd" + space
    elif integer_day == 3 or integer_day == 23:
        word += str(integer_day) + "rd" + space
    else:
        word += str(integer_day) + "th" + space
    
    month = int(date_list[1])
    month_number = month - 1
    access = month_names[month_number]
    word += access + "," + space

    word = word + date_list[2]
    
    return word 

date = raw_input("Enter a date in dd/mm/yyyy format: ")
print date_converter(date)
