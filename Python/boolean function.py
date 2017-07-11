def boolean_function(x, y):
    if x or y:
        print x, "or", y, "is", x or y
    elif not x and y:
        print x, "and", y, "is", not x and y
    elif not x or not y:
        print x, "or", y, "is", not x or not y
    elif x and not y:
        print x, "and", y, "is", x and not y
        
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    s_without_vowels = ""
    for letter in s:
        if letter not in vowels:
            s_without_vowels += letter
    return s_without_vowels
