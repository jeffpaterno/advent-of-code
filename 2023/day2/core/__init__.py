import re
from typing import Iterable


def load(file: str):
    with open(file, mode='r') as file_io:
        for line_raw in file_io:
            line_clean = line_raw.strip()
            if line_clean:
                yield line_clean


def extract_game_id(value: str) -> int:
    game_regex = re.compile('(?:Game\s)(\d*)(?:\:)')
    game_search = game_regex.search(value)
    if game_search:
        game_id, *x = game_search.groups()
        return int(game_id)
    return 0


def extract_subsets(value: str) -> Iterable[str]:
    subsets_regex = re.compile('(?:Game\s\d*\:\s)(.*)')
    subsets_search = subsets_regex.search(value)
    if subsets_search:
        subsets, *x = subsets_search.groups()
        return subsets.split(';')
    return []


def extract_color(value: str, color: str) -> int:
    color_regex = re.compile(f'(\d*)\s(?:{color})')
    color_search = color_regex.search(value)
    if color_search:
        color, *x = color_search.groups()
        return int(color)
    return 0
