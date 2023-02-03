import random

pack = []
player_hand = []
computer_hand = []

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
        print("Display Rules")
        display_rules()
    elif option == "p":
        print("Play Game")
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
    Creates an ordered pack (list) of playing cards
    consisting of (suit symbol, suit name) and
    (card symbol, card points value) and shuffles them.
    """
    global pack
    suits = [("\u2666", "Diamonds"), ("\u2665", "Hearts"), ("\u2663", "Clubs"), ("\u2660", "Spades")]
    ranks = [("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("10", 10), 
            ("Jack", 10), ("Queen", 10), ("King", 10), ("Ace", 11)]
    pack = [(suit, rank) for suit in suits for rank in ranks]
    random.shuffle(pack)
    return pack

def create_player_hand(pack):
    global player_hand
    while len(player_hand) < 2:
        player_hand.append(pack.pop(-1))
    print(player_hand)

def play_game():
    """
    Starts the game
    """
    print("Play Game Function")

game_introduction()
create_card_pack()
create_player_hand(pack)