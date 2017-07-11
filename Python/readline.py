import os
os.chdir("C:/Users/Jung Woo Park/Desktop")



def count_apluses(filename):
    files = open(filename)
    readline = files.readline()
    while readline:
        readline = files.readline()
        split = readline.split(", ")
        print split

files.close()
print count_apluses("1 to 100.txt")
