while True:
    print"Welcome!"
    import time
    time.sleep(1)

    print"To this program"
    import time
    time.sleep(1)

    print"to announce you ages in months, days, hours, minutes and seconds"
    import time
    time.sleep(2)

    print"please enter your name"
    name = raw_input("name: ")

    print"please enter your age"
    age = int(input("age: "))

    months = age * 12
    days = age * 365
    hours = age * 8760
    minutes = age * 525600
    seconds = age * 31536000

    print".....Calculating. Please wait."
    import time
    time.sleep(5)

    print"the results came out and says that you have been alive for"
    import time
    time.sleep(2)
    print"on this place called Earth for:", months, "months or", days, "days or", hours, "hours or", minutes, "minutes or", seconds, "seconds. Have a good day!"
    import time
    time.sleep(5)
    
