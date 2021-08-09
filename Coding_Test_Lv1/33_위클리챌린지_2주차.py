# https://programmers.co.kr/learn/courses/30/lessons/83201

def grading(score):
    if 90 <= score:
        return "A"
    elif 80 <= score:
        return "B"
    elif 70 <= score:
        return "C"
    elif 50 <= score:
        return "D"
    return "F"

def solution(scores):
    result = ""
    n = len(scores)
    
    for j in range(n):
        m = n
        sum_score = 0
        flag_max = False # 최고점수가 두 개 이상인지 체크
        flag_min = False # 최하점수가 두 개 이상인지 체크
        max_value = -1
        min_value = 101
        for i in range(n):
            value = scores[i][j]
            sum_score += value
            if max_value < value:
                max_value = value
                flag_max = False
            elif max_value == value:
                flag_max = True
                
            if min_value > value:
                min_value = value
                flag_min = False
            elif min_value == value:
                flag_min = True
        
        if not flag_min:
            if min_value == scores[j][j]:
                m -= 1
                sum_score -= min_value
        if not flag_max:
            if max_value == scores[j][j]:
                m -= 1
                sum_score -= max_value
        
        sum_score /= m
        result += grading(sum_score)

    return result