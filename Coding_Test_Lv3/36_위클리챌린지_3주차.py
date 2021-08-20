# https://programmers.co.kr/learn/courses/30/lessons/84021

from collections import deque
from numpy import rot90, pad
dr = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(flag, board):
    result = []
    n = len(board)
    m = len(board[0])
    q = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == flag:
                temp = []
                board[i][j] = 2
                q.append((i, j))
                temp.append((i, j))
                count = 1

                while q:
                    x, y = q.popleft()
                    for dx, dy in dr:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == flag:
                            board[nx][ny] = 2
                            q.append((nx, ny))
                            temp.append((nx, ny))
                            count += 1
                
                temp.sort()
                result.append((count, temp))

    result.sort(key=lambda x:x[0])

    return result

def rotate(key):
    min_x, max_x = 50, -1
    min_y, max_y = 50, -1
    for x, y in key:
        if min_x > x:
            min_x = x
        if max_x < x:
            max_x = x
        if min_y > y:
            min_y = y
        if max_y < y:
            max_y = y

    n = max_x - min_x
    m = max_y - min_y
    new_key = [[0] * (m+1) for _ in range(n+1)]
    for x, y in key:
        x -= min_x
        y -= min_y
        new_key[x][y] = 1
    
    new_key = pad(new_key, max(n, m))
    new_key = rot90(new_key)

    return dfs(1, new_key)[0][1]


def check(n, key, door):
    in_door = []
    for i in range(n-1):
        x1, y1 = door[i]
        x2, y2 = door[i+1]
        in_door.append((x1-x2, y1-y2))

    for _ in range(4):
        in_key = []
        for i in range(n-1):
            x1, y1 = key[i]
            x2, y2 = key[i+1]
            in_key.append((x1-x2, y1-y2))

        for i in range(n-1):
            if in_key[i] != in_door[i]:
                key = rotate(key)
                break
        else:
            return True

    return False


def solution(game_board, table):
    answer = 0
    doors = dfs(0, game_board)
    keys = dfs(1, table)
    used = [False] * len(keys)
    for i in range(len(doors)):
        x, door = doors[i]
        for j in range(len(keys)):
            y, key = keys[j]
            if used[j] or x != y:
                continue

            if check(x, key, door):
                used[j] = True
                answer += x
                break
    
    return answer