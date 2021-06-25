# https://programmers.co.kr/learn/courses/30/lessons/1843?language=python3

def solution(arr):
    answer = float('-inf')
    
    def btk(brr):
        nonlocal answer
        if len(brr) == 1:
            result = int(brr[0])
            if answer < result:
                answer = result
            return

        for i in range(0, len(brr)-1, 2):
            value = str(eval(brr[i] + brr[i+1] + brr[i+2]))
            btk(brr[:i] + [value] + brr[i+3:])
    
    btk(arr)
    
    return answer