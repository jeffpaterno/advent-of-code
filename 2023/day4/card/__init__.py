from typing import Set


class Card:
    def __init__(self, *args, **kwargs):
        self._id = kwargs.get('id', -1)
        self._winning_numbers = kwargs.get('winning_numbers', set())
        self._numbers = kwargs.get('numbers', set())

    def __eq__(self, other):
        return self.id == other.id and self.winning_numbers == other.winning_numbers and self.numbers == other.numbers

    @property
    def id(self):
        return self._id

    @property
    def winning_numbers(self) -> Set[int]:
        return self._winning_numbers

    @property
    def numbers(self) -> Set[int]:
        return self._numbers

    @property
    def matching_numbers(self) -> Set[int]:
        return {n for n in self.numbers if n in self.winning_numbers}

    @property
    def winnings(self) -> Set[int]:
        return {self.id + i for i in range(1, len(self.matching_numbers) + 1)}

    def get_score(self):
        matches = self.matching_numbers
        return 2 ** (len(matches) - 1) if matches else 0
