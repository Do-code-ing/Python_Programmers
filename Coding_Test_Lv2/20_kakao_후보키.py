# https://programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations

def solution(relation):
    # 유일성만 체크
    def unique(arr):
        db = [""] * n
        for i in range(n):
            for j in arr:
                db[i] += " " + relation[i][j]

        if len(db) == len(set(db)):
            return arr
        return
    # 유일성 + 최소성 체크
    def check(arr):
        nonlocal answer
        for can in candi:
            if can.issubset(arr):
                break
        else:
            candi.append(arr)
            answer += 1

    n = len(relation)
    m = len(relation[0])
    answer = 0
    candi = [] # 최소성 저장

    for i in range(1, m+1):
        for arr in combinations(range(m), i):
            arr = unique(arr)
            if arr:
                check(set(arr))

    return answer