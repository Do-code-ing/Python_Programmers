# https://programmers.co.kr/learn/courses/30/lessons/81302#fn1

from collections import deque
n = 5
dr = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def check(place, i, j):
    visit = [[False] * n for _ in range(n)]
    visit[i][j] = True
    q = deque([(i, j, 0)])
    while q:
        x, y, count = q.popleft()
        if count == 2: # 조건 1 (하단 참조)
            continue

        for dx, dy in dr:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                visit[nx][ny] = True
                pos = place[nx][ny]
                if pos == "X":
                    continue
                elif pos == "P":
                    return False
                else:
                    q.append((nx, ny, count+1))
    
    return True

def solution(places):
    answer = []
    for place in places:
        temp = [] # 거리두기를 지키지 않은 P의 모임
        for i in range(n):
            for j in range(n):
                if place[i][j] == "P":
                    temp.append(check(place, i, j))

        answer.append(int(all(temp)))

    return answer

# 조건 1
# 0 0 1 0 0
# 0 1 1 1 0
# 1 1 P 1 1
# 0 1 1 1 0
# 0 0 1 0 0
# P의 위치에서 1만 확인하면 된다.
# 그러므로 첫 i, j로 부터 시작한 x, y는 최대 두 번까지 q 에 삽입하여 확인하면 된다.