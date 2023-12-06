from sys import argv

from almanac import Seed, CategoryMap
from core import load, is_seeds, extract_seeds, is_category_map, extract_category_map

if __name__ == '__main__':
    script, puzzle_input, *a = argv

    category_maps = []
    _category_map = None
    _maps = None

    for puzzle_line in load(puzzle_input):
        if is_seeds(puzzle_line):
            seeds = extract_seeds(puzzle_line)
        elif is_category_map(puzzle_line):
            if _category_map:
                category_maps.append(CategoryMap(src=_category_map[0], dst=_category_map[1], maps=_maps))
            _category_map = extract_category_map(puzzle_line)
            _maps = None
        else:
            if not _maps:
                _maps = []
            _maps.append(puzzle_line)
    # don't forget the last category map
    if _category_map:
        category_maps.append(CategoryMap(src=_category_map[0], dst=_category_map[1], maps=_maps))

    print('done')
