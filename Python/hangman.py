def hangman(string, start, end):
    """

    >>> hangman("banana", 0, 5)
    'b****a'
    >>> hangman("passionfruit", 0, 7)
    'p******f****'
    >>> hangman("watermelons", -1, -1)
    '***********'
    >>> hangman("peaches", 2, 10)
    '**a****'
    """
    lists = list(string)
    i = 0
    word = ""
    
    while i < len(lists):
        if i != start and i != end:
            word += "*"
            i += 1
        elif i == start or i == end:
            word += lists[i]
            i += 1

    return word

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    

def table(letters, numbers):
    """

    >>> table("abcd", 1234)
    'a1 b2 c3 d4'
    """
    i = 0
    s_num = str(numbers)
    while i < len(letters):
        print letters[i]+s_num[i],
        i += 1
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

    
def mix_match(letters, numbers):
    """

    >>> mix_match("abcd",1234)
    'a1 b2'
    'c3 d4'
    """
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    

def print_multiples(n,high):
    i = 1
    while i <= high:
        print n*i, "\t",
        i += 1
    print

def print_mult_table(high):
    i = 1
    while i <= high:
        print_multiples(i,high)
        i += 1
print_mult_table(2)

