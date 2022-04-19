# https://programmers.co.kr/learn/courses/30/lessons/92341?language=python3

def time_conversion(time):
    hour, minute = int(time[:2]) * 60, int(time[3:])
    result = hour + minute
    return result


def solution(fees, records):
    answer = []
    LAST_TIME = time_conversion('23:59')
    basic_time, basic_price, unit_time, unit_price = int(
        fees[0]), int(fees[1]), int(fees[2]), int(fees[3])
    total_time = dict()
    state = dict()

    for record in records:
        time, car, history = record.split()
        time = time_conversion(time)
        car = int(car)

        if car not in total_time:
            total_time[car] = 0

        if history == "IN":
            state[car] = [True, time]
        else:
            total_time[car] += time - state[car][1]
            state[car] = [False, None]

    for car in state:
        stay, time = state[car]
        if stay == True:
            total_time[car] += LAST_TIME - time

    result = list()
    for car, time in total_time.items():
        result.append((car, time))

    result.sort()

    for _, time in result:
        answer.append(basic_price)
        if time <= basic_time:
            continue

        time -= basic_time
        time, temp = divmod(time, unit_time)
        if temp:
            time += 1

        answer[-1] += time * unit_price

    return answer
