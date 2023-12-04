from common import load, extract


if __name__ == '__main__':
    total = 0
    for line in load('input.txt'):
        calibration_value = extract(line)
        total += calibration_value
    print(total)
