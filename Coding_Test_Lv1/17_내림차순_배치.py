n = 118372

def solution(n):
    n_list = list(reversed(sorted(str(n))))
    n_len = len(str(n))
    a = 0
    for i, m in enumerate(n_list):
        a += int(m)*10**(n_len-i)
    return int(a/10)

print(solution(n))

def solution(n):
    n = list(reversed(sorted(str(n))))
    return int("".join(n))