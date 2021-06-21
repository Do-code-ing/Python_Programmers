s = "qwer"

def solution(s):
    if len(s) % 2 == 1:
        s = s[:int(len(s)/2+0.5)]
        answer = s[-1]
    else:
        s = s[:int(len(s)/2+1)]
        answer = s[-2:]
    return answer

print(solution(s))
