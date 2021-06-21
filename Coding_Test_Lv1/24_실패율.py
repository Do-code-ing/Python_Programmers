N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):
    temp = {} # 모든 단계의 실패율 집합
    users = len(stages)
    for stage in range(1, N+1):
        if users != 0: #
            losers = stages.count(stage) # n단계 실패자 모음
            temp[stage] = losers/users # 실패율 집합에 저장
            users -= losers
        else:
            temp[stage] = 0
    return sorted(temp, key=lambda x:temp[x], reverse=True)

print(solution(N, stages))