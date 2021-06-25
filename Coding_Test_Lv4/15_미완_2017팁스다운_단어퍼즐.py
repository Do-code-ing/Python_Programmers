# https://programmers.co.kr/learn/courses/30/lessons/12983?language=python3

def solution(strs, t):
    answer = float('inf')
    n = len(t)
    m = len(strs)
    
    def btk(start, value):
        nonlocal answer
        if start == n:
            if answer > value:
                answer = value
            return
        
        for char in strs:
            if t[start:].startswith(char):
                btk(start + len(char), value + 1)

    btk(0, 0)

    return answer if answer != float('inf') else -1