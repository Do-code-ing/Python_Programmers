d = [1,3,2,5,4]
budget = 9

def solution(d, budget):
    answer = 0
    d = sorted(d)
    if sum(d) <= budget:
        answer += len(d)
    else:
        for x in d:
            if budget - x >= 0:
                budget -= x
                answer += 1
    return answer

print(solution(d, budget))