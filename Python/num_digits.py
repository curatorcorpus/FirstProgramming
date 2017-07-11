def num_digits(n):
    #>>> num_digits(12345)
    #5
    #>>> num_digits(0)
    #1
    #>>> num_digits(-12345)
    #5
 
    count = len(str(abs(n)))
    return count

