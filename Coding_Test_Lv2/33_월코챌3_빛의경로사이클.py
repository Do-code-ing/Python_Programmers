def check(nx, ny, n, m):
    if nx < 0:
        return 0
    if nx == n:
        return 1
    if ny < 0:
        return 2
    if ny == m:
        return 3
    return -1


def initialization(nx, ny, n, m, value):
    if value == 0:
        return n-1, ny
    if value == 1:
        return 0, ny
    if value == 2:
        return nx, m-1
    return nx, 0


def solution(grid):
    answer = []
    n = len(grid)
    m = len(grid[0])
    dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상 우 하 좌
    left = [3, 0, 1, 2]
    right = [1, 2, 3, 0]

    dp = [[[False, False, False, False] for _ in range(m)] for _ in range(n)]

    for x in range(n):
        for y in range(m):
            for k in range(-4, 0, 1):
                if dp[x][y][k] == True:
                    continue

                count = 0
                while True:
                    if k < 0:
                        k += 4
                    elif grid[x][y] == "L":
                        k = left[k]
                    elif grid[x][y] == "R":
                        k = right[k]

                    if dp[x][y][k] == True:
                        break

                    dp[x][y][k] = True

                    nx = x + dr[k][0]
                    ny = y + dr[k][1]
                    value = check(nx, ny, n, m)
                    if value == -1:
                        x, y = nx, ny
                        count += 1
                    else:
                        x, y = initialization(nx, ny, n, m, value)
                        if not (x == nx and y == ny):
                            count += 1

                answer.append(count)

    answer.sort()

    return answer
