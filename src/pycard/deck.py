import itertools as it
from collections.abc import MutableSequence

from pycard.card import Card, Rank, Suit


class Deck(MutableSequence[Card]):
    def __init__(self):
        self.elements = [Card(rank, suit) for rank, suit in it.product(Rank, Suit)]
