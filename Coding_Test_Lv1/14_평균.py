arr = [1,2,3,4]

def solution(arr):
    answer = 0
    for a in arr:
        answer += a
    answer = answer/len(arr)
    return answer

def solution(arr):
    answer = sum(a for a in arr)/len(arr)
    return answer

print(solution(arr))