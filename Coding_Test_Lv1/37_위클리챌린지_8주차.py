# https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    max_x, max_y = 0, 0

    for x, y in sizes:
        if x < y:
            x, y = y, x

        if max_x < x:
            max_x = x
        if max_y < y:
            max_y = y

    return int(max_x * max_y)
