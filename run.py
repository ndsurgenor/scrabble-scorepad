# Write your code to expect a terminal of 80 characters wide and 24 rows high

def welcome_message():
    """
    Presents the user with an introductory message.
    """
    print('------------------------------')
    print(' WELCOME TO SCRABBLE SCOREPAD')
    print('------------------------------\n')

    print('When presented with options, simply type the number of your choice and hit Enter\n')


def main():
    """
    Run all functions within the program
    """
    welcome_message()


main()