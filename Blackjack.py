import random

#=====================
## OUTCOMES

## Player busts (goes over 21)
## Player stops under 21, dealer plays until it busts
## Player stops under 21, dealer plays until it gets blackjack or beats the player

## Face cards have a value of 10
## Aces can count as either 1 or 11
#=====================
# PLAYER OPTIONS

## HIT (receive a card)
## STAY (stop receiving cards)
#=====================
# IDEA FOR COUNTER

# IF HAND + ACE > 21, ACE DEFAULTS FROM 11 TO 1
#=====================
# CURRENCY RULES

# PLAYER HAS A POOL OF "CHIPS"
# WIN DOUBLES THE PLAYER'S BET
# LOSS REMOVES THE PLAYER'S BET
#=====================
# VARIABLES

# PLAYER'S HAND
# PLAYER'S COUNT
# DEALER'S HAND
# DEALER'S COUNT
# DECK
# DISCARD PILE
# PLAYER'S CHIP COUNT

# *OPTIONAL*
# WIN-LOSS PERCENTAGE
#=====================
# FUNCTIONS

# HIT
# STAY (SWITCH FROM PLAYER TO DEALER)
# COUNT CARD TOTAL
# PLACE BET
# RETURN WINNINGS
# SHUFFLE DECK
# START NEW GAME
#=====================

class Deck:

    def __init__(self):
        self.cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K',
                      'A','2','3','4','5','6','7','8','9','10','J','Q','K',
                      'A','2','3','4','5','6','7','8','9','10','J','Q','K',
                      'A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5,
                       '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                       'J': 10, 'Q': 10, 'K': 10}
        self.deck = []
        self.discard_pile = []

    def create_deck(self):
        while len(self.deck) < 52:
            card = random.randint(0, len(self.cards) - 1)
            self.deck.append(self.cards.pop(card))

    def shuffle(self):
        while len(self.deck) < 52:
            card = random.randint(0, len(self.discard_pile) - 1)
            self.deck.append(self.discard_pile.pop(card))

    def new_card(self):
        return self.deck.pop()



class Player:

    def _init__(self,hand,chips=50):
        self.hand = []
        self.chips = chips

    def hit(self):
        pass

    def stay(self):
        pass

    def show_hand(self):
        pass

class Dealer:

    def __init__(self,hand):
        self.hand = []

    def deal(self):
        pass

    def hit(self):
        pass

    def show_hand(self):
        pass

####### BEGIN GAME #######
if __name__ == '__main__':
    deck = Deck()
    deck.create_deck()
    player1 = Player()
    i = 1
    while i < 52:
        print(deck.new_card())
        i += 1