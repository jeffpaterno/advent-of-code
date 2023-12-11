import pytest
from camel_cards import get_strength, rank
from typing import Dict, List


@pytest.mark.parametrize('hand, expected', [
    ('12345', 1),
    ('32T3K', 2),
    ('KK677', 3),
    ('KTJJT', 3),
    ('T55J5', 4),
    ('QQQJA', 4),
    ('23332', 5),
    ('33332', 6),
    ('2AAAA', 6),
    ('AAAAA', 7)
])
def test_get_strength(hand: str, expected: int):
    actual = get_strength(hand)
    assert actual == expected


@pytest.mark.parametrize('hands, expected', [
    (['33332', '2AAAA'], {'33332': 2, '2AAAA': 1})
])
def test_rank(hands: List[str], expected: Dict[str, int]):
    actual = rank(hands)
    assert actual == expected
