from typing import List

import pytest

from cubes import Constraints, Game
from cubes.solve import is_game_possible, get_possible_games, find_fewest_cubes


@pytest.mark.parametrize('game, rules, expected', [
    (Game(subsets=[Constraints(red=0, green=0, blue=0)]), Constraints(red=0, green=0, blue=0), True),
    (Game(subsets=[Constraints(red=1, green=0, blue=0)]), Constraints(red=1, green=1, blue=1), True),
    (Game(subsets=[Constraints(red=0, green=1, blue=0)]), Constraints(red=1, green=1, blue=1), True),
    (Game(subsets=[Constraints(red=0, green=0, blue=1)]), Constraints(red=1, green=1, blue=1), True),
    (Game(subsets=[Constraints(red=1, green=0, blue=0)]), Constraints(red=0, green=0, blue=0), False),
    (Game(subsets=[Constraints(red=0, green=1, blue=0)]), Constraints(red=0, green=0, blue=0), False),
    (Game(subsets=[Constraints(red=0, green=0, blue=1)]), Constraints(red=0, green=0, blue=0), False),
    (Game(subsets=[Constraints(red=4, green=0, blue=3)]), Constraints(red=12, green=13, blue=14), True),
    (Game(subsets=[Constraints(red=20, green=8, blue=6)]), Constraints(red=12, green=13, blue=14), False)
])
def test_is_game_possible(game: Game, rules: Constraints, expected: bool):
    actual = is_game_possible(game, rules)
    assert actual == expected


@pytest.mark.parametrize('games, rules, expected', [
    ([],
     Constraints(red=0, green=0, blue=0),
     []),
    ([Game(id=1, subsets=[Constraints(red=4, blue=3),
                          Constraints(red=1, green=2, blue=6),
                          Constraints(green=2)])],
     Constraints(red=12, green=13, blue=14),
     [1]),
    ([Game(id=1, subsets=[Constraints(red=4, blue=3),
                          Constraints(red=1, green=2, blue=6),
                          Constraints(green=2)]),
      Game(id=2, subsets=[Constraints(green=2, blue=1),
                          Constraints(red=1, green=3, blue=4),
                          Constraints(green=1, blue=1)]),
      Game(id=3, subsets=[Constraints(red=20, green=8, blue=6),
                          Constraints(red=4, green=13, blue=5),
                          Constraints(red=1, green=5)]),
      Game(id=4, subsets=[Constraints(red=3, green=1, blue=6),
                          Constraints(red=6, green=3),
                          Constraints(red=14, green=3, blue=15)]),
      Game(id=5, subsets=[Constraints(red=6, green=3, blue=1),
                          Constraints(red=1, green=2, blue=2)])],
     Constraints(red=12, green=13, blue=14),
     [1, 2, 5])
])
def test_get_possible_games(games: List[Game], rules: Constraints, expected: List[int]):
    actual = list(get_possible_games(games, rules))
    assert actual == expected


@pytest.mark.parametrize('game, expected', [
    (Game(id=1, subsets=[Constraints(red=4, blue=3),
                         Constraints(red=1, green=2, blue=6),
                         Constraints(green=2)]),
     Constraints(red=4, green=2, blue=6)),
    (Game(id=2, subsets=[Constraints(green=2, blue=1),
                         Constraints(red=1, green=3, blue=4),
                         Constraints(green=1, blue=1)]),
     Constraints(red=1, green=3, blue=4)),
    (Game(id=3, subsets=[Constraints(red=20, green=8, blue=6),
                         Constraints(red=4, green=13, blue=5),
                         Constraints(red=1, green=5)]),
     Constraints(red=20, green=13, blue=6)),
    (Game(id=4, subsets=[Constraints(red=3, green=1, blue=6),
                         Constraints(red=6, green=3),
                         Constraints(red=14, green=3, blue=15)]),
     Constraints(red=14, green=3, blue=15)),
    (Game(id=5, subsets=[Constraints(red=6, green=3, blue=1),
                         Constraints(red=1, green=2, blue=2)]),
     Constraints(red=6, green=3, blue=2))
])
def test_find_fewest_cubes(game: Game, expected: Constraints):
    actual = find_fewest_cubes(game=game)
    assert actual == expected
