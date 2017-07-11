print "How are we today?"
emotions = raw_input("I am feeling: ")

if emotions == "great": #boolean expression (condition)
    print "It is good that you feel awesome"
elif emotions == "not bad":
    print "I'm sure you can do better."
elif emotions == "shit":
    print "Aww why would your day be shit? Be more positive! You can do it"
elif emotions == "not too bad":
    print "Alright then have a great day!"
elif emotions == "swell": #elif functions means if else and can contain variable
    print "oh jolly thats good to hear"
else: #means otherwise print
    print "well good for you then, sl**"
#new question
print "now you should really tell me how old you are?... in numerical values if possible"
age = raw_input("age: ")

if age >= 18:
    print "Hmm greetings old timer"
elif age < 18 or age == "i dont have one":#fix semantic error
    print "WOW man your still such a baby!"
        
        
