def is_prime(n):
    for num in range(2,n/2):
        if n%num == 0:
            break
    else:
        print n,
            
def all_prime(prime):
    for n in range(2, prime+1):
        is_prime(n)


def all_prime_combo(prime):
    for n in range(2, prime+1):
        for num in range(2,n):# this works but a little slower
            #if num in range(2,(n+1)/2)), prints out 4. because (n+1)/2=2
            #and range(2,2) returns [], and invalid value, how to fix?
            if n%num==0:
                break
        else:
            print n,

all_prime_combo(10000)
