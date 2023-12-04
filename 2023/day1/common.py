def load(file: str):
    with open(file, mode='r') as file_io:
        for line_raw in file_io:
            line_clean = line_raw.strip()
            if line_clean:
                yield line_clean


def check_digit(c: str) -> bool:
    return c.isdigit() if c else False


def extract(value: str) -> int:
    if not value:
        return 0
    digits = [x for x in value if check_digit(x)]
    return int(''.join((digits[0], digits[-1]))) if digits else 0

