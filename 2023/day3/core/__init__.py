import re
from typing import Iterable, Tuple


def load(file: str):
    with open(file, mode='r') as file_io:
        for line_raw in file_io:
            line_clean = line_raw.strip()
            if line_clean:
                yield line_clean


def extract_numbers(value: str) -> Iterable[Tuple[int, Tuple[int, int]]]:
    for m in re.finditer('(\d+)', value):
        if m.groups():
            num, *g = m.groups()
            yield int(num), m.span()


def extract_symbols(value: str) -> Iterable[Tuple[str, Tuple[int, int]]]:
    for m in re.finditer('([^\.\d]+)', value):
        if m.groups():
            sym, *g = m.groups()
            yield sym, m.span()
