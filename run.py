import random

def game_introduction():
    """
    Displays an introduction/ welcome message to the user
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
    else:
        print("error")

def create_card_pack():
    """
    Creates an ordered pack (list) of playing cards
    consisting of (suit symbol, suit name) and
    (card symbol, card points value) and shuffles them.
    """
    suits = [("\u2666", "Diamonds"), ("\u2665", "Hearts"), ("\u2663", "Clubs"), ("\u2660", "Spades")]
    ranks = [("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("10", 10), 
            ("Jack", 10), ("Queen", 10), ("King", 10), ("Ace", 11)]
    pack = [(suit, rank) for suit in suits for rank in ranks]
    random.shuffle(pack)

game_introduction()
create_card_pack()