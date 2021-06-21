n = 7

def solution(n):
    if n % 2 == 1:
        return n//2*"수박"+"수"
    else:
        return n//2*"수박"

print(solution(n))

def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)