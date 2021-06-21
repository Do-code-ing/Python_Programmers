# https://programmers.co.kr/learn/courses/30/lessons/76502

from collections import deque

def solution(s):
    left = ["(", "[", "{"]
    table = [("(", ")"), ("[", "]"), ("{", "}")]
    
    n = len(s) # 최대 회전수 = 괄호 개수
    q = deque(list(s))
    answer = 0
    count = 0
    while count < n:
        # 현재 문자열이 올바른 괄호인지 체크
        stack = []
        for c in q:
            # 여는 괄호라면 스택에 넣고
            if c in left:
                stack.append(c)
            # 닫는 괄호인데 짝이 맞다면 스택에서 제거
            elif stack and (stack[-1], c) in table:
                stack.pop()
            # 아니라면 스택에 넣기
            else:
                stack.append(c)
                break
        # 왼쪽으로 돌리기
        q.rotate(-1)
        count += 1
        # 올바른 괄호라면 체크
        if not stack:
            answer += 1
    
    return answer