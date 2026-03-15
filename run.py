# IMPORTS
import os
from flask import Flask, render_template, request, redirect, url_for
from data import LETTER_VALUES, scored_words, scores_only
from classes import CheckedString
from styles import yellow, green, white, red, bright, cyan

app = Flask(__name__)


# FUNCTIONS

def string_validator(specified_str):
    """
    Checks firstly that the string is at least two characters long, then that
    the input contains only valid characters. If both are true, further checks
    ensure that the input starts with a letter and only one modifier per letter
    has been indicated. NB: the specific order of these checks is crucial in
    allowing the function to run without exceptions bring raised!
    """
    errors = []
    
    error = check_length(specified_str)
    if error:
        errors.append(error)

    error = check_characters(specified_str)
    if error:
        errors.append(error)

    if not errors:
        error = check_start(specified_str)
        if error:
            errors.append(error)
        error = check_mods(specified_str)
        if error:
            errors.append(error)

    return errors


def check_length(specified_str):
    """
    Checks that the string is at least two characters long.
    """
    if len(specified_str) < 2:
        return 'Input must be at least 2 characters long. Valid words in Scrabble must be 2 to 15 letters in length.'
    return None


def check_characters(specified_str):
    """
    Checks that the string only contains letters and valid modifiers.
    """
    for character in specified_str:
        try:
            LETTER_VALUES[character]
        except Exception:
            return 'Input contains invalid character(s). Only letters and the characters *, 2, or 3 are allowed.'
    return None


def check_start(specified_str):
    """
    Checks that the string starts with a letter.
    """
    if LETTER_VALUES[specified_str[0]] < 1:
        return 'Input must begin with a letter. Modifiers are to be placed AFTER the letter they refer to.'
    return None


def check_mods(specified_str):
    """
    Checks that the string contains max one modifier after each letter.
    """
    for character, next_character in zip(specified_str, specified_str[1:]):
        if LETTER_VALUES[character] + LETTER_VALUES[next_character] < 1:
            return 'Max ONE modifier per letter allowed. If * and 2/3 are applicable, simply enter *.'
    return None


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
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'assets', 'wordlists', wordlist_file)
    with open(file_path, 'r') as wordlist_txt:
        wordlist_txtlist = wordlist_txt.read().splitlines()

    if specified_word in wordlist_txtlist:
        return None
    else:
        message = f'{specified_word.upper()} is not a valid word on this list'
        if len(specified_word) < 2 or len(specified_word) > 15:
            message += ' Valid words in Scrabble must be 2 to 15 letters in length.'
        return message


def evaluate_word(specified_str, specified_word, multiplier, bonus):
    """
    Returns the final score breakdown of the specified string and adds it to
    the scored_words[] list. If the word is not valid, the program will
    continue to the end_menu() function
    """
    if specified_word != 0:
        this_word = CheckedString(specified_str, specified_word)

        this_word.basic = evaluate_letters(specified_str)
        this_word.multiplied = this_word.basic * multiplier
        
        if len(specified_word) < 7:
            this_word.final = this_word.multiplied
        else:
            this_word.final = this_word.multiplied + bonus
            if bonus > 0:
                this_word.bonus = 'Yes'

        this_word.list_append()
        return this_word


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


@app.route('/')
def index():
    return render_template('index.html', scores=scored_words, total_score=sum(scores_only))

@app.route('/score', methods=['POST'])
def score():
    word = request.form['word'].lower()
    wordlist = request.form['wordlist']
    multiplier = int(request.form['multiplier'])
    bonus = 50 if 'bonus' in request.form else 0

    errors = string_validator(word)
    if errors:
        return render_template('index.html', errors=errors, scores=scored_words, total_score=sum(scores_only))

    plain_word = word_extractor(word)
    error = word_validator(wordlist, plain_word)
    if error:
        errors.append(error)
        return render_template('index.html', errors=errors, scores=scored_words, total_score=sum(scores_only))

    scored_word = evaluate_word(word, plain_word, multiplier, bonus)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', 8080)),
            debug=True)
