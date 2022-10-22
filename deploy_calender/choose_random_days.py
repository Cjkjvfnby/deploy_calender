from calendar import monthrange
from random import Random
from typing import Iterable, Iterator

from deploy_calender.month import Day, Month, Weekday
from deploy_calender.settings import Zodiac

_SAT = 6
_SUN = 0

WEEKEND_DAYS = {_SAT, _SUN}


def _iter_weekdays(start_day: Weekday) -> Iterator[Weekday]:
    while True:
        yield start_day
        start_day = (start_day + 1) % 7


def _get_month_days(month: Month) -> Iterator[tuple[Day, Weekday]]:
    first_week_day, number_of_days = monthrange(month.year, month.month)
    for day, week_day in zip(range(number_of_days), _iter_weekdays(first_week_day)):
        yield day, week_day


def _get_working_days(month: Month) -> Iterator[Day]:
    for day, week_day in _get_month_days(month):
        if week_day not in WEEKEND_DAYS:
            yield day


def _split_days(
    random: Random, days: Iterable[Day], number: int
) -> tuple[set[Day], set[Day]]:
    days = list(days)
    selected_days = set(random.choices(days, k=number))
    rest = set(days).difference(selected_days)
    return selected_days, rest


def get_deploy_and_avoid_dates(
    month: Month, sign: Zodiac, max_days_in_group: int = 5
) -> tuple[set[Day], set[Day]]:
    seed = f"{month.year}{month.month}{sign}"
    random = Random(seed)
    working_days = _get_working_days(month)

    deploy_days, rest_working_days = _split_days(
        random, working_days, max_days_in_group
    )
    avoid_days, _ = _split_days(random, rest_working_days, max_days_in_group)
    return deploy_days, avoid_days
