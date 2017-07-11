#Film critic.py Lab Exercise 4.6 Question 8

def film_critic(movie):
    print "Give this movie a rating"
    rating = input("Rating: ")
    print 'Movie: ', movie, 'Your rating; ', rating

#movie = raw_input("Movie: ")
#print film_critic(movie)

#remove comments to activate

def name_age(name, age):
    print "Hello ", name, "you are ", age, "years old."
    print "next year you will be, ", age + 1

#name = raw_input("name: ")

def score_summaries(x, y, z):
    maximum = max(x, y, z)
    minimum = min(x, y, z)
    average = (x + y + z)/2
    return maximum, minimum, average

