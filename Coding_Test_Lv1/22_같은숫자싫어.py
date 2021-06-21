arr = [1,1,3,3,0,1,1]

def solution(arr):
    answer = []
    if arr[0] == arr[-1]:
        answer.append(arr[0])
    for idx, x in enumerate(arr):
        a = arr[idx]
        b = arr[idx-1]
        if a != b:
            answer.append(x)
    return answer

print(solution(arr))


def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]:
            continue
        a.append(i)
    return a

print(no_continuous(arr))