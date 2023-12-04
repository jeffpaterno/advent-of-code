from sys import argv

from card import Card
from core import load, extract_card_id, extract_numbers

if __name__ == '__main__':
    script, puzzle_input, *a = argv
    scores = []
    for puzzle_line in load(puzzle_input):
        card_id = extract_card_id(puzzle_line)
        nums_win, nums = extract_numbers(puzzle_line)
        c = Card(id=card_id, winning_numbers=nums_win, numbers=nums)
        scores.append(c.get_score())
    print(sum(scores))
    print('done')
