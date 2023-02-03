import random

def create_card_deck():
    """
    Creates an ordered deck (list) of playing cards
    consisting of (suit symbol, suit name) and
    (card symbol, card points value) and shuffles them.
    """
    suits = [("\u2666", "Diamonds"), ("\u2665", "Hearts"), ("\u2663", "Clubs"), ("\u2660", "Spades")]
    ranks = [("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("10", 10), 
            ("Jack", 10), ("Queen", 10), ("King", 10), ("Ace", 11)]
    deck = [(suit, rank) for suit in suits for rank in ranks]
    random.shuffle(deck)

create_card_deck()