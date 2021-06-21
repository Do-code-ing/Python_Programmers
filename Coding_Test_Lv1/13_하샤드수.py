x = 10

def solution(x):
    answer = True
    y = len(str(x))
    n = 0
    for i in range(y):
        z = str(x)[i]
        n += int(z)
    if x % n != 0:
        answer = False
    return answer

print(solution(x))

def solution(x):
    answer = True
    z = 0
    for y in str(x):
        z += int(y)
    if x % z != 0:
        answer = False
    return answer

print(solution(x))

def solution(x):
    answer = True
    if x % sum(int(y) for y in str(x)):
        answer = False
    return answer

print(solution(x))