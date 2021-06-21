# https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3#

def solution(n, results):
    # 승패 그래프 초기화
    dp = [[0] * n for _ in range(n)]
    for a, b in results:
        dp[a-1][b-1] = 1
        dp[b-1][a-1] = -1
    
    # 각 선수별로
    for i in range(n):
        win = []    # 누구한테 이겼는지 저장
        lose = []   # 누구한테 졌는지 저장
        for j in range(n):
            if dp[i][j] == 1:
                win.append(j)
            if dp[i][j] == -1:
                lose.append(j)
        
        if not lose:    # 진 적이 없다면 continue
            continue
        
        for idx in win: # 업데이트 시작
            for jdx in lose:
                dp[idx][jdx] = -1   # 나한테 진 사람은 나한테 이긴 사람보다 약함
                dp[jdx][idx] = 1    # 나한테 이긴 사람은 나한테 진 사람보다 강함
    
    answer = 0
    for i in range(n):
        if dp[i].count(0) == 1:     # 나를 제외하고 힘의 우위를 가늠할 수 있다면 + 1
            answer += 1

    return answer