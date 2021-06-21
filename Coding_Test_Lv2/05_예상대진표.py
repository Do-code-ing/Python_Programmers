# https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    c = 1
    a, b = min(a, b), max(a, b)
    while c:
        if a+1 == b and b%2 == 0:
            return c
        a = a//2 + a%2
        b = b//2 + b%2
        c += 1

n = 8
a = 4
b = 7
print(solution(n, a, b))