# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
Dictionary containing the values for
each letter in a game of Scrabble.
"""
LETTER_VALUES = {
    'a': 1,
    'b': 3,
    'c': 3,
    'd': 2,
    'e': 1,
    'f': 4,
    'g': 2,
    'h': 4,
    'i': 1,
    'j': 8,
    'k': 5,
    'l': 1,
    'm': 3,
    'n': 1,
    'o': 1,
    'p': 3,
    'q': 10,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'v': 4,
    'w': 4,
    'x': 8,
    'y': 4,
    'z': 10,
}

def welcome_message():
    """
    Presents the user with an introductory message.
    """
    print('------------------------------')
    print(' WELCOME TO SCRABBLE SCOREPAD')
    print('------------------------------')
    print('When presented with options simply type the number of your choice and hit Enter.\n')    


def wordlist_selector():
    """
    Sets the specific wordlist to be used
    for the purpose of word validation.
    """
    while True:
        print('WORDLISTS')
        print('1 - EU/World (SWOPODS)')
        print('2 - USA/Canada (TWL06)\n')

        wordlist_value = input('Please indicate which wordlist you require: ')

        if wordlist_value == '1':
            print('Loading EU/World (SWOPODS) wordlist...\n')
            wordlist_txt = open('wl-eu-sowpods.txt', 'r')
            break
        elif wordlist_value == '2':
            print('Loading USA/Canada (TWL06) wordlist...\n')
            wordlist_txt = open('wl-us-twl.txt', 'r')
            break
        else:
            print(f'Sorry, {wordlist_value} is not a valid option.\n')
    
    return wordlist_txt
        

def main():
    """
    Run all functions within the program
    """
    welcome_message()
    wordlist_selector()


main()