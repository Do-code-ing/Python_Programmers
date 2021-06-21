# https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    x = 0
    y = 1
    cnt = 1
    while cnt < n:
        z = x + y
        x = y
        y = z
        cnt += 1
    return z%1234567