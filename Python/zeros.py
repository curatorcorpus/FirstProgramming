def zeros(columns, rows):
    """

    >>> A = zeros(3,2)
    >>> A
    [[0, 0], [0, 0], [0, 0]]
    >>> A[0][1] = 1
    >>> A
    [[0, 1], [0, 0], [0, 0]]
    """
    start = []
    i = 0
    while i < columns:
        start += [0]*rows,
        i+=1
    return start


def insert_sorted(lst, element):
    """

    >>> insert_sorted([1,3,5], 4)
    [1, 3, 4, 5]
    >>> insert_sorted([1,2,3], 0)
    [0, 1, 2, 3]
    >>> insert_sorted([1,2,3], 4)
    [1, 2, 3, 4]
    """
    new_list = []
    for num in lst:
        if num+1 == element:
            new_list += num,
            new_list += element,
        elif num-1 == element and num-1 not in new_list:
            new_list += element,
            new_list += num,
        else:
            new_list += num,
    return new_list


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
