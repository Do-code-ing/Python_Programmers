# https://programmers.co.kr/learn/courses/30/lessons/67259?language=python3

from collections import deque

def solution(board):
    n = len(board)
    dp = [[float('inf')] * n for _ in range(n)] # 해당 좌표에 도달했을 때의 최소 비용 저장
    dr = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    answer = float("inf")
    q = deque([(0, 0, -1, 0)])
    while q:
        x, y, course, cost = q.popleft() # x좌표, y좌표, 현재 진행 방향, 여태까지 비용
        if x == n-1 and y == n-1:
            if answer > cost:
                answer = cost
            continue
        
        for i in range(4): # i = (0:하, 1:상, 2:우, 3:좌)
            nx = x + dr[i][0]
            ny = y + dr[i][1]
            next_cost = cost
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if course == -1 or course == i: # 직진도로 라면
                    next_cost += 100
                else:                           # 코너라면
                    next_cost += 600
                if dp[nx][ny] < next_cost:      # 최소 비용으로 도달했는지 체크
                    continue
                
                dp[nx][ny] = next_cost
                q.append((nx, ny, i, next_cost))

    return answer