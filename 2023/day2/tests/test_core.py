import pytest
from core import extract_game_id, extract_subsets, extract_color
from typing import List


@pytest.mark.parametrize('line, expected', [
    ('', 0),
    ('Game Bad: 1 red, 1 green, 1 blue; 2 red, 2 green, 2 blue', 0),
    ('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 1),
    ('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', 2),
    ('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', 3),
    ('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', 4),
    ('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green', 5),
    ('Game 10: 3 green, 5 red, 6 blue; 4 blue, 4 red, 5 green; 5 green, 9 red, 5 blue; 4 green, 6 blue, 10 red', 10),
    ('Game 100: 5 green, 11 blue, 6 red; 5 green, 12 blue; 1 green, 14 blue, 1 red; 3 blue, 5 red, 6 green', 100)
])
def test_extract_game_id(line: str, expected: int):
    actual = extract_game_id(line)
    assert actual == expected


@pytest.mark.parametrize('line, expected', [
    ('', [])
])
def test_extract_subsets(line: str, expected: List[str]):
    actual = extract_subsets(line)
    assert actual == expected


@pytest.mark.parametrize('value, color, expected', [
    ('', 'red', 0),
    ('', 'green', 0),
    ('', 'blue', 0),
    ('1 blue', 'red', 0),
    ('1 blue', 'green', 0),
    ('1 blue', 'blue', 1),
    ('1 red', 'red', 1),
    ('1 red', 'green', 0),
    ('1 red', 'blue', 0),
    ('1 green', 'red', 0),
    ('1 green', 'green', 1),
    ('1 green', 'blue', 0),
    ('1 red 2 blue', 'red', 1),
    ('1 red 2 blue', 'green', 0),
    ('1 red 2 blue', 'blue', 2),
    ('2 blue 1 red', 'red', 1),
    ('2 blue 1 red', 'green', 0),
    ('2 blue 1 red', 'blue', 2)
])
def test_extract_color(value: str, color: str, expected: int):
    actual = extract_color(value, color)
    assert actual == expected