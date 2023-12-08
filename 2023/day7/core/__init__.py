from typing import Iterable


def load(file: str) -> Iterable[str]:
    with open(file, mode='r') as file_io:
        for line_raw in file_io:
            line_clean = line_raw.strip()
            if line_clean:
                yield line_clean
