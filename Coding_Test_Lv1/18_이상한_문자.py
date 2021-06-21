s = "try hello world"

def solution(s):
    answer = ""
    s = s.split(" ")
    for x in s:
        for i, y in enumerate(x):
            if i % 2 == 0:
                answer += y.upper()
            else:
                answer += y.lower()
        answer += " "
    return answer[:-1]

print(solution(s))