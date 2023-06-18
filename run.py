# IMPORTED LIBRARIES

from letters import LETTER_VALUES
from colorama import init, Fore, Style
init(autoreset = True)


# CLASSES

class CheckedWord:
    """
    Records various score attributes of the specified word.
    """
    def __init__(self, name, basic, multiplied, bonus, final):
        self.name = name
        self.basic = basic
        self.multiplied = multiplied
        self.bonus = bonus
        self.final = final

    def score_breakdown(self):
        print(Style.BRIGHT + f'The score breakdown for {self.name.upper()} is as follows:')
        print(Style.BRIGHT + f'Basic score = {self.basic}')
        print(Style.BRIGHT + f'Multiplied score = {self.multiplied}')
        print(Style.BRIGHT + f'Bonus (+50) applied = {self.bonus}')
        print(Style.BRIGHT + f'FINAL WORD SCORE = {self.final}\n')


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
            wordlist_txt = open('wl-eu-sowpods.txt', 'r')
            break
        elif wordlist_value == '2':
            print(Fore.WHITE + 'Loading USA/CANADA (TWL06) wordlist...\n')
            wordlist_txt = open('wl-us-twl.txt', 'r')
            break
        else:
            print(Fore.RED + Style.BRIGHT + f'Sorry, {wordlist_value.upper()} is not a valid option.\n')
    
    return wordlist_txt


def string_validator(wordlist_txt):
    """
    Checks that the string entered is at least two characters long,
    does not contain invalid characters, and only one modifier per letter has been indicated.
    """
    print(Fore.YELLOW + Style.BRIGHT + 'Word Validation and Scoring')
    print('Please include modifiers for blank tiles (*), double letter (2) or triple ')
    print('letter (3) scores AFTER their respective letters (max ONE modifier per letter; ')
    print('use * over 2 or 3 if both apply). For example, entering W*ORD3S would indicate ')
    print('a blank tile for W and triple letter score on D.\n')

    while True:
        specified_string = (input(Fore.GREEN + Style.BRIGHT + 'Please enter the word (including modifiers) to be checked and scored:\n')).lower()

        if len(specified_string) > 1:
                     
            for character, next_character in zip(specified_string, specified_string[1:]):
                try:
                    LETTER_VALUES[character] and LETTER_VALUES[next_character]
                except:
                    print(Fore.RED + f'Input contains invalid character(s)')
                    print('Only letters and the characters *, 2, or 3 are allowed.\n')
                    string_valid = False
                    break
                else:
                    if LETTER_VALUES[character] + LETTER_VALUES[next_character] < -1:
                        print(Fore.RED + 'Max ONE modifier per letter allowed.\n')
                        string_valid = False
                        break
                    else:
                        string_valid = True
                        continue

            if string_valid == True:
                break
        else:
            print(Fore.RED + f'Input must be at least 2 characters long.\n')
    
    return specified_string


def word_validator(specified_string):
    """
    Checks that the word is contained within the selected wordlist.
    """
    specified_word = word_extractor(specified_string)

    if specified_word in wordlist_txt.read():
        print(Fore.WHITE + f'The word {specified_word.upper()} is valid!\n')
    else:
        print(Fore.RED + Style.BRIGHT + f'Sorry, {specified_word.upper()} is not a valid word on this list.\n')
        specified_word = 0  #tells the next function that no score is to be evaluted
    
    wordlist_txt.close()
    return specified_word


def word_extractor(specified_string):
    """
    Removes any modifiers from the input string.
    """
    for character in specified_string:

        specified_word = specified_word + character

    return specified_word


def evaluate_word(specified_word):
    """
    Returns the score breakdown and final score of the specified word.
    If the word is not valid, the program will continue to the end_menu() function.
    """
    if specified_word != 0:
        this_word = CheckedWord(specified_word,0,0,'No',0) #creates an instance of the CheckedWord class

        this_word.basic = evaluate_letters(specified_word)
        this_word.multiplied = evaluate_multiplier(this_word.basic)
        if len(specified_word) < 7:
            this_word.bonus = 'No'
            this_word.final = this_word.multiplied
        else:
            this_word.bonus = 'Yes'
            this_word.final = evaluate_bonus(this_word.multiplied)
            
        this_word.score_breakdown()


def evaluate_letters(specified_word):
    """
    Calculates the letter score including specified modifiers.
    """
    word_score = 0

    for letter in specified_word:
        individual_value = LETTER_VALUES.get(letter)
        word_score = word_score + individual_value

    return word_score


def evaluate_multiplier(word_score):
    """
    Multiplies the letter score, if appropriate.
    """
    while True:
        print(Fore.YELLOW + Style.BRIGHT + 'Any Double or Triple word score?')
        print(Fore.YELLOW + Style.BRIGHT + '1 - None')
        print(Fore.YELLOW + Style.BRIGHT + '2 - Double')
        print(Fore.YELLOW + Style.BRIGHT + '3 - Triple\n')

        multiplier = input(Fore.GREEN + Style.BRIGHT + 'Please select an option:\n').lower()

        if multiplier == '1' or multiplier == 'none' or multiplier == 'n':
            print(Fore.WHITE + 'No multiplier to be applied\n')
            break
        elif multiplier == '2' or multiplier == 'double' or multiplier == 'd':
            print(Fore.WHITE + 'Doubling word score...\n')
            word_score = word_score * 2
            break
        elif multiplier == '3' or multiplier == 'triple' or multiplier == 't':
            print(Fore.WHITE + 'Tripling word score...\n')
            word_score = word_score * 3
            break
        else:
            print(Fore.RED + Style.BRIGHT + f'Sorry, {multiplier.upper()} is not a valid option.\n')

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


def end_menu():
    """
    Allows the user to either check another word or end the program.
    """
    while True:
        print(Fore.YELLOW + Style.BRIGHT + 'Options:')
        print(Fore.YELLOW + Style.BRIGHT + '1 - Score another word')
        print(Fore.YELLOW + Style.BRIGHT + '2 - Close program\n')

        option_value = input(Fore.GREEN + Style.BRIGHT + 'Please indicate which option you require:\n')

        if option_value == '1':
            main()
            break
        elif option_value == '2':
            print(Fore.WHITE + 'Closing program... \n')
            print(Fore.CYAN + Style.BRIGHT + '--------------------------------------')
            print(Fore.CYAN + Style.BRIGHT + 'Thank you for using Scrabble ScorePad!')
            print(Fore.CYAN + Style.BRIGHT + '--------------------------------------\n')
            break
        else:
            print(Fore.RED + Style.BRIGHT + f'Sorry, {option_value.upper()} is not a valid option.\n')


def main():
    """
    Runs all top level functions within the program.
    """
    wordlist = wordlist_selector()
    string = string_validator(wordlist)
    # word = word_validator(string)
    # score = evaluate_word(word)
    # end_menu()
    

# PROGRAM EXECUTION

print(Fore.CYAN + Style.BRIGHT + '-----------------------------')
print(Fore.CYAN + Style.BRIGHT + 'Welcome To Scrabble ScorePAD!')
print(Fore.CYAN + Style.BRIGHT + '-----------------------------')
print('When presented with options simply type the number of your choice and hit Enter.\n')

main()