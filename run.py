# WORDLIST AND LETTER VALUE CONSTANTS

"""
Dictionary containing the values for each letter in a game of Scrabble.
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


# FUNCTIONS

def wordlist_selector():
    """
    Sets the specific wordlist to be used for the purpose of word validation.
    """
    while True:
        print('Available Wordlists:')
        print('1 - EU/World (SWOPODS)')
        print('2 - USA/Canada (TWL06)\n')

        wordlist_value = input('Please indicate which wordlist you require:\n')

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
        

def word_validator(wordlist_txt):
    """
    Validates that the word is contained within the selected wordlist.
    """
    print('Word Validation and Scoring')
    print('----------------------------')
    print('Any modifiers for blank tiles (*), or double (2)/triple (3) letter scores ')
    print('should be placed AFTER their respective letters. For example, entering ')
    print("'wo*rd3s' indicates a blank tile for 'o' and triple letter score on 'd'.\n")

    word_value = input('Please enter the word to be checked and scored:\n') 

    if word_value in wordlist_txt.read():
        print(f"The word '{word_value}' is valid!\n")        
    else:
        print(f"Sorry, '{word_value}' is not a valid word on this list.\n")
        word_value = 0  # 0 is used to indicate that the word is invalid
    
    wordlist_txt.close()
    return word_value


def word_score(word_value):
    """
    Evaluates the score of the entered word.
    """
    if word_value != 0:
        print(word_value)


def end_menu():
    """
    Allows the user to either check another word or end the program.
    """
    while True:
        print('Options:')
        print('1 - Restart')
        print('2 - Close Program\n')

        option_value = input('Please indicate which option you require:\n')

        if option_value == '1':
            main()
            break
        elif option_value == '2':
            print('Closing program... \n')
            print('----------------------------------------')
            print('Many thanks for using Scrabble Scorepad!')
            print('----------------------------------------\n')
            break
        else:
            print(f'Sorry, {option_value} is not a valid option.\n')


def main():
    """
    Run all top level functions within the program.
    """
    wordlist = wordlist_selector()
    value = word_validator(wordlist)
    score = word_score(value)
    end_menu()
    

# PROGRAM EXECUTION

print('----------------------------')
print('WELCOME TO SCRABBLE SCOREPAD')
print('----------------------------')
print('When presented with options simply type the number of your choice and hit Enter.\n')

main()