from sys import argv

import core
from cubes import Game, Constraints
from cubes.solve import get_possible_games, get_power_of_sets

if __name__ == '__main__':
    script, puzzle_input, *a = argv
    games = []
    for game_line in core.load(file=puzzle_input):
        id = core.extract_game_id(value=game_line)
        subsets = core.extract_subsets(value=game_line)
        game = Game(id=id, subsets=[Constraints(red=core.extract_color(value=s, color='red'),
                                                green=core.extract_color(value=s, color='green'),
                                                blue=core.extract_color(value=s, color='blue')) for s in subsets])
        games.append(game)
    possible_games = get_possible_games(games=games, rules=Constraints(red=12, green=13, blue=14))
    print(sum(possible_games))
    print('done')
