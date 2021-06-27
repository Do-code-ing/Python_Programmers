def solution(n, cores):
    # 총 작업량이 코어의 개수보다 적다면 n번째 코어 리턴
    if n < len(cores):
        return n
    
    rest = n - len(cores)   # 나머지 작업량(0시간에는 모두들 작업하므로 그 만큼 작업시간에서 빼주기)
    left = 1
    right = max(cores) * n  # 제일 오래걸리는 시간은 처리시간이 제일 긴 코어가 모두 작업할 때이다.
    while left < right:
        mid = (left+right) // 2 # mid: 각 시간별로 처리되는 작업량
        count = 0               # mid시간까지 처리된 작업량 저장
        for core in cores:
            count += mid // core
        
        if count < rest:    # 작업이 끝나지 않았다면 left 조정
            left = mid + 1
        else:               # 작업이 끝나거나 그 시간이 넘어갔다면 right 조정
            right = mid
    
    # 작업이 끝나거나 넘어간 시각 right에서 한 시간전으로 되돌아가서 
    # 작업량이 n개 이하로 남을 수 있게 처리
    for core in cores:
        rest -= (right-1) // core

    # n개 이하의 작업량에서
    # 만약 right 시간에 작업을 처리할 수 있는 코어라면
    # 작업한 처리 rest -= 1해주고
    # rest가 0이 되면 index + 1로 리턴
    for i in range(len(cores)):
        if right % cores[i] == 0:
            rest -= 1
            if rest == 0:
                return i + 1