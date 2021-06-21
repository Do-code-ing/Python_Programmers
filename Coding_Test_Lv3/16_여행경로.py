# https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3

def solution(tickets):
    n = len(tickets)+1
    answer = []
    edge = {}
    for i in range(len(tickets)):
        a, b = tickets[i]
        if a not in edge:
            edge[a] = []
        edge[a].append((b, i))

    def dfs(start, path, visit):
        nonlocal answer
        if len(path) == n:
            answer.append(path[:])
            return

        if start not in edge:
            return
        
        for to_node, index in edge[start]:
            if index in visit:
                continue

            visit.append(index)
            path.append(to_node)
            dfs(to_node, path, visit)
            visit.pop()
            path.pop()
    
    dfs("ICN", ["ICN"], [])
    answer.sort()

    return answer[0]