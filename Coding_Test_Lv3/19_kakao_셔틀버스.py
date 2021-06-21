# https://programmers.co.kr/learn/courses/30/lessons/17678?language=python3

# hh:mm 을 분 단위로
def time_split(time):
    result = 0
    result += int(time[:2]) * 60
    result += int(time[3:])
    return result

# 분 단위를 hh:mm 형태로
def time_beautiful(time):
    hour = str(time // 60).zfill(2)
    minute = str(time % 60).zfill(2)
    return hour + ":" + minute

def solution(n, t, m, timetable):
    timetable.sort(reverse=True)
    cur_time = 540 - t
    for _ in range(n):
        cur_time += t
        cur_time_str = time_beautiful(cur_time)
        bus_in = 0
        while timetable and bus_in < m:
            if timetable[-1] <= cur_time_str: # 버스 도착 시간 대기한 인원 태우기
                bus_in += 1
                last_time = timetable.pop()
            else: # 이번 버스 시간까지 오지 못한 사람이라면
                break
        
        # 버스에 자리가 있다면 버스가 도착할 때 정류장에 도착하면 됨
        if bus_in < m:
            answer = cur_time
        # 버스가 꽉 찼다면 마지막에 온 사람보다 1분 먼저 오면 됨
        elif bus_in == m:
            answer = time_split(last_time)-1

    return time_beautiful(answer)