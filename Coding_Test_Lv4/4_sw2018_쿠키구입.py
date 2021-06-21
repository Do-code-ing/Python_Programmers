# https://programmers.co.kr/learn/courses/30/lessons/49995?language=python3

def solution(cookie):
    # prefix sum 저장
    dp = [0]
    for x in cookie:
        dp.append(dp[-1] + x)

    n = len(cookie)
    answer = 0
    for i in range(1, n+1):
        l = i-1
        m = i
        r = i+1
        while 0 <= l and r <= n:
            first = dp[m] - dp[l]   # 첫 째 아들 과자
            second = dp[r] - dp[m]  # 둘 째 아들 과자
            if first == second:     # 둘이 가진 양이 같다면
                if answer < first:
                    answer = first
                l -= 1              # 더 많이 살 수 있나 한 바구니씩 더 줘보기
                r += 1
            elif first < second:    # 첫 째가 조금 가졌다면 첫 째에게 한 바구니 더
                l -= 1
            else:                   # 둘 째가 조금 가졌다면 둘 째에게 한 바구니 더
                r += 1
    
    return answer