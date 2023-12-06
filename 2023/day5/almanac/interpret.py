from typing import List

from . import CategoryMap


def find(src: str, dst: str, num: int, category_maps: List[CategoryMap]) -> int:
    if src == dst:
        return num
    _curr = next((m for m in category_maps if m.source == src), None)
    _num = num
    while _curr and _curr.destination != dst:
        _num = _curr.translate(_num)  # translate before moving to the next category map
        _curr = next((m for m in category_maps if m.source == _curr.destination), None)
    if _curr and _curr.destination == dst:
        return _curr.translate(_num)
    return _curr.translate(_num) if _curr and _curr.destination == dst else -1
