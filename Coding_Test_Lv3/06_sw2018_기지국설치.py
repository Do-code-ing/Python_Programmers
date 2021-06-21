# https://programmers.co.kr/learn/courses/30/lessons/12979?language=python3

from math import ceil

def solution(n, stations, w):
    answer = 0
    dp = []
    # 1부터 첫 안테나 사이에 전파가 안통하는 구간
    if stations[0] - w - 1 >= 1:
        dp.append([1, stations[0] - w - 1])
    # 첫 안테나부터 마지막 안테나 사이에 전파가 안통하는 구간
    for i in range(len(stations)-1):
        start = stations[i] + w + 1
        end = stations[i+1] - w - 1
        if start <= end:
            dp.append([start, end])
    # 마지막 안테나부터 n 사이에 전파가 안통하는 구간
    if stations[-1] + w + 1 <= n:
        dp.append([stations[-1] + w + 1, n])
    # 구간별로 설치
    for start, end in dp:
        length = end - start + 1
        answer += ceil(length / (w*2+1))

    return answer