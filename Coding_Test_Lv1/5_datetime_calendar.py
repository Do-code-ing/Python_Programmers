a = 5
b = 24

import datetime

def solution(a, b):
    weeks = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return weeks[datetime.date(2016, a, b).weekday()]

print(solution(a, b))

import calendar

def solution(a, b):
    weeks = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return weeks[calendar.weekday(2016, a, b)]