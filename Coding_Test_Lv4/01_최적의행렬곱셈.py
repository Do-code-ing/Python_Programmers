# https://programmers.co.kr/learn/courses/30/lessons/12942?language=python3

def solution(matrix_sizes):
    n = len(matrix_sizes)
    p = matrix_sizes[0]
    for i in range(1, n):
        p.append(matrix_sizes[i][1])
    
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][i] = 0
    
    for diagonal in range(1, n):
        for i in range(1, n-diagonal+1):
            j = i + diagonal
            for k in range(i, j):
                if dp[i][j] > dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]:
                    dp[i][j] = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]
    
    return dp[1][-1]