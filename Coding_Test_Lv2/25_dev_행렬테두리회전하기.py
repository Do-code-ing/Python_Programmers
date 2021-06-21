# https://programmers.co.kr/learn/courses/30/lessons/77485?language=python3

def solution(rows, columns, queries):
    answer = []
    # 초기화
    graph = [[0] * (columns+1) for _ in range(rows+1)]
    num = 1
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            graph[i][j] = num
            num += 1
    # 돌리고 돌리고
    for top, left, bottom, right in queries:
        first = graph[top][left]
        value = first
        for i in range(top, bottom):
            graph[i][left] = graph[i+1][left]
            if value > graph[i][left]:
                value = graph[i][left]
        
        for j in range(left, right):
            graph[bottom][j] = graph[bottom][j+1]
            if value > graph[bottom][j]:
                value = graph[bottom][j]
        
        for i in range(bottom, top, -1):
            graph[i][right] = graph[i-1][right]
            if value > graph[i][right]:
                value = graph[i][right]
        
        for j in range(right, left, -1):
            graph[top][j] = graph[top][j-1]
            if value > graph[top][j]:
                value = graph[top][j]
        
        graph[top][left+1] = first
        answer.append(value)
        
    return answer