# hh:mm:ss 형식의 시각을 초 단위 시각으로 만들기
def time_split(time):
    result = 0
    result += int(time[0:2]) * 3600
    result += int(time[3:5]) * 60
    result += int(time[6:])
    return result

def solution(play_time, adv_time, logs):
    play_time = time_split(play_time)   # 플레이 시간 초 단위로 변환
    adv_time = time_split(adv_time)     # 광고 시간 초 단위로 변환     
    time = [0] * (play_time+1)          # 플레이 시간동안 각 초마다 몇 명이 시청했는지 저장
    for log in logs:
        start, end = map(time_split, log.split("-"))
        time[start] += 1                # 시청 시작 시각에는 +1
        time[end] -= 1                  # 시청 종료 시각에는 -1
    
    for i in range(1, play_time+1):     # 각 초 별로 몇 명이 보고있는지 갱신
        time[i] += time[i-1]
    
    # 0초부터 광고를 재생했을 경우 최대 시청 수 = default value
    cur_value = 0
    for i in range(adv_time+1):
        cur_value += time[i]

    # 시각마다 시청자 수를 비교하며 업데이트
    high_value = cur_value
    start_time = 0
    for start in range(play_time-adv_time):
        end = start + adv_time
        cur_value += time[end] - time[start]
        if high_value < cur_value:
            high_value = cur_value
            start_time = start + 1

    # 초 단위의 시각을 hh:mm:ss 형식의 시각으로 변환
    h = str(start_time // 3600).zfill(2)
    start_time = start_time % 3600
    m = str(start_time // 60).zfill(2)
    start_time = start_time % 60
    s = str(start_time).zfill(2)

    return h + ":" + m + ":" + s