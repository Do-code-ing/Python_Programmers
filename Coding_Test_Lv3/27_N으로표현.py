# https://programmers.co.kr/learn/courses/30/lessons/42895?language=python3

def solution(N, number):
    dp = []
    for i in range(1, 9):
        set_N = {int(str(N)*i)}     # {N}, {NN}, ... , {NNNNNNNN}
        for j in range(i-1):        # 만약 N을 3개 사용한 결과를 모두 저장하려면,
            for x in dp[j]:         # N을 1개 사용한 집합과 N을 2개 사용한 집합에 대해 연산을 위해.
                for y in dp[-j-1]:  # 3 = 1+2, 3 = 2+1
                    for value in [x+y, x-y, x*y, x//y]:     # 모든 경우의 수 저장
                        if value != 0:
                            set_N.add(value)

        # 정답이 있다면 i 반환
        if number in set_N:
            return i

        # 다음 연산을 위해 저장
        dp.append(set_N)
        
    # N을 8번 사용해도 못 만들었으므로 -1 반환
    return -1