# https://programmers.co.kr/learn/courses/30/lessons/12907?language=python3

def solution(n, money):
    dp = [0] * (n+1)
    dp[0] = 1
    
    for coin in money:
        for i in range(1, n+1):
            if coin > i:
                continue
            
            dp[i] += dp[i-coin]

    return dp[n]