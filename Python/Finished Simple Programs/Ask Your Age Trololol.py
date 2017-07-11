while True:
    print 'Hello everyone!'
    import time
    time.sleep(1)

    print 'I shall calculate the number of days, minutes or seconds you have lived in this place called earth.'
    import time
    time.sleep(3)

    print 'May I have your name good sir? Or if your a gal. Madam?'
    name = raw_input("Name: ")

    print 'Pleased to meet you', name, 'would you like to tell me your age?'
    age = int(input('Age: '))

    days = age * 365
    minutes = age * 525600
    seconds = age * 31536000

    print '.....Calculating. Please wait.'

    import time
    time.sleep(5)

    print name, 'has lived', days, 'in days', minutes, 'in minutes and', seconds, 'in seconds. Congratulations.'
    print 'Have another go.'
    import time
    time.sleep(3)
    
