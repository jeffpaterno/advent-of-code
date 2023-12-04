import re
from typing import Tuple, Set


def load(file: str):
    with open(file, mode='r') as file_io:
        for line_raw in file_io:
            line_clean = line_raw.strip()
            if line_clean:
                yield line_clean


def extract_card_id(value: str) -> int:
    card_regex = re.compile('(?:Card\s+)(\d*)(?:\:)')
    card_search = card_regex.search(value)
    if card_search:
        card_id, *x = card_search.groups()
        return int(card_id)
    return 0


def extract_numbers(value: str) -> Tuple[Set[int], Set[int]]:
    nums_regex = re.compile('(?:Card\s+\d+\:\s+)(.*)')
    nums_search = nums_regex.search(value)
    if nums_search:
        nums_raw, *x = nums_search.groups()
        nums = [set(map(int, n.split())) for n in nums_raw.split('|')]
        if len(nums) >= 2:
            return nums[0], nums[1]
    return {}, {}
