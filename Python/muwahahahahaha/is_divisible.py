def is_divisible(a_number, x):
    if a_number%x == 0:
        print a_number, "is divisible by ", x
    else:
        print a_number, "is not divisible by ", x

print "enter 2 number to find out if it is divisible or not"
a_number = input("a number: ")
x = input("second number: ")
is_divisible(a_number, x)
