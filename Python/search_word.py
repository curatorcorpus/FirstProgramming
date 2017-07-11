import os
os.chdir("c://Users/Jung Woo Park/Desktop")


def search_word(search_name, filename):
    files = open(filename)
    line = files.readline()

    count = 1
    occurrence = 0
    while line != "":
        split = line.split()
        if split[0] == search_name: #this doesnt work if line == search_name (line == string)? why?            
            occurrence += 1
            print "line", count
            count += 1
            line = files.readline()

        count += 1
        line = files.readline()

    files.close()
    return occurrence

print search_word("daffodils", "mary.txt")
