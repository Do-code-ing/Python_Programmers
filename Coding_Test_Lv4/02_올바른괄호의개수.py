# https://programmers.co.kr/learn/courses/30/lessons/12929

from math import factorial

def solution(n):
    numer = factorial(2*n) // (n+1)
    fact_n = factorial(n)
    deno = fact_n * fact_n

    return numer // deno

# 1 = 1
# 2 = 2
# 3 = 5
# 4 = 14
# ...
# 카탈란 수 구하기
# Cn = (2n)! / n!n! / n+1