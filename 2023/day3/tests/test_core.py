from typing import List, Tuple

import pytest

from core import extract_numbers, extract_symbols


@pytest.mark.parametrize('line, expected', [
    ('', []),
    ('467..114..', [(467, (0, 3)), (114, (5, 8))]),
    ('...*......', []),
    ('..35..633.', [(35, (2, 4)), (633, (6, 9))]),
    ('.....+.58.', [(58, (7, 9))])
])
def test_extract_numbers(line: str, expected: List[Tuple[int, Tuple[int, int]]]):
    actual = list(extract_numbers(line))
    assert actual == expected


@pytest.mark.parametrize('line, expected', [
    ('', []),
    ('467..114..', []),
    ('...*......', [('*', (3, 4))]),
    ('..35..633.', []),
    ('.....+.58.', [('+', (5, 6))])
])
def test_extract_symbols(line: str, expected: List[Tuple[str, Tuple[int, int]]]):
    actual = list(extract_symbols(line))
    assert actual == expected
