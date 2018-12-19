"""Golf solitaire."""
from itertools import zip_longest
from textwrap import dedent
from cards import Deck


class Solitaire:
    """
    Solitaire class representing a game of Golf Solitaire.

    This game has 7 columns and 5 cards in each column,
    but the methods should work with other valid values as well.
    """

    cards_in_column = 1
    columns = 1

    def __init__(self):
        """
        Constructor, do the setup here.

        After setup with Solitaire.columns = 7, Solitaire.cards_in_column = 5
        You should have:
        self.tableau -> 7 columns of cards with 5 cards in each column
        self.stock -> 16 cards
        self.waste -> 1 card
        """
        self.deck = Deck()  # -> Deck instance
        self.deck.shuffle_deck()
        self.tableau = [[self.deck.deal_card() for cards in range(self.cards_in_column)] for x in range(self.columns)]  # -> list of (columns[lists] (where each list -> cards_in_column * Card instances))
        self.waste = [self.deck.deal_card()]  # -> list of Card instances
        self.stock = [self.deck.deal_card() for cards in range(3 - (self.columns * self.cards_in_column + 1))]  # ->
        # list of Card instances
        # print(self.tableau)
        # print(self.waste)
        # print(self.stock)
        # print()

    def can_move(self, card) -> bool:
        """
        Validate if a card from the tableau can be moved to the waste pile.

        The card must be last in the column list and adjacent by rank
        to the topmost card of the waste pile (last in waste list).
        Example: 8 is adjacent to 7 and 9. Ace is only adjacent to 2.
        King is only adjacent to Queen.
        """
        card_in_last_columns_check = False
        for column in self.tableau:
            if column and column[-1] == card:
                card_in_last_columns_check = True
                break
        if not card_in_last_columns_check:
            print("Card not last in any column!")
            return False
        value_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
        if str(card)[1] == "A" and str(self.waste[-1])[1] == "2" or str(card)[1] == "K" and str(self.waste[-1])[1] == "Q":
            return True
        elif str(card)[1] in value_list[1:-1]:
            index = value_list.index(str(card)[1])
            if str(self.waste[-1])[1] == value_list[index - 1] or str(self.waste[-1])[1] == value_list[index + 1]:
                return True
        print("That move can not be made!")  # Will also be printed if stock is empty and lose cond is being checked.
        return False

    def move_card(self, col: int):
        """
        Move a card from the tableau to the waste pile.

        Does not validate the move.
        :param col: index of column
        """
        self.waste.append(self.tableau[col].pop(-1))

    def deal_from_stock(self):
        """
        Deal last card from stock pile to the waste pile.

        If the stock is empty, do nothing.
        """
        if not self.stock:
            pass
        else:
            self.waste.append(self.stock.pop(-1))

    def has_won(self) -> bool:
        """Check for the winning position - no cards left in tableau."""
        if self.tableau == [[]for x in range(self.columns)]:
            return True
        return False

    def has_lost(self) -> bool:
        """
        Check for the losing position.

        Losing position: no cards left in stock and no possible moves.
        """
        if len(self.stock) == 0 and not self.available_moves():
            return True
        return False

    def available_moves(self) -> bool:
        """Check for possible moves in all tableau columns. Return True if any exist."""
        for column in self.tableau:
            if column and self.can_move(column[-1]):
                return True
        return False

    def print_game(self):
        """
        Print the game.

        Assumes:
        Card(decorated=True) by default it is already set to True
        self.tableau -> a list of lists (each list represents a column of cards)
        self.stock -> a list of Card objects that are in the stock
        self.waste_pile -> a list of Card objects that are in the waste pile

        You may modify/write your own print_game.
        """
        print(f" {'    '.join(list('0123456'))}")
        print('-' * 34)
        print("\n".join([(" ".join((map(str, x)))) for x in (zip_longest(*self.tableau, fillvalue="    "))]))
        print()
        print(f"Stock pile: {len(self.stock)} card{'s' if len(self.stock) != 1 else ''}")
        print(f"Waste pile: {self.waste[-1] if self.waste else 'Empty'}")

    @staticmethod
    def rules():
        """Print the rules of the game."""
        print("Rules".center(40, "-"))
        print(dedent("""
                Objective: Move all the cards from each column to the waste pile.

                A card can be moved from a column to the waste pile if the
                rank of that card is one higher or lower than the topmost card
                of the waste pile. Only the first card of each column can be moved.

                You can deal cards from the stock to the waste pile.
                The game is over if the stock is finished and
                there are no more moves left.

                The game is won once the tableau is empty.

                Commands:
                  (0-6) - integer of the column, where the topmost card will be moved
                  (d) - deal a card from the stock
                  (r) - show rules
                  (q) - quit
                  """))

    @staticmethod
    def convert_str_of_int_to_int(command):
        """Convert string of int to int if possible. Return converted command/nonconvertible command, True/False."""
        try:
            return int(command), True
        except ValueError:
            return command, False

    def play(self):
        """
        Play a game of Golf Solitaire.

        Create the game loop here.
        Use input() for player input.
        Available commands are described in rules().
        """
        while True:
            # print(self.stock)
            self.print_game()
            command = input("Next move:").lower()
            command, conversion_success = self.convert_str_of_int_to_int(command)
            if conversion_success and 0 <= command < self.columns and self.can_move(self.tableau[command][-1]):
                self.move_card(command)
            elif command == "d" and self.stock:
                self.waste.append(self.stock.pop(-1))
            elif command == "r":
                self.rules()
                continue
            elif command == "q":
                break
            else:
                print("Invalid input")
                continue
            if self.has_won():
                print("You won!")
                break
            if self.has_lost():
                print("Game over, You lost!")
                break


if __name__ == '__main__':
    s = Solitaire()
    s.play()
