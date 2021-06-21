# https://programmers.co.kr/learn/courses/30/lessons/12927?language=python3

def solution(n, works):
    if n >= sum(works):
        return 0
    
    works.append(0) # 최소값을 위해 0 추가
    works.sort()
    # 뒷 번호부터 탐색
    for i in range(1, len(works)):
        minus = works[-i] - works[-(i+1)]
        # 앞의 숫자와의 차이 * 빼야될 것들의 개수가 n 보다 작다면
        if n > minus * i:
            n -= minus * i
            # 모두 수행
            for j in range(1, i+1):
                works[-j] -= minus
        # 아니라면
        else:
            minus = n // i
            n %= i
            # 아니라면 뺄 수 있는 애들만 빼주기
            for j in range(1, i+1):
                works[-j] -= minus
            # 남은 n개에 대해 일괄적으로 1씩 빼주기
            for j in range(1, n+1):
                works[-j] -= 1
            break
    
    answer = 0
    for work in works:
        answer += work**2

    return answer