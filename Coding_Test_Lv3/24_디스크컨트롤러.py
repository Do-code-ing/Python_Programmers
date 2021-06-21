# https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3

from heapq import heappush, heappop

def solution(jobs):
    jobs.sort()
    result = 0
    q = []
    cur_time = 0
    for job in jobs:
        if job[0] < cur_time:                           # 현재 시각보다 시작 시각이 빠르다면
            heappush(q, (job[1], job[0]))               # 대기열에 추가
        else:                                           # 아니라면
            if q:                                       # 만약 대기열이 있다면
                while q and job[0] > cur_time:          # 시작 시각이 현재 시각보다 낮을 수 있게 대기 작업들 수행
                    end, start = heappop(q)
                    result += cur_time - start + end
                    cur_time += end
                heappush(q, (job[1], job[0]))           # 수행을 마친 뒤 대기열에 추가
            else:                                       # 대기열이 비어있다면
                start, end = job                        # 현재 시각을 시작 시각으로 업데이트하고 작업 수행
                cur_time = start + end
                result += end
    
    while q:                                            # 잔반 처리
        end, start = heappop(q)
        if cur_time < start:
            cur_time = start

        result += cur_time - start + end
        cur_time += end

    return result // len(jobs)

# 조금 더 이쁜 풀이
from heapq import heappush, heappop
from collections import deque

def solution(jobs):
    q = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x:(x[1], x[0])))  # 작업이 들어오는 순서대로, 그리고
    cur_time = 0                                                                # 총 작업 시간 순으로 저장
    result = 0
    hq = []
    heappush(hq, q.popleft())
    while hq:
        end, start = heappop(hq)
        cur_time = max(cur_time + end, start + end)
        result += cur_time - start

        while q and q[0][1] < cur_time:                 # 아직 작업할게 남아 있고, 다음 순번 작업의 시작 시각이
            heappush(hq, q.popleft())                   # 현재 시각보다 빠르다면 대기열에 추가
        if q and not hq:                                # 아직 작업할게 남아 있고, 대기열이 비어있다면
            heappush(hq, q.popleft())                   # 대기열에 추가

    return result // len(jobs)