def file_length(x, y):
    files1 = open(x)
    files2 = open(y)
    
    reading1 = files1.read()
    reading2 = files2.read()

    print reading1
    print reading2
    
    if len(reading1)>len(reading2):
        return x, "file is longer"
    else:
        return y, "file is longer"

x = raw_input("enter the first file in strings: ")
y = raw_input("enter the second file in strings: ")

print file_length(x, y)

files1.close()
files2.close()
