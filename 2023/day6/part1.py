from sys import argv
from core import extract, is_distances, is_times, load
from race import get_possible
import math

if __name__ == '__main__':
    script, puzzle_input, *a = argv
    for puzzle_line in load(puzzle_input):
        if is_times(puzzle_line):
            times = list(extract(puzzle_line, 'Time'))
        elif is_distances(puzzle_line):
            distances = list(extract(puzzle_line, 'Distance'))
    possibilities = [list(get_possible(t, distances[i])) for i, t in enumerate(times)]
    print(math.prod(len(p) for p in possibilities))
    print('done')
