def is_prime2(x):
    for num in range(2,x):
        is_prime = True
        i = 2
        for prime in range(2, num):
            if num%i == 0:
                is_prime = False
                i += 1
            else:
                is_prime = True
                print num
def may_prime(n):
    i = 0
    tuples = ()
    rng = range(2,n+1)
    while i < len(rng):
        tuples += rng[i],
        i += 1
        
    for num in tuples:
        div = 1
        lists = []
        while div <= len(range(num)):
            if num%1 == 0 and num%num == 0 and (num+1)%2 == 0 and num not in lists or num == 2:
                lists += num,
                div += 1
            else:
                div += 1
        print lists


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

def is_it_prime2(n): #debugging required
    lists = []
    rng = range(2, n+1)
    for num in rng:
        if is_prime(num) == True:
            lists += num,
    return lists
print is_it_prime2(100)
def is_it_prime3(n):#debugging required
    lists = []
    rng = range(2, n+1)

    for num in rng:
        count = 0
        i = 1
        while i <= num:
            if num%i == 0:
                count += num/i
                i += 1
            i += 1
        if count == 1+num:
            lists += count,
    return lists

def prime2(n):
    p = 2
    tuples = ()
    while p < n:# 7 <= 10
        for i in range(2, p):
            print i
            if p%i == 0 and p/i == 1: #8%2, 3, 4, 5, 6, 7, 8
                p += 1 
        tuples += p,
        print tuples
        
        p += 1
    print tuples
        

def all_prime(n):
    for p in range(2, n+1):
        for i in range(2, p):
            if p % i != 0:
                print p

