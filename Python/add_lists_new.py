def add_lists(a,b):
    """

    >>> add_lists([1, 1], [1, 1])
    [2, 2]
    >>> add_lists([1, 2], [1, 4])
    [2, 6]
    >>> add_lists([1, 2, 1], [1, 4, 3])
    [2, 6, 4]
    >>> list1=[1, 2, 1]
    >>> list2=[1, 4, 3]
    >>> sum = add_lists(list1, list2)
    >>> list1 == [1 ,2, 1]
    True
    >>> list2 == [1, 4, 3]
    True
    """

    for i in range(len(a)):
        a[i] += b[i]
    return a

list1 = [1,2,3]
list2 = [3,4,6]
print list1
print list2
print add_lists(list1,list2)
