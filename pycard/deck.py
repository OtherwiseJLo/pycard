import itertools as it
from random import shuffle
from typing import List

from pycard.card import Card, RankEnum, SuitEnum


class Deck:
    """
    A class used to represent a deck of cards

    ...

    Attributes
    ----------
    cards : List[Card]
        A list of `Card` holding each card in deck

    Methods
    -------
    draw(number_of_cards: int = 1)
        Pops the specified number of cards from self.cards
        Defaults to 1
    shuffle()
        Shuffles the cards list

    """

    def __init__(self):
        """ """
        self.cards = [Card(r, s) for r, s in it.product(RankEnum, SuitEnum)]

    def shuffle(self) -> None:
        """
        Shuffles elements in `self.cards`
        """
        shuffle(self.cards)

    def draw(self, number_of_cards: int = 1) -> List[Card]:
        """
        Pick cards from deck

        Parameters
        ----------
        number_of_cards : int, optional
            Number of cards to draw from deck (default is 1)

        Returns
        -------
        list
            A list of cards drawn from the deck
        """
        if self.cards:
            drawn_cards = self.cards[:number_of_cards]
            self.cards = self.cards[number_of_cards:]
            return drawn_cards
        else:
            raise ValueError("Deck is empty")

    def __len__(self) -> int:
        return len(self.cards)
