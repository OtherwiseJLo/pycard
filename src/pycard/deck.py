import itertools as it
from enum import EnumMeta, IntEnum
from random import shuffle
from typing import Iterator, List, Tuple

from pycard.card import Card
from pycard import RankEnum, SuitEnum


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
    def __init__(self, rank: RankEnum, suit: SuitEnum):
        """
        """
        self.cards = [Card(r, s) for r, s in it.product(rank, suit)]

    def shuffle(self) -> None:
        """
        Shuffles elements in `self.cards`
        """
        shuffle(self.cards)

    def draw(self, number_of_cards: int=1) -> List[Card]:
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
        drawn_cards = self.cards[:number_of_cards]
        self.cards = self.cards[number_of_cards:]
        return drawn_cards
