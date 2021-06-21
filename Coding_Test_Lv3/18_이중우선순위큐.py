# https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3

# deque, bisect를 사용한 풀이
from collections import deque
from bisect import bisect_left

def solution(operations):
    q = deque()
    for operation in operations:
        command, value = operation.split()
        value = int(value)
        if command == "I":
            q.insert(bisect_left(q, value), value)
        else:
            if q:
                if value == -1:
                    q.popleft()
                else:
                    q.pop()
    
    if q:
        return [q[-1], q[0]]
    return [0, 0]

# heapq를 이용한 풀이
from heapq import heappush, heappop, heapify

def solution(operations):
    q = []
    for operation in operations:
        command, value = operation.split()
        value = int(value)
        if command == "I":
            heappush(q, value)
        elif q:
            if value == -1:
                heappop(q)
            else:
                q.remove(max(q))
                heapify(q)
    if q:
        return [max(q), min(q)]
    return [0, 0]