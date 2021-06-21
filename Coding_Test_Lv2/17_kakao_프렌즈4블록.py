# https://programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    answer = 0
    graph = []
    for i in board:
        graph.append(list(i))
    
    while True:
        coord = set() # 터트릴 수 있는 블록 좌표 저장
        for i in range(m-1):
            for j in range(n-1):
                if graph[i][j] == 0:
                    continue
                # 4 * 4 크기의 좌표 값 찾고 저장
                if [graph[i][j]] * 3 == [graph[i+1][j], graph[i][j+1], graph[i+1][j+1]]:
                    coord.add((i, j))
                    coord.add((i+1, j))
                    coord.add((i, j+1))
                    coord.add((i+1, j+1))
        # 더이상 터트릴 게 없다면 반환
        if len(coord) == 0:
            return answer
        # 터트린 블록 수 추가
        answer += len(coord)
        # 터트리기
        for x, y in coord:
            graph[x][y] = 0
        # 터트린 곳 매꿔주기
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if graph[i][j] == 0:
                    x = i-1
                    while graph[x][j] == 0 and x >= 0:
                        x -= 1
        
                    if x == -1:
                        continue

                    graph[i][j] = graph[x][j]
                    graph[x][j] = 0