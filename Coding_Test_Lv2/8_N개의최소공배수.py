# https://programmers.co.kr/learn/courses/30/lessons/12953

from math import *

def solution(arr):
    x = int(arr[0] * arr[1] / gcd(arr[0], arr[1]))
    idx = 2
    while idx < len(arr):
        x = int(x * arr[idx] / gcd(x, arr[idx]))
        idx += 1
    return x

from math import *

def solution(arr):
    answer = arr[0]
    for n in arr:
        answer = int(n * answer / gcd(n, answer))
    return answer