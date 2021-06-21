# https://programmers.co.kr/learn/courses/30/lessons/72413?language=python3

from heapq import heappush, heappop
INF = float('inf')

def dykstra(edge, start, n):
    dp = [INF] * (n+1)
    dp[start] = 0
    q = []
    heappush(q, (0, start))
    while q:
        cur_cost, cur_node = heappop(q)
        if dp[cur_node] < cur_cost:
            continue
        
        for to_node, to_cost in edge[cur_node]:
            to_cost += cur_cost
            if dp[to_node] > to_cost:
                dp[to_node] = to_cost
                heappush(q, (to_cost, to_node))
    
    return dp

def solution(n, s, a, b, fares):
    edge = [[] for _ in range(n+1)]
    for c, d, f in fares:
        edge[c].append((d, f))
        edge[d].append((c, f))
    
    answer = INF
    # 문제에서 원하는 것을 잘 생각해보면
    # 결국 어디까지 같이타고, 어디부터 나눠탈 것인가가 중요하다.
    # 모든 지점에 대해 노드 s, a, b까지의 거리를 구하고, 그 거리의 합 중 최소값이 정답이 된다.
    for k in range(1, n+1):
        k_ = dykstra(edge, k, n)
        answer = min(answer, k_[s] + k_[a] + k_[b])

    return answer