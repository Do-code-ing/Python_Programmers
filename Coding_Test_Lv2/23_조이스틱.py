def solution(name):
    answer = 0
    n = len(name)
    visit = [False] * n
    count = n # 처리해야할 알파벳 개수
    
    for i in range(n):
        if name[i] == "A":
            visit[i] = True
            count -= 1
    
    # 현재 커서 위치에서 가장 가까운 "A"가 아닌 지점 찾기
    def dykstra(start):
        nonlocal answer
        visit[start] = True
        min_value = float("inf")
        min_idx = start

        # 거리 계산
        for i in range(n):
            if visit[i]:
                continue
            
            value = min(start+n-i, abs(start-i))
            if min_value > value:
                min_value = value
                min_idx = i
        
        if min_idx == start:
            return

        answer += min_value
        dykstra(min_idx)

    dykstra(0)
    
    # 각 지점에서 A에서 해당 알파벳으로 만드는 비용
    for value in name:
        value = ord(value)
        if value < 78: # Up
            answer += value - 65
        else: # Down
            answer += 91 - value

    return answer