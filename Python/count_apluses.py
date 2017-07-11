import os
os.chdir("C:/Users/Jung Woo Park/Desktop")



def count_apluses(filename):
    files = open(filename)
    line = files.readline()

    i = 0
    while line != "":
        replace1 = line.replace(",", "")
        replace2 = replace1.replace("\n", "")
        split = replace2.split()
        for numbers in split:
            if 90 < int(numbers) < 100:
                i += 1

        line = files.readline()

    return i
    files.close()
        
            
    
print count_apluses("1 to 100.txt")

