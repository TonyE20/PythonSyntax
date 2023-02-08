def print_upper_words(list):
    """ function will convert words in list uppercase and print them """   
    
    for word in list:
        print(word.upper())


def print_upper_words(list):
    """ prints words that start with 'e' upper or lower case """   
    
    for word in list:
        word_lower = word.lower()
        if word_lower[0] == 'e':
            print(word.upper())


def print_upper_words(list, must_start_with):
    """ prints words that start letters in must_start_with"""   
    
    for word in list:
        word_lower = word.lower()
        for char in must_start_with:
            if word_lower[0] == char:
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with=["h", "y"])        