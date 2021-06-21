# https://programmers.co.kr/learn/courses/30/lessons/60062?language=python3

from collections import deque
from itertools import permutations

def solution(n, weak, dist):
    answer = 9 # len(dist) < 9 이므로 상한선 9
    q = deque(weak)
    count = 0
    # weak = [1,2,3]이고 n = 1이라면, [1,2,3], [2,3,4], [3,4,5]이 모든 순서에 대해 탐색
    while count < len(weak):
        # 친구들 출발 순서
        for candi in permutations(dist):
            idx = 0     # 친구 순서
            start = 0   # idx친구가 맡을 출발 지점
            end = 1     # idx 친구가 맡을 마지막 지점
            temp = 0    # 현재 친구들 출발 순서로 마무리할 수 있는 최종 지점
            while end < len(weak) and idx < len(dist):
                cur_dist = q[end] - q[start]
                # 이 친구가 해당 지역을 맡을 수 있다면
                if candi[idx] >= cur_dist:
                    temp = end+1    # 최종 지점 업데이트
                    end += 1        # 좀 더 갈 수 있나 파악
                # 안된다면
                else:
                    idx += 1        # 다음 친구에게 맡기기
                    start = end     # 다음 친구가 맡을 지역 업데이트
                    end += 1
            # 만약 모든 weak 지점에 대해 보수를 했다면
            # 출발한 친구 수를 정답으로 업데이트
            if temp == len(weak):
                if answer > idx+1:
                    answer = idx+1
            else:
                # 만약 보수 지점 수보다 친구들 수가 많다면
                # 보수 지점수를 정답으로 업데이트 (한 명당 한 곳을 가면 되니까)
                if len(dist) >= len(weak):
                    if answer > len(weak):
                        answer = len(weak)
        # [1,2,3] -> [2,3,4] -> [3,4,5]를 해주기
        x = q.popleft()
        q.append(x+n)
        count += 1

    return answer if answer != 9 else -1