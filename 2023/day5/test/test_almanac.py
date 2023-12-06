import pytest

from almanac import CategoryMap


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
