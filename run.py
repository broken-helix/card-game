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
    name = input("Please enter your player name: ")
    print(f"Welcome to Blackjack {name}.")
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

def create_player_hand(pack):
    """
    Selects two cards for the player from 
    the shuffled pack, adds them to a new list 
    and prints the results.
    """
    player_hand = []
    while len(player_hand) < 2:
        player_hand.append(pack.popitem())
    print("Your cards are:")
    print(f"{player_hand[0][0]} and {player_hand[1][0]}.")
    return player_hand

def create_computer_hand(pack):
    """
    Selects two cards for the computer from 
    the shuffled pack, adds them to a new list 
    and prints the first card.
    """
    computer_hand = []
    while len(computer_hand) < 2:
        computer_hand.append(pack.popitem())
    print(f"The computer's show card is {computer_hand[0][0]}.")
    return computer_hand

def play_game():
    """
    Starts the game
    """
    pack = create_card_pack()
    player_hand = create_player_hand(pack)
    computer_hand = create_computer_hand(pack)

game_introduction()