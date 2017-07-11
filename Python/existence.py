def existence(filename, string):
    import os
    os.chdir("C:/Users/Jung Woo Park/Desktop")
    files = open(filename)
    reading = files.read()
    splitting = reading.split()
    print splitting

    i = 0
    while i<len(splitting):
        index = splitting[i]
        i += 1
        for char in index:
            print char
            if char == string:
                return "there is the string ", string, "in this file"
            elif char != string:
                return "there is no string ", string, "in this file"
        


print existence("hubble.txt", "a")

