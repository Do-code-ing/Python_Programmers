# https://programmers.co.kr/learn/courses/30/lessons/12923?language=python3

def solution(begin, end):
    answer = []
    for num in range(begin, end+1):
        if num == 1:
            answer.append(0)
        else:
            # 해당 숫자가 소수인 경우, 제일 작은 약수로 나눈 몫을 저장하면 된다.
            # 블록의 제한이 1번 ~ 10,000,000번까지이므로, 10**7 이하일 때만 저장한다.
            for x in range(2, int(num**0.5)+1):
                if num % x == 0 and num // x <= 10**7:
                    answer.append(num//x)
                    break
            # 소수가 아니거나, 나눈 몫이 10**7을 넘는다면 1로 업데이트한다.
            else:
                answer.append(1)
        
    return answer

