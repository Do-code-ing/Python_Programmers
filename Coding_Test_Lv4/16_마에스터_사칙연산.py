# https://programmers.co.kr/learn/courses/30/lessons/1843?language=python3

def solution(arr):
    n = len(arr)
    dp = [[None] * n for _ in range(n)]
    for i in range(0, n, 2):
        dp[i][i] = int(arr[i])
    
    # arr의 마지막 부분부터 재귀적으로 구하기
    def find_value(i, j): # i : 살펴볼 수식의 첫 인덱스, j : 살펴볼 수식의 마지막 인덱스
        if dp[i][j] != None:
            return dp[i][j]
        
        if i == 0 or arr[i-1] == "+":   # arr의 맨 앞이거나, 수식의 앞이 덧셈 부호라면,
            result = float('-inf')      # 해당 값은 제일 커야하므로 max로 재귀 호출
            for k in range(i, j, 2):
                if arr[k+1] == "+":
                    result = max(result, find_value(i, k) + find_value(k+2, j))
                else:
                    result = max(result, find_value(i, k) - find_value(k+2, j))
        else:                           # 수식의 앞이 뺄셈 부호라면,
            result = float('inf')       # 해당 값은 제일 작아야하므로 min으로 재귀 호출
            for k in range(i, j, 2):
                if arr[k+1] == "+":
                    result = min(result, find_value(i, k) + find_value(k+2, j))
                else:
                    result = min(result, find_value(i, k) - find_value(k+2, j))
        
        dp[i][j] = result
        return result

    return find_value(0, n-1)