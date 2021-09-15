# https://programmers.co.kr/learn/courses/30/lessons/86048

def solution(enter, leave):
    n = len(enter)
    answer = [0] * (n+1)
    dp = [[False] * (n+1) for _ in range(n+1)]
    room = set()

    i, j = 0, 0
    while i < n and j < n:
        while leave[j] in room:
            room.remove(leave[j])
            j += 1

        y = enter[i]
        room.add(y)
        i += 1

        if len(room) > 1:
            for x in room:
                dp[x][y] = dp[y][x] = True

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                continue

            if dp[i][j]:
                answer[i] += 1

    return answer[1:]
