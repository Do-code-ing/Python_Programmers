participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

from collections import Counter # Counter는 list를 key와 value 값을 만들어 dictionary으로 저장

def solution(participant, completion):
    answer = ''
    p = Counter(participant)
    c = Counter(completion)
    answer = list(p-c)[0]
    return answer

print(solution(participant, completion))
    
def solution(participant, completion):
    answer = ''
    dic = {}
    temp = 0 # 해시 값 보관
    for par_person in participant:
        dic[hash(par_person)] = par_person # 사전형 변수 dic에 hash값을 key로 하여 value 값 저장
        temp += hash(par_person) # 임시 변수 temp에 해시 값 저장
    for com_person in completion:
        temp -= hash(com_person) # 임시 변수 temp에 저장되어있는 해시 값 제거
    answer = dic[temp] # dic에 temp 값을 등장

    return answer