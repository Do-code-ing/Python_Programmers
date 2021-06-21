# https://programmers.co.kr/learn/courses/30/lessons/72415?language=python3

from itertools import permutations
from copy import deepcopy

# 최단거리 찾기
def find_dist(board, x, y, target_x, target_y):
    # 현재 좌표와 목표 좌표가 같다면 0 return
    if x == target_x and y == target_y:
        return 0

    # 현재 x좌표와 목표의 x좌표를 비교하여 목표의 좌표 인덱스가 크다면 각각 +1
    # x = 0, target_x = 3인 경우, 확인해야할 x좌표는 1, 2, 3이므로 range(1, 4)로 해주기 위함
    # x = 3, target_x = 0인 경우, 확인해야할 x좌표는 0, 1, 2이므로 range(0, 3)으로 해주기 위함
    rx, target_rx = x, target_x
    if rx < target_rx:
        rx += 1
        target_rx += 1
    
    ry, target_ry = y, target_y
    if ry < target_ry:
        ry += 1
        target_ry += 1
    
    # x좌표가 같을 때, y좌표로만 이동하며 항상 마지막 y좌표에는 0이 아닌 숫자가 있으므로,
    # y = 0, target_y = 3인 경우, y를 변화시키며 1, 2, 3 인덱스를 확인하여, 0이 아닌 숫자의 개수만큼 이동 횟수 추가
    if x == target_x:
        count = 0
        for j in range(min(ry, target_ry), max(ry, target_ry)):
            if board[x][j] != 0:
                count += 1
        return count
    
    # y좌표가 같을 때 (x좌표가 같을 때와 동일)
    if y == target_y:
        count = 0
        for i in range(min(rx, target_rx), max(rx, target_rx)):
            if board[i][y] != 0:
                count += 1
        return count

    # 이하 직각선으로 이동
    # x좌표 먼저 이동
    x_first = 0
    for i in range(min(rx, target_rx), max(rx, target_rx)):     # 먼저 x좌표를 이동시키며, 0이 아닌 개수 파악
        if board[i][y] != 0:
            x_first += 1

    if x_first == 0:                                        # 만약 경로가 비어있다면(모두 0이라면)
        if target_x == 0 or target_x == 3:                      # 만약 목표 x좌표가 0이나 3이라면
            x_first = 1                                             # 좌표 끝까지 이동을 한번에 하므로 1로 업데이트
        else:                                                   # 아니라면
            x_first = abs(target_x-x)                               # 이동한 칸의 개수만큼으로 업데이트
    elif board[target_x][y] == 0:                           # 만약 경로가 비어있지 않으면서 도착한 곳이 0이라면
        x_first += 1                                            # 멈추기 위해서 +1
    # y좌표 이동
    for j in range(min(ry, target_ry), max(ry, target_ry)):     # y좌표 이동시 항상 board[target_x][target_y]에
        if board[target_x][j] != 0:                             # 0이 아닌 숫자가 있으므로,
            x_first += 1                                        # 이동하며 0이 아닌 숫자의 개수만큼 카운트
    
    # y좌표 먼저 이동 (x좌표 먼저 이동과 동일)
    y_first = 0
    for j in range(min(ry, target_ry), max(ry, target_ry)):
        if board[x][j] != 0:
            y_first += 1

    if y_first == 0:
        if target_y == 0 or target_y == 3:
            y_first = 1
        else:
            y_first = abs(target_y-y)
    elif board[x][target_y] == 0:
        y_first += 1

    for i in range(min(rx, target_rx), max(rx, target_rx)):
        if board[i][target_y] != 0:
            y_first += 1

    return min(x_first, y_first)    # 더 적은 이동 횟수 리턴

def btk(board, x, y, value, idx, order):
    global answer
    if idx == high_card:
        if answer > value:
            answer = value
        return

    target = order[idx]
    (x1, y1), (x2, y2) = coord[target]

    dist_1 = find_dist(board, x, y, x1, y1) + find_dist(board, x1, y1, x2, y2)  # 1 -> 2 순서로 카드 뒤집기
    dist_2 = find_dist(board, x, y, x2, y2) + find_dist(board, x2, y2, x1, y1)  # 2 -> 1 순서로 카드 뒤집기
    
    board[x1][y1] = board[x2][y2] = 0
    btk(board, x2, y2, value+dist_1+2, idx+1, order)    # value + 2 하는 이유 = 카드를 뒤집는 동작 카운트
    btk(board, x1, y1, value+dist_2+2, idx+1, order)
    board[x1][y1] = board[x2][y2] = target

answer, high_card = float("inf"), 0
coord = {}
def solution(board, r, c):
    global high_card, coord
    for i in range(4):
        for j in range(4):      # 카드 개수 확인
            if high_card < board[i][j]:
                high_card = board[i][j]
            
            if board[i][j]:     # 좌표 저장
                if board[i][j] not in coord:
                    coord[board[i][j]] = []
                coord[board[i][j]].append((i, j))
    
    for order in permutations(range(1, high_card+1)):   # 어떤 순서로 카드를 뒤집을 것인가
        order = list(order)
        board_ = deepcopy(board)
        btk(board_, r, c, 0, 0, order)
    
    return answer

# 다른 사람들은 dfs, bfs로 풀었는데, 나는 완전탐색으로 풀었다. 그러다보니 코드가 길어진 것 같다.
# find_dist함수에 중복되는 부분을 sub함수로 나눈다면 코드의 길이를 조금 줄일 수 있을 것 같다.
# 하지만 시간 복잡도가 다른 알고리즘으로 푼 풀이에 비해 빠르다. (비트연산제외..)
#      my_code = 0.36608147621154785
# use_bit_code = 0.1560344696044922
#   other_code = 1.275282859802246
#              = 1.0162255764007568
#              = 3.869861125946045
#              = 10.941434621810913