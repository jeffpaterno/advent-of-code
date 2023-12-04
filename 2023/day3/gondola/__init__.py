from typing import Iterable, Tuple


class SchematicEntry:
    def __init__(self, *args, **kwargs):
        r = kwargs.get('row', -1)
        if r < 0:
            raise ValueError('must be non-negative int(): \'row\'')
        self._row = r
        c = kwargs.get('col', -1)
        if c < 0:
            raise ValueError('must be non-negative int(): \'col\'')
        self._col = c

    @property
    def row(self) -> int:
        return self._row

    @property
    def column(self) -> int:
        return self._col

    @property
    def row_bounds(self) -> Tuple[int, int]:
        return self.row, self.row

    @property
    def column_bounds(self):
        return self.column, self.column


class Part(SchematicEntry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        n = kwargs.get('num', -1)
        if n < 0:
            raise ValueError('must be non-negative int(): \'num\'')
        self._num = n

    def __eq__(self, other):
        return self.number == other.number and self.number_length == other.number_length and self.row == other.row and self.column == other.column

    @property
    def number(self) -> int:
        return self._num

    @property
    def number_length(self) -> int:
        return len(str(self._num))

    @property
    def column_bounds(self):
        return self.column, self.column + self.number_length - 1


class Symbol(SchematicEntry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sym = kwargs.get('sym', '')

    @property
    def symbol(self):
        return self._sym
