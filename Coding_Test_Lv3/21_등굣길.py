# https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3

def solution(m, n, puddles):
    p = 1000000007
    dr = [(1, 0), (0, 1)]
    dp = [[-1] * m for _ in range(n)]
    board = [[0] * m for _ in range(n)]
    for y, x in puddles:
        board[x-1][y-1] = 1

    def dfs(x, y):
        if x == n-1 and y == m-1:
            return 1

        if dp[x][y] != -1:
            return dp[x][y] % p

        dp[x][y] = 0
        for dx, dy in dr:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                dp[x][y] += dfs(nx, ny) % p

        return dp[x][y] % p

    return dfs(0, 0)