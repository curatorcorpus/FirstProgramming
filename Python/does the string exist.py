def string_existence(filename, string):
    for char in filename:
        if char == string:
            return "Yes the string appears in this file"
        else:
            return "No it doesn't exist"
        filename.close()
        
        
