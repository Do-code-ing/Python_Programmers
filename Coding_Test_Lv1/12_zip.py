arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

def solution(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return answer

print(solution(arr1, arr2))

# (a, b)
# (([1,2],[3,4]), ([2,3],[5,6]))