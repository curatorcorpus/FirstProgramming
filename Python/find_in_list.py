def find_in_list(a_list):
    length = len(a_list)-1
    if length == 4:
        return a_list[4]
    elif length < 4:
        return "No such element"
    

def the_last_two_in_list(a_list):
    length = len(a_list)-1
    if length >= 2:
        return a_list[length-1], a_list[length]

def find_every_second_element(a_list):
    every_second_element = range(1,len(a_list),2)
    if 1<=len(a_list):
        for number in every_second_element:
            convert = int(number)
            print a_list[convert]


def list_length(a_list):
    i=0
    while i<len(a_list):
        print len(a_list[i])
        i += 1
        
def add_lists(a,b):
    list1 = a
    list2 = b
    in_list = []

    i = 0
    while i < len(list1) and i < len(list2):
        in_list += [list1[i]+list2[i]]
        i += 1
    return in_list


def multi_list(a,b):
    """

    >>> multi_list([1, 1],[1, 1])
    2
    >>> multi_list([1, 2],[1, 4])
    9
    >>> multi_list([1, 2, 1],[1, 4, 3])
    12
    """

    list1 = a
    list2 = b
    list_product = 0
    i = 0

    while i < len(list1) and i < len(list2):
        list_product += list1[i]*list2[i]
        i += 1
    return list_product

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
