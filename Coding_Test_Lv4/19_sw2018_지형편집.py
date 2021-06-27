# https://programmers.co.kr/learn/courses/30/lessons/12984

def solution(land, P, Q):
    # land를 1차원 배열로 만들고 오름차순으로 정렬
    dp = []
    for la in land:
        dp += la
    
    dp.sort()
    n = len(dp)
    total = sum(dp)     # 모든 블록의 개수
    answer = total * Q  # 모든 블록을 제거한 것을 기준으로 정답을 초기화
    cost = (total - (dp[0] * n)) * Q    # 제일 낮은 층으로 만들 때의 비용
    if answer > cost:
        answer = cost
    
    for i in range(1, n):
        if dp[i] != dp[i-1]:    # 블록 층 수의 변동이 생기면(예를 들어, 한 층 더 높이에서의 변동 값을 계산)
            # 이전 낮은 층으로 만들 때의 비용에서 다음 높이의 층을 계산하려면,
            # 층수가 올라간 만큼,
            # i개의 빈 칸이 생기고, n-i개의 블록을 안 지워도 되므로 각각 계산
            cost += (P * i * (dp[i] - dp[i-1])) - (Q * (n-i) * (dp[i] - dp[i-1]))
            if answer > cost:
                answer = cost

    return answer