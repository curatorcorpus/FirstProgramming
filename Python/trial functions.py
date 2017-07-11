#trial functions
def print_multiples(n, high):
    i=1
    while i <= high:
        print n*i, "\t",
        i += 1
    print

def print_mult_table(high):
    i = 1
    while i <= high:
        print_multiples(i, i)
        i += 1
        
def sqrt_newton(n):
    eps = 1e-8
    approx = n/2.0
    better = (approx + n/approx)/2.0
    while abs(better-approx) > eps:
        approx = better
        better = (approx + n/approx)/2.0
    return approx
