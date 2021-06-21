# https://programmers.co.kr/learn/courses/30/lessons/60061?language=python3

def check_build(dp, x, y, bo):
    if bo == 0: # 기둥이라면
        if y == 0: # 바닥이라면
            dp[x][y][0] = True #설치
        else: # 바닥이 아니라면
            if dp[x-1][y][1] or dp[x][y][1] or dp[x][y-1][0]:
                dp[x][y][0] = True
    
    elif bo == 1: # 보라면
        if dp[x][y-1][0] or dp[x+1][y-1][0] or (dp[x-1][y][1] and dp[x+1][y][1]):
            dp[x][y][1] = True

def check_delete(dp, x, y, bo, n):
    dp[x][y][bo] = False
    for i in range(n+1):
        for j in range(n+1):
            for k in range(2):
                if dp[i][j][k]:
                    if k == 0:
                        if j == 0:
                            continue
                        
                        if not any((dp[i-1][j][1], dp[i][j][1], dp[i][j-1][0])):
                            dp[x][y][bo] = True
                            return
                    
                    elif k == 1:
                        if not any((dp[i][j-1][0], dp[i+1][j-1][0], (dp[i-1][j][1] and dp[i+1][j][1]))):
                            dp[x][y][bo] = True
                            return

def solution(n, build_frame):
    dp = [[[False, False] for _ in range(n+1)] for _ in range(n+1)]
    
    for x, y, bo, command in build_frame:
        if command:
            check_build(dp, x, y, bo)
        else:
            check_delete(dp, x, y, bo, n)
    
    answer = []
    for i in range(n+1):
        for j in range(n+1):
            for k in range(2):
                if dp[i][j][k]:
                    answer.append((i, j, k))

    return answer