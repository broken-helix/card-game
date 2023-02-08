import random

suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def game_introduction():
    """
    Displays an introduction/ welcome message to the user, 
    asks the user for their name and asks the user if they 
    would like to read the rules or play the game.
    """
    print("Welcome to the blackjack game!")
    while True:
        name = input("Please enter your player name: ").capitalize()
        if (name != "Computer") and (name != ""):
            print(f"Welcome to Blackjack {name}.")
            break
        elif name == "Computer":
            print("Sorry. You can't choose that name. Please try again")
        else:
            print("Sorry. You chose a blank name. Please try again")
    option = input("Would you like to read the rules (R) or play the game (P)?: ").lower()
    if option == "r":
        display_rules()
    elif option == "p":
        play_game()
    else:
        print("error")


def display_rules():
    """
    Displays rules of the game
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
    computer_score = 0
    while len(computer_hand) < 2:
        computer_hand.append(pack.popitem())
    print("The computer's show card is:")
    print(f"{computer_hand[0][0]}")
    computer_hand = dict(computer_hand)
    computer_score = sum(computer_hand.values())
    return computer_hand

def create_player_hand(pack):
    """
    Removes two cards for the player from the shuffled 
    dictionary (pack), adds them to a new list (player_hand)
    and converts list to dictionary
    """
    player_score = 0
    player_hand = []
    while len(player_hand) < 2:
        player_hand.append(pack.popitem())
    player_hand = dict(player_hand)
    player_score = sum(player_hand.values())
    print("Your cards are:")
    for keys, value in player_hand.items():
        print(keys)
    print(f"Your score is {player_score}")
    stick_twist = input("Would you like to Stick (S) or Twist (T)?: ").lower()
    if stick_twist == "s":
        print("You chose to Stick")
    elif stick_twist == "t":
        print("You chose to Twist")
    else:
        print("error")
    return player_hand

def play_game():
    """
    Starts the game
    """
    pack = create_card_pack()
    computer_hand = create_computer_hand(pack)
    player_hand = create_player_hand(pack)

game_introduction()