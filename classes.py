# IMPORTS

from data import scored_words, scores_only
from colorama import init, Fore, Style


# CLASSES

class CheckedString:
    """
    Records various score attributes of the input string.
    """
    def __init__(self, string, word):
        self.string = string
        self.word = word
        self.basic = 0
        self.factor = 'n/a'
        self.multiplied = 0
        self.m_indicator = ''        
        self.bonus = 'No'
        self.b_indicator = ''
        self.final = 0       


    def score_breakdown(self):
        """
        Gives the score breakdown for a particular string.
        """
        if self.multiplied/self.basic > 1:
            self.factor = f'x{int(self.multiplied/self.basic)}'

        print(Fore.CYAN + Style.BRIGHT + f'The final score for {self.word.upper()} is as follows:')
        print(Style.BRIGHT + f'--- {self.string.lower()} ---')
        print(Style.BRIGHT + f'Letter score = {self.basic}')
        print(Style.BRIGHT + f'Multiplied score ({self.factor}) = {self.multiplied}')
        print(Style.BRIGHT + f'Bonus (+50) = {self.bonus}')
        print(Style.BRIGHT + f'FINAL WORD SCORE = {self.final}\n')


    def list_append(self):        
        """
        Adds the score, string, and word values to their respective lists for recall.
        """
        scores_only.append(self.final)

        if self.multiplied/self.basic == 1 and self.bonus == 'No':
            scored_words.append(f'{self.word.upper()} [{self.string.lower()}] = {self.final}')
        else:
            if self.multiplied/self.basic == 2:
                self.m_indicator = 'D'
            elif self.multiplied/self.basic == 3:
                self.m_indicator = 'T'

            if self.bonus == 'Yes':
                self.b_indicator = 'B'

            scored_words.append(f'{self.word.upper()} [{self.string.lower()} {self.m_indicator}{self.b_indicator}] = {self.final}')     