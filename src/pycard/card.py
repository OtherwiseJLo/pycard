from __future__ import annotations

from typing import NamedTuple
from pycard import RankEnum, SuitEnum

class Card(NamedTuple):
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

    def __ge__(self, other: Card) -> bool:
        return self.rank >= other.rank

    def __repr__(self) -> str:
        return f"{self.rank.name} OF {self.suit.name}"
