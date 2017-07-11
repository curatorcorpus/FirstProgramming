# count how many a there are in a txt document
def count_a(document, strng):
    reading = document.read()
    count = 0
    for char in reading:
        if char == strng:
            count += 1
    return count

import os
os.chdir('C:\Users\Jung Woo Park\Desktop')
document = open("document.txt")
strng = "a"
print count_a(document, strng)
document.close()


