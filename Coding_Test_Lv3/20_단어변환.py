# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

# 완전탐색을 이용한 풀이
def check(begin, word):
    if sum([x!=y for x, y in zip(begin, word)]) == 1:
        return True
    
    return False

def solution(begin, target, words):
    if target not in words:
        return 0
    
    m = len(words)
    answer = float('inf')

    def transform(begin, table, value):
        nonlocal answer
        if begin == target:
            if answer > value:
                answer = value
            return
        
        for i in range(m):
            if i in table:
                continue
            
            if check(begin, words[i]):
                table.append(i)
                transform(words[i], table, value+1)
                table.pop()
    
    transform(begin, [], 0)
    
    return answer

# DFS를 사용한 풀이
from collections import deque

def check(cur_node, to_node):
    if sum([x!=y for x, y in zip(cur_node, to_node)]) == 1:
        return True
    
    return False

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    while q:
        cur_node, count = q.popleft()
        if cur_node == target:
            return count
        
        for i in range(len(words)-1, -1, -1):
            if check(cur_node, words[i]):
                q.append((words.pop(i), count+1))