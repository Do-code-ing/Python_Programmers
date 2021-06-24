# https://programmers.co.kr/learn/courses/30/lessons/12902?language=python3

def solution(n):
    if n % 2 == 1:
        return 0
    
    p = 10**9 + 7
    dp = [0] * (n+1)
    dp[2] = 3
    prefix_sum = 0
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 3 + 2 + 2 * prefix_sum
        dp[i] %= p
        prefix_sum += dp[i-2]
        prefix_sum %= p

    return dp[n]