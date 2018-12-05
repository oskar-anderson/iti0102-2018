"""Simple game of blackjack."""
from textwrap import dedent

import requests
import sys
import re


class Card:
    """Simple dataclass for holding card information."""

    def __init__(self, value: str, suit: str, code: str):
        self.value = value
        self.suit = suit
        self.code = code

    def __repr__(self):
        return self.code


class Hand:
    """Simple class for holding hand information."""

    def __init__(self):
        self.score = 0
        self.cards = []
        self.aces_turned_to_one = 0

    def add_card(self, card: Card):
        """Add drawn card to cards list and calculate hand score."""
        if card.value in ["JACK", "QUEEN", "KING", "ACE"]:
            if card.value == "ACE":
                self.score += 11
            else:
                self.score += 10
        else:
            self.score += int(card.value)
        self.cards.append(card)
        if self.score > 21:
            regex = "A[A-Z]"
            if len(re.findall(regex, str(self.cards))) != self.aces_turned_to_one:
                self.score -= 10 * (len(re.findall(regex, str(self.cards))) - self.aces_turned_to_one)
                self.aces_turned_to_one = len(re.findall(regex, str(self.cards)))

            for element in self.cards:
                print(["AS", "AD", "AC", "AH"].count(element))  # 0 even if element is ace
                for check in ["AS", "AD", "AC", "AH"]:
                    print(element)  # AC
                    print(check)   # AC
                    print(element == check)  # False, how?
                    print()
        # print(self.score)


class Deck:
    """Deck of cards. Provided via api over the network."""

    def __init__(self, shuffle=False):
        """
        Tell api to create a new deck.

        :param shuffle: if shuffle option is true, make new shuffled deck.
        """
        if not shuffle:
            url = "https://deckofcardsapi.com/api/deck/new"
            self.deck = requests.get(url).json()
            self.is_shuffled = False
        else:
            url = "https://deckofcardsapi.com/api/deck/new/shuffle"
            self.deck = requests.get(url).json()
            self.is_shuffled = True
        self.deck_id = self.deck["deck_id"]
        print(self.deck_id)

    def shuffle(self):
        """Shuffle the deck."""
        url = f"https://deckofcardsapi.com/api/deck/{self.deck_id}/shuffle"
        self.deck = requests.get(url).json()
        self.is_shuffled = True

    def draw(self) -> Card:
        """
        Draw card from the deck.

        :return: card instance.
        """
        url = f"https://deckofcardsapi.com/api/deck/{self.deck_id}/draw"
        drawn_card = requests.get(url).json()
        print(drawn_card)
        return Card((drawn_card["cards"][0]["value"]), drawn_card["cards"][0]["suit"], drawn_card["cards"][0]["code"])


class BlackjackController:
    """Blackjack controller. For controlling the game and data flow between view and database."""

    def __init__(self, deck: Deck, view: 'BlackjackView'):
        """
        Start new blackjack game.

        :param deck: deck to draw cards from.
        :param view: view to communicate with.
        """
        self.deck = deck
        self.view = view
        if not deck.is_shuffled:
            deck.shuffle()
        dealer = Hand()
        player = Hand()
        player.add_card(self.deck.draw())
        dealer.add_card(self.deck.draw())
        player.add_card(self.deck.draw())
        dealer.add_card(self.deck.draw())
        print(f"Dealer score: {dealer.score}")
        print(f"Player score: {player.score}")
        if player.score == 21:
            state = {"dealer": dealer, "player": player}
            self.view.player_won(state)
            sys.exit()
        while True:
            state = {"dealer": dealer, "player": player}
            if self.view.ask_next_move(state) == "S":
                print("Player holds")
                while player.score >= dealer.score:
                    dealer.add_card(self.deck.draw())
                    if dealer.score > 21:
                        state = {"dealer": dealer, "player": player}
                        self.view.player_won(state)
                        sys.exit()
                state = {"dealer": dealer, "player": player}
                self.view.player_lost(state)
                sys.exit()
            else:
                print("Player hits")
                player.add_card(self.deck.draw())
                if player.score > 21:
                    state = {"dealer": dealer, "player": player}
                    self.view.player_lost(state)
                    sys.exit()
                if player.score == 21:
                    state = {"dealer": dealer, "player": player}
                    self.view.player_won(state)
                    sys.exit()


class BlackjackView:
    """Minimalistic UI/view for the blackjack game."""

    def ask_next_move(self, state: dict) -> str:
        """
        Get next move from the player.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        :return: parsed command that user has choses. String "H" for hit and "S" for stand
        """
        self.display_state(state)
        while True:
            action = input("Choose your next move hit(H) or stand(S) > ")
            if action.upper() in ["H", "S"]:
                return action.upper()
            print("Invalid command!")

    def player_lost(self, state):
        """
        Display player lost dialog to the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        """
        self.display_state(state, final=True)
        print("You lost")

    def player_won(self, state):
        """
        Display player won dialog to the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        """
        self.display_state(state, final=True)
        print("You won")

    def display_state(self, state, final=False):
        """
        Display state of the game for the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        :param final: boolean if the given state is final state. True if game has been lost or won.
        """
        dealer_score = state["dealer"].score if final else "??"
        dealer_cards = state["dealer"].cards
        if not final:
            dealer_cards_hidden_last = [c.__repr__() for c in dealer_cards[:-1]] + ["??"]
            dealer_cards = f"[{','.join(dealer_cards_hidden_last)}]"

        player_score = state["player"].score
        player_cards = state["player"].cards
        print(dedent(
            f"""
            {"Dealer score":<15}: {dealer_score}
            {"Dealer hand":<15}: {dealer_cards}

            {"Your score":<15}: {player_score}
            {"Your hand":<15}: {player_cards}
            """
        ))


if __name__ == '__main__':
    BlackjackController(Deck(), BlackjackView())  # start the game.
