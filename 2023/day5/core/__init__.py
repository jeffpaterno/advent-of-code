import re
from typing import Iterable, List, Tuple
from itertools import islice


def load(file: str) -> Iterable[str]:
    with open(file, mode='r') as file_io:
        for line_raw in file_io:
            line_clean = line_raw.strip()
            if line_clean:
                yield line_clean


def is_seeds(value: str) -> bool:
    if re.match('(seeds\\:).*', value):
        return True
    return False


def extract_seeds(value: str) -> List[int]:
    return list(map(int, value.strip('seeds:').split()))


def extract_seeds_ranges(value: str) -> Iterable[Tuple[int, int]]:
    it = iter(map(int, value.strip('seeds:').split()))
    while batch := tuple(islice(it, 2)):
        yield batch


def extract_seeds_all(value: str) -> Iterable[int]:
    return [i for r in extract_seeds_ranges(value) for i in range(r[0], r[0] + r[1])]


def is_category_map(value: str) -> bool:
    if re.match('(\\w+-to-\\w+\\smap\:)', value):
        return True
    return False


def extract_category_map(value: str) -> Tuple[str, str]:
    regex = re.compile('(?:(\\w+)-to-(\\w+)\\smap\\:)')
    search = regex.search(value)
    if search:
        return search.groups()
    return None
