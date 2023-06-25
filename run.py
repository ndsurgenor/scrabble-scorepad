# IMPORTS

from data import LETTER_VALUES, scored_words, scores_only
from classes import CheckedString
from colorama import init, Fore, Style
init(autoreset = True)


# FUNCTIONS

def wordlist_selector():
    """
    Sets the specific wordlist to be used for the purpose of word validation.
    """
    while True:
        print(Fore.YELLOW + Style.BRIGHT + 'Available Wordlists')
        print(Fore.YELLOW + Style.BRIGHT + '1 - EU/World (SWOPODS)')
        print(Fore.YELLOW + Style.BRIGHT + '2 - USA/Canada (TWL06)\n')

        wordlist_value = input(Fore.GREEN + Style.BRIGHT + 'Please indicate which wordlist you require:\n')

        if wordlist_value == '1':
            print(Fore.WHITE + 'Loading EU/WORLD (SWOPODS) wordlist...\n')
            wordlist_file = 'wl-eu-sowpods.txt'
            break
        elif wordlist_value == '2':
            print(Fore.WHITE + 'Loading USA/CANADA (TWL06) wordlist...\n')
            wordlist_file = 'wl-us-twl.txt'
            break
        else:
            print(Fore.RED + Style.BRIGHT + f'Sorry, {wordlist_value.upper()} is not a valid option.\n')
    
    return wordlist_file


def string_validator():
    """
    Checks firstly that the string is at least two characters long, then than the input contains only valid characters.
    If both are true, further checks ensure that the input starts with a letter and only one modifier per letter has been indicated.
    <! NB The specific order of these checks is crucial in allowing the function to run without exceptions bring raised !>
    """
    print(Fore.YELLOW + Style.BRIGHT + 'Word Validation and Scoring')
    print('Please include modifiers for blank tiles (*), double letter (2) or triple ')
    print('letter (3) scores AFTER their respective letters (max ONE modifier per letter; ')
    print('use * over 2 or 3 if both apply). For example, entering W*ORD3S would indicate ')
    print('a blank tile for W and triple letter score on D.\n')

    while True:
        specified_string = (input(Fore.GREEN + Style.BRIGHT + 'Please enter the word (including modifiers) to be checked and scored:\n')).lower()

        if check_length(specified_string) == True:
            if check_characters(specified_string) == True:
                if check_start(specified_string) == check_mods(specified_string) == True: 
                    break
                else:
                    print('')
    
    return specified_string


def check_length(specified_string):
    """
    Checks that the string is at least two characters long.
    """
    if len(specified_string) < 2:
        print(Fore.RED + Style.BRIGHT + f'Input must be at least 2 characters long\n')
        string_valid = False     
    else:
        string_valid = True
    
    return string_valid


def check_characters(specified_string):
    """
    Checks that the string only contains letters and valid modifiers.
    """
    for character in specified_string:
        try:
            LETTER_VALUES[character]
        except:
            print(Fore.RED + Style.BRIGHT + f'Input contains invalid character(s)')
            print('Only letters and the characters *, 2, or 3 are allowed.\n')
            string_valid = False
            break
        else:
            string_valid = True
            continue
    
    return string_valid


def check_start(specified_string):
    """
    Checks that the string starts with a letter.
    """
    if LETTER_VALUES[specified_string[0]] < 1:                  
        print(Fore.RED + Style.BRIGHT + f'Input must begin with a letter')
        print('Modifiers are to be placed AFTER the letter they refer to.')
        string_valid = False 
    else:
        string_valid = True
    
    return string_valid


def check_mods(specified_string):
    """
    Checks that the string contains max one modifier after each letter.
    """
    for character, next_character in zip(specified_string, specified_string[1:]):
        if LETTER_VALUES[character] + LETTER_VALUES[next_character] < 1:
            print(Fore.RED + Style.BRIGHT + 'Max ONE modifier per letter allowed')
            print('If * and 2/3 are applicable, simply enter *.')
            string_valid = False
            break
        else:
            string_valid = True
    
    return string_valid
   

def word_extractor(specified_string):
    """
    Removes modifiers from the input string in order to read the specified word.
    """
    specified_word = ''
    
    for character in specified_string:
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
        print(Fore.WHITE + f'The word {specified_word.upper()} is valid!\n')
    else:
        print(Fore.RED + Style.BRIGHT + f'Sorry, {specified_word.upper()} is not a valid word on this list.\n')
        specified_word = 0  #tells the next function that no score is to be evaluted
    
    wordlist_txt.close()
    return specified_word


def evaluate_word(specified_string, specified_word):
    """
    Returns the final score breakdown of the specified string and adds it to the scored_words[] list.
    If the word is not valid, the program will continue to the end_menu() function.
    """
    if specified_word != 0:
        this_word = CheckedString(specified_string, specified_word)

        this_word.basic = evaluate_letters(specified_string)
        this_word.multiplied = evaluate_multiplier(this_word.basic)
        if len(specified_word) < 7:
            this_word.final = this_word.multiplied
        else:
            this_word.final = evaluate_bonus(this_word.multiplied)
            if this_word.final > this_word.multiplied:
                this_word.bonus = 'Yes'
            
        this_word.score_breakdown()
        this_word.list_append()


def evaluate_letters(specified_string):
    """
    Calculates the letter score taking modifiers into account.
    """
    specified_string = specified_string + '!' #Ensures the final character of the original string is evaluated.
    word_score = 0

    for character, next_character in zip(specified_string, specified_string[1:]):
        if next_character == '*':
            individual_value = 0
        elif next_character == '2' or next_character == '3':
            individual_value = LETTER_VALUES[character] * int(next_character)
        else:
            individual_value = LETTER_VALUES[character]

        word_score = word_score + individual_value
            
    return word_score


def evaluate_multiplier(word_score):
    """
    Multiplies the word score, if appropriate.
    """
    while True:
        print(Fore.YELLOW + Style.BRIGHT + 'Any Double or Triple word score?')
        print(Fore.YELLOW + Style.BRIGHT + '1 - None')
        print(Fore.YELLOW + Style.BRIGHT + '2 - Double')
        print(Fore.YELLOW + Style.BRIGHT + '3 - Triple')
        print(Fore.YELLOW + Style.BRIGHT + '4 - Double x2')
        print(Fore.YELLOW + Style.BRIGHT + '5 - Triple x2')
        print(Fore.YELLOW + Style.BRIGHT + '6 - Triple x3\n')

        multiplier = input(Fore.GREEN + Style.BRIGHT + 'Please select an option:\n')

        try:
            int(multiplier)
        except:
            print(Fore.RED + Style.BRIGHT + f'Sorry, {multiplier.upper()} is not a valid option.\n')
        else:
            if int(multiplier) in range (1,7):
                break
            else:
               print(Fore.RED + Style.BRIGHT + f'Sorry, {multiplier.upper()} is not a valid option.\n') 

    if int(multiplier) == 1:
        print(Fore.WHITE + 'No multiplier to be applied\n')
    else:
        if int(multiplier) > 4:
            multiplier = (3 * int(multiplier)) - 9 # Converts input 5 or 6 to 6/9 respectively

        print(Fore.WHITE + f'Multiplying word score by {multiplier}...\n')
        word_score = word_score * int(multiplier)

    return word_score


def evaluate_bonus(word_score):
    """
    Adds a bonus to the final score, if appropriate.
    """
    while True:
        print(Fore.YELLOW + Style.BRIGHT + 'All tiles played on this turn?')
        print(Fore.YELLOW + Style.BRIGHT + "NB: Only select 'Yes' once if scoring multiple words per turn")
        print(Fore.YELLOW + Style.BRIGHT + '1 - Yes')
        print(Fore.YELLOW + Style.BRIGHT + '2 - No\n')

        bonus = input(Fore.GREEN + Style.BRIGHT + 'Please select an option:\n').lower()

        if bonus == '1' or bonus == 'yes' or bonus == 'y':
            print(Fore.WHITE + 'Adding bonus...\n')
            word_score = word_score + 50         
            break
        elif bonus == '2' or bonus == 'no' or bonus == 'n':
            print(Fore.WHITE + 'No bonus to be applied\n')
            break
        else:
            print(Fore.RED + Style.BRIGHT + f'Sorry, {bonus.upper()} is not a valid option.\n')

    return word_score


def end_menu(wordlist_file):
    """
    Allows the user to either check another word or end the program.
    """
    while True:
        print(Fore.YELLOW + Style.BRIGHT + 'Options:')
        print(Fore.YELLOW + Style.BRIGHT + '1 - Score another word')
        print(Fore.YELLOW + Style.BRIGHT + '2 - Change wordlist')
        print(Fore.YELLOW + Style.BRIGHT + '3 - Total score statistics')
        print(Fore.YELLOW + Style.BRIGHT + '4 - Close program\n')

        option_value = input(Fore.GREEN + Style.BRIGHT + 'Please indicate which option you require:\n')

        if option_value == '1':
            print(Fore.WHITE + 'Loading validator... \n')
            main(wordlist_file)
            break
        elif option_value == '2':
            print(Fore.WHITE + 'Loading wordlists... \n')
            wordlist_file = 'notset'
            main(wordlist_file)
            break
        elif option_value == '3':
            print(Fore.WHITE + 'Loading scores... \n')
            score_stats()
        elif option_value == '4':
            print(Fore.WHITE + 'Closing program... \n')
            print(Fore.CYAN + Style.BRIGHT + '--------------------------------------')
            print(Fore.CYAN + Style.BRIGHT + 'Thank you for using Scrabble ScorePAD!')
            print(Fore.CYAN + Style.BRIGHT + '--------------------------------------\n')
            break
        else:
            print(Fore.RED + Style.BRIGHT + f'Sorry, {option_value.upper()} is not a valid option.\n')


def score_stats():
    """
    Displays the individual and total score of all valid words input by the user.
    """
    print ('D/T = double/triple')
    print ('B = bonus\n')
    print(Fore.CYAN + Style.BRIGHT + '--- SCORED WORDS ---')
    
    num = 0    
    for item in scored_words:
        num = num + 1
        print (Fore.WHITE + Style.BRIGHT + f'{num}. {item}')

    total = 0    
    for item in scores_only:
        total = total + item

    print('')    
    print(Fore.CYAN + Style.BRIGHT + f'TOTAL SCORE = {total}\n')


def main(wordlist):
    """
    Runs all top level functions within the program.
    """
    if wordlist == 'notset':
        wordlist = wordlist_selector()

    string = string_validator()
    word = word_extractor(string)
    valid_word = word_validator(wordlist, word)
    score = evaluate_word(string, valid_word)
    end_menu(wordlist)
    

# PROGRAM EXECUTION

print(Fore.CYAN + Style.BRIGHT + '-----------------------------')
print(Fore.CYAN + Style.BRIGHT + 'Welcome To Scrabble ScorePAD!')
print(Fore.CYAN + Style.BRIGHT + '-----------------------------')
print('When presented with options simply type the number of your choice and hit Enter.\n')

wordlist_file = 'notset'
main(wordlist_file)