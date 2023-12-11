from sys import argv

from cartography import navigate
from core import load, extract

if __name__ == '__main__':
    script, puzzle_input, *x = argv
    instructions = None
    nodes = {}
    for puzzle_line in load(puzzle_input):
        if not instructions:
            instructions = puzzle_line
        else:
            node, left, right = extract(puzzle_line)
            nodes[node] = {'left': left, 'right': right}
    steps = navigate(instructions, nodes)
    print(f'steps: {steps}')
    print('done')
