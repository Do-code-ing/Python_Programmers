n = 5
arr1 = [0, 0, 0, 0, 0]
arr2 = [30, 1, 21, 17, 28]

import re

def solution(n, arr1, arr2):
    answer = [] # 합쳐진 지도
    answer2 = [] # 해독 과정
    answer3 = [] # 해독 내용
    answer4 = [] # 해독 결과
    temp1 = [] # 비밀지도 1 해독내용
    temp2 = [] # 비밀지도 2 해독내용
    temp3 = [] # 합친 지도 해독내용
    for i in arr1: # 비밀지도 1
        temp1.append(int(f"{i:b}"))
    for i in arr2:
        temp2.append(int(f"{i:b}"))
    answer = list(zip(temp1, temp2))
    for i in answer:
        answer2.append(int(sum(i)))
    for i in answer2:
        i = str(i)
        a = []
        if len(i) < n:
            a = list(reversed(i))
            for i in range(n-len(i)):
                a.append("0")
            b = "".join(list(reversed(a)))
            temp3.append(b)
        else:
            temp3.append(i)
    for i in temp3:
        answer3 = re.sub("[12]", "#", i)
        answer3 = re.sub("[0]", " ", answer3)
        answer4.append(answer3)
    return answer4

print(solution(n, arr1, arr2))

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

print(solution(n, arr1, arr2))

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.zfill(n)
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

print(solution(n, arr1, arr2))