from typing import List, Tuple

import pytest

from core import is_seeds, is_category_map, extract_seeds, extract_category_map


@pytest.mark.parametrize('value, expected', [
    ('', False),
    ('seeds: 79 14 55 13', True),
    ('seed-to-soil map:', False),
    ('50 98 2', False),
    ('52 50 48', False)
])
def test_is_seeds(value: str, expected: bool):
    actual = is_seeds(value)
    assert actual == expected


@pytest.mark.parametrize('value, expected', [
    ('', False),
    ('seeds: 79 14 55 13', False),
    ('seed-to-soil map:', True),
    ('50 98 2', False),
    ('52 50 48', False)
])
def test_is_category_map(value: str, expected: bool):
    actual = is_category_map(value)
    assert actual == expected


@pytest.mark.parametrize('value, expected', [
    ('', []),
    ('seeds: 79 14 55 13', [79, 14, 55, 13])
])
def test_extract_seeds(value: str, expected: List[int]):
    actual = extract_seeds(value)
    assert actual == expected


@pytest.mark.parametrize('value, expected', [
    ('', None),
    ('seed-to-soil map:', ('seed', 'soil')),
    ('soil-to-fertilizer map:', ('soil', 'fertilizer')),
    ('fertilizer-to-water map:', ('fertilizer', 'water'))
])
def test_extract_category_map(value: str, expected: Tuple[str, str]):
    actual = extract_category_map(value)
    assert actual == expected
