#creating an encrypter

# step 1: 1-26:26-1
# step 2: backwards
# step 3: spc ---> !@#$%^&*()_+
# step 4: change spc to no.
# step 5: *2
# step 6: +2
# step 7: /4

def reverse_string(strng):
    word = ""
    for char in strng:
        word = char + word
    return word


def par_encryption(message):
    """

    >>> par_encryption("hello")
    '^##58'
    >>> par_encryption("it is such a nice day")
    ',14.539%.1.83+).)9._9'
    """
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                "n","o","p","q","r","s","t","u","v","w","x","y","z"]

    aa = ["1","2","3","4","5","6","7","8","9","!","@","#","$",
          "%","^","&","*","(",")","_","+","[","]",";",",","~"]# aa = alphabet_association

    encryption = ""
    space = " "
    for char in message:
        if char == space:
            encryption += "."
        
        elif char == alphabet[0]:
            encryption += aa[0]

        elif char == alphabet[1]:
            encryption += aa[1]

+        elif char == alphabet[2]:
            encryption += aa[2]

        elif char == alphabet[3]:
            encryption += aa[3]

        elif char == alphabet[4]:
            encryption += aa[4]

        elif char == alphabet[5]:
            encryption += aa[5]

        elif char == alphabet[6]:
            encryption += aa[6]

        elif char == alphabet[7]:
            encryption += aa[7]

        elif char == alphabet[8]:
            encryption += aa[8]

        elif char == alphabet[9]:
            encryption += aa[9]
        
        elif char == alphabet[10]:
            encryption += aa[10]

        elif char == alphabet[11]:
            encryption += aa[11]

        elif char == alphabet[12]:
            encryption += aa[12]

        elif char == alphabet[13]:
            encryption += aa[13]

        elif char == alphabet[14]:
            encryption += aa[14]

        elif char == alphabet[15]:
            encryption += aa[15]

        elif char == alphabet[16]:
            encryption += aa[16]

        elif char == alphabet[17]:
            encryption += aa[17]

        elif char == alphabet[18]:
            encryption += aa[18]
            
        elif char == alphabet[19]:
            encryption += aa[19]

        elif char == alphabet[20]:
            encryption += aa[20]

        elif char == alphabet[21]:
            encryption += aa[21]

        elif char == alphabet[22]:
            encryption += aa[22]

        elif char == alphabet[23]:
            encryption += aa[23]

        elif char == alphabet[24]:
            encryption += aa[24]

        elif char == alphabet[25]:
            encryption += aa[25]

        elif char >= 0:
            encryption += char # problems with intepreting numbers and symbols conflicts.


    return reverse_string(encryption)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
