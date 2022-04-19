# https://programmers.co.kr/learn/courses/30/lessons/92342

from collections import deque


def brute_search(n, info):
    result = list()
    q = deque([(0, [0] * 11)])
    max_gap = 0

    while q:
        target, arrow = q.popleft()
        if sum(arrow) == n:
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:
                gap = lion - apeach
                if max_gap > gap:
                    continue
                if max_gap < gap:
                    max_gap = gap
                    result = list()
                result.append(arrow)
        elif sum(arrow) > n:
            continue
        elif target == 10:
            temp = arrow.copy()
            temp[target] = n - sum(temp)
            q.append((-1, temp))
        else:
            temp = arrow.copy()
            temp[target] = info[target] + 1
            q.append((target+1, temp))
            q.append((target+1, arrow))

    return result


def solution(n, info):
    answer = brute_search(n, info)
    if answer:
        return answer[-1]
    return [-1]
