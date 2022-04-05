from pycard.deck import Deck
import pytest


def test_deck_successfully_initialized():
    """Assert that the starting card size if 52"""
    deck = Deck()
    assert len(deck) == 52


def test_deck_draw_card():
    """Assert that drawing a card reduces the size of the deck"""
    deck = Deck()
    for i in range(1, 53):
        deck.draw()
        assert len(deck) == 52 - i


def test_deck_draw_card_from_empty_deck_raises_exception():
    """Assert that attempting to draw a card from an empty deck raises an exception"""
    deck = Deck()
    for _ in range(52):
        deck.draw()
    with pytest.raises(ValueError):
        deck.draw()


def test_deck_shuffle():
    """Assert the shuffled deck cards do not match the ordered deck cards"""
    ordered_deck = Deck()
    shuffled_deck = Deck()
    shuffled_deck.shuffle()

    same_count = 0
    for card_a, card_b in zip(ordered_deck.cards, shuffled_deck.cards):
        same_count += int(card_a == card_b)
    assert same_count < 52
