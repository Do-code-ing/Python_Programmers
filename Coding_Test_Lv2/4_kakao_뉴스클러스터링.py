# https://programmers.co.kr/learn/courses/30/lessons/17677

import math
from collections import deque

str1 = "aaabbbb"
str2 = "aaaabbb"

def divide(string, n):
    arr = []
    for i in range(n):
        if i == n-1:
            continue
        if (string[i]+string[i+1]).isalpha():
            arr.append((string[i]+string[i+1]).lower())
    return arr

def multiset(arr1, arr2):
    q = deque(arr1)
    q2 = arr2
    low = 0
    high = []
    while q:
        v = q.popleft()
        if v in q2:
            low += 1
            high.append(v)
            q2.remove(v)
        else:
            high.append(v)
    high = len(high) + len(q2)
    if high == low:
        return 1, 1
    return low, high

def solution(str1, str2):
    arr1 = divide(str1, len(str1))
    arr2 = divide(str2, len(str2))
    low, high = multiset(arr1, arr2)
    answer = int(math.floor(low/high*65536))
    return answer

print(solution(str1, str2))

###

def solution(str1, str2):
    arr1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    arr2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    print(arr1)
    print(arr2)

    inter = set(arr1) & set(arr2)
    union = set(arr1) | set(arr2)
    print(inter)
    print(union)

    if len(union) == 0:
        return 65536

    low = sum([min(arr1.count(i), arr2.count(i)) for i in inter])
    high = sum([max(arr1.count(i), arr2.count(i)) for i in union])

    return int(low/high*65536)

str1 = "aa1+aa2"
str2 = "AAAA12"
print(solution(str1, str2))