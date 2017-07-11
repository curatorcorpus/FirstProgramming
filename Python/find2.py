def find_number(strng, x):
    """

    >>> find_number("346576345043","3")
    '(0) (6) (11) '
    >>> find_number("31/03/2133", "3")
    '(0) (4) (8) (9) '
    """

    i = 0
    word = ""
    
    while i < len(strng):
        if strng[i] == x:
            word += "("+str(i)+") "
        i += 1
    return word

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
