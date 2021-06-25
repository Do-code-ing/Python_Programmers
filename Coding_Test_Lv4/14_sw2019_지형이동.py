# https://programmers.co.kr/learn/courses/30/lessons/62050?language=python3

from heapq import heappush, heappop
from collections import deque
import sys
sys.setrecursionlimit(10**6)
dr = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution(land, height):
    n = len(land)
    answer = 0
    
    def bfs(x, y, visit, ladder):
        nonlocal answer
        visit[x][y] = True
        q = deque([(x, y)])
        while q:
            x, y = q.popleft()
            for dx, dy in dr:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if visit[nx][ny]:
                        continue
                    
                    gap = abs(land[x][y] - land[nx][ny])
                    if gap <= height:
                        visit[nx][ny] = True
                        q.append((nx, ny))
                    else: # 사다리를 놓아야 하는 경우
                        heappush(ladder, (gap, x, y, nx, ny))
        
        while ladder:
            gap, x, y, nx, ny = heappop(ladder)
            if visit[nx][ny]: # 빙 돌아서 방문이 가능했을 수도 있으므로 한 번 체크
                continue
            
            answer += gap # 제일 적은 비용으로 사다리를 놓고
            bfs(nx, ny, visit, ladder) # 이동 후 재 탐색
            break
    
    visit = [[False] * n for _ in range(n)]
    visit[0][0] = True
    bfs(0, 0, visit, [])
    
    return answer