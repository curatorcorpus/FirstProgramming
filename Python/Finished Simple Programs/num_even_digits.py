def num_even_digits(n):
    """

    >>> num_even_digits(123456)
    3
    >>> num_even_digits(2468)
    4
    >>> num_even_digits(1357)
    0
    >>> num_even_digits(2)
    1
    >>> num_even_digits(20)
    2
    """
    string = str(n)
    word = ""
    for number in string:
        if int(number)%2==0:
            word += number
    return len(word)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
            
