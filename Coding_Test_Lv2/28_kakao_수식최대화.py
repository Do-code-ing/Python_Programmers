# https://programmers.co.kr/learn/courses/30/lessons/67257?language=python3

from itertools import permutations

def solution(expression):
    # 표현식 안에 '*', '+', '-' 가 있는지 확인
    sign = [x for x in ["*", "+", "-"] if x in expression]
    # 부호가 하나라면 그대로 출력
    if len(sign) == 1:
        return abs(eval(expression))
    # 역순으로 split
    answer = 0
    for order in permutations(sign):
        last = order[0]
        second = order[1]
        arr = []
        for formula in expression.split(last):
            temp = [f"({i})" for i in formula.split(second)]
            arr.append(f"({second.join(temp)})")
        arr = abs(eval(last.join(arr)))
        if answer < arr:
            answer = arr               
        
    return answer