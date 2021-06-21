n = 9
lost = [2,4,7,8]
reserve = [3,6,9]

def solution(n, lost, reserve):
    for i in range(1, n+1):
        if i in lost and i in reserve:
            reserve.remove(i)
            lost.remove(i)
    for i in range(1, n+1):
        if i in lost:
            if (i-1) in reserve:
                reserve.remove(i-1)
                lost.remove(i)
            elif (i+1) in reserve:
                reserve.remove(i+1)
                lost.remove(i)
    return n - len(lost)

print(solution(n, lost, reserve))