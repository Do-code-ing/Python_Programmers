# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

from itertools import permutations


def solution(numbers):
    answer = 0
    # 에라토스테네스의 체 구현
    n = 10 ** (len(numbers))
    dp = [True] * (n+1)
    dp[0] = dp[1] = False
    for i in range(2, int(n**0.5)+1):
        if dp[i]:
            for j in range(i, n+1, i):
                dp[j] = False
            dp[i] = True
    # numbers안에 있는 문자로 가능한 모든 조합 만들기
    temp = list(numbers)
    arr = set()
    for i in range(1, len(numbers)+1):
        for num in permutations(temp, i):
            num = int("".join(num))
            arr.add(num)
    # 소수 판별
    for num in arr:
        if dp[num]:
            answer += 1

    return answer
