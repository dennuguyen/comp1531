from datetime import date, time, datetime
from timetable import timetable
import pytest


def test_some_dates():
    assert timetable([
        date(2019, 9, 27),
        date(2019, 9, 30),
    ], [time(14, 10), time(10, 30)]) == [
        datetime(2019, 9, 27, 10, 30),
        datetime(2019, 9, 27, 14, 10),
        datetime(2019, 9, 30, 10, 30),
        datetime(2019, 9, 30, 14, 10),
    ]


def test_empty_list():
    assert timetable([], []) == []


def test_same_list():
    assert timetable(
        [date(2, 1, 1)],
        [time(2, 1, 1)],
    ) == [
        datetime(2, 1, 1, 2, 1, 1),
    ]


test_some_dates()
test_empty_list()
test_same_list()