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
            print('Loading EU/WORLD (SWOPODS) wordlist...\n')
            wordlist_txt = open('wl-eu-sowpods.txt', 'r')
            break
        elif wordlist_value == '2':
            print('Loading USA/CANADA (TWL06) wordlist...\n')
            wordlist_txt = open('wl-us-twl.txt', 'r')
            break
        else:
            print(f'Sorry, {wordlist_value.upper()} is not a valid option.\n')
    
    return wordlist_txt
        

def word_validator(wordlist_txt):
    """
    Validates that the word is contained within the selected wordlist.
    """
    print('Word Validation and Scoring')
    print('----------------------------')
    print('Required modifiers for blank tiles (*), or double (2)/triple (3) letter ')
    print('scores should be placed AFTER their respective letters. For example, entering ')
    print("'w*ord3s' would indicate a blank tile for W and triple letter score on D.\n")

    specified_word = (input('Please enter the word to be checked and scored:\n')).lower()

    if specified_word in wordlist_txt.read():
        print(f'The word {specified_word.upper()} is valid!\n')        
    else:
        print(f'Sorry, {specified_word.upper()} is not a valid word on this list.\n')
        specified_word = 0  #tells the next function that no score is to be evaluted
    
    wordlist_txt.close()
    return specified_word


def evaluate_word(specified_word):
    """
    Returns the score of the specified word. If the word is not valid,
    the program will continue to the end_menu() function.
    """
    if specified_word != 0:
        basic_score = evaluate_letters(specified_word)
        multiplied_score = evaluate_multiplier(basic_score)
        final_score = evaluate_bonus(multiplied_score)

        print(f'Final score for {specified_word.upper()} is {final_score}')


def evaluate_letters(specified_word):
    """
    Calculates the letter score including specified modifiers.
    """
    word_score = 0

    for letter in specified_word:
        individual_value = LETTER_VALUES.get(letter)
        word_score = word_score + individual_value

    print(f'The basic score of {specified_word.upper()} is {word_score}')
    return word_score


def evaluate_multiplier(word_score):
    """
    Multiplies the letter score, if appropriate.
    """
    while True:
        print('Double or Triple word score?')
        print('1 - None')
        print('2 - Double word score')
        print('3 - Triple word score\n')

        multiplier = input('Please select an option:\n').lower()

        if multiplier == '1' or multiplier == 'none' or multiplier == 'n':
            print('No multiplier to be applied\n')
            break
        elif multiplier == '2' or multiplier == 'double' or multiplier == 'd':
            print('Doubling word score...\n')
            word_score = word_score * 2
            break
        elif multiplier == '3' or multiplier == 'triple' or multiplier == 't':
            print('Tripling word score...\n')
            word_score = word_score * 3
            break
        else:
            print(f'Sorry, {multiplier.upper()} is not a valid option.\n')

    return word_score


def evaluate_bonus(word_score):
    """
    Adds a bonus to the final score, if appropriate.
    """
    while True:
        print('All tiles played on this turn?')
        print('1 - Yes')
        print('2 - No\n')

        bonus = input('Please select an option:\n').lower()

        if bonus == '1' or bonus == 'yes' or bonus == 'y':
            print('Bonus added for playing all seven tiles\n')
            word_score = word_score + 50
            break
        elif bonus == '2' or bonus == 'no' or bonus == 'n':
            print('No bonus to be applied\n')
            break
        else:
            print(f'Sorry, {bonus.upper()} is not a valid option.\n')

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
            print('--------------------------------------')
            print('Thank you for using Scrabble ScorePad!')
            print('--------------------------------------\n')
            break
        else:
            print(f'Sorry, {option_value.upper()} is not a valid option.\n')


def main():
    """
    Runs all top level functions within the program.
    """
    wordlist = wordlist_selector()
    word = word_validator(wordlist)
    score = evaluate_word(word)
    end_menu()
    

# PROGRAM EXECUTION

print('-----------------------------')
print('Welcome To Scrabble ScorePAD!')
print('-----------------------------')
print('When presented with options simply type the number of your choice and hit Enter.\n')

main()