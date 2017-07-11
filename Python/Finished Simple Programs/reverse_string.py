def reverse_string(strng):
    word = ""
    for char in strng:
        word = char + word
    return word
