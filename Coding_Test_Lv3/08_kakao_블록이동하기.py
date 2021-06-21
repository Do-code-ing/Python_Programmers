# https://programmers.co.kr/learn/courses/30/lessons/60063?language=python3

from collections import deque

def solution(board):
    n = len(board)
    dr = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visit = [{(0, 0), (0, 1)}]
    q = deque([(0, 0, 0, 1, 0)])
    while q:
        x1, y1, x2, y2, count = q.popleft()
        print(x1, y1, x2, y2)
        if (x1 == n-1 and y1 == n-1) or (x2 == n-1 and y2 == n-1):
            return count
        # 일반적인 이동
        for dx, dy in dr:
            nx1 = x1 + dx
            ny1 = y1 + dy
            nx2 = x2 + dx
            ny2 = y2 + dy
            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
                if board[nx1][ny1] == 0 and board[nx2][ny2] == 0 and {(nx1, ny1), (nx2, ny2)} not in visit:
                    visit.append({(nx1, ny1), (nx2, ny2)})
                    q.append([nx1, ny1, nx2, ny2, count+1])
        # 드론이 가로로 서있을 때 (위나 아래로만 회전 가능)
        if x1 == x2:
            # 왼쪽 날개 기준으로 회전하기
            # 위로 회전
            if 0 <= x2-1 < n:
                if board[x2-1][y2] == 0 and board[x2-1][y1] == 0 and {(x1, y1), (x2-1, y1)} not in visit:
                    visit.append({(x1, y1), (x2-1, y1)})
                    q.append([x1, y1, x2-1, y1, count+1])
            # 아래로 회전
            if 0 <= x2+1 < n:
                if board[x2+1][y2] == 0 and board[x2+1][y1] == 0 and {(x1, y1), (x2+1, y1)} not in visit:
                    visit.append({(x1, y1), (x2+1, y1)})
                    q.append([x1, y1, x2+1, y1, count+1])
            # 오른쪽 날개 기준으로 회전하기
            # 위로 회전
            if 0 <= x1-1 < n:
                if board[x1-1][y1] == 0 and board[x1-1][y2] == 0 and {(x1-1, y2), (x2, y2)} not in visit:
                    visit.append({(x1-1, y2), (x2, y2)})
                    q.append([x1-1, y2, x2, y2, count+1])
            # 아래로 회전
            if 0 <= x1+1 < n:
                if board[x1+1][y1] == 0 and board[x1+1][y2] == 0 and {(x1+1, y2), (x2, y2)} not in visit:
                    visit.append({(x1+1, y2), (x2, y2)})
                    q.append([x1+1, y2, x2, y2, count+1])
        # 드론이 세로로 서있을 때 (왼쪽이나 오른쪽으로만 회전 가능)
        if y1 == y2:
            # 윗 날개 기준으로 회전하기
            # 왼쪽으로 회전
            if 0 <= y2-1 < n:
                if board[x2][y2-1] == 0 and board[x1][y2-1] == 0 and {(x1, y1), (x1, y2-1)} not in visit:
                    visit.append({(x1, y1), (x1, y2-1)})
                    q.append([x1, y1, x1, y2-1, count+1])
            # 오른쪽으로 회전
            if 0 <= y2+1 < n:
                if board[x2][y2+1] == 0 and board[x1][y2+1] == 0 and {(x1, y1), (x1, y2+1)} not in visit:
                    visit.append({(x1, y1), (x1, y2+1)})
                    q.append([x1, y1, x1, y2+1, count+1])
            # 아랫 날개 기준으로 회전하기
            # 왼쪽으로 회전
            if 0 <= y1-1 < n:
                if board[x1][y1-1] == 0 and board[x2][y1-1] == 0 and {(x2, y1-1), (x2, y2)} not in visit:
                    visit.append({(x2, y1-1), (x2, y2)})
                    q.append([x2, y1-1, x2, y2, count+1])
            # 오른쪽으로 회전
            if 0 <= y1+1 < n:
                if board[x1][y1+1] == 0 and board[x2][y1+1] == 0 and {(x2, y1+1), (x2, y2)} not in visit:
                    visit.append({(x2, y1+1), (x2, y2)})
                    q.append([x2, y1+1, x2, y2, count+1])