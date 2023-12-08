import math
from sys import argv

from core import extract_combo, is_distances, is_times, load
from race import get_possible

if __name__ == '__main__':
    script, puzzle_input, *a = argv
    for puzzle_line in load(puzzle_input):
        if is_times(puzzle_line):
            time = extract_combo(puzzle_line, 'Time')
        elif is_distances(puzzle_line):
            distance = extract_combo(puzzle_line, 'Distance')
    possibilities = list(get_possible(time, distance))
    print(len(possibilities))
    print('done')
