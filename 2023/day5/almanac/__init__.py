from functools import cache


class Seed:
    def __init__(self, *args, **kwargs) -> None:
        self._id = kwargs.get('id', 0)

    @property
    def id(self) -> int:
        return self._id


class CategoryMap:
    def __init__(self, *args, **kwargs) -> None:
        self._src = kwargs.get('src', 'undefined')
        self._dst = kwargs.get('dst', 'undefined')
        self._maps_raw = kwargs.get('maps', [])
        self._maps = [list(map(int, m.split())) for m in self._maps_raw]

    @property
    def source(self) -> str:
        return self._src
    
    @property
    def destination(self) -> str:
        return self._dst

    @cache
    def translate(self, num: int) -> int:
        for m in self._maps:
            dst_start, src_start, delta, *x = m
            if src_start <= num < (src_start + delta):
                return num - src_start + dst_start
        return num
