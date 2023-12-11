from typing import Dict, List

import pytest

from camel_cards import get_strength, rank, replace_joker


@pytest.mark.parametrize('hand, use_joker, expected', [
    ('12345', False, 1),
    ('32T3K', False, 2),
    ('KK677', False, 3),
    ('KTJJT', False, 3),
    ('KTJJT', True, 6),
    ('T55J5', False, 4),
    ('T55J5', True, 6),
    ('QQQJA', False, 4),
    ('QQQJA', True, 6),
    ('23332', False, 5),
    ('33332', False, 6),
    ('2AAAA', False, 6),
    ('AAAAA', False, 7)
])
def test_get_strength(hand: str, use_joker: bool, expected: int):
    actual = get_strength(hand, use_joker)
    assert actual == expected


@pytest.mark.parametrize('hands, expected', [
    (['33332', '2AAAA'], {'33332': 2, '2AAAA': 1})
])
def test_rank(hands: List[str], expected: Dict[str, int]):
    actual = rank(hands)
    assert actual == expected


@pytest.mark.parametrize('hand, expected', [
    ('32T3K', '32T3K'),
    ('KK677', 'KK677'),
    ('T55J5', 'T5555'),
    ('KTJJT', 'KTTTT'),
    ('QQQJA', 'QQQQA'),
    ('JJJJJ', 'JJJJJ')
])
def test_replace_joker(hand: str, expected: str):
    actual = replace_joker(hand)
    assert actual == expected
