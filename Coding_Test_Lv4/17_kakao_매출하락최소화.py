# https://programmers.co.kr/learn/courses/30/lessons/72416

def solution(sales, links):
    n = len(sales)
    edge = {i+1:[] for i in range(n)}
    for a, b in links:
        edge[a].append(b)
        edge[b].append(a)
    
    dp = {i+1:[0, sales[i]] for i in range(n)} # [i가 참석안 할 때의 손해, i가 참석할 때의 손해]
    visit = {i+1:False for i in range(n)}

    def dfs(i):
        visit[i] = True
        next_visit = [k for k in edge[i] if visit[k] == False] # 리프 노드 판별 및 재귀를 위한 리스트
        next_k0 = 0
        next_k1 = 0
        for k in next_visit:
            dfs(k)
            next_k0 += dp[k][0] # k가 참석 안 할 때 발생하는 최소 누적 손해합
            next_k1 += min(dp[k][0], dp[k][1]) # k가 참석할 때 발생하는 최소 누적 손해합
        
        dp[i][0] += next_k1 # 여태까지의 최소 누적 손해합을 더하여 갱신
        dp[i][1] += next_k1
        # 만약 i가 리프 노드가 아니면,
        if next_visit and next_k0 == next_k1:
            # i가 참석 안 할 때를 같은 팀의 다른 멤버가 참여함으로 생기는 손해합 중 최소값으로 갱신한다.
            dp[i][0] = min([next_k1 - dp[k][0] + dp[k][1] for k in next_visit])

        return min(dp[i])
    
    return dfs(1)