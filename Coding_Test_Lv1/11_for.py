x = 2
n = 5

def solution(x, n):
    answer = []
    for y in range(1, n+1):
        answer.append(x*y)
    return answer

print(solution(x, n))

def solution(x, n):
    return [i * x + x for i in range(n)]
