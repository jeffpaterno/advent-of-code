from sys import argv

from camel_cards import rank
from core import load

if __name__ == '__main__':
    script, puzzle_input, *x = argv
    hands = []
    bids = {}
    strengths = {}
    for puzzle_line in load(puzzle_input):
        hand, bid = puzzle_line.split()
        hands.append(hand)
        bids[hand] = int(bid)
    rankings = rank(hands)
    total_winnings = sum(bids.get(h, 0) * rankings.get(h, 0) for h in hands)
    print(total_winnings)
    print('done')
