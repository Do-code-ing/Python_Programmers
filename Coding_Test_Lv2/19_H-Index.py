# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    n = max(citations)
    dp = [0] * (n+1) # 1회부터 최대 인용된 횟수까지 각각 몇 개의 논문이 인용되었는지 저장
    for i in range(1, n+1):
        for x in citations:
            if x >= i:
                dp[i] += 1

    answer = 0
    for i in range(1, n+1):
        if dp[i] >= i:
            answer = i
        else:
            break

    return answer

print(solution([3, 0, 6, 1, 5]))