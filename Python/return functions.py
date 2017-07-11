def print_square_root(x):
    if x<0:
        print "Error: cannot take square root of a negative number."
        return

    result = x**0.5
    print "The square root of", x, "is ", result

def square_root(x):
    if x<0:
        print "error"

    result = x**0.5
    return result

def area_of_circle(radius):
    if radius<0:
        print "error"
        return

    area = 3.14159*radius**0.5
    return area

def absolute_value(x):
    if x=<0:
        return -x
    return x
    
