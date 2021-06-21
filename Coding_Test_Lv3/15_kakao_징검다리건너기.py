# https://programmers.co.kr/learn/courses/30/lessons/64062?language=python3

def solution(stones, k):
    answer = 0
    start = 0
    end = max(stones)
    while start <= end:
        mid = (start+end) // 2
        seq_minus = 0    # 연속된 음수 개수
        max_minus = 0    # 여태까지 연속된 음수 개수의 최대 값
        for stone in stones:
            if stone - mid < 0:     # 음수라면, 즉 아예 건널 수 없음
                seq_minus += 1      # (x <= 0이 아닌 이유는, 딱 0이 되었으면 그 사람까지는 건넌 것이므로)
                if max_minus < seq_minus:
                    max_minus = seq_minus
            else:
                seq_minus = 0       # 아니라면 초기화
                
        if max_minus < seq_minus:
            max_minus = seq_minus
        
        if max_minus < k:   # k보다 작아야 건널 수 있기 때문에 x < k
            if answer < mid:
                answer = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return answer

stones, k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1],	3
print(solution(stones, k))