from typing import List, Tuple

import pytest

from core import extract_category_map, extract_seeds, extract_seeds_all, extract_seeds_ranges, is_category_map, is_seeds


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
    ('', []),
    ('seeds: 79 14 55 13', [(79, 14), (55, 13)]),
    ('seeds: 3121711159 166491471 3942191905 154855415 3423756552 210503354', [(3121711159, 166491471),
                                                                               (3942191905, 154855415),
                                                                               (3423756552, 210503354)])
])
def test_extract_seed_ranges(value: str, expected: List[Tuple[int, int]]):
    actual = list(extract_seeds_ranges(value))
    assert actual == expected


@pytest.mark.parametrize('value, expected', [
    ('', []),
    ('seeds: 79 14 55 13', [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67])
])
def test_extract_seeds_all(value: str, expected: List[int]):
    actual = extract_seeds_all(value)
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
