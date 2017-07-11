
import os
os.chdir("C:/Users/Jung Woo Park/Desktop")

files = open(raw_input("Enter a file from Desktop: "))
reading = files.read()
  
splitting = reading.split()
number = len(splitting)

while number > 0:
    number -= 1
    string = splitting[number]

    def remove_vowels(string):
        """

        >>> remove_vowels("hubble")
        'h_bbl_'
        >>> remove_vowels("bubble")
        'b_bbl_'
        >>> remove_vowels("toil")
        't__l'
        >>> remove_vowels("and")
        '_nd'
        >>> remove_vowels("trouble")
        'tr__bl_'
        """
        vowels = "aeiou"
        word = ""
        for char in string:
            if char in vowels:
                word += "_"
            else:
                word += char
        return word

    if __name__ == "__main__":
        import doctest
        doctest.testmod()

    print remove_vowels(string)
    
