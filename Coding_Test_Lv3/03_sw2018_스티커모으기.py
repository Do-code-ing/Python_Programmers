# https://programmers.co.kr/learn/courses/30/lessons/12971?language=python3

def solution(sticker):
    n = len(sticker)
    # 스티커가 한장이면 리턴
    if n == 1:
        return sticker[0]
    
    dp1 = [0] * n
    dp2 = [0] * n
    # 첫 번째 스티커부터 뜯을 때 (맨 뒤에 스티커는 못 씀)
    for i in range(n-1):
        dp1[i] = max(sticker[i] + dp1[i-2], dp1[i-1])
    # 두 번째 스티커부터 뜯을 때 (첫 번째 스티커는 못 씀)
    for i in range(1, n):
        dp2[i] = max(sticker[i] + dp2[i-2], dp2[i-1])
    
    return max(max(dp1), max(dp2))