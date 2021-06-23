# https://programmers.co.kr/learn/courses/30/lessons/43236?language=python3

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)  # 도착 지점도 체크해야 하므로 추가
    start = 0
    end = distance
    while start <= end:
        mid = (start+end) // 2  # 예상되는 지점간의 최소 거리
        min_value = distance    # 지점간의 최소 거리 저장
        cur_pos = 0             # 이전 바위 위치 (출발 지점부터 시작)
        count = 0               # 몇 개의 바위를 치웠는지
        for dist in rocks:
            value = dist - cur_pos  # 현재 값 = 현재 바위 위치 - 이전 바위 위치
            if value < mid:             # 만약 현재 값이 예상되는 최소 거리보다 크다면
                count += 1              # 바위를 치운다.
                if count > n:           # 만약 치운 바위가 최대 치울 수 있는 바위 개수보다 많다면 break
                    break
            else:                       # 만약 현재 값이 예상되는 최소 거리보다 작다면
                if min_value > value:   # min_value update
                    min_value = value
                cur_pos = dist          # 이 바위는 안 치웠기 때문에 현재 바위 위치를 이전 바위 위치로 update
        if count > n:       # 최대 치울 수 있는 바위 개수보다 많이 치웠다면
            end = mid - 1   # 지점간 최소 거리 줄이기
        else:               # 아니라면
            answer = min_value  # 정답 저장
            start = mid + 1     # 더 먼 거리도 가능한지 체크

    return answer