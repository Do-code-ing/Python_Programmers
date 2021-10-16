# https://programmers.co.kr/learn/courses/30/lessons/87391

def solution(n, m, x, y, queries):

    def move(i, j, q):
        arrow, dist = q
        if arrow == 0:
            j = max(j-dist, 0)
        elif arrow == 1:
            j = min(j+dist, m-1)
        elif arrow == 2:
            i = max(i-dist, 0)
        else:
            i = min(i+dist, n-1)
        return i, j

    def result(i, j, queries):
        for idx, q in enumerate(queries):
            if (idx, q) in dp[i][j]:
                return False
            i, j = move(i, j, q)

        return i, j

    def check(i, j, queries):
        for idx, q in enumerate(queries):
            dp[i][j].append((idx, q))
            i, j = move(i, j, q)

    answer = 0
    dp = [[[] for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            value = result(i, j, queries)
            if value == False:
                answer += 1
            elif (value[0] == x and value[1] == y):
                answer += 1
                check(i, j, queries)

    return answer


n, m, x, y, queries = 2, 5, 0, 1, [
    [3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]
print(solution(n, m, x, y, queries))

# 각 좌표마다 다음 행동에 대해 인덱스를 기록하고, 결과를 기록한다.
# 일단 0, 0 부터 출발시켜보고, x, y 좌표에 도달한 경우, 정답으로 인정한 뒤
# 해당 쿼리 인덱스가 각각 어디에 도달했는지를 기록하고,
# 다른 좌표에서 출발해서 정답 인덱스와 일치하는 구간이 나타나면 그 뒤는 계산하지 않고 정답처리
# 그러지 않은 경우, 계속 진행.
#   2
# 0   1
#   3
