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
JOKER = 'J'
CARD_STRENGTHS_JOKER = {'A': 13,
                        'K': 12,
                        'Q': 11,
                        'T': 10,
                        '9': 9,
                        '8': 8,
                        '7': 7,
                        '6': 6,
                        '5': 5,
                        '4': 4,
                        '3': 3,
                        '2': 2,
                        'J': 1}


def replace_joker(hand: str) -> str:
    if not hand or JOKER not in hand:
        return hand
    cards = sorted({c: CARD_STRENGTHS_JOKER[c] for c in hand}.items(),
                   key=lambda item: item[1],
                   reverse=True)
    alt_hands = [hand.replace(JOKER, c[0]) for c in cards]
    alt_hands_scored = {h: get_strength(h) for h in alt_hands}
    best, *rest = sorted(alt_hands_scored.items(),
                         key=lambda item: item[1],
                         reverse=True)
    return best[0] if best else hand


def get_strength(hand: str, use_joker: bool = False) -> int:
    hand = replace_joker(hand) if use_joker else hand
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


def rank(hands: List[str], use_joker: bool = False) -> Dict[str, int]:
    _card_strengths = CARD_STRENGTHS_JOKER if use_joker else CARD_STRENGTHS
    hands_scored = {h: get_strength(h, use_joker) for h in hands}
    hands_ranked = []
    for strength in range(MIN_STRENGTH, MAX_STRENGTH + 1):
        _hands = (h for h, s in hands_scored.items() if s == strength)
        for h in sorted(_hands,
                        key=lambda ele: sum((100 ** (5 - i)) * _card_strengths.get(c, 0) for i, c in enumerate(ele))):
            hands_ranked.append(h)
    return {h: i + 1 for i, h in enumerate(hands_ranked)}
