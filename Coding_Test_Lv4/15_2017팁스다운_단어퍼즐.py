# https://programmers.co.kr/learn/courses/30/lessons/12983?language=python3

def solution(strs, t):
    n = len(t)
    dp = [0] * (n+1)
    strs = set(strs) # 중복 문자열 제거
    
    for i in range(1, n+1): # t[s:i]를 위해 1부터 시작
        dp[i] = float('inf') # 일단 무한으로 갱신
        for k in range(1, 6): # strs안에 있는 각 문자열의 길이가 1이상 5이하이므로 
            if i - k < 0: # 시작 인덱스가 음수가 되버린다면 0으로
                s = 0
            else:
                s = i - k
            if t[s:i] in strs:
                value = dp[i-k] + 1
                if dp[i] > value:
                    dp[i] = value
    
    return dp[-1] if dp[-1] != float('inf') else -1