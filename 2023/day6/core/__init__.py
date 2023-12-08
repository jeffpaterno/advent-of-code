import re
from typing import Iterable, List


def load(file: str) -> Iterable[str]:
    with open(file, mode='r') as file_io:
        for line_raw in file_io:
            line_clean = line_raw.strip()
            if line_clean:
                yield line_clean


def is_times(value: str) -> bool:
    if re.match('(Time\\:).*', value):
        return True
    return False


def is_distances(value: str) -> bool:
    if re.match('(Distance\\:).*', value):
        return True
    return False


def extract(value: str, typ: str) -> List[int]:
    return list(map(int, value.strip(f'{typ}:').split()))


def extract_combo(value: str, typ: str) -> int:
    return int(''.join(str(e) for e in extract(value, typ)))
