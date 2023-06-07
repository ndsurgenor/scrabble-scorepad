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

    specified_word = input('Please enter the word to be checked and scored:\n') 

    if specified_word in wordlist_txt.read():
        print(f"The word '{specified_word}' is valid!\n")        
    else:
        print(f"Sorry, '{specified_word}' is not a valid word on this list.\n")
        specified_word = 0  # 0 is used to indicate that the word is invalid
    
    wordlist_txt.close()
    return specified_word


def evaluate_word(specified_word):
    """
    Returns the score of the specified word.
    """
    if specified_word != 0:
        evaluate_letters()
        evaluate_multiplier()
        evaluate_bonus()


def evaluate_letters(specified_word)
    """
    Calculates the letter score including specifed modifiers.
    """

    return word_score


def evaluate_multiplier(word_score)
    """
    Multiplies the letter score, if appropriate.
    """
    while True:
        print('Double or Triple word score?')
        print('1 - No multiplier')
        print('2 - Double word score')
        print('3 - Triple word score\n')

        multiplier = input('Please select an option:\n')

        if multiplier == '1':
            print('No multiplier to be applied\n')
            break
        elif multiplier == '2':
            print('Doubling word score...\n')
            word_score = word_score * 2
            break
        elif multiplier == '3':
            print('Tripling word score...\n')
            word_score = word_score * 3
            break
        else:
            print(f'Sorry, {multiplier} is not a valid option.\n')

    return word_score


def evaluate_bonus(word_score)
    """
    Adds a bonus to the final score, if appropriate.
    """
    while True:
        print('All tiles played on this turn?')
        print('Y - Yes')
        print('N - No\n')

        bonus = input('Please select an option:\n')

        if bonus == 'y' or 'yes':
            print('Bonus added for playing all seven tiles\n')
            word_score = word_score + 50
            break
        elif bonus == 'n' or 'no':
            print('No bonus to be applied\n')
            break
        else:
            print(f'Sorry, {bonus} is not a valid option.\n')

    return word_score


def end_menu():
    """
    Allows the user to either check another word or end the program.
    """
    while True:
        print('Options:')
        print('1 - Check another word')
        print('2 - Close program\n')

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
    word = word_validator(wordlist)
    score = evaluate_word(word)
    end_menu()
    

# PROGRAM EXECUTION

print('----------------------------')
print('WELCOME TO SCRABBLE SCOREPAD')
print('----------------------------')
print('When presented with options simply type the number of your choice and hit Enter.\n')

main()