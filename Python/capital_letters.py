def capital_letter(word):
    words = "abcdefghijklmnopqrstuvwxyz"
    for letter in word:
        if letter not in words:
            return letter
