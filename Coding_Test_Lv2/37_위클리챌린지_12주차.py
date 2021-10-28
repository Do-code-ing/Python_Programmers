# https://programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations


def solution(k, dungeons):
    answer = 0
    n = len(dungeons)

    for dungeon in permutations(dungeons):
        cur_k = k
        result = 0
        for least, must in dungeon:
            if cur_k < least or cur_k - must < 0:
                continue

            cur_k -= must
            result += 1

        if answer < result:
            answer = result

        if answer == n:
            return answer

    return answer
