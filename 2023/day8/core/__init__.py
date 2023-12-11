import re
from typing import Iterable, List


def load(file: str) -> Iterable[str]:
    with open(file, mode='r') as file_io:
        for line_raw in file_io:
            line_clean = line_raw.strip()
            if line_clean:
                yield line_clean


def extract(value: str) -> List[str]:
    return [it.group() for it in re.finditer('(\\w{3})', value)]
