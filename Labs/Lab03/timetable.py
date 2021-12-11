# timetable.py assumes dates and times have correct values and types

from datetime import date, time, datetime

def timetable(dates, times):

    result = []

    # get all possible combinations
    for date in dates:
        for time in times:
            date_time = datetime.combine(date, time)
            result.append(date_time)

    return sorted(result)
