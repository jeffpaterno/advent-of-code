import pytest

from card import Card


@pytest.mark.parametrize('card, expected', [
    (Card(), 0),
    (Card(id=1, winning_numbers={}, numbers={}), 0),
    (Card(id=2, winning_numbers={1, 2, 3}, numbers={4, 5, 6}), 0),
    (Card(id=3, winning_numbers={1, 2, 3}, numbers={1, 5, 6}), 1),
    (Card(id=4, winning_numbers={1, 2, 3}, numbers={1, 2, 6}), 2),
    (Card(id=5, winning_numbers={1, 2, 3}, numbers={1, 2, 3}), 4),
    (Card(id=6, winning_numbers={1, 2, 3, 4, 5, 6}, numbers={1, 2, 3, 4}), 8)
])
def test_get_score(card: Card, expected: int):
    actual = card.get_score()
    assert actual == expected


@pytest.mark.parametrize('card, expected', [
    (Card(), 0),
    (Card(id=1, winning_numbers={41, 48, 83, 86, 17}, numbers={83, 86, 6, 31, 17, 9, 48, 53}), 4),
    (Card(id=2, winning_numbers={13, 32, 20, 16, 61}, numbers={61, 30, 68, 82, 17, 32, 24, 19}), 2),
    (Card(id=3, winning_numbers={1, 21, 53, 59, 44}, numbers={69, 82, 63, 72, 16, 21, 14, 1}), 2),
    (Card(id=4, winning_numbers={41, 92, 73, 84, 69}, numbers={59, 84, 76, 51, 58, 5, 54, 83}), 1),
    (Card(id=5, winning_numbers={87, 83, 26, 28, 32}, numbers={88, 30, 70, 12, 93, 22, 82, 36}), 0),
    (Card(id=6, winning_numbers={31, 18, 13, 56, 72}, numbers={74, 77, 10, 23, 35, 67, 36, 11}), 0)
])
def test_matching_numbers(card: Card, expected: int):
    actual = card.matching_numbers
    assert len(actual) == expected
