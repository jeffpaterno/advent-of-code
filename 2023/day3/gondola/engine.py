from . import Part, Symbol
from typing import Iterable, Tuple


def get_adjacent_symbols(part: Part, symbols: Iterable[Symbol]) -> Iterable[Symbol]:
    row_lower, row_upper = part.row - 1, part.row + 1
    col_lower, col_upper = part.column - 1, part.column + part.number_length
    return (s for s in symbols if row_lower <= s.row <= row_upper and col_lower <= s.column <= col_upper)


def get_engine_parts(parts: Iterable[Part], symbols: Iterable[Symbol]) -> Iterable[Part]:
    return (p for p in parts if any(get_adjacent_symbols(p, symbols)))


def get_adjacent_parts(symbol: Symbol, parts: Iterable[Part]) -> Iterable[Part]:
    row_lower, row_upper = symbol.row - 1, symbol.row + 1
    col_lower, col_upper = symbol.column - 1, symbol.column + 1
    return (p for p in parts if row_lower <= p.row <= row_upper and (
                col_lower <= p.column <= col_upper or col_lower <= p.column_bounds[1] <= col_upper))


def get_gear_ratios(parts: Iterable[Part], symbols: Iterable[Symbol]) -> Iterable[Tuple[int, int]]:
    for s in (_ for _ in symbols if _.symbol == '*'):
        adjacent_parts = list(get_adjacent_parts(s, parts))
        if len(adjacent_parts) == 2:
            yield adjacent_parts[0].number, adjacent_parts[1].number
