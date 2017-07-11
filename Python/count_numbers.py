def count_numbers(filename):
    import os
    os.chdir("C://Users/Jung Woo Park/Desktop")

    files = open(filename)
    read = files.read()
    split = read.split()

    addition = 0
    for numbers in split:
        number = int(numbers)
        addition += number

    return addition


print count_numbers("numbers.txt")
