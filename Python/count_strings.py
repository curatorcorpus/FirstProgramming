def count_numbers(strings):
    count = 0
    while count < len(strings):
        count += 1
    return count

def num_zero_and_five_digits(n):
    count = 0
    while n > 0:
        digit = n% 10
        if digit == 0 or digit == 5:
            count += 1
        n /= 10
    return count


#creating tables

def tables(x):
    count = 0
    while count <= x:
        print count, "\t", 2**count
        count += 1

#encapsulation and generalisation

#encapsulation: process of wrapping a piece of code inside a function
#generalisation: is the process of taking something specific, such as printing
#the multiple of 2 and making it more general by printing the multiple of
#any integer.

def print_multiples(n):
    i = 1
    while i <= 6:
        print n*i, "\t",
        i += 1
    print

def print_mutli_tabels(high):
    i = 1
    while i <= high:
        print_multiples(i)
        i += 1

def newtons_method(n):
    eps = 1e-8
    approx = n/2.0
    better = (approx + n/approx)/2.0
    while abs(better-approx) > eps:
        approx = better
        better = (approx + n/approx)/2.0
    return approx

print newtons_method(144)
