# https://programmers.co.kr/learn/courses/30/lessons/12973

from collections import deque

def solution(s):
    q = deque(list(s))
    stack = [q.popleft()]
    while q:
        x = q.popleft()
        if not stack or x != stack[-1]:
            stack.append(x)
        else:
            stack.pop()
    if stack:
        return 0
    else:
        return 1


def solution(s):
    stack = []
    for c in s:
        if not stack:
            stack.append(c)
        elif c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    return int(not stack)