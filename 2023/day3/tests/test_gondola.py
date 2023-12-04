from typing import List, Tuple

import pytest

from gondola import Part, Symbol
from gondola.engine import get_engine_parts, get_gear_ratios


@pytest.mark.parametrize('parts, symbols, expected', [
    ([], [], []),
    ([Part(num=1, row=0, col=0)],
     [Symbol(sym='*', row=1, col=0)],
     [Part(num=1, row=0, col=0)]),
    ([Part(num=467, row=0, col=0),
      Part(num=114, row=0, col=5),
      Part(num=35, row=2, col=2),
      Part(num=633, row=2, col=6),
      Part(num=617, row=4, col=0),
      Part(num=58, row=5, col=7),
      Part(num=592, row=6, col=2),
      Part(num=755, row=7, col=6),
      Part(num=664, row=9, col=1),
      Part(num=598, row=9, col=5)],
     [Symbol(sym='*', row=1, col=3),
      Symbol(sym='#', row=3, col=6),
      Symbol(sym='*', row=4, col=3),
      Symbol(sym='+', row=5, col=5),
      Symbol(sym='$', row=8, col=3),
      Symbol(sym='*', row=8, col=5)],
     [Part(num=467, row=0, col=0),
      Part(num=35, row=2, col=2),
      Part(num=633, row=2, col=6),
      Part(num=617, row=4, col=0),
      Part(num=592, row=6, col=2),
      Part(num=755, row=7, col=6),
      Part(num=664, row=9, col=1),
      Part(num=598, row=9, col=5)])
])
def test_get_engine_parts(parts: List[Part], symbols: List[Symbol], expected: List[Part]):
    actual = list(get_engine_parts(parts, symbols))
    assert actual == expected


@pytest.mark.parametrize('parts, symbols, expected', [
    ([], [], []),
    ([Part(num=467, row=0, col=0),
      Part(num=114, row=0, col=5),
      Part(num=35, row=2, col=2),
      Part(num=633, row=2, col=6),
      Part(num=617, row=4, col=0),
      Part(num=58, row=5, col=7),
      Part(num=592, row=6, col=2),
      Part(num=755, row=7, col=6),
      Part(num=664, row=9, col=1),
      Part(num=598, row=9, col=5)],
     [Symbol(sym='*', row=1, col=3),
      Symbol(sym='#', row=3, col=6),
      Symbol(sym='*', row=4, col=3),
      Symbol(sym='+', row=5, col=5),
      Symbol(sym='$', row=8, col=3),
      Symbol(sym='*', row=8, col=5)],
     [(467, 35),
      (755, 598)])
])
def test_get_gear_ratios(parts: List[Part], symbols: List[Symbol], expected: List[Tuple[int, int]]):
    actual = list(get_gear_ratios(parts, symbols))
    assert actual == expected
