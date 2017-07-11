
def print_powers(n, high):
    i = 1
    while i <= high:
        print n**i, "\t",
        i += 1

    print 


def print_powers_table(high):
    i = 1
    while i <= high:
        print_powers(i, high)
        i += 1

    print


def is_prime2(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in xrange(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def is_prime(n):
    num = 0
    i = 1
    while i <= n:
        if n%i == 0:
            num += n/i
        i += 1
    if num == 1+n:
        return True
    else:
        return False
print is_prime(11)
            
def all_prime_numbers(n):
    num = 0
    i = 1
    while i <= n:
        for numbers in range(1, n+1):
            if n%i == 0:
                divide = n/i
                num += divide
                print numbers
        i += 1

def is_prime_new(n):# doesnt work, needs debugging
    for numbers in range(2, n+1):
        i = 2
        num = 0
        while i <= numbers:
            remainder = numbers%i
            if remainder == 0:
                divide = numbers/i
                num += divide
            i += 1
            if num == 1+n:
                print num
            
            

def ip(n):
    div = 2
    isNPrime = True
    while n%div != 0:
        if (n+1)/2 == div:
            return False
        div += 1
    if n== 2:
        return True
    elif isNPrime:
        return False

