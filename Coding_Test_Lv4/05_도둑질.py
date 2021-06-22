# https://programmers.co.kr/learn/courses/30/lessons/42897?language=python3

def solution(money):
    n = len(money)
    if n < 4:
        return max(money)
    
    dpf = [0] * n
    dps = [0] * n
    dpf[0] = money[0]
    dpf[1] = max(money[1], money[0])
    dps[1] = money[1]
    dps[2] = max(money[2], money[1])
    
    for i in range(2, n-1):
        dpf[i] = max(money[i] + dpf[i-2], dpf[i-1])
    
    for i in range(3, n):
        dps[i] = max(money[i] + dps[i-2], dps[i-1])
    
    return max(max(dpf), max(dps))