n = 12

def solution(n):
    set_n = set(i for i in range(2, n+1))
    for x in range(2, n+1):
        if x in set_n:
            # x의 배수 지우기
            set_n -= set(i for i in range(x*x, n+1, x))
    print(set_n)
    return len(set_n)

print(solution(n))

# 에라토스테네스의 체

n = 12

def solution(n):
    set_n = set(i for i in range(2, n+1))
    for x in range(2, n+1):
        if x in set_n:
            set_n -= set(i for i in range(x*x, n+1,x))
    return len(set_n)

print(solution(n))