# https://programmers.co.kr/learn/courses/30/lessons/72412

from bisect import bisect_left, insort_left

def solution(info, query):
    # 데이터 테이블 만들기
    data = dict()
    for a in ["cpp", "java", "python", "-"]:
        for b in ["backend", "frontend", "-"]:
            for c in ["junior", "senior", "-"]:
                for d in ["chicken", "pizza", "-"]:
                    data.setdefault((a, b, c, d), list())
    
    # 데이터 테이블에 지원자 점수를 정렬하면서 기입
    for i in info:
        i = i.split()
        value = int(i[4])
        for a in [i[0], "-"]:
            for b in [i[1], "-"]:
                for c in [i[2], "-"]:
                    for d in [i[3], "-"]:
                        insort_left(data[(a, b, c, d)], value)

    # 합격 기준 데이터와 비교
    answer = list()
    for q in query:
        q = q.split()
        pool = data[(q[0], q[2], q[4], q[6])]
        score = int(q[7])
        idx = bisect_left(pool, score)
        answer.append(len(pool)-idx)
        
    return answer

info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"
    ]
query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"
    ]
    
print(solution(info, query))
answer = [1, 1, 1, 1, 2, 4]