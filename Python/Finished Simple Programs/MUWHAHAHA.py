#guess_my_number function
def guess_my_number(x):
    if x>10 and x<=15 or x>22 and x<=25:
        print "hmm your pretty close for a great surprise!"
        import time
        time.sleep(2)
        print "try again!"
        import time
        time.sleep(2)
    elif x>5 and x<=10 or x>25 and x<28:
        print "Dude (or hey girl! If you're a girl)."
        import time
        time.sleep(2)
        print "Polar Bears are freezing too death. It is way too cold!"
        import time
        time.sleep(2)
        print "try again!"
        import time
        time.sleep(2)
    else:
        if x<=5 or x>=28:
            print "Are you an animal? Because if you are, then I suggest"
            import time
            time.sleep(2)
            print "you be a domestic turkey!"
            import time
            time.sleep(2)
            print "If you want to know why you should be a domestic turkey,"
            import time
            time.sleep(2)
            print "then visit this website: https://answers.yahoo.com/question/index?qid=20061028182629AAEhkJ1"
            import time
            time.sleep(2)
            print "try again!"
            import time
            time.sleep(2)
#end of function
        
#start of main_frame:
print "I suggest that you really guess my number come on it will be fun!!"
import time
time.sleep(2)
print "Guess it, it's a surprise!"
import time
time.sleep(2)
while True:
    print "Guess my number which is between 0 to 30. Think wisely!"
    x = input("Your Guess: ")
    if x == 22:
        import time
        time.sleep(1)
        print "Considering....."
        import time
        time.sleep(2)
        print "BANG! RIGHT ON THE MONEY! NOW THAT IS THE NUMBERS OF LASHES THAT YOU SHALL GET!"
        break
    else:
        guess_my_number(x)
