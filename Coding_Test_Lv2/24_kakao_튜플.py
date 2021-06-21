# https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3

def solution(s):
    # 문자열 슬라이싱
    answer = []
    arrs = s.split("},{")
    arrs[0] = arrs[0][2:]
    arrs[-1] = arrs[-1][:-2]
    # 문자열 슬라이싱 + 숫자로 저장
    arr2 = []
    for arr in arrs:
        arr = arr.split(",")
        arr = list(map(int, arr))
        arr2.append(arr)
    # 정답 도출
    arr2.sort(key=lambda x:len(x))
    for arr in arr2:
        for num in arr:
            if num not in answer:
                answer.append(num)
                
    return answer