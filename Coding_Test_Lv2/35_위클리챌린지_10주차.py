# https://programmers.co.kr/learn/courses/30/lessons/87377

def get_x(a, b, c, d, e, f):
    try:
        result = (b*f - e*d) / (a*d - b*c)
    except:
        result = None
    return result


def get_y(a, b, c, d, e, f):
    try:
        result = (e*c - a*f) / (a*d - b*c)
    except:
        result = None
    return result


def solution(line):
    INF = float("inf")
    coord = []
    n = len(line)
    max_x = max_y = -INF
    min_x = min_y = INF

    for i in range(n):
        a, b, e = line[i]
        for j in range(i+1, n):
            c, d, f = line[j]

            x = get_x(a, b, c, d, e, f)
            y = get_y(a, b, c, d, e, f)
            if x == None or y == None:
                continue

            if int(x) != x or int(y) != y:
                continue

            x, y = int(x), int(y)
            coord.append((x, y))
            if max_x < x:
                max_x = x
            if max_y < y:
                max_y = y
            if min_x > x:
                min_x = x
            if min_y > y:
                min_y = y

    n = max_y - min_y + 1
    m = max_x - min_x + 1

    result = [[False] * m for _ in range(n)]

    for x, y in coord:
        i = max_y-y
        j = x-min_x
        result[i][j] = True

    answer = []
    for i in range(n):
        temp = ""
        for j in range(m):
            if result[i][j] == True:
                temp += "*"
            else:
                temp += "."
        answer.append(temp)

    return answer
