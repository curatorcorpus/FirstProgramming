def replace_names(s, old, new):
    """

    >>> replace_names("Mississippi", "i", "I")
    'MIssIssIppI'
    >>> s = "I love spom! Spom is my favorite food. Spom, spom, spom, yum!"
    >>> replace_names(s, "o", "a")
    'I lave spam! Spam is my favarite faad. Spam, spam, spam, yum!'
    """
    
#    return s.replace(old, new) or
    name = ""
    for char in s:
        if char == old:
             name += new
        else:
            name += char
    return name
        
def replace_mult_names(s, old, new):
    """

    >>> replace_mult_names("Mississippi", "is", "I")
    'MIsIsippi'
    >>> s = "I love spom! Spom is my favorite food. Spom, spom, spom, yum!"
    >>> replace_mult_names(s, "om", "am")
    'I love spam! Spam is my fovorite food. Spam, spam, spam, yum!'
    """
    scan1 = 1
    scan2 = 2
    
    word = [s[0]+s[1]]
            
    while scan2 < len(s):
        if s[scan1] in word:
            word += ""
        else:
            word += s[scan1] + s[scan2],
        scan1 += 1
        scan2 += 1
    print word
    new_list = []
    for biword in word:
        print biword
        if biword == old:
            new_list += biword,
    while scan2 < len(s):
        if s[scan1] in word:
            word += ""
        else:
            word += s[scan1] + s[scan2],
        scan1 += 1
        scan2 += 1            

    return new_list
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
