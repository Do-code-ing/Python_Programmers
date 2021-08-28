# https://programmers.co.kr/learn/courses/30/lessons/84325

def solution(table, languages, preference):
    max_job = "Z"
    max_score = 0
    for arr in table:
        job, *arr = arr.split()
        score = 0
        for i in range(len(arr)):
            for j in range(len(languages)):
                if arr[i] == languages[j]:
                    score += (5-i) * preference[j]

        if max_score < score:
            max_score = score
            max_job = job

        elif max_score == score:
            if max_job > job:
                max_job = job

    return max_job
