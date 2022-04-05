from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum


class RankEnum(IntEnum):
    """
    Enum class holding rank enums
    """
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


class SuitEnum(IntEnum):
    """
    Enum class holding suit enums
    """
    SPADES = 1
    CLUBS = 2
    DIAMONDS = 3
    HEARTS = 4


@dataclass(order=True, frozen=True, slots=True)
class Card:
    """
    A class to represent a playing card

    ...

    Attributes
    ----------
    rank : EnumMeta
        An enum object with card rank
    suit : EnumMeta
        An enum object with card suit
    """
    rank: RankEnum
    suit: SuitEnum

    # def __ge__(self, other: Card) -> bool:
    #     return self.rank >= other.rank

    def __repr__(self) -> str:
        return f"{self.rank.name} OF {self.suit.name}"
