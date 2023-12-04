import sys

from common import load, extract, check_digit

_translations = {'one': '1',
                 'two': '2',
                 'three': '3',
                 'four': '4',
                 'five': '5',
                 'six': '6',
                 'seven': '7',
                 'eight': '8',
                 'nine': '9'}


def convert(value: str) -> str:
    value_conv = ''
    idx = 0
    while idx < len(value):
        move = 1
        val = value[idx]
        if check_digit(val):
            value_conv += val  # Take the digit
        else:
            for key_len in {len(k) for k in _translations.keys()}:
                d = _translations.get(value[idx:idx + key_len])
                if d and idx + key_len <= len(value):
                    value_conv += d  # Take the converted spelled out digit
                    move = key_len - 1  # Skip ahead past the recognized spelled out digit
        idx += move
    return value_conv


if __name__ == '__main__':
    total = 0
    for line in load('input.txt'):
        line_conv = convert(line)
        calibration_value = extract(line_conv)
        total += calibration_value
        print(f'line = "{line}", line_conv = "{line_conv}", calibration_value = {calibration_value}')
    print(total)
