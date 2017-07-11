def print_multiples(n, high):
    i=1
    while i <= 6:
        print n*i, "\t",
        i += 1
    print

def print_mult_table(high):
    i = 1
    while i <= high:
        print_multiples(i, high)
        i += 1

        
