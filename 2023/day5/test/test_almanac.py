from typing import List

import pytest

from almanac import CategoryMap
from almanac.interpret import find


@pytest.mark.parametrize('category_map, num, expected', [
    (CategoryMap(), 1, 1),
    (CategoryMap(maps=['50 98 2', '52 50 48']), 1, 1),
    (CategoryMap(maps=['50 98 2', '52 50 48']), 49, 49),
    (CategoryMap(maps=['50 98 2', '52 50 48']), 50, 52),
    (CategoryMap(maps=['50 98 2', '52 50 48']), 51, 53),
    (CategoryMap(maps=['50 98 2', '52 50 48']), 96, 98),
    (CategoryMap(maps=['50 98 2', '52 50 48']), 97, 99),
    (CategoryMap(maps=['50 98 2', '52 50 48']), 98, 50),
    (CategoryMap(maps=['50 98 2', '52 50 48']), 99, 51),
    (CategoryMap(maps=['50 98 2', '52 50 48']), 100, 100)
])
def test_category_map_translate(category_map: CategoryMap, num: int, expected: int):
    actual = category_map.translate(num)
    assert actual == expected


@pytest.mark.parametrize('category_maps, src, dst, num, expected', [
    ([
         CategoryMap()
     ], 'undefined', 'undefined', 1, 1),
    ([
         CategoryMap(src='seed', dst='soil', maps=['50 98 2', '52 50 48']),
         CategoryMap(src='soil', dst='fertilizer', maps=['0 15 37', '37 52 2', '39 0 15'])
     ], 'seed', 'location', 79, -1),
    ([
         CategoryMap(src='seed', dst='soil', maps=['50 98 2', '52 50 48']),
         CategoryMap(src='soil', dst='fertilizer', maps=['0 15 37', '37 52 2', '39 0 15']),
         CategoryMap(src='fertilizer', dst='water', maps=['49 53 8', '0 11 42', '42 0 7', '57 7 4']),
         CategoryMap(src='water', dst='light', maps=['88 18 7', '18 25 70']),
         CategoryMap(src='light', dst='temperature', maps=['45 77 23', '81 45 19', '68 64 13']),
         CategoryMap(src='temperature', dst='humidity', maps=['0 69 1', '1 0 69']),
         CategoryMap(src='humidity', dst='location', maps=['60 56 37', '56 93 4'])
     ], 'seed', 'location', 79, 82),
    ([
         CategoryMap(src='seed', dst='soil', maps=['50 98 2', '52 50 48']),
         CategoryMap(src='soil', dst='fertilizer', maps=['0 15 37', '37 52 2', '39 0 15']),
         CategoryMap(src='fertilizer', dst='water', maps=['49 53 8', '0 11 42', '42 0 7', '57 7 4']),
         CategoryMap(src='water', dst='light', maps=['88 18 7', '18 25 70']),
         CategoryMap(src='light', dst='temperature', maps=['45 77 23', '81 45 19', '68 64 13']),
         CategoryMap(src='temperature', dst='humidity', maps=['0 69 1', '1 0 69']),
         CategoryMap(src='humidity', dst='location', maps=['60 56 37', '56 93 4'])
     ], 'seed', 'location', 14, 43),
    ([
         CategoryMap(src='seed', dst='soil', maps=['50 98 2', '52 50 48']),
         CategoryMap(src='soil', dst='fertilizer', maps=['0 15 37', '37 52 2', '39 0 15']),
         CategoryMap(src='fertilizer', dst='water', maps=['49 53 8', '0 11 42', '42 0 7', '57 7 4']),
         CategoryMap(src='water', dst='light', maps=['88 18 7', '18 25 70']),
         CategoryMap(src='light', dst='temperature', maps=['45 77 23', '81 45 19', '68 64 13']),
         CategoryMap(src='temperature', dst='humidity', maps=['0 69 1', '1 0 69']),
         CategoryMap(src='humidity', dst='location', maps=['60 56 37', '56 93 4'])
     ], 'seed', 'location', 55, 86),
    ([
         CategoryMap(src='seed', dst='soil', maps=['50 98 2', '52 50 48']),
         CategoryMap(src='soil', dst='fertilizer', maps=['0 15 37', '37 52 2', '39 0 15']),
         CategoryMap(src='fertilizer', dst='water', maps=['49 53 8', '0 11 42', '42 0 7', '57 7 4']),
         CategoryMap(src='water', dst='light', maps=['88 18 7', '18 25 70']),
         CategoryMap(src='light', dst='temperature', maps=['45 77 23', '81 45 19', '68 64 13']),
         CategoryMap(src='temperature', dst='humidity', maps=['0 69 1', '1 0 69']),
         CategoryMap(src='humidity', dst='location', maps=['60 56 37', '56 93 4'])
     ], 'seed', 'location', 13, 35)
])
def test_interpret_find(category_maps: List[CategoryMap], src: str, dst: str, num: int, expected: int):
    actual = find(src, dst, num, category_maps)
    assert actual == expected
