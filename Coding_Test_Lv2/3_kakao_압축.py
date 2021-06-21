# https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    dic = dict()
    idx = 1
    for i in range(ord("A"), ord("Z")+1):
        dic[chr(i)] = idx
        idx += 1
    j = 1
    while msg:
        if msg in dic:
            answer.append(dic[msg])
            break
        while msg[0:j] in dic:
            j += 1
        if msg[0:j-1] in dic:
            answer.append(dic[msg[0:j-1]])
        if not msg[0:j] in dic:
            dic[msg[0:j]] = idx
            idx += 1
            msg = msg.replace(msg[0:j-1], "", 1)
            j = 1
        else: j = 1

    return answer

msg = "KAKAO"
print(solution(msg))