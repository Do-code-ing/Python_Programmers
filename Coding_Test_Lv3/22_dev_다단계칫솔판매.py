# https://programmers.co.kr/learn/courses/30/lessons/77486?language=python3

from math import ceil

def solution(enroll, referral, seller, amount):
    n = len(enroll)
    # 각 사람마다 번호 부여
    db = {"-":0}
    for i in range(n):
        x = enroll[i]
        db[x] = i+1

    # 각 사람마다 누구의 추천으로 들어왔는지 갱신
    parent = [i for i in range(n+1)]
    for i in range(n):
        x = referral[i]
        parent[i+1] = db[x]

    dp = [0] * (n+1) # 수익 저장 테이블
    m = len(seller)
    for i in range(m):
        x = db[seller[i]]
        money = amount[i] * 100
        
        while parent[x] != x:
            money_value = ceil(money * 0.9)
            dp[x] += money_value
            money -= money_value
            x = parent[x]
            if money == 0:
                break
        
        dp[x] += money

    return dp[1:]