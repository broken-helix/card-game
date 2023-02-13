import random
import sys
import pyfiglet
import time

suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

new_line = "\n"

def typing_print(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typing_input(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value  

def game_introduction():
    """
    Displays an introduction / welcome message to the user, 
    asks the user for their name and asks the user if they 
    would like to read the rules or play the game.
    """
    print(pyfiglet.figlet_format("WELCOME TO"))
    print(pyfiglet.figlet_format("BLACKJACK  !"))
    while True:
        name = typing_input("Please enter your player name: ").capitalize()
        if (name != "Computer") and (name != ""):
            print("")
            print(pyfiglet.figlet_format(f"Hello {name} !"))
            break
        elif name == "Computer":
            typing_print("Sorry. You can't choose that name. Please try again...")
        else:
            typing_print("Sorry. You chose a blank name. Please try again...")
    while True:
        option = typing_input("Would you like to read the rules (R) or play the game (P)?: ").lower()
        if option == "r":
            display_rules()
        elif option == "p":
            print("")
            print(pyfiglet.figlet_format("Let's Play ..."))
            play_game()
        else:
            print("")
            print("Sorry. You can only select 'R' (rules) or 'P' (play game)...")


def display_rules():
    """
    Displays the rules of the game
    """
    print("Display Rules Function")


def create_card_pack():
    """
    Creates an ordered list (pack) of playing cards as 
    strings, converts list to dictionary (cardpack) to add 
    card values to card keys, converts dictionary (cardpack) 
    back to list (pack), shuffles list (pack) and converts 
    shuffled list (pack) to shuffled dictionary (pack)
    """
    pack = []
    for suit in suits:
        for rank in ranks:
            pack.append(rank + ' of ' + suit)
    cardpack = dict(zip(pack, values*4))
    pack = list(cardpack.items())
    typing_print("Shuffling the pack...\n")
    random.shuffle(pack)
    pack = dict(pack)
    return pack


def create_computer_hand(pack):
    """
    Selects two cards for the computer from 
    the shuffled pack, adds them to a new list,
    prints the first card, then converts list to 
    dictionary and sums values to get score
    """
    computer_hand = []
    while len(computer_hand) < 2:
        computer_hand.append(pack.popitem())
    typing_print("Dealing out the cards...\n")
    print("")
    typing_print("The computer's show card is: \n")
    time.sleep(0.5)
    print(f"{computer_hand[0][0]}")
    time.sleep(0.5)
    print("")
    computer_hand = dict(computer_hand)
    return computer_hand


def create_player_hand(pack):
    """
    Removes two cards for the player from the shuffled 
    dictionary (pack), adds them to a new list (player_hand)
    and converts list to dictionary
    """
    player_hand = []
    # removes two cards from pack and adds to player hand
    while len(player_hand) < 2:
        player_hand.append(pack.popitem())
    # converts player hand back to dictionary and totals values
    player_hand = dict(player_hand)
    player_score = sum(player_hand.values())
    # adjusts score in event of two aces as first cards
    player_score = player_ace_values(player_hand)
    typing_print("Your cards are: \n")
    time.sleep(0.5)
    for keys, value in player_hand.items():
        print(keys)
    print("")
    time.sleep(0.5)
    typing_print(f"Your score is {player_score}{new_line}")
    print("")
    time.sleep(0.5)
    return player_hand


def player_choice(pack, player_hand):
    """
    Asks the player if they would like to Stick with their
    current hand or Twist (receive another card)
    """
    player_score = player_ace_values(player_hand)
    if player_score == 21:
        time.sleep(1.0)
        print(pyfiglet.figlet_format("Blackjack !"))
        return player_score
    else:
        while player_score < 21:
            stick_twist = typing_input("Would you like to Stick (S) or Twist (T)?: ").lower()
            if stick_twist == "t":
                print("")
                time.sleep(0.5)
                typing_print("You chose to Twist...\n")
                player_hand = twist(pack, player_hand)
                player_score = sum(player_hand.values())
                continue
            elif stick_twist == "s":
                print("")
                typing_print(f"You chose to Stick with {player_score} points{new_line}")
                return player_score
                break
            else:
                print("")
                print("Error. You can only select Stick (S) or Twist (T)!/n")
                continue
        return player_score   


def twist(pack, player_hand):
    """
    Draws a new card from the deck, adds to player_hand
    and totals player_score
    """
    player_hand_list = list(player_hand.items())
    time.sleep(0.5)
    typing_print("Dealing you a new card...\n")
    print("")
    player_hand_list.append(pack.popitem())
    time.sleep(0.5)
    typing_print(f"Your new card is the {player_hand_list[-1][0]}{new_line}")
    print("")
    player_hand = dict(player_hand_list)
    player_score = sum(player_hand.values())
    time.sleep(0.5)
    typing_print("Your cards are: \n")
    time.sleep(0.5)
    for keys, value in player_hand.items():
        print(keys)
    player_score = player_ace_values(player_hand)
    print("")
    time.sleep(0.5)
    typing_print(f"Your score is: {player_score}{new_line}")
    time.sleep(0.5)
    print("")
    if player_score < 21:
        return player_hand
    elif player_score > 21:
        time.sleep(1.0)
        print(pyfiglet.figlet_format("BUST !"))
        return player_hand
    elif player_score == 21:
        time.sleep(1.0)
        print(pyfiglet.figlet_format("BLACKJACK !"))
        return player_hand


def player_ace_values(player_hand):
    """
    Checks player hand for aces if score greater is than 21
    and changes Ace value from 11 to 1, while score remains
    higher than 21.
    """
    player_score = sum(player_hand.values())
    if player_score > 21:
        for key, value in player_hand.items():
            if "Ace" in key and value == 11:
                updated_value = {key: 1}
                player_hand.update(updated_value)
                update_score = sum(player_hand.values())
                if update_score > 21:
                    continue
                else:
                    player_score = update_score
                    break
    return player_score


def computer_ace_values(computer_hand):
    """
    Checks computer hand for aces if score greater than 21
    and changes Ace value from 11 to 1, while score remains
    higher than 21
    """
    computer_score = sum(computer_hand.values())
    if computer_score > 21:
        for key, value in computer_hand.items():
            if "Ace" in key and value == 11:
                updated_value = {key: 1}
                computer_hand.update(updated_value)
                update_score = sum(computer_hand.values())
                if update_score > 21:
                    continue
                else:
                    computer_score = update_score
                    break
    return computer_score


def computer_twist(pack, computer_hand):
    """
    Selects new cards for computer hand until score
    reaches a random total approaching the game limit
    """
    computer_score = sum(computer_hand.values())
    # checks for aces and changes value if score over 21
    computer_score = computer_ace_values(computer_hand)
    while computer_score <= random.choice(range(16, 19)):
        print("")
        time.sleep(0.5)
        typing_print("The computer selected Twist\n")
        print("")
        time.sleep(0.5)
        typing_print("Dealing the computer a new card\n")
        computer_hand_list = list(computer_hand.items())
        computer_hand_list.append(pack.popitem())
        time.sleep(0.5)
        typing_print(f"The computer's new card is the {computer_hand_list[-1][0]}{new_line}")
        computer_hand = dict(computer_hand_list)
        computer_score = sum(computer_hand.values())
    print("")
    time.sleep(0.5)
    typing_print("The computer chose to Stick\n")
    print("")
    computer_score = computer_ace_values(computer_hand)
    time.sleep(0.5)
    typing_print("The computer has: \n")
    time.sleep(0.5)
    for keys, value in computer_hand.items():
        print(keys)
    print("")
    time.sleep(0.5)
    typing_print(f"The computer scored: {computer_score}{new_line}")
    return computer_score


def compare_scores(player_score, computer_score):
    typing_print(f"You scored: {player_score}{new_line}")


def play_again():
    """
    Asks user whether they would like to restart the game or end the game
    """
    time.sleep(0.5)
    new_game = typing_input("Would you like to play again? (Y or N): ").lower()
    if new_game == "y":
        play_game()
    elif new_game == "n":
        time.sleep(0.5)
        typing_print("Bye-bye!\n")
        sys.exit()
    else:
        play_again()


def play_game():
    """
    Starts the game
    """
    pack = create_card_pack()
    computer_hand = create_computer_hand(pack)
    player_hand = create_player_hand(pack)
    player_score = player_choice(pack, player_hand)
    computer_score = computer_twist(pack, computer_hand)
    compare_scores(player_score, computer_score)
    play_again()

game_introduction()