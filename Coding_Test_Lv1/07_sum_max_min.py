a = 5
b = 3

def solution(a, b):
    answer = 0
    min_num = min(a,b)
    max_num = max(a,b)
    for i in range(min_num, max_num+1):
        answer += i
    return answer

print(solution(a,b))

def solution(a, b):
    return sum(range(min(a,b),max(a,b)+1))