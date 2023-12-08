from sys import maxsize
from typing import List, Dict

from . import CategoryMap


def find(src: str, dst: str, num: int, category_maps: Dict[str, CategoryMap]) -> int:
    if src == dst:
        return num
    _curr = category_maps.get(src)
    _num = num
    while _curr and _curr.destination != dst:
        _num = _curr.translate(_num)  # translate before moving to the next category map
        _curr = category_maps.get(_curr.destination)
    return _curr.translate(_num) if _curr and _curr.destination == dst else maxsize
