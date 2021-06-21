# https://programmers.co.kr/learn/courses/30/lessons/70130?language=python3

from collections import Counter

def solution(a):
    n = len(a)
    answer = 0
    # 어떤 숫자를 기준으로 스타수열을 만들 것인가
    values = Counter(a)
    for value in values:
        # 만약 그 숫자의 개수가 여태까지 나온 정답보다 작거나 같으면
        # 어차피 정답과 작거나 같을 것이므로 continue
        if values[value] <= answer:
            continue
        
        count = 0
        idx = 0
        while idx < n-1:
            # 스타 수열 규칙에 맞다면 2칸 index 이동
            if a[idx] == value or a[idx+1] == value:
                if a[idx] != a[idx+1]:
                    count += 1
                    idx += 2
                    continue
            # 아니라면 1칸 index 이동
            idx += 1

        if answer < count:
            answer = count
    
    return answer * 2