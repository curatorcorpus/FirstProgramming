def guess_right(guess, secret):
    if guess == 55:
        print "you win. ", guess, "is equall to ", secret
    else:
        guess != 55
        print "you lose. ", guess, "is not equall to ", secret

secret = 55
guess = input("guess a number between 50 and 100: ")
guess_right(guess, secret)

