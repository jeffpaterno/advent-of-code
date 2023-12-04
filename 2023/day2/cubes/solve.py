from typing import Iterable

from . import Constraints, Game


def is_game_possible(game: Game, rules: Constraints) -> bool:
    for s in game.subsets:
        if s.red > rules.red or s.blue > rules.blue or s.green > rules.green:
            return False
    return True


def get_possible_games(games: Iterable[Game], rules: Constraints) -> Iterable[int]:
    for g in games:
        if is_game_possible(g, rules):
            yield g.id


def find_fewest_cubes(game: Game) -> Constraints:
    red, green, blue = 1, 1, 1
    for s in game.subsets:
        red = max(red, s.red)
        green = max(green, s.green)
        blue = max(blue, s.blue)
    return Constraints(red=red, green=green, blue=blue)


def get_power_of_sets(games: Iterable[Game]) -> Iterable[int]:
    for g in games:
        fewest_cubes = find_fewest_cubes(g)
        yield fewest_cubes.red * fewest_cubes.green * fewest_cubes.blue
