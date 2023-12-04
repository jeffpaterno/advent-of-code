from typing import Tuple, Set

import pytest

from core import extract_card_id, extract_numbers


@pytest.mark.parametrize('line, expected', [
    ('', 0),
    ('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53', 1),
    ('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19', 2),
    ('Card 12:  1 21 53 59 44 | 69 82 63 72 16 21 14  1', 12),
    ('Card 1234: 41 92 73 84 69 | 59 84 76 51 58  5 54 83', 1234),
    ('Card   1: 81  1 43 40 49 51 38 65 36  4 | 21 15  1 43 60  9 83 81 35 49 40 38 82 65 20  4 58 94 16 89 84 10 77 48 76', 1)
])
def test_extract_game_id(line: str, expected: int):
    actual = extract_card_id(line)
    assert actual == expected


@pytest.mark.parametrize('line, expected', [
    ('', ({}, {})),
    ('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53', ({41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53}))
])
def test_extract_numbers(line: str, expected: Tuple[Set[int], Set[int]]):
    actual = extract_numbers(line)
    assert actual == expected
