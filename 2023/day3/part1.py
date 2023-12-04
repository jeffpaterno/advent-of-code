from sys import argv

from core import load, extract_numbers, extract_symbols
from gondola import Part, Symbol
from gondola.engine import get_engine_parts

if __name__ == '__main__':
    script, puzzle_input, *a = argv
    parts = []
    symbols = []
    row = 0
    for puzzle_line in load(file=puzzle_input):
        parts.extend((Part(num=n[0], row=row, col=n[1][0]) for n in extract_numbers(puzzle_line)))
        symbols.extend((Symbol(sym=s[0], row=row, col=s[1][0]) for s in extract_symbols(puzzle_line)))
        row += 1
    print(sum((p.number for p in get_engine_parts(parts, symbols))))
    print('done')
