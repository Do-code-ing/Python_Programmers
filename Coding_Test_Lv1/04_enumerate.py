answers = [1,2,3,4,5]

def solution(answers):
    student = {1:[1,2,3,4,5], 2:[2,1,2,3,2,4,2,5], 3:[3,3,1,1,2,2,4,4,5,5]}
    score = {1:0, 2:0, 3:0}
    
    for idx, answer in enumerate(answers): # 정답을 순서대로 idx값과 answer값으로 나누고 반복한다.
        for key, value in student.items(): # 스튜던트의 key값과 value값을 반복한다.
            if answer == value[idx % len(value)]: # value의 idx 친구를 for문 순환주기마다 초기화...;; 이 부분 공부
                score[key] += 1 # 정답 처리
    highest = max(score.values()) # 제일 높은 값 표기
    result = [key for key, value in score.items() if value == highest] # 한줄 if, key값 표기,
    # 그 key값은 score에서 가져왔다. value가 highest랑 같은 값만, 즉 점수가 가장 높은사람의 key값을 가져온다
    return result

print(solution(answers))