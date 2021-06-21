# https://programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    answer = '0'
    for i in range(1, t*m):
        temp = "" # 진수 넣어둘 곳
        while i>0:
            a, b = divmod(i, n)
            if b < 10:
                temp += str(b)
            elif b >= 10:
                if b == 10:
                    temp += "A"
                if b == 11:
                    temp += "B"
                if b == 12:
                    temp += "C"
                if b == 13:
                    temp += "D"
                if b == 14:
                    temp += "E"
                if b == 15:
                    temp += "F"
            i = a
        answer += temp[::-1]
    answer = answer[p-1:t*m:m]
    return answer

# n : 진법
# t : 말해야하는 갯수
# m : 인원
# p : 순서

# i : 범위 >= 말해야하는 갯수 * 인원