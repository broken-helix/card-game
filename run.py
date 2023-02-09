import random

suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
#ranks = ["Ace"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
#values = [11]

def game_introduction():
    """
    Displays an introduction / welcome message to the user, 
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
    while len(computer_hand) < 2:
        computer_hand.append(pack.popitem())
    print("The computer's show card is:")
    print(f"{computer_hand[0][0]}")
    computer_hand = dict(computer_hand)
    return computer_hand


def create_player_hand(pack):
    """
    Removes two cards for the player from the shuffled 
    dictionary (pack), adds them to a new list (player_hand)
    and converts list to dictionary
    """
    player_score = 0
    player_hand = []
    # removes two cards from pack and adds to player hand
    while len(player_hand) < 2:
        player_hand.append(pack.popitem())
    # converts player hand back to dictionary and totals values
    player_hand = dict(player_hand)
    player_score = sum(player_hand.values())
    # adjusts score in event of two aces as first cards
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
    print("Your cards are:")
    for keys, value in player_hand.items():
        print(keys)
    print(f"Your score is {player_score}")
    return player_hand


def player_choice(pack, player_hand):
    """
    Asks the player if they would like to Stick with their
    current hand or Twist (receive another card)
    """
    stick_twist = input("Would you like to Stick (S) or Twist (T)?: ").lower()
    if stick_twist == "s":
        print("You chose to Stick")
    elif stick_twist == "t":
        twist(pack, player_hand)
    else:
        print("error")


def twist(pack, player_hand):
    player_hand_list = list(player_hand.items())
    player_hand_list.append(pack.popitem())
    player_hand = dict(player_hand_list)
    player_score = sum(player_hand.values())
    print("Your cards are:")
    for keys, value in player_hand.items():
        print(keys)
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
    print(f"Your score is {player_score}")
    if player_score < 21:
        player_choice(pack, player_hand)
    elif player_score == 21:
        print("Blackjack!")
    else:
        print("BUST!!!")


def ace_values(computer_hand):
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


def computer_twist(pack, computer_hand):
    computer_score = sum(computer_hand.values())
    ace_values(computer_hand)
    while computer_score <= random.choice(range(16, 19)):
        computer_hand_list = list(computer_hand.items())
        computer_hand_list.append(pack.popitem())
        computer_hand = dict(computer_hand_list)
        computer_score = sum(computer_hand.values())
        ace_values(computer_hand)
    print("The computer has:")
    for keys, value in computer_hand.items():
        print(keys)
    print(f"The computer scored: {computer_score}")

def play_again():
    new_game = input("Would you like to play again? (Y or N): ").lower()
    if new_game == "y":
        play_game()
    elif new_game == "n":
        print("Bye-bye!")
    else:
        play_again()


def play_game():
    """
    Starts the game
    """
    pack = create_card_pack()
    computer_hand = create_computer_hand(pack)
    player_hand = create_player_hand(pack)
    player_choice(pack, player_hand)
    computer_twist(pack, computer_hand)
    play_again()

game_introduction()