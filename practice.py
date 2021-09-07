from collections import deque


def check_arrow(x, y, nx, ny):
    if y == ny:
        if x > nx:
            return 0
        return 4
    elif x + y == nx + ny:
        if x > nx:
            return 1
        return 5
    elif x == nx:
        if y < ny:
            return 2
        return 6
    else:
        if x < nx:
            return 3
        return 7


def solution(arrows):
    dr = {
        0: (-1, 0),
        1: (-1, 1),
        2: (0, 1),
        3: (1, 1),
        4: (1, 0),
        5: (1, -1),
        6: (0, -1),
        7: (-1, -1),
    }
    n = len(arrows) * 2 + 1
    m = n // 2
    x, y = m, m
    edge = [[set() for _ in range(n)] for _ in range(n)]
    for arrow in arrows:
        dx, dy = dr[arrow]
        nx, ny = x + dx, y + dy
        edge[x][y].add((nx, ny))
        edge[nx][ny].add((x, y))
        x, y = nx, ny

    vortex = [[None] * n for _ in range(n)]
    visit = set()
    v = set()
    e = set()
    q = deque()
    for nx, ny in edge[m][m]:
        arrow = check_arrow(m, m, nx, ny)
        q.append((nx, ny, arrow))

    while q:
        x, y, cur_arrow = q.popleft()
        for nx, ny in edge[x][y]:
            new_arrow = check_arrow(x, y, nx, ny)
            if (nx, ny) in visit:
                if vortex[nx][ny]:
                    continue

                for nnx, nny, in edge[nx][ny]:
                    if (x, y) == (nnx, nny):
                        continue

                    new_new_arrow = check_arrow(nx, ny, nnx, nny)
                    if new_arrow != new_new_arrow:
                        vortex[nx][ny] = (nx, ny)
                        v.add((nx, ny))
                        e.add((x, y, nx, ny))
                        e.add((nx, ny, x, y))
                        break
                continue

            if cur_arrow != new_arrow:
                vortex[x][y] = (x, y)
                v.add((x, y))
                e.add((x, y, nx, ny))
                e.add((nx, ny, x, y))

            visit.add((nx, ny))
            q.append((nx, ny, new_arrow))

    e = len(e) // 2
    v = len(v)
    return 1 - v + e


arrows = [6, 0, 3, 0, 5, 2, 6, 0, 3, 0, 5]
print(solution(arrows))
