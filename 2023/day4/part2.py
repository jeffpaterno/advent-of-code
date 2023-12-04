from collections import defaultdict
from sys import argv

from card import Card
from core import load, extract_card_id, extract_numbers

if __name__ == '__main__':
    script, puzzle_input, *a = argv
    cards = {}
    totals = defaultdict(int)
    for puzzle_line in load(puzzle_input):
        cid = extract_card_id(puzzle_line)
        nums_win, nums = extract_numbers(puzzle_line)
        c = Card(id=cid, winning_numbers=nums_win, numbers=nums)
        cards[cid] = c
        totals[cid] += 1  # track "original" card
        for cp in range(totals[cid]):  # track "copies" of "copies"
            for wid in c.winnings:
                totals[wid] += 1
    print(sum((t for t in totals.values())))
    print('done')
