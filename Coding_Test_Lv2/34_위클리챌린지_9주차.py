# https://programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque


def solution(n, wires):
    answer = float("inf")
    for i in range(len(wires)):
        edge = [[] for _ in range(n+1)]
        for j, (a, b) in enumerate(wires):
            if i == j:
                continue

            edge[a].append(b)
            edge[b].append(a)

        count = 1
        visited = [False] * (n+1)
        visited[1] = True
        q = deque([(1)])
        while q:
            x = q.popleft()
            for y in edge[x]:
                if visited[y]:
                    continue

                visited[y] = True
                q.append(y)
                count += 1

        result = abs(n-count-count)
        if answer > result:
            answer = result

    return answer
