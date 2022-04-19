# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    temp = dict()
    result = dict()
    for i, id_ in enumerate(id_list):
        temp[id_] = i
        result[id_] = set()
    
    for rep in report:
        a, b = rep.split()
        result[b].add(a)
    
    answer = [0 for i in range(len(id_list))]
    for id_ in result:
        if len(result[id_]) >= k:
            for x in result[id_]:
                answer[temp[x]] += 1

    return answer
