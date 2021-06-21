# https://programmers.co.kr/learn/courses/30/lessons/42884?language=python3

from collections import deque

def solution(routes):
    # 차량이 고속도로에서 빠져나가는 순서대로 정렬
    routes.sort(key=lambda x:x[1])

    q = deque(routes)
    # 첫 번째 차량이 나가는 지점에 카메라 설치 (answer += 1)
    cur_idx = routes[0][1]
    # 차량의 대수가 1개 이상이므로 무조건 1개 이상 설치
    answer = 1
    while q:
        start, end = q.popleft()
        # 현재 설치된 위치에 다음 차량이 지나간다면 continue
        if cur_idx in range(start, end+1):
            continue
        # 아니라면 카메라 새로 설치
        cur_idx = end
        answer += 1

    return answer