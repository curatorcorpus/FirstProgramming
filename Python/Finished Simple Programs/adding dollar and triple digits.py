
import os
os.chdir("C:/Users/Jung Woo Park/Desktop")

inputs = raw_input("Enter a file in Desktop: ")
files = open(inputs)
reading = files.read()
splitting = reading.split()


length = len(splitting)
    
for n in range(length -1):
    if n > 0:
        find = splitting[n]

    def adding_dollar(find):
        dollar = "$"
        dollar += find + "000"
        return dollar

print adding_dollar(find)
