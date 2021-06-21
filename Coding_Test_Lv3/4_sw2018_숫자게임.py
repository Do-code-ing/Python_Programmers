# https://programmers.co.kr/learn/courses/30/lessons/12987?language=python3

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    while A and B:
        if B[-1] > A[-1]:
            answer += 1
            B.pop()
        A.pop()

    return answer