def is_prime(n):
    num_counter = 0
    lists = []
    rng = range(2, n+1)
    i = 0
    
    while i < len(rng):
        divide = 1
        number = rng[i]
        while divide <= number:
            if number%divide == 0:
                num_counter += divide
            if num_counter == 1+number:
                lists += number,
            divide += 1
        i += 1

    return lists

is_prime(5)
