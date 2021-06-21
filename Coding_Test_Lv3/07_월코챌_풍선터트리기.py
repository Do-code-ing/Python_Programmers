# https://programmers.co.kr/learn/courses/30/lessons/68646?language=python3

def solution(a):
    answer = len(a)
    i = 0 # 왼쪽 시작 인덱스
    j = len(a)-1 # 오른쪽 시작 인덱스
    left_min = a[0] # 왼쪽 최소값
    right_min = a[-1] # 오른쪽 최소값
    while i < j:
        # 왼쪽 값이 더 크다면
        if a[i] > a[j]:
            # 다음 인덱스로 이동
            i += 1
            # 왼쪽 최소값보다 다음 인덱스 값이 더 작다면 업데이트
            if left_min > a[i]:
                left_min = a[i]
            # 아니라면 후보 제외
            else:
                answer -= 1
        # 오른쪽 값이 더 크다면
        else:
            # 다음 인덱스로 이동
            j -= 1
            # 오른쪽 최소값보다 다음 인덱스 값이 더 작다면 업데이트
            if right_min > a[j]:
                right_min = a[j]
            # 아니라면 후보 제외
            else:
                answer -= 1

    return answer