# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    tq = deque(truck_weights)
    q = deque([0 for _ in range(bridge_length)]) # 다리 리스트
    time = 0
    cur_value = 0
    while q:
        value = q.popleft()
        cur_value -= value
        time += 1
        # 아직 출발하지 않은 트럭이 있다면
        if tq:
            # 그 트럭이 다리에 올라갈 수 있다면 출발시키기
            if cur_value + tq[0] <= weight:
                left = tq.popleft()
                cur_value += left
                q.append(left)
            else:
                # 아니라면 시간보내기
                q.append(0)

    return time