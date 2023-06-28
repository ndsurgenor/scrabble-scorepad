# IMPORTS

from data import scored_words, scores_only
from styles import bright, cyan


# CLASSES

class CheckedString:
    """
    Records various score attributes of the input string.
    """

    def __init__(self, string, word):
        """
        Initialises attributes within the class
        """
        self.string = string
        self.word = word
        self.basic = 0
        self.factor = 'n/a'
        self.multiplied = 0
        self.bonus = 'No'
        self.final = 0

    def score_breakdown(self):
        """
        Gives the score breakdown for a particular string
        """
        if self.multiplied/self.basic > 1:
            self.factor = f'x{int(self.multiplied/self.basic)}'

        print(cyan + f'The final score for {self.word.upper()} is as follows:')
        print(bright + f'--- {self.string.lower()} ---')
        print(bright + f'Letter score = {self.basic}')
        print(bright + f'Multiplied score ({self.factor}) = {self.multiplied}')
        print(bright + f'Bonus (+50) = {self.bonus}')
        print(bright + f'FINAL WORD SCORE = {self.final}\n')

    def list_append(self):
        """
        Adds the score, string, and word values to their respective lists
        """
        scores_only.append(self.final)
        word_multiplier = self.multiplied/self.basic
        wrd = self.word.upper()
        stg = self.string.lower()

        if word_multiplier == 1 and self.bonus == 'No':
            scored_words.append(f'{wrd} [{stg}] = {self.final}')
        else:
            if word_multiplier == 2 or word_multiplier == 4:
                mul = 'D' * int(word_multiplier / 2)
            elif word_multiplier % 3 == 0:
                mul = 'T' * int(word_multiplier / 3)

            if self.bonus == 'Yes':
                bon = 'B'
            else:
                bon = ''

            scored_words.append(f'{wrd} [{stg} {mul}{bon}] = {self.final}')
