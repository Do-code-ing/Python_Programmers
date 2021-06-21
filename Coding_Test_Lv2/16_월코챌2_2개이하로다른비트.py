# https://programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []
    for num in numbers:
        # 입력값이 짝수라면 +1 해주기
        if num % 2 == 0:
            answer.append(num+1)
        # 짝수가 아니라면
        else:
            # 입력값을 2진법으로 쓴 수에 0이 없을 수도 있으므로 0을 맨 왼쪽에 추가
            x = "0" + f"{num:b}"
            # 입력값의 오른쪽 인덱스부터 첫 번째 0이 등장하는 인덱스 찾기
            where = x.rfind("0")
            x = list(x)
            # 1, 0 스왑
            x[where] = "1"
            x[where+1] = "0"
            answer.append(int("".join(x), 2))
            
    return answer