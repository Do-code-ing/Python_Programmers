# https://programmers.co.kr/learn/courses/30/lessons/67260?language=python3

# 노드 B를 방문하기 전에 노드 A를 방문해야 하므로, 위상 정렬을 통해 가능한지 불가능한지 판별
from collections import deque

def solution(n, path, order):
    edge = [[] for _ in range(n)]
    for a, b in path:
        edge[a].append(b)
        edge[b].append(a)
    
    # 0부터 시작해 방문처리를 하며 방향그래프로 만들기 + 진입차수 계산
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    visit = [False] * n
    visit[0] = True
    q = deque([0])
    while q:
        cur_node = q.popleft()
        for to_node in edge[cur_node]:
            if not visit[to_node]:
                visit[to_node] = True
                graph[cur_node].append(to_node)
                indegree[to_node] += 1
                q.append(to_node)

    # 그래프에 간선 추가 및 진입차수 추가 계산
    for a, b in order:
        graph[a].append(b)
        indegree[b] += 1
    
    # 위상정렬
    result = []
    q = deque([0])
    while q:
        cur_node = q.popleft()
        result.append(cur_node)
        for to_node in graph[cur_node]:
            indegree[to_node] -= 1
            if indegree[to_node] == 0:
                q.append(to_node)
    
    # 정렬 결과 모든 노드를 방문할 수 있는지 체크
    if len(result) == n:
        return True

    return False