# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    dic = dict()
    for r in record:
        if "Enter" in r or "Change" in r:
            cmd, uid, name = r.split()
            dic[uid] = name
    for r in record:
        if "Enter" in r:
            cmd, uid, name = r.split()
            answer.append(str(dic[uid])+'님이 들어왔습니다.')
        if "Leave" in r:
            cmd, uid = r.split()
            answer.append(str(dic[uid])+'님이 나갔습니다.')
    return answer