n = 12

def solution(n):
    answer = 0
    if n == 0:
        answer = 0
    else:
        for i in range(1, 3001):
            if n % i == 0:
                answer += i
    return answer

print(solution(n))

def solution(n):
    answer = 0
    if n == 0:
        answer = 0
    else:
        for i in range(1, n//2+1):
            if n % i == 0:
                answer += i
    return answer+n

def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])