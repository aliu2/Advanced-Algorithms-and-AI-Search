def read_dictionary(filename, length):
    # your code here
    
    words = []
    with open(filename, 'r') as myFile:
        lines = myFile.readlines()
        for word in lines:
            word = word.replace('\n','')
            if len(word) == length and word.islower() and word not in words:
                words.append(word)
    
    return words # a list of the words in the dictionary which comprise only lower case letters and are of the correct length
