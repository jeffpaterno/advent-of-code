from typing import Iterable


class Constraints:
    def __init__(self, *args, **kwargs):
        self._red = kwargs.get('red', 0)
        self._green = kwargs.get('green', 0)
        self._blue = kwargs.get('blue', 0)

    def __eq__(self, other):
        return self.red == other.red and self.green == other.green and self.blue == other.blue

    @property
    def red(self) -> int:
        return self._red

    @property
    def green(self) -> int:
        return self._green

    @property
    def blue(self) -> int:
        return self._blue


class Game:
    def __init__(self, *args, **kwargs):
        self._id = kwargs.get('id', 0)
        self._subsets = kwargs.get('subsets', [])

    @property
    def id(self) -> int:
        return self._id

    @property
    def subsets(self) -> Iterable[Constraints]:
        return self._subsets
