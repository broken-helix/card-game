import random
import sys
import pyfiglet
import time

suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King", "Ace"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

game_wins = {"Player Wins": 0, "Computer Wins": 0}


def typing_print(text):
    """
    Controls for typing effect
    for print statements
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typing_input(text):
    """
    Controls for typing effect
    for input print statements
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


def game_introduction():
    """
    Displays an introduction / welcome message
    to the player, asks their name and if they
    would like to read the rules or play the game.
    """
    # name input and welcome messaging
    print("\n")
    print(pyfiglet.figlet_format("WELCOME TO\nBLACKJACK  !"))
    while True:
        name = typing_input("Please enter your player name: \n").capitalize()
        if (name != "Computer") and (name != ""):
            print("\n")
            print(pyfiglet.figlet_format(f"Hello {name} !"))
            break
        elif name == "Computer":
            typing_print("\nSorry. You can't choose that name."
                         " Please try again...\n")
        else:
            typing_print("\nSorry. You chose a blank name."
                         " Please try again...\n")
    # input for game or rules option
    while True:
        option = input("Would you like to read the rules 'R'"
                       " or play the game 'P'?: \n").lower()
        if option == "r":
            display_rules()
        elif option == "p":
            print("\n")
            print(pyfiglet.figlet_format("Let's Play ..."))
            play_game()
        else:
            print("Sorry. You can only select 'R' (rules)"
                  " or 'P' (play game)...\n")


def display_rules():
    """
    Displays the rules of the game
    """
    print("""\n

BLACKJACK RULES AND GAMEPLAY

The aim of the game is to score more points than the computer,
without scoring more than 21 points.

Points are awarded equal to the number on the playing cards
dealt to each player.

Picture cards (Jack, Queen and King) are worth 10 points each.

The Ace is worth 11 points OR 1 point, depending on the total score.

When the game starts, players are dealt 2 cards each from the shuffled
pack of cards. You will only 'see' one of the computer's cards.

If you have a score less than 21 points, you will have the option
to either STICK with the cards you have or TWIST and receive another card.

If you score 21 points with your first 2 cards,
you score BLACKJACK and the game continues.

If you score more than 21 points, you will be BUST and the game continues.

The computer will choose to 'TWIST' or 'STICK' - which finishes the game.""")
    # input to start or exit the game
    option = input("\n\nPress 'P' to Play or 'X' to exit: \n").lower()
    if option == "x":
        print("\n")
        print(pyfiglet.figlet_format("Come  back\nsoon !!!"))
        sys.exit()
    elif option == "p":
        print("\n")
        print(pyfiglet.figlet_format("Let's Play ..."))
        play_game()
    else:
        print("\nSorry. You can only select 'P' (play game)"
              " or 'X' (exit game)...\n")


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
    time.sleep(0.5)
    random.shuffle(pack)
    pack = dict(pack)
    return pack


def create_computer_hand(pack):
    """
    Selects two cards for the computer from
    the shuffled pack, adds them to a new list,
    prints the first card, converts list to
    dictionary and sums values to get score
    """
    computer_hand = []
    while len(computer_hand) < 2:
        computer_hand.append(pack.popitem())
    typing_print("Dealing out the cards...\n")
    time.sleep(0.5)
    typing_print("\nThe computer's show card is: ")
    time.sleep(0.5)
    print(f"\n{computer_hand[0][0]}")
    time.sleep(0.5)
    computer_hand = dict(computer_hand)
    return computer_hand


def create_player_hand(pack):
    """
    Removes two cards for the player
    from the shuffled dictionary (pack),
    adds them to a new list (player_hand)
    and converts list to dictionary
    """
    player_hand = []
    while len(player_hand) < 2:
        player_hand.append(pack.popitem())
    player_hand = dict(player_hand)
    player_score = sum(player_hand.values())
    # adjust score and ace values in event of two aces
    player_score = player_ace_values(player_hand)
    typing_print("\nYour cards are: \n")
    time.sleep(0.5)
    for keys, value in player_hand.items():
        print(keys)
    time.sleep(0.5)
    your_score = (
        "Your score is: "
        f"{player_score}\n\n"
    )
    typing_print(f"\n{your_score}")
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
            stick_twist = input("Would you like to Stick 'S'"
                                " or Twist 'T'?: \n").lower()
            if stick_twist == "t":
                time.sleep(0.5)
                print("You chose to Twist...\n")
                player_hand = twist(pack, player_hand)
                player_score = sum(player_hand.values())
                continue
            elif stick_twist == "s":
                print("")
                you_chose = (
                    "You chose to stick with "
                    f"{player_score} points\n"
                )
                print(you_chose)
                return player_score
                break
            else:
                print("Error. You can only select Stick 'S'"
                      " or Twist 'T'!\n")
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
    player_hand_list.append(pack.popitem())
    time.sleep(0.5)
    new_card = (
        f"\nYour new card is "
        f"the {player_hand_list[-1][0]}\n"
    )
    typing_print(new_card)
    player_hand = dict(player_hand_list)
    player_score = sum(player_hand.values())
    time.sleep(0.5)
    typing_print("\nYour cards are: \n")
    time.sleep(0.5)
    for keys, value in player_hand.items():
        print(keys)
    # adjust score and ace values if score > 21
    player_score = player_ace_values(player_hand)
    time.sleep(0.5)
    typing_print(f"\nYour score is: {player_score}\n\n")
    time.sleep(0.5)
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
    and changes one Ace value from 11 to 1, while score
    remains higher than 21.
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
    and changes Ace value from 11 to 1, while score
    remains higher than 21
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
    # adjust score and ace values if score > 21
    computer_score = computer_ace_values(computer_hand)
    while computer_score <= random.choice(range(16, 19)):
        time.sleep(0.5)
        print("\nThe computer selected Twist\n")
        time.sleep(0.5)
        typing_print("Dealing the computer a new card\n\n")
        computer_hand_list = list(computer_hand.items())
        computer_hand_list.append(pack.popitem())
        time.sleep(0.5)
        comp_card = (
            "The computer's new card is "
            f"the {computer_hand_list[-1][0]}\n"
        )
        typing_print(comp_card)
        computer_hand = dict(computer_hand_list)
        computer_score = sum(computer_hand.values())
        # adjust score and ace values if score > 21
        computer_score = computer_ace_values(computer_hand)
    time.sleep(0.5)
    print("The computer chose to Stick\n")
    time.sleep(0.5)
    typing_print("The computer has: \n")
    time.sleep(0.5)
    for keys, value in computer_hand.items():
        print(keys)
    time.sleep(0.5)
    typing_print(f"\nThe computer scored: {computer_score}\n\n")
    if computer_score == 21:
        time.sleep(1.0)
        print(pyfiglet.figlet_format("BLACKJACK !"))
        return computer_score
    elif computer_score > 21:
        time.sleep(1.0)
        print(pyfiglet.figlet_format("BUST !"))
        return computer_score
    else:
        return computer_score


def compare_scores(player_score, computer_score):
    """
    Prints the players score again and then
    compares scores to decide on the winner and
    increments the game wins values in the dictionary
    """
    typing_print(f"You scored: {player_score}\n\n")
    time.sleep(1.0)
    if player_score == 21:
        if computer_score > 21:
            print("You won with BlackJack!!!\n")
            if "Player Wins" in game_wins:
                game_wins["Player Wins"] += 1
        elif computer_score == 21:
            print("You both got Blackjack!!! It's a draw!\n")
        else:
            print("You won with BlackJack!!!\n")
            if "Player Wins" in game_wins:
                game_wins["Player Wins"] += 1
    elif player_score > 21:
        if computer_score == 21:
            print("The computer got Blackjack!!! You lost the game!\n")
            if "Computer Wins" in game_wins:
                game_wins["Computer Wins"] += 1
        elif computer_score > 21:
            print("You both went BUST!!!\n")
        elif computer_score < 21:
            print("You lost the game!\n")
            if "Computer Wins" in game_wins:
                game_wins["Computer Wins"] += 1
    else:
        if computer_score == 21:
            print("The computer got Blackjack!!! You lost the game!\n")
            if "Computer Wins" in game_wins:
                game_wins["Computer Wins"] += 1
        elif computer_score > 21:
            print("The computer went BUST!!! You won the game!\n")
            if "Player Wins" in game_wins:
                game_wins["Player Wins"] += 1
        else:
            if computer_score < player_score:
                print("You won the game!\n")
                if "Player Wins" in game_wins:
                    game_wins["Player Wins"] += 1
            elif computer_score > player_score:
                print("You lost the game!\n")
                if "Computer Wins" in game_wins:
                    game_wins["Computer Wins"] += 1
            else:
                print("It's a draw!\n")
    time.sleep(1.0)
    print(f'Player Wins: {game_wins["Player Wins"]}')
    print(f'Computer Wins: {game_wins["Computer Wins"]}\n')


def play_again():
    """
    Asks user whether they would like to restart the game or end the game
    """
    time.sleep(1.0)
    new_game = input("Would you like to play again? (Y or N): \n").lower()
    if new_game == "y":
        print("\n")
        print(pyfiglet.figlet_format("Let's Play ..."))
        play_game()
    elif new_game == "n":
        time.sleep(0.5)
        print("\n")
        print(pyfiglet.figlet_format("Thanks for\nplaying\nBlackjack !!!"))
        sys.exit()
    else:
        print("Sorry. You can only select Yes 'Y' or No 'N'. Please try again.\n")
        play_again()


def play_game():
    """
    Starts and runs the game
    """
    pack = create_card_pack()
    computer_hand = create_computer_hand(pack)
    player_hand = create_player_hand(pack)
    player_score = player_choice(pack, player_hand)
    computer_score = computer_twist(pack, computer_hand)
    compare_scores(player_score, computer_score)
    play_again()


game_introduction()
