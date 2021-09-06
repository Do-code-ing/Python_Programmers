# https://programmers.co.kr/learn/courses/30/lessons/85002

def solution(weights, head2head):
    n = len(weights)
    score = [[0, 0] for _ in range(n)]
    result = [[i, 0, 0, weights[i]] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if head2head[i][j] == "W":
                score[i][0] += 1
                if weights[i] < weights[j]:
                    result[i][2] += 1
            elif head2head[i][j] == "L":
                score[i][1] += 1

    for i, (win, lose) in enumerate(score):
        match = win + lose
        if match == 0:
            continue

        result[i][1] = win / match

    result.sort(key=lambda x: x[3], reverse=True)
    result.sort(key=lambda x: x[2], reverse=True)
    result.sort(key=lambda x: x[1], reverse=True)

    answer = []
    for i in range(n):
        answer.append(result[i][0]+1)

    return answer
