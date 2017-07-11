def remove_duplicates(s):
    """

    >>> remove_duplicates("apple")
    'aple'
    >>> remove_duplicates("Mississippi")
    'Misp'
    >>> remove_duplicates("The quick brown fox jumps over the lazy dog")
    'The quick brown fx jmps v t lazy dg'
    >>> remove_duplicates("What Will We Do with the drunken whaler")
    'What il e Do w  drunk '
    """
    word = ""
    whitespace = " "
    for char in s:
        if char not in word:
            word += char
        elif char == whitespace:
            word += char
    return word
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
