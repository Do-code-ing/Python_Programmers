# https://programmers.co.kr/learn/courses/30/lessons/76503?language=python3

import sys
sys.setrecursionlimit(100000)

def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    edge = [[] for _ in range(len(a))]
    for node_a, node_b in edges:
        edge[node_a].append(node_b)
        edge[node_b].append(node_a)
    
    answer = 0
    def dfs(cur_node, purpose_node):
        nonlocal answer
        for next_node in edge[cur_node]:
            if next_node != purpose_node:
                dfs(next_node, cur_node)
        
        a[purpose_node] += a[cur_node]  # 가중치 몰아주기
        answer += abs(a[cur_node])      # 가중치 몰아준 만큼 카운트
        a[cur_node] = 0                 # 가중치를 몰아줬기 때문에 0으로 업데이트
    
    dfs(0, 0)
    
    return answer