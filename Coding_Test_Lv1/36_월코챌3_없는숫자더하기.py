# https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    answer = 45
    for x in numbers:
        answer -= x

    return answer
