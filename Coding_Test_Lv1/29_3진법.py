n = 45

def solution(n):
    answer = ''
    while (n>=3):
        answer+=str(n%3)
        n = n//3
    answer += str(n)
    print(answer)
    answer = int(answer,3)
    return answer

print(solution(n))
