from typing import Iterable


def get_possible(race_time: int, record_distance: int) -> Iterable[int]:
    for hold_time in range(race_time + 1):
        speed = hold_time * 1
        remaining_time = race_time - hold_time
        distance = speed * remaining_time
        if distance > record_distance:
            yield hold_time
