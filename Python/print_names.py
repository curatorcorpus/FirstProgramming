def print_names(name_list):
    """

    >>> print_names(["Brown",["Bob","Betty"],"Green",["Geoff","Gemma","Gail"]])
    Bob Brown
    Betty Brown
    Geoff Green
    Gemma Green
    Gail Green
    >>> print_names(["Carter",["Cathy"],"Downer",["Don"]])
    Cathy Carter
    Don Downer
    """
    real_index1 = 0
    surname1 = name_list[0]

    while real_index1 < len(name_list[1]):
        print name_list[1][real_index1] + " " + surname1
        real_index1 += 1

    real_index2 = 0
    surname2 = name_list[2]
    while real_index2 < len(name_list[3]):
        print name_list[3][real_index2] + " " + surname2
        real_index2 += 1

def print_names1(name_list):
    """

    >>> print_names1(["Brown",["Bob","Betty"],"Green",["Geoff","Gemma","Gail"]])
    ['Bob Brown', 'Betty Brown', 'Geoff Green', 'Gemma Green', 'Gail Green']
    >>> print_names1(["Carter",["Cathy"],"Downer",["Don"]])
    ['Cathy Carter', 'Don Downer']
    """
    real_index1 = 0
    surname1 = name_list[0]
    list1 = []
    list2 = []

    while real_index1 < len(name_list[1]):
        list1 += name_list[1][real_index1] + " " + surname1,
        real_index1 += 1
        
    real_index2 = 0
    surname2 = name_list[2]
    while real_index2 < len(name_list[3]):
        list2 += name_list[3][real_index2] + " " + surname2,
        real_index2 += 1
    return list1 + list2

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
