from __future__ import annotations

from enum import IntEnum
from typing import NamedTuple


class Rank(IntEnum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Suit(IntEnum):
    SPADES = 1
    CLUBS = 2
    DIAMONDS = 3
    HEARTS = 4


class Card(NamedTuple):
    rank: Rank
    suit: Suit

    def __ge__(self, other: Card) -> bool:
        return self.rank >= other.rank

    def __repr__(self) -> str:
        return f"{self.rank.name} OF {self.suit.name}"
