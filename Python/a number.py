def is_divisible_by_3(a_number):
    if a_number%3 == 0:
        print a_number, "is divisible by three."
    else:
        print a_number, "is not divisible by three"

print "enter a number to find out if it is divisible by three"
a_number = input("a number: ")
is_divisible_by_3(a_number)

