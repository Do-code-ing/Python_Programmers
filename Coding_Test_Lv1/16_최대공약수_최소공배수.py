n = 3
m = 12

import math

def solution(n, m):
    answer = []
    gcd_a = math.gcd(n,m)
    lcm_a = int(n*m/gcd_a)
    answer.append(gcd_a)
    answer.append(lcm_a)
    return answer

print(solution(n, m))

def solution(n, m):
    a, b = max(n, m), min(n, m)
    c = 1
    while c > 0:
        c = a % b
        a, b = b, c
    answer = [a, int(n*m/a)]

    return answer

print(solution(n, m))