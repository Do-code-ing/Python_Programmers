# https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3

def solution(gems):
    LG = len(gems)
    LSG = len(set(gems))
    start, end = 0, 0
    min_value = float("inf")
    db = {}
    while end < LG and start < LG:
        # 모든 보석을 한 개 이상씩 사게될 때까지 end 증가
        while LSG != len(db) and end < LG:
            if gems[end] not in db:
                db[gems[end]] = 0
            db[gems[end]] += 1
            end += 1
        # 모든 보석을 한개 이상씩 사게될 때까지 start 증가
        while LSG == len(db) and start < end:
            db[gems[start]] -= 1
            if db[gems[start]] == 0:
                del db[gems[start]]
            start += 1
            if min_value > end-start:
                min_value = end-start
                answer = [start, end]

    return answer