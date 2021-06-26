# https://programmers.co.kr/learn/courses/30/lessons/68937?language=python3

from collections import deque

def solution(n, edges):
    edge = {i:[] for i in range(1, n+1)}
    for a, b in edges:
        edge[a].append(b)
        edge[b].append(a)
    
    def bfs(start):
        visit = [False] * (n+1)
        visit[start] = True
        dp = []
        q = deque([(start, 0)])
        while q:
            cur_node, cost = q.popleft()
            dp.append((cur_node, cost))
            cost += 1
            for to_node in edge[cur_node]:
                if visit[to_node]:
                    continue
                
                visit[to_node] = True
                q.append((to_node, cost))
        
        return dp

    start = bfs(1)
    check_1, check_2 = start[-1][1], start[-2][1]
    end = bfs(start[-1][0])

    if check_1 == check_2: # 지름의 한 쪽이 될 수 있는 노드가 두 개 이상이라면
        return end[-1][1] # 중간 값은 항상 지름
    
    return end[-2][1] # 아니라면 중간 값은 지름보다 한 단계 낮은 값

n, edges = 8, [[1,2],[1, 3], [1, 7], [7, 8], [1, 4], [4, 5], [4, 6]]
print(solution(n, edges))