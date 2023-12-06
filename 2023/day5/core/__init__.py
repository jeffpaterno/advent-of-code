import re
from typing import Iterable, List, Tuple


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
