# IMPORTS

from data import LETTER_VALUES, scored_words, scores_only
from classes import CheckedString
from styles import yellow, green, white, red, bright, cyan


# FUNCTIONS

def wordlist_selector():
    """
    Sets the specific wordlist to be used for the purpose of word validation.
    """
    while True:
        print(yellow + 'Available Wordlists')
        print(yellow + '1 - EU/World (SWOPODS)')
        print(yellow + '2 - USA/Canada (TWL06)\n')

        wordlist_value = input(green + 'Please select a wordlist:\n')

        if wordlist_value == '1':
            print(white + 'Loading EU/WORLD (SWOPODS) wordlist...\n')
            wordlist_file = 'wl-eu-sowpods.txt'
            break
        elif wordlist_value == '2':
            print(white + 'Loading USA/CANADA (TWL06) wordlist...\n')
            wordlist_file = 'wl-us-twl.txt'
            break
        else:
            print(red + f'{wordlist_value.upper()} is not a valid option\n')

    return wordlist_file


def string_validator():
    """
    Checks firstly that the string is at least two characters long, then that
    the input contains only valid characters. If both are true, further checks
    ensure that the input starts with a letter and only one modifier per letter
    has been indicated. NB: the specific order of these checks is crucial in
    allowing the function to run without exceptions bring raised!
    """
    print(yellow + 'Word Validation and Scoring')
    print('Please include modifiers for blank tiles (*), double letter (2) or')
    print('triple letter (3) scores AFTER their respective letters (max ONE')
    print('modifier per letter; use * over 2/3 if both apply). For example,')
    print('entering W*ORD3S would indicate a blank tile for W')
    print('and a triple score on D.\n')

    while True:
        specified_str = (input(
            green + 'Enter word (+modifiers) to be checked/scored:\n')).lower()

        if check_length(specified_str):
            if check_characters(specified_str):
                if check_start(specified_str) and check_mods(specified_str):
                    break
                else:
                    print('')

    return specified_str


def check_length(specified_str):
    """
    Checks that the string is at least two characters long.
    """
    if len(specified_str) < 2:
        print(red + f'Input must be at least 2 characters long')
        print('Valid words in Scrabble must be 2 to 15 letters in length.\n')
        string_valid = False
    else:
        string_valid = True

    return string_valid


def check_characters(specified_str):
    """
    Checks that the string only contains letters and valid modifiers.
    """
    for character in specified_str:
        try:
            LETTER_VALUES[character]
        except ValueError:
            print(red + f'Input contains invalid character(s)')
            print('Only letters and the characters *, 2, or 3 are allowed.\n')
            string_valid = False
            break
        else:
            string_valid = True
            continue

    return string_valid


def check_start(specified_str):
    """
    Checks that the string starts with a letter.
    """
    if LETTER_VALUES[specified_str[0]] < 1:
        print(red + f'Input must begin with a letter')
        print('Modifiers are to be placed AFTER the letter they refer to.')
        string_valid = False
    else:
        string_valid = True

    return string_valid


def check_mods(specified_str):
    """
    Checks that the string contains max one modifier after each letter.
    """
    for character, next_character in zip(specified_str, specified_str[1:]):
        if LETTER_VALUES[character] + LETTER_VALUES[next_character] < 1:
            print(red + 'Max ONE modifier per letter allowed')
            print('If * and 2/3 are applicable, simply enter *.')
            string_valid = False
            break
        else:
            string_valid = True

    return string_valid


def word_extractor(specified_str):
    """
    Removes modifiers from input string to read the specified word
    """
    specified_word = ''

    for character in specified_str:
        if LETTER_VALUES[character] > 0:
            specified_word = str(specified_word + character)

    return specified_word


def word_validator(wordlist_file, specified_word):
    """
    Checks that the word is contained within the selected wordlist.
    """
    wordlist_txt = open('assets/wordlists/' + wordlist_file, 'r')
    wordlist_txtlist = (wordlist_txt.read()).split('\n')

    if specified_word in wordlist_txtlist:
        print(white + f'The word {specified_word.upper()} is valid!\n')
    else:
        print(
            red + f'{specified_word.upper()} is not a valid word on this list')
        if len(specified_word) < 2 or len(specified_word) > 15:
            print('Valid words in Scrabble must be 2 to 15 letters in length.')
        print('')
        specified_word = 0  # tells the next function to not evaluate a score

    wordlist_txt.close()
    return specified_word


def evaluate_word(specified_str, specified_word):
    """
    Returns the final score breakdown of the specified string and adds it to
    the scored_words[] list. If the word is not valid, the program will
    continue to the end_menu() function
    """
    if specified_word != 0:
        this_word = CheckedString(specified_str, specified_word)

        this_word.basic = evaluate_letters(specified_str)
        this_word.multiplied = evaluate_multiplier(
            specified_word, this_word.basic)
        if len(specified_word) < 7:
            this_word.final = this_word.multiplied
        else:
            this_word.final = evaluate_bonus(this_word.multiplied)
            if this_word.final > this_word.multiplied:
                this_word.bonus = 'Yes'

        this_word.score_breakdown()
        this_word.list_append()


def evaluate_letters(specified_str):
    """
    Calculates the letter score taking modifiers into account.
    NB: The '!' added to the string in the first step is essential
    to ensuring the final character of the input is evaluated correctly
    """
    specified_str = specified_str + '!'
    word_score = 0

    for character, next_character in zip(specified_str, specified_str[1:]):
        if next_character == '*':
            individual_value = 0
        elif next_character == '2' or next_character == '3':
            individual_value = LETTER_VALUES[character] * int(next_character)
        else:
            individual_value = LETTER_VALUES[character]

        word_score = word_score + individual_value

    return word_score


def evaluate_multiplier(specified_word, word_score):
    """
    Multiplies the word score, if appropriate.
    """
    upper_limit = 4

    while True:
        print(yellow + 'Any Double or Triple word score?')
        print(yellow + '1 - None')
        print(yellow + '2 - Double')
        print(yellow + '3 - Triple')
        if len(specified_word) > 6:
            print(yellow + '4 - Double x2')
            upper_limit = 5
        if len(specified_word) > 7:
            print(yellow + '5 - Triple x2')
            upper_limit = 6
        if len(specified_word) == 15:
            print(yellow + '6 - Triple x3')
            upper_limit = 7
        print('')

        multiplier = input(green + 'Please select an option:\n')

        try:
            int(multiplier)
        except ValueError:
            print(red + f'{multiplier.upper()} is not a valid option.\n')
        else:
            if int(multiplier) in range(1, upper_limit):
                break
            else:
                print(red + f'{multiplier.upper()} is not a valid option.\n')

    if int(multiplier) == 1:
        print(white + 'No multiplier to be applied\n')
    else:
        if int(multiplier) == 5:
            multiplier = 6
        elif int(multiplier) == 6:
            multiplier = 9

        print(white + f'Multiplying word score by {multiplier}...\n')
        word_score = word_score * int(multiplier)

    return word_score


def evaluate_bonus(word_score):
    """
    Adds a bonus to the final score, if appropriate.
    """
    while True:
        print(yellow + 'All tiles played on this turn?')
        print("Only select 'Yes' once if scoring multiple words per turn\n")
        print(yellow + '1 - Yes')
        print(yellow + '2 - No\n')

        bonus = input(green + 'Please select an option:\n').lower()

        if bonus == '1' or bonus == 'yes' or bonus == 'y':
            print(white + 'Adding bonus...\n')
            word_score = word_score + 50
            break
        elif bonus == '2' or bonus == 'no' or bonus == 'n':
            print(white + 'No bonus to be applied\n')
            break
        else:
            print(red + f'Sorry, {bonus.upper()} is not a valid option.\n')

    return word_score


def end_menu(wordlist_file):
    """
    Allows the user to either check another word or end the program.
    """
    while True:
        print(yellow + 'Options:')
        print(yellow + '1 - Score another word')
        print(yellow + '2 - Change wordlist')
        print(yellow + '3 - Total score statistics')
        print(yellow + '4 - Close program\n')

        option_value = input(green + 'Please select an option:\n')

        if option_value == '1':
            print(white + 'Loading validator... \n')
            main(wordlist_file)
            break
        elif option_value == '2':
            print(white + 'Loading wordlists... \n')
            wordlist_file = 'notset'
            main(wordlist_file)
            break
        elif option_value == '3':
            print(white + 'Loading scores... \n')
            score_stats()
        elif option_value == '4':
            print(white + 'Closing program... \n')
            print(cyan + '--------------------------------------')
            print(cyan + 'Thank you for using Scrabble ScorePAD!')
            print(cyan + '--------------------------------------\n')
            break
        else:
            print(red + f'{option_value.upper()} is not a valid option.\n')


def score_stats():
    """
    Displays the individual and total score
    of all valid words input by the user
    """
    print('D/T = double/triple')
    print('B = bonus\n')
    print(cyan + '--- SCORED WORDS ---')

    num = 0
    for item in scored_words:
        num = num + 1
        print(white + bright + f'{num}. {item}')

    total = 0
    for item in scores_only:
        total = total + item

    print('')
    print(cyan + f'TOTAL SCORE = {total}\n')


def main(wordlist):
    """
    Runs all top level functions within the program.
    """
    if wordlist == 'notset':
        wordlist = wordlist_selector()

    string = string_validator()
    word = word_extractor(string)
    valid_word = word_validator(wordlist, word)
    evaluate_word(string, valid_word)
    end_menu(wordlist)


# PROGRAM EXECUTION

print(cyan + '-----------------------------')
print(cyan + 'Welcome To Scrabble ScorePAD!')
print(cyan + '-----------------------------')
print('When options appear type the number of your choice and hit Enter\n')

wordlist_file = 'notset'
main(wordlist_file)
