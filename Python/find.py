def find(string, ch):
    index = 0
    while index < len(string):
        if string[index] == ch:
            return index
        index += 1
    return -1

print find('A bigram is not a trigram', 'i' )

