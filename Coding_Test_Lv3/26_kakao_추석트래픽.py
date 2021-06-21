# https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3

def solution(lines):
    n = len(lines)
    start_times = []
    end_times = []
    
    # 해당 작업의 시작 시각과 끝나는 시각 저장
    for line in lines:
        _, end_time, run_time = line.split()
        end_time = tuple(map(float, end_time.split(":")))
        end_time = end_time[0] * 3600 + end_time[1] * 60 + end_time[2]
        run_time = float(run_time[:-1])
        start_times.append(end_time - run_time + 0.001)
        end_times.append(end_time + 1)
    
    start_times.sort()
    count = 0       # 현재 1초사이의 작업량
    answer = 0      
    start = 0
    end = 0
    while start < n and end < n:
        if start_times[start] < end_times[end]:
            count += 1
            start += 1
            if answer < count:
                answer = count
        else:
            count -= 1
            end += 1
    
    return answer