num = 16

def solution(num):
    answer = 0
    for i in range(500):
        while i == 499:
            if num == 1:
                break
            elif num % 2 == 1:
                num = num*3+1
            else:
                num = num/2
            answer += 1
        if answer >= 500:
            answer = -1
    return answer

print(solution(num))