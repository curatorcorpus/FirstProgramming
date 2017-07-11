
# step 1: 1-26:26-1
# step 2: backwards
# step 3: spc ---> !@#$%^&*()_+
# step 4: *2
# step 5: +2
# step 6: /4

def reverse_string(strng):
    word = ""
    for char in strng:
        word = char + word
    return word


def par_decryption(message):# message must be in strings
    """

    >>> par_decryption('^##58')
    'hello'
    >>> par_decryption(',14.539%.1.83+).)9._9')
    'it is such a nice day'
    """
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                "n","o","p","q","r","s","t","u","v","w","x","y","z"]

    #aa = ["1","2","3","4","5","6","7","8","9","10","11","12","13",
    #      "14","15","16","17","18","19","20","21","22","23","24","25","26"]# aa = alphabet_association

    aa = ["1","2","3","4","5","6","7","8","9","!","@","#","$",
          "%","^","&","*","(",")","_","+","[","]",";",",","~"]

    reversed_msg = reverse_string(message)
    encryption = ""
    space = "."
    for char in reversed_msg:
        if char == space:
            encryption += " "
        
        elif char == aa[0]:
            encryption += alphabet[0]

        elif char == aa[1]:
            encryption += alphabet[1]

        elif char == aa[2]:
            encryption += alphabet[2]

        elif char == aa[3]:
            encryption += alphabet[3]

        elif char == aa[4]:
            encryption += alphabet[4]

        elif char == aa[5]:
            encryption += alphabet[5]

        elif char == aa[6]:
            encryption += alphabet[6]

        elif char == aa[7]:
            encryption += alphabet[7]

        elif char == aa[8]:
            encryption += alphabet[8]

        elif char == aa[9]:
            encryption += alphabet[9]
        
        elif char == aa[10]:
            encryption += alphabet[10]

        elif char == aa[11]:
            encryption += alphabet[11]

        elif char == aa[12]:
            encryption += alphabet[12]

        elif char == aa[13]:
            encryption += alphabet[13]

        elif char == aa[14]:
            encryption += alphabet[14]

        elif char == aa[15]:
            encryption += alphabet[15]

        elif char == aa[16]:
            encryption += alphabet[16]

        elif char == aa[17]:
            encryption += alphabet[17]

        elif char == aa[18]:
            encryption += alphabet[18]
            
        elif char == aa[19]:
            encryption += alphabet[19]

        elif char == aa[20]:
            encryption += alphabet[20]

        elif char == aa[21]:
            encryption += alphabet[21]

        elif char == aa[22]:
            encryption += alphabet[22]

        elif char == aa[23]:
            encryption += alphabet[23]

        elif char == aa[24]:
            encryption += alphabet[24]

        elif char == aa[25]:
            encryption += alphabet[25]

    return encryption

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
    
