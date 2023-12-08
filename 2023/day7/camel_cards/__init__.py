from typing import Dict, List

MIN_STRENGTH = 1
MAX_STRENGTH = 7
CARD_STRENGTHS = {'A': 13,
                  'K': 12,
                  'Q': 11,
                  'J': 10,
                  'T': 9,
                  '9': 8,
                  '8': 7,
                  '7': 6,
                  '6': 5,
                  '5': 4,
                  '4': 3,
                  '3': 2,
                  '2': 1}


def get_strength(hand: str) -> int:
    g = {c: hand.count(c) for c in hand}
    v = set(g.values())
    if {5} == v:
        return 7  # five of a kind
    elif {1, 4} == v:
        return 6  # four of a kind
    elif {2, 3} == v:
        return 5  # full house
    elif {1, 3} == v:
        return 4  # three of a kind
    elif {1, 2} == v and len(g.keys()) == 3:
        return 3  # two pair
    elif {1, 2} == v:
        return 2  # one pair
    return 1


def get_multiplier(i: int) -> int:
    return 10 ** (5 - i)


def rank(hands: List[str]) -> Dict[str, int]:
    hands_scored = {h: get_strength(h) for h in hands}
    hands_ranked = []
    for strength in range(MIN_STRENGTH, MAX_STRENGTH + 1):
        _hands = (h for h, s in hands_scored.items() if s == strength)
        for h in sorted(_hands, key=lambda ele: sum((10**(5 - i)) * CARD_STRENGTHS.get(c, 0) for i, c in enumerate(ele))):
            hands_ranked.append(h)
    return {h: i + 1 for i, h in enumerate(hands_ranked)}
