# **Blackjack**
## **Project Overview**

  Blackjack is a python terminal game hosted on Heroku.  Blackjack is a classic card game where players try to get a higher score than the opponent, without going higher than 21 points. If the player gets a score of exactly 21, they have Blackjack.<br><br>
  The Blackjack python game is played by a single player, with the opponent being the computer.  Unless the score is equal to or greater than 21 points, the player will be given the option to either stick with their current cards or twist, which tells the program to deal another card to the players hand. Once the player has finished their turn, either by selecting to stick, reaching a score of 21 or going over the 21 point limit, the computer will make its choice to stick or twist, unless it has a score of equal to or greater than 21 point. Once all selections have been completed, the program decides who won and increments the game play scores.<br><br>
  Each card in the pack has a value:
* Number cards have the same value as their respective number (for example: the 2 of Hearts is worth 2 points)
* Jack, Queen and King cards have a value of 10 points
* The Ace starts with a score of 11 points, but can change to 1 point if the overall score is too high

[View the live project here](https://blackjack-game.herokuapp.com/)

![Title Screenshot](/docs/title-screen.jpg)
***

## Table of contents:
1. [**Project Overview**](#project-overview)
1. [**Planning stage**](#planning-stage)
    * [***Flowchart***](#flowcharts)
    * [***Target Audiences***](#target-audiences)
    * [***User Stories***](#user-stories)
    * [***Site Aims***](#site-aims)
1. [**Current Features**](#current-features)
    * [***Page Title***](#page-title)
    * [***Game Start Options***](#game-start-options)
    * [***Dealing Hands***](#dealing-hands)
    * [***Twisting***](#twisting)
    * [***Ace Values***](#ace-values)
    * [***Compare Scores***](#compare-scores)
    * [***Play Again***](#play-again)
    * [***Typing Text***](#typing-text)
    * [***Pyfiglet Generator***](#pyfiglet-generator)
    * [***Time Pauses***](#time-pauses)
1. [**Future-Enhancements**](#future-enhancements)
1. [**Testing Phase**](#testing-phase)
1. [**Deployment**](#deployment)
1. [**Tech**](#tech)
1. [**Credits**](#credits)
    * [**Honorable mentions**](#honorable-mentions)
    * [**General reference**](#general-reference)
***

## **Planning stage**

### **Flowchart:**

A Lucid flowchart was created to map out the flow of the game

![Flowchart](/docs/flowchart-lucid.jpg)
***

### **Target Audiences:**

* People who want to learn about the game of Blackjack
* People who want to play a simple game of cards
***

### **User Stories:**

* As a user, I want to be able to read the rules of the game
* As a user, I want to believe I can influence the game by selecting options
* As a user, I want to believe the game is one of chance and the cards are randomly assigned
***

### **Site Aims:**

* To introduce the user to the Rock, Paper, Scissors game.
* For playing the game to be simple and intuitive.
* To keep a record of the total score.
* To provide the user with a clear indication of who won.
* To build a python terminal game
***

## **Current Features**

#### *Welcome Title:*

* The welcome title welcomes the user to the game and shows the player the name of the game in large font, achieved with the pyfiglet ASCII text generator. It immediately asks the player to enter their name and displays a 'Hello Name' message, again with the pyfiglet ASCII text generator, when they have entered their name correctly.<br><br>
* Error handling deals with blank inputs or the event of the player selecting 'computer' as their name. This latter feature is currently not required to run the game, as the player name 
does not feature in the rest of the game, but would handle conflicts if the player name was incorporated into the game at a later stage.

![Welcome Title](/docs/welcome-title.jpg)

![Hello Player Title](/docs/hello-name.jpg)

![Name options errors](/docs/computer-name-error.jpg)

#### *Game Start Options:*

* After the 'Hello name' greeting, the player is immediately asked if they would like to go ahead and play the game or read the rules. Error handling deals with events where the 
player chooses a letter other than the two options listed and repeats the game start option input message.<br><br>
* If the player chooses the read the rules, the rules are displayed and the player has an option to leave the game or play the game. Error handling again checks the players response and repeats the question if a selection is made other than the two offered.

![Game Start Options](/docs/start-game-options.jpg)

![Rules Display](/docs/rules.jpg)

![Game Start Error Message](/docs/start-game-error.jpg)

#### *Dealing Hands:*

* When the player selects to play the game, a shuffled dictionary of 52 cards is created, with each card containing a key of the card symbol and suit and a value. The computer and player 
are then given two cards from pack of cards.<br><br>
* The player will only be shown one of the computer cards and will not be told the computer starting score. The player will be told what both 
of their cards are.<br><br>
* If the player is dealt two Aces, which would give the player a score of 22, the cards are checked and one of the Ace values is changed from 11 points to 1 point before 
the player is told their current score.<br><br>
* If the player has 21 points at this stage, a message is displayed to inform the player that they have Blackjack and play switches to the computer.<br><br>
* If the player has any score below 21, they are asked if they would like to stick with their cards and end their turn or receive an additional card (Twist).

![Dealing Hands](/docs/lets-play.jpg)

#### *Twisting:*

* When the player chooses to Twist, the program selects a new card from the pack and places it in the players hand. The card values are totalled and checked for Aces with a value of 11 
if the score is greater than 21 points. If the score is higher than 21 after Aces have been checked for and revalued if necessary, the player will be told they are bust and their turn will 
end. If the score is 21, the player will be informed they have blackjack and their turn will end. If the score is less than 21 points, they player will again be asked if they would like 
to stick or twist.<br><br>
* Once the player has selected to stick, their turn will end.

![Blackjack Message](/docs/blackjack.jpg)

* Once the player has finished creating their hand, either by sticking, going bust or reaching blackjack, the program will run the process for the computer. At this stage, the computer score 
will be totalled, any Aces checked for high values if the score is over 21 and the program will decide whether the computer should stick or twist.<br><br>
* The computer will twist if the score is below a certain number of points, which is randomly selected each time. This ensures the player cannot determine what score will be likely to win.<br><br>
* Each time the computer twists, the scores are tallied and any Aces are checked for high values if the score is greater than 21 points. Once Aces have been checked and revalued if required, the score will be complete and the twist/ stick process will be carried out again.<br><br>
* Once the score reaches the randomly assigned threshold or a score of 21 or greater, the computer will stick. If the computer goes bust or achieves blackjack a message will be displayed to that effect.

![Twist Example](/docs/twist-example.jpg)
​
#### *Ace Values:*

* In Blackjack, an Ace card can have two values, 11 or 1 points. An Ace card is considered to have 1 point if the score would otherwise be greater than 21 points.<br><br>
* A separate function handles these cases, first assessing if the score is (or remains) above 21 points, then looking for Aces in the player hand with a value of 11 and changing the first incidence to a value of 1.  When the score is less than or equal to 21 or is greater than 21 and there are no Aces with a value of 11, the game continues.

![Ace Values](/docs/ace-values.jpg)

#### *Compare Scores:*

* When both the player and computer have completed their turns - either because they chose to stick, or the respective score was equal to or greater than 21 - the scores of the player 
and the computer are compared and a message is displayed to let the player know who won the game.

![Compare Scores](/docs/compare-scores.jpg)

#### *Play Again:*

* Once the game is complete, the player is presented with the option to continue playing another game or to exit the game.<br><br>
* If the player chooses to continue the game, the incremented score total is maintained, so that the player can play a series of games and receive a running total of games won.<br><br>
* An error handling option deals with situations where the player selects an option other than the two presented and repeats the original input request.

![Play Again With Error](/docs/play-again-with-error.jpg)

![End Game Message](/docs/come-back-soon.jpg)

#### *Typing text:*

* Most print statements use a typing text effect, which assists in slowing down the presentation of information, so the user can easily keep track of the game. This function also adds suspense, making the game more interesting for the player. Only one of the input messages, for the player name, uses the typing text function, to avoid the player having to wait to select their option. Some other print statements, feeding back to the player the choice made, also avoid typing text, to avoid slowing down the game too much.

#### *Pyfiglet Generator:*

* The pyfiglet import allows the display of ASCII text to display messages. It is used for the welcome messages and to flag that either player has achieved Blackjack or went Bust.

![Pyfiglet Messages](/docs/pyfiglet-bust.jpg)
​
#### *Time Pauses:*

* The import of time enables the use of pauses to add drama and suspense to the game, particularly when waiting for the results of actions to be presented. For instance, there is a small pause before blackjack or bust messages are displayed and while the player is waiting to see the results of a twist action.

## **Future-Enhancements**

* Limit the number of cards that can be selected by either player, so that a hand can only have a maximum number of cards.
* Disable the ability to press keys during typing text inputs, which can result in the program misinterpreting the chosen option if the input message is interrupted.
* Add colours to print messages to highlight win and loss states
* Add an option to reset the scores and continue playing the game without exiting and restarting
***

## **Testing Phase**

* Validation - The code was passed through the Code Institute PEP8 validation tool, and errors with whitespace and lines too long in length were corrected.

![PEP8 Validation](/docs/PEP8-validation.jpg)
​
* Functionality - The game has been played multiple times, in the Heroku deployment and within the GitPod terminal, to ensure that all options are covered. This involved manually attributing cards to player and computer, for instance to check that a starting hand of two Aces did not result in a score of 22, which would make either player bust before they had begun the game. At points, the code was slimmed down and hand values were manually attributed in Python Tutor, to check the flow of the code and fix issues with return statements not returning the correct score for comparing results. Options have been checked to ensure that incorrect values are handled correctly and do not result in errors which prevent the continuation of the game.  Examples of these error handling features have been included throughout this file.

![Testing Image](/docs/ace-testing.jpg)
***

## **Bugs**

* Issue - When the function to compare the scores was added, the player scores were not updating.
* Cause - Careful dissection of the code with Python Tutor showed errors in the way results were being returned between the player choice function and the player twist function.
* Resolution - A series of return statements were added to each possible outcome of the player twist function to ensure the updated score was passed back.

* Issue - When new lines are required to create space between print statements, the lines are too large when the new lines are incorporated into the pyfiglet ASCII text displays.
* Cause - The line associated with the pyfiglet output is larger than a single line, due to the size of the input.
* Resolution - Separate input statements were added to create single line breaks around pyfiglet displays.
***

## **Deployment**

I deployed the page on Heroku via the following procedure:
​
1. I selected new on the apps page of Heroku's dashboard and created a new app
2. I added a key of PORT and a value of 8000 to the Config Vars
3. I added two buildpacks, python and nodejs, with python listed first
4. I searched for the repository and manually deployed to Heroku
​
The live site can be found at the following URL - [Blackjack](https://blackjack-game/herokuapp.com)
***

## **Tech**
​
The following technologies were employed in the creation of the site:
​
- Python
- Pyfiglet Generator
- Typing text
- PythonTutor Composing Program
- Lucid Flowcharts
***

## **Credits**

* [Typing text](https://www.101computing.net/python-typing-text-effect/)

* [Pyfiglet ASCII Text Generator](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/)

* [Python Tutor Composing Program](https://pythontutor.com/cp/composingprograms.html#mode=edit)

* [Exiting the Game with sys.exit()](https://stackoverflow.com/questions/65653491/is-there-a-way-to-stop-a-program-from-running-if-an-input-is-incorrect-python/)

### **Honorable mentions**

* I would like to thank my mentor, Richard Wells, particularly in helping me to understand how to check the Aces and change the values incrementally.
***

### **General Reference**

* Pyfiglet source - [Pyfiglet](https://pypi.org/project/pyfiglet/0.7/)

* Flowchart source - [Lucid Chart](https://lucidchart.com/)
