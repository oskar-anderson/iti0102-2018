"""Cards module that contains Card and Deck classes."""

from itertools import zip_longest
import random


class Card:
    r"""
    Card class representing a playing card.

    Unicode values used for suits:
    Clubs    '\u2663' (♣)
    Spades   '\u2660' (♠)
    Diamonds '\u2666' (♦)
    Hearts   '\u2665' (♥)
    """

    RANKS = (None, 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
    SUITS = ("c", "s", "d", "h")
    SYMBOLS = ('♣', '♠', '♦', '♥')

    def __init__(self, rank, suit, face_up=True, symbols=False, decorated=True):
        """
        Constructor.

        :param rank: int (1-13) or character from Card.RANKS
        :param suit: int (0-4) or character from Card.SUITS
        :param face_up: boolean, if True the card is initially face up
        and face down when False
        :param symbols: boolean, if True the card representation uses symbols
        as suits otherwise if False it uses characters from Card.Suits
        :param decorated: boolean, if True the card representation is
        decorated with borders
        """
        self._rank = self.rank = rank
        self._suit = self.suit = suit
        self.face_up = face_up
        self.symbols = symbols
        self.decorated = decorated

    @property
    def rank(self) -> int:
        """Get the rank as int."""
        return self._rank

    @property
    def suit(self) -> int:
        """Get the suit as int."""
        return self._suit

    @rank.setter
    def rank(self, value):
        """Set the rank."""
        if isinstance(value, int) and 1 <= value <= 13:
            self._rank = value
        elif isinstance(value, str) and value in Card.RANKS:
            self._rank = Card.RANKS.index(value)
        else:
            raise ValueError("Invalid rank value!")

    @suit.setter
    def suit(self, value):
        """Set the suit."""
        if isinstance(value, int) and 0 <= value <= 3:
            self._suit = value
        elif isinstance(value, str) and value in Card.SUITS:
            self._suit = Card.SUITS.index(value)
        else:
            raise ValueError("Invalid suit value!")

    def is_face_up(self) -> bool:
        """Check if the card face up."""
        return self.face_up

    def flip(self):
        """Flip the card."""
        self.face_up = not self.face_up

    def __lt__(self, other):
        """Less than operator, used for sorting."""
        if self.rank == other.rank:
            return self.suit < other.suit
        return self.rank < other.rank

    def __repr__(self):
        """
        Represent the card as a string when printed.

        If self.decorated is True, borders are used.
        If self.face_up is False, card face is hidden.
        """
        b = ('', '')
        if self.decorated:
            b = ('[', ']')
        if not self.face_up:
            return f"{b[0]}##{b[1]}"
        return f"{b[0]}{Card.RANKS[self._rank]}" + f"{Card.SYMBOLS[self.suit] if self.symbols else Card.SUITS[self.suit]}{b[1]}"


class Deck:
    """
    Deck class representing a deck of cards.

    Implemented as a list of Card objects.
    """

    def __init__(self, face_up=True, symbols=False, decorated=True):
        """
        Constuctor.

        Creates a list of 52 Card objects.
        :param face_up: boolean, if True all cards in the deck are initially face up
        :param symbols: boolean, if True symbol representation is used for all cards
        :param decorated: boolean, if True card representations are decorated with borders
        """
        self.cards = []
        for rank in range(1, 14):
            for suit in range(4):
                self.cards.append(Card(rank, suit, face_up=face_up, symbols=symbols, decorated=decorated))

    def add_card(self, card):
        """Add a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card):
        """Remove a card from the deck."""
        self.cards.remove(card)

    def deal_card(self, i=-1) -> Card:
        """
        Deal a card from the deck.

        :param i: index of card to pop, pops the last by default
        """
        return self.cards.pop(i)

    def shuffle_deck(self):
        """Shuffle the deck in place."""
        random.shuffle(self.cards)

    def sort_deck(self):
        """Sort the deck in place."""
        self.cards.sort()

    def is_empty(self) -> bool:
        """Check if the deck has any cards."""
        return not self.cards

    def __str__(self):
        """Represent the whole deck as rows of length 4 when printed."""
        return "\n".join(map(' '.join, zip_longest(*[map(str, self.cards)] * 4, fillvalue="")))

    def __repr__(self):
        """
        Lazy representation of the deck.

        Called in the shell and when printing
        the object in a dictionary/tuple/list.
        """
        return str(self.cards)


if __name__ == '__main__':
    # creating a card
    # use integers or characters from Card.RANKS, Card.SUITS
    c1 = Card(13, 2)
    c2 = Card('A', 's', decorated=False, symbols=True)

    # __str__() gives us a nice string when printing
    print(c1)
    print(c2)
    print()

    # getting the rank and suit
    print(c1.rank)
    print(c2.suit)

    # setting the rank and suit
    c1.rank = 5
    c2.suit = 'c'

    # creating a deck of cards
    d = Deck()

    # dealing cards (pop)
    d.deal_card()
    d.deal_card()

    # shuffling the deck
    d.shuffle_deck()
    print()
    print(d)
    print()

    # sorting the deck
    d.sort_deck()
    print(d)
