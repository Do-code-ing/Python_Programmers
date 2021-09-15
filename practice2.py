# https://programmers.co.kr/learn/courses/30/lessons/86054

from sys import setrecursionlimit
setrecursionlimit(10**7)


def solution(a, s):

    def lefty(i, cell):
        for x in range(i-1, -1, -1):
            if cell[x]:
                return x
        return -1

    def backtracking(i, c, cell, n):
        nonlocal count
        if i == n:
            count.add(" ".join(map(str, c)))
            return

        left = lefty(i, cell)
        if left == -1:
            backtracking(i+1, c, cell, n)
        else:
            backtracking(i+1, c, cell, n)
            if sum(cell[i]) == sum(cell[left]):
                c.append(i)
                m = len(cell[left])
                for _ in range(m):
                    cell[i].append(cell[left].pop())
                backtracking(i, c, cell, n)
                c.pop()
                for _ in range(m):
                    cell[left].append(cell[i].pop())

    answer = []
    p = 10**9 + 7
    end = 0
    for n in s:
        end += n
        start = end - n
        cell = [[i] for i in a[start:end]]
        count = set()
        backtracking(0, [], cell, n)
        answer.append(len(count) % p)

    return answer


a, s = [1, 1, 1, 1], [4]
print(solution(a, s))
