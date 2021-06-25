# https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations

def solution(orders, course):
    answer = []
    table = {}
    n = 0
    # 제일 많이 주문된 음식 조합 찾기
    for order in orders:
        order = sorted(order)
        if n < len(order):
            n = len(order)

        for i in range(2, len(order)+1):
            for arr in combinations(range(len(order)), i):
                temp = ""
                for j in arr:
                    temp += order[j]
                if temp not in table:
                    table[temp] = 0
                table[temp] += 1

    # 각 음식 조합을 길이별로 분류
    dp = [[] for _ in range(max(n, course[-1])+1)]
    for candi in table:
        if len(candi) in course:
            dp[len(candi)].append((candi, table[candi]))
    
    # 각 길이별로 가장 빈도가 높은 순으로 정렬
    for i in dp:
        i.sort(key=lambda x:x[1], reverse=True)

    # 2번 이상 등장했으면서 가장 많이 등장한 음식 조합 선별
    for i in course:
        if not dp[i]:
            continue

        x = dp[i][0][1]
        if x < 2:
            continue
        
        # 선별 후 코스 요리로 등록
        idx = 0
        while idx < len(dp[i]) and x == dp[i][idx][1]:
            answer.append(dp[i][idx][0])
            idx += 1

    answer.sort()
    return answer

orders, course = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]
print(solution(orders, course))