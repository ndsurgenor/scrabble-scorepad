# Scrabble ScorePAD

Scrabble ScorePAD is an application designed to help validate and score words during a game of Scrabble.

[LIVE LINK TO SITE](https://scrabble-scorepad.herokuapp.com/)

The main aims of the application are as follows:
- To provide a helpful and intuitive app for scoring Scrabble which runs in a basic python terminal inside a browser window
- To allow the user to ensure that a word played is valid for the particular Scrabble wordlist they are using
- To allow the user to easily indicate blank tiles, double/triple letter/word scores and 'bingo' bonuses as they score each word
- To keep track of all words played and provide a running total of their scores

![Overview](assets/images/overview.png)

## Initial Development

With these aims in mind, the following flowchart was drawn up as blueprint for writing the program, breaking down the various stages of input, decision, logic and function. The diagram was created using the chart design site [Lucid](https://lucid.app/lucidchart/db42b587-b151-4fc3-8d91-86050208ea20/edit?viewport_loc=-227%2C56%2C2938%2C1533%2C0_0&invitationId=inv_cbd12e3b-9927-4e6d-a169-3cadd1183444)

![Flowchart](assets/images/flowchart.png)

As development of the program progressed various new checks and functions were added into what is shown above, but this diagram provided a good starting point for the initial writing of the code.

## How To Use The Program

1. When presented with a list of options simply type the relevant number and hint 'Enter' on the keyboard
2. Firstly, one of two initial offical Scrabble lists must be selected, then the user can enter the first word for scoring
3. The word to be checked should be entered along with any indication of blank tiles used and/or double/triple letter scores:
- Use '*' after a letter to indicate the tile is blank
- Use '2' after a letter to indicate a double letter score
- Use '3' after a letter to indicate a double letter score
- If a blank tile and double/triple letter score appear togrther simply use '*'
4. The input will be checked to ensure it is valid and that the word appears on the previously selected wordlist
5. The user will then be offered the oppurtunity to indicate a double/triple word score and 'bingo' (all tiles used) bonus, if applicable
6. Once all scoring types have been indicated, the final score and breakdown is presented to the user
7. The user is then presented with the option of scoring another word, changing the wordlist, showing a full list of words scored or closing the program
8. The program will run and continue to score words/keep score until the user chooses to close the program 

## Features 

### Page Layout & Styling

__Tab, Title & Background__

- A favicon is included as part of the tab styling, taking the form of an 'S' tile found in Scrabble.
- The title is placed at the top of the page above the terminal to clearly indicate the program in use.
- Clicking the title will not refresh/redirect the page as this would interrupt the program.
- No navigation bar is provided as this site has a one-page focus; interaction occurs through means of the terminal.
- A background image of a Scrabble board empasises the theme of the program and helps with eye strain , preventing a dark terminal on a bright background

![Main Page](assets/images/mainpage.png)

__Terminal Formatting__

- Text within the terminal has been coloured to help with readibility and information perception:
  - <span style='color:cyan'>Cyan</span> is used for main headings such as the welcome/closing messages.
  - <span style='color:yellow'>Yellow</span> is used for menu headings and their options.
  - <span style='color:lightgreen'>Green</span> is used for those times user input is required.
  - <span style='color:red'>Red</span> is used for error messages.
  - <span style='color:white'>White</span> is used for all other pieces of informational text.

![Terminal](assets/images/terminal.png)

__'Run Program' Button__

- A button is placed below the terminal as a means of restarting the program after it ends or in the event of an error.
- The button is styled with hover elements to provide feedback to the user.

![Button](assets/images/button.png)

### Program Features

__Wordlist Selection__
- The user has the option of selecting one of two official Scrabble wordlists
- This allows casual/tournament players and those from different regions to make use of the program
- Any invalid data entry is noted by the program and notice is given to the user

![Wordlist Selection](assets/images/2-1.png)

__Word & Modifier Input__
- After selecting the relevant wordlist, the word to be checked/scored is entered
- At this point the user also indicates blank tiles and/or double/triple letter scores
- Asking for input of letters and modifiers together keeps data-string entry to a minimum
- Any invalid data entry is noted by the program and notice is given to the user
- Specifically, the following errors will be caught and require correction before proceeding:
  - Data entry less than two chracters long (no one-letter words exist on Scrabble lists)
  - Data entry that contains invalid charcters (only letters and *,2,3 permitted)
  - More than one modifier indicated beside a letter (blank takes precedence over double/triple)
  - Data entry that begins with a modifier (modifiers are to be placed after letters)
- Valid inputs have their letter values taken from an in-built dictionary and are ignored/doubled/tripled where appropriate

![Input](assets/images/3-1.png)

__Word Validation__
- Any modifiers entered in the previous step are ommitted by the proram so the word can be read correctly
- The program checks to see if the word entered appears on the previously selected wordlist
- If an invalid word is entered the user is notified and the end program menu is presented
- A valid word causes the program to proceed to the final checks before scoring

![Invalid](assets/images/3-9.png)
![Valid](assets/images/3-8.png)

__Multiplier menu__
- If a valid word is entered, options for double/triple word scores are presented
- Certain options will only appear depending on word length given the layout of an official Scrabble board
  - Words < 7 letters can only have a single double/triple word score
  - Words of 7+ letters also have a double x2 option
  - Words of 8+ letters also have a triple x2 option
  - Words of 15 letters have a triple x3 option
- Any double/triple score selected is apllied to the base value of the word from the previous step

![Multipliers](assets/images/4-4.png)

__Bonus Menu__
- Allows for scoring of ‘bingo’
- Only appears as an option if word is seven letters or longer

__End Of Program Menu__
- Various options to benefit the user experience
- User can immediately score a new word without the need to change wordlist
- User can change wordlist before scoring again
- User can view all words scored so far, including their individual scores and total
- User can safely exit the program when finished

__Total Score Screen__
- Shows all words scored up to that point
- Displays the word, string entered, any extra scoring and the final score for each word
- Also shows the total score of all words up to that point

### Features to Implement

! TO BE ADDED !

<!-- The following are ideas which can be implemented into the site at a later time (when skillset allows):
- Add the ability to save high-scores and usernames to a back-end server allowing users to compare their scores with all visitors to the site.
- Add keyboard navigation for desktop users allowing them to move around the grid using WASD/arrow keys and select blocks using Spacebar. -->

## Testing

The following tests have been run on each part of the program to ensure that it is operating as expected:

`Initial Startup`
| Feature | Test | Input(s) | Expected | Result | Display | Pass/Fail |
|-|-|-|-|-|-|-|
| Welcome Message | Run program | <span style='color:gray'>n/a</span> | Welcome message showing program is running | Welcome message displayed as expected | ![1-1](assets/images/1-1.png) | Pass |

`Wordlist Selection`
| Feature | Test | Input(s) | Expected | Result | Display | Pass/Fail |
|-|-|-|-|-|-|-|
| Wordlist Menu | Run program | <span style='color:gray'>n/a</span> | Menu showing options '1 - EU/Word (SOWPODS), 2 - US/Canada (TWL06)' awaiting input from user | Options and input request displayed as expected | ![2-1](assets/images/2-1.png) | Pass |
| Wordlist Selection | <span style='color:lightgreen'>Valid input</span> | 1</br>2 | Confirmation message referencing chosen wordlist |  Confirmation message displayed as expected | ![2-2](assets/images/2-2.png)<br/>![2-3](assets/images/2-3.png) | Pass |
| Wordlist Selection | <span style='color:tomato'>Invalid inputs:</br><1</br>>2</br>String</span> | 0</br>3</br>6y75er | Error message referencing input and redisplaying of valid options | Error message and repeat of options menu displayed as expected | ![2-4](assets/images/2-4.png)<br/>![2-5](assets/images/2-5.png)<br/>![2-6](assets/images/2-6.png) | Pass |

`Word & Modifier Input`
| Feature | Test | Input(s) | Expected | Result | Display | Pass/Fail |
|-|-|-|-|-|-|-|
| Word Validation Instruction | Run program | <span style='color:gray'>n/a</span> | Message showing input instructions, awaiting input from user | Message and input request displayed as expected | ![3-1](assets/images/3-1.png) | Pass |
| Word Input | <span style='color:lightgreen'>Letters only</span> | rainbow | Confirmation message showing word (capitilised) as valid | Confirmation message displayed as expected | ![3-2](assets/images/3-2.png) | Pass |
| Word Input | <span style='color:lightgreen'>Letters with valid modifiers</span> | r2ain*bow3 | Confirmation message showing word without modifiers (capitilised) as valid | Confirmation message displayed as expected | ![3-3](assets/images/3-3.png) | Pass |
| Word Input | <span style='color:tomato'>Invalid characters</span> | rai4nbow | Error message giving detail of invalid characters and a reminder of what is allowed | Error message displyed as expected | ![3-4](assets/images/3-4.png) | Pass |
| Word Input | <span style='color:tomato'><2 characters</span> | a | Error message explaining words must be at least 2 letters long | Error message displyed as expected | ![3-5](assets/images/3-5.png) | Pass |
| Word Input | <span style='color:tomato'>Opening modifier</span> | 2rainbow | Error message explaining input must begin with a letter | Error message displyed as expected | ![3-6](assets/images/3-6.png) | Pass |
| Word Input | <span style='color:tomato'>>2 modifiers on one letter</span> | rain*3bow | Error message explaining only one modifier per letter is allowed | Error message displyed as expected | ![3-7](assets/images/3-7.png) | Pass |
| Word Validator | <span style='color:lightgreen'>Valid word entered</span> | colorise [EU wordlist] | Confirmation message showing word (capitilised) as valid | Confirmation message displayed as expected | ![3-8](assets/images/3-8.png) | Pass |
| Word Validator | <span style='color:tomato'>Invalid word entered</span> | colorise [US wordlist] | Error message showing word (capitilised) as invalid for particular list | Error message displyed as expected | ![3-9](assets/images/3-9.png) | Pass |

`Double/Triple Score Indication`
| Feature | Test | Input(s) | Expected | Result | Display | Pass/Fail |
|-|-|-|-|-|-|-|
| Double/Triple Score Menu | Word <7 letters length | object | Menu showing options '1 - None, 2 - Double, 3 - Triple' awaiting input from user | Specified options and input request displayed as expected | ![4-1](assets/images/4-1.png) | Pass |
| Double/Triple Score Menu | Word 7 letters length | objects | Menu showing all options above plus '4 - Double x2' along with input request from user | Specified options and input request displayed as expected | ![4-2](assets/images/4-2.png) | Pass |
| Double/Triple Score Menu | Word 8-14 letters length | objectify | Menu showing all options above plus '5 - Triple x2' along with input request from user | Specified options and input request displayed as expected | ![4-3](assets/images/4-3.png) | Pass |
| Double/Triple Score Menu | Word 15 letters length | objectification | Menu showing all options above plus '6 - Triple x3' along with input request from user | Specified options and input request displayed as expected | ![4-4](assets/images/4-4.png) | Pass |
| Multiplier Selection | <span style='color:lightgreen'>Valid inputs</span> | 1</br>2</br>3</br>4</br>5</br>6 | Confirmation message showing multiplication factor specific to chosen option | Confirmation and correct multiplication factor displayed as expected | ![4-5](assets/images/4-5.png)</br>![4-6](assets/images/4-6.png)</br>![4-7](assets/images/4-7.png)</br>![4-8](assets/images/4-8.png)</br>![4-9](assets/images/4-9.png)</br>![4-10](assets/images/4-10.png) | Pass |
| Multiplier Selection | <span style='color:tomato'>Invalid inputs:</br><1</br>>max</br>String</span> | 0</br>4</br>6y75er | Error message referencing input and redisplaying of valid options | Error message and repeat of options menu displayed as expected | ![4-11](assets/images/4-11.png)</br>![4-12](assets/images/4-12.png)</br>![4-13](assets/images/4-13.png) | Pass |

`Bonus Score Indication`
| Feature | Test | Input(s) | Expected | Result | Display | Pass/Fail |
|-|-|-|-|-|-|-|
| Bonus Score Menu | Word <7 letters length | object | Menu does not display as word contains <7 letters | Menu is skipped as expected (Final word score displayed immediately) | ![5-1](assets/images/5-1.png) | Pass |
| Bonus Score Menu | Word >6 letters length | rainbow | Menu showing options '1 - Yes, 2 - No' awaiting input from user | Menu and input request displayed as expected | ![5-2](assets/images/5-2.png) | Pass |
| Bonus Selection | <span style='color:lightgreen'>Valid inputs</span> | 1</br>2 | Confirmation message showing bonus applied/not applied as appropriate | Confirmation displayed as expected | ![5-3](assets/images/5-3.png)</br>![5-4](assets/images/5-4.png) | Pass |
| Bonus Selection | <span style='color:tomato'>Invalid inputs:</br><1</br>>2</br>String</span> | 0</br>3</br>6y75er | Error message referencing input and redisplaying of valid options | Error message and repeat of options menu displayed as expected | ![5-5](assets/images/5-5.png)</br>![5-6](assets/images/5-6.png)</br>![5-7](assets/images/5-7.png) | Pass |

`Final Word Score Breakdown`
| Feature | Test | Input(s) | Expected | Result | Display | Pass/Fail |
|-|-|-|-|-|-|-|
| Final Score Message | <span style='color:lightgreen'>Valid inputs:</br>multiple mods only,</br>one mod word x2,</br>no mods word x3 bonus</span> | r2ain*bow3</br>col3orise</br>objects | Final word score showing breakdown of letter score (including modifiers) and any multipliers/bonuses | Final word score breakdown displayed as expected | ![6-1](assets/images/6-1.png)</br>![6-2](assets/images/6-2.png)</br>![6-3](assets/images/6-3.png) | Pass |

`Next Steps Selection`
| Feature | Test | Input(s) | Expected | Result | Display | Pass/Fail |
|-|-|-|-|-|-|-|
| Next Steps Menu | Run program | <span style='color:gray'>n/a</span> | Menu showing options '1 - Score another word, 2 - Change wordlist, 3 - Total score statistics, 4 - Close Program' awaiting input from user | Menu and input request displayed as expected | ![7-1](assets/images/7-1.png) | Pass |
| Next Selection | <span style='color:lightgreen'>Valid input</span> | 1 | Program returns to Word Validation message and input line | Message and input request displayed as expected | ![7-2](assets/images/7-2.png) | Pass |
| Next Selection | <span style='color:lightgreen'>Valid input</span> | 2 | Program returns to Wordlist menu and input line | Menu and input request displayed as expected | ![7-3](assets/images/7-3.png) | Pass |
| Next Selection | <span style='color:lightgreen'>Valid input</span> | 3 | Program returns a list showing all words scored and their scoring types, alongside individual scores and an overall total | Words and scores displayed as expected | ![7-4](assets/images/7-4.png) | Pass |
| Next Selection | <span style='color:lightgreen'>Valid input</span> | 4 | Program exits safely displaying a farewell message and no further options | Program stops and farewell message displayed as expected | ![7-5](assets/images/7-5.png) | Pass |
| Next Selection | <span style='color:tomato'>Invalid inputs:</br><1</br>>4</br>String</span> | 0</br>5</br>6y75er | Error message referencing input and redisplaying of valid options | Error message and repeat of options menu displayed as expected | ![7-6](assets/images/7-6.png)</br>![7-7](assets/images/7-7.png)</br>![7-8](assets/images/7-8.png) | Pass |


### Validator Testing 

- HTML: No errors were returned when passing each HTML page through the official W3C HTML validator
  - [index.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fndsurgenor.github.io%2Fquadulo%2Findex.html)
  - [404.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fndsurgenor.github.io%2Fquadulo%2F404.html)
- PEP8: No errors were returned when passing the program through the [PEP8 Validator](https://pep8ci.herokuapp.com/)
- Accessibility & Performance: A perfect accessibility score was confirmed using Lighthouse in Chrome Developer Tools for both mobile and desktop sites. Performance scored 92/100 for Mobile and a perfect 100 on Desktop.

  ![Lighthouse Report](assets/images/lighthouse.png)

### Fixed Bugs

! TO BE ADDED !

### Unfixed Bugs

- No operational/exceptional bugs are known at this time.

## Deployment

A live link to the site can be found here: https://dashboard.heroku.com/apps/scrabble-scorepad 

### Heroku App Deployment

- This site was deployed to Heroku as an app. Steps for deployment are as follows: 
  - In the GitHub repository, navigate to the Settings tab (top right)
  - From the options in the lefthand side menu, select Pages
  - From the Branch section drop-down menus, select 'main' and '/root' then click 'Save'
  - The page will be automatically refreshed (after a short period) to indicate the successful deployment.

### Forking the GitHub Repository

- Forking the repository allows for a copy to be made without affecting the original. Steps for forking are as follows:
  - Log in to GitHub (requires an account) and locate the [GitHub Repository for Scrabble ScorePAD](https://github.com/ndsurgenor/scrabble-scorepad)
  - Locate and click the 'Fork' button near the very top right of the repository page.
  - This will create a copy of the original Scrabble ScorePAD repository in your own GitHub account.

## Credits 

- Overview image created using [Am I Responsive?](https://ui.dev/amiresponsive?url=https://scrabble-scorepad.herokuapp.com/)
- Flowchart designed using [Lucid Charts](https://lucid.app/lucidchart/db42b587-b151-4fc3-8d91-86050208ea20/edit?viewport_loc=-227%2C56%2C2938%2C1660%2C0_0&invitationId=inv_cbd12e3b-9927-4e6d-a169-3cadd1183444)
- Favicon created with [favicon.io](https://favicon.io/)
- Background image attributed to 'Barrow Boy' used under Creative Commons licence via [Wikipedia Commons](https://upload.wikimedia.org/wikipedia/commons/5/5d/Scrabble_game_in_progress.jpg)
- README.md file adapted from the [Code Institute 'ULTIMATE Battleships'](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware) example