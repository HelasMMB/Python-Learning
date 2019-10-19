import random
import time


# Cycles through the participants...
def deal_cards(*args):
    for game_participant in args:
        new_hand(game_participant)


# ...and gives them their 2 starting cards
def new_hand(game_participant):
    game_participant.hand.append(deck.new_card())
    game_participant.hand.append(deck.new_card())


# Asks the player for their wager, confirms that it is a) affordable and b) an integer,
# then returns the wager amount
def collect_wager(player):
    while True:
        print(f"\nYou have {player.chips} chips.")
        try:
            bet = int(input('How many chips would you like to wager?: '))
            if bet <= player.chips:
                return bet
            else:
                print('Not enough chips.')
        except ValueError:
            print('Please provide a number.')
        else:
            print('Invalid input.')


# Gives player a yes/no option
def decision():
    while True:
        choice = input('Y/N: ')
        if choice.lower() == 'n':
            return True
        elif choice.lower() == 'y':
            return False
        else:
            print('Invalid input.')


# Compares the participant's cards to the card value dict
# Converts ace card value from 11 to 1 when applicable to stay under 21
# Returns the finalized score
def check_score(game_participant):
    score = 0
    ace_count = game_participant.hand.count('A')
    for i in game_participant.hand:
        score += deck.values[i]
        if score > 21:
                while score > 21 and ace_count > 0:
                    ace_count -= 1
                    score -= 10
    return score


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
        self.deck = [i for i in random.sample(self.cards, 52)]

    def shuffle(self):
        pass

    def new_card(self):
        if len(self.deck) == 0:
            self.create_deck()
        new_card = self.deck.pop()
        self.discard_pile.append(new_card)
        return new_card


class Player:

    def __init__(self, chips=50):
        self.hand = []
        self.chips = chips

    def hit(self):
        self.hand.append(deck.new_card())


class Dealer:

    def __init__(self):
        self.hand = []

    def hit(self):
        self.hand.append(deck.new_card())


# -------BEGIN GAME------- #
if __name__ == '__main__':
    exit_game = False
    while not exit_game:
        # allows for rematch option
        game_complete = False
        player_one = Player()
        time.sleep(1)
        print('\nWelcome to Blackjack: The Movie: The Game')
        time.sleep(1)
        print('Initializing new game...')
        time.sleep(1)
        while not game_complete:

            # Determines whether the player will keep (TIE), lose (PLAYER LOSS),
            # or double (PLAYER WIN) their wager at the game's end
            player_win = False
            tie_game = False

            # determines whether or not the dealer will have a turn (depending on player turn outcome)
            dealer_turn = True

            # Starts the game by creating the dealer + deck, and dealing the first two cards
            deck = Deck()
            deck.create_deck()
            dealer = Dealer()
            deal_cards(player_one, dealer)
            print('\nBeginning round.')
            time.sleep(1)

            # Collects wager
            wager = collect_wager(player_one)

            # Begin player round, displays dealer's face up card
            continue_round = True
            print(f"\nDealer card: {dealer.hand[0]}")
            time.sleep(1)

            # Player round will cycle until the player score > 21 (BUST), == 21 (BLACKJACK),
            # or player chooses to STAY (BEGIN DEALER ROUND)
            while continue_round:
                print(f"\nYour cards: {' '.join(player_one.hand)}")
                print(f"Current score: {check_score(player_one)}")
                time.sleep(1)
                if check_score(player_one) > 21:
                    print('\nBUST')
                    print('You lose!')
                    dealer_turn, continue_round = False, False
                elif check_score(player_one) == 21:
                    print('\nBLACKJACK')
                    print('You win!')
                    player_win, dealer_turn, continue_round = True, False, False
                if continue_round:
                    time.sleep(1)
                    hit_or_stay = input('\nWould you like to HIT or STAY?: ')
                    if hit_or_stay.lower() == 'hit':
                        player_one.hit()
                    elif hit_or_stay.lower() == 'stay':
                        continue_round = False
                    else:
                        print('Invalid input.')

            # Begin dealer round
            while dealer_turn:
                # Continually appends cards to dealer until their score is above 17
                # Once score is > 17, checks if it is > 21 (BUST), == 21 (BLACKJACK),
                # or > the player's score (PLAYER LOSS CONDITION)
                print('\nBeginning dealer round.\n')
                time.sleep(1)
                print(f"Dealer cards: {' '.join(dealer.hand)}")
                print(f"Dealer score: {check_score(dealer)}\n")
                time.sleep(1)
                if check_score(dealer) < 17:
                    while check_score(dealer) < 17:
                        print('Dealer hits.\n')
                        dealer.hit()
                        print(f"Dealer cards: {' '.join(dealer.hand)}")
                        print(f"Dealer score: {check_score(dealer)}\n")
                        time.sleep(1)
                if check_score(dealer) > 21:
                    print('BUST. You win!')
                    player_win, dealer_turn = True, False
                elif check_score(dealer) == 21:
                    print('BLACKJACK')
                    print('Dealer wins!')
                    dealer_turn = False
                time.sleep(1)
                if dealer_turn:
                    print(f"Player one score: {check_score(player_one)}")
                    print(f"Dealer score: {check_score(dealer)}\n")
                    time.sleep(1)
                    if check_score(player_one) > check_score(dealer):
                        print('You win!')
                        player_win, dealer_turn = True, False
                    elif check_score(player_one) < check_score(dealer):
                        print('You lose!')
                        dealer_turn = False
                    else:
                        print('Tie game!')
                        tie_game, dealer_turn = True, False

            if tie_game:
                pass
            elif player_win:
                player_one.chips += wager
            else:
                player_one.chips -= wager

            if player_one.chips == 0:
                time.sleep(1)
                print('\nYou are out of chips.')
                print('Game over!')
                game_complete = True

            player_one.hand.clear()

            # Rematch option
            if not game_complete:
                print('\nPlace another bet?')
                game_complete = decision()

        print('\nBegin a new game?')
        exit_game = decision()

    print('\nThank you for playing!')
