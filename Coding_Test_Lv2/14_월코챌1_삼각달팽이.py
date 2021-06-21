# https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    dp = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1

    for i in range(n):
        for _ in range(i, n):
            # 아래로 진행하며 숫자쓰기
            if i % 3 == 0:
                x += 1
            # 오른쪽으로 진행하며 숫자쓰기
            elif i % 3 == 1:
                y += 1
            # 좌대각으로 진행하며 숫자쓰기
            elif i % 3 == 2:
                x -= 1
                y -= 1
            # 숫자 기입
            dp[x][y] = num
            num += 1
    
    for i in dp:
        for j in i:
            if j == 0:
                break
            answer.append(j)

    return answer

solution(4)