string1 = "banana"
string2 = "banana"
if id(string1)==id(string2):
    print "Same"
else:
    print "Different"
list1 = [1,2,3]
list2 = [1,2,3]
if id(list1)==id(list2):
    print "Same"
else:
    print "Different"
