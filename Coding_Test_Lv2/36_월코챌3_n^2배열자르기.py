# https://programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = []

    for i in range(left, right+1):
        answer.append(max(divmod(i, n)) + 1)

    return answer

# left ~ right 까지의 숫자들을 n 으로 나눈 몫과 나머지 중 큰 값에 1을 더해주면,
# 해당 index 의 숫자를 알 수 있다.
