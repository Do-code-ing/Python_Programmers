from collections import deque
from sys import setrecursionlimit
setrecursionlimit(10**6)

def solution(sales, links):
    INF = float('inf')
    n = len(sales)
    edge = [[] for _ in range(n+1)]
    for a, b in links:
        edge[a].append(b)
        edge[b].append(a)
    
    leader = [False] * (n+1)
    parent = [[i] for i in range(n+1)]
    visit = [False] * (n+1)
    visit[1] = True
    q = deque([1])
    while q:
        cur_node = q.popleft()
        for to_node in edge[cur_node]:
            if visit[to_node]:
                continue
            
            visit[to_node] = True
            leader[cur_node] = True
            parent[cur_node].append(to_node)
            q.append(to_node)

    leader = [i for i in range(1, n+1) if leader[i]]
    team = [[] for _ in range(n+1)]
    m = 0
    for i in range(1, n+1):
        if len(parent[i]) > 1:
            m += 1
            min_value = INF
            min_person = None
            for member in parent[i]:
                if member in leader:
                    team[i].append(member)
                else:
                    if min_value > sales[member-1]:
                        min_value = sales[member-1]
                        min_person = member
            if min_person != None:
                team[i].append(min_person)

    def choice(idx, choose, value):
        nonlocal answer
        if idx == m:
            if answer > value:
                answer = value
            return

        for member in team[leader[idx]]:
            if choose[member]:
                choice(idx+1, choose, value)
                continue
            
            choose[member] = True
            choice(idx+1, choose, value + sales[member-1])
            choose[member] = False
    
    answer = INF
    choice(0, [False] * (n+1), 0)

    return answer

sales, links = 	[5, 6, 5, 1, 4], [[2, 3], [1, 4], [2, 5], [1, 2]]
print(solution(sales, links))