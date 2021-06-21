# https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3

# numpy를 이용한 풀이
from numpy import pad, rot90

def solution(key, lock):
    n = len(lock)
    m = len(key)
    start = n-m+1 # 첫 인덱스
    end = 2*n # 마지막 인덱스
    for _ in range(4): # 0도, 90도, 180도, 270도로 열쇠를 회전해보면서
        for i in range(start, end): # 열쇠가 들어갈 x좌표
            for j in range(start, end): # 열쇠가 들어갈 y좌표
                lock_pad = pad(lock, n) # 패드로 만들어주고
                for a in range(i, i+m): # 위치에 따른 열쇠 홈에 맞춰서 업데이트
                    for b in range(j, j+m):
                        lock_pad[a][b] += key[a-i][b-j]

                # 열쇠와 자물쇠가 잘 맞물렸는지 확인
                flag = True
                for x in range(n, 2*n):
                    if flag:
                        for y in range(n, 2*n):
                            if lock_pad[x][y] == 0 or lock_pad[x][y] == 2:
                                flag = False
                                break
                
                if flag:
                    return True
                    
        # 열쇠 회전
        key = rot90(key)
    
    return False

# numpy 모듈을 불러오지 않고 함수로 구현하여 사용한 풀이
def rot90_(key, m):
    new_key = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            new_key[i][j] = key[-j-1][i]
    return new_key

def pad_(lock, n):
    lock_pad = [[0] * (3*n) for _ in range(3*n)]
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            lock_pad[i][j] = lock[i-n][j-n]
    return lock_pad

def solution(key, lock):
    n = len(lock)
    m = len(key)
    start = n-m+1
    end = 2*n
    for _ in range(4):
        for i in range(start, end):
            for j in range(start, end):
                lock_pad = pad_(lock, n)
                for a in range(i, i+m):
                    for b in range(j, j+m):
                        lock_pad[a][b] += key[a-i][b-j]

                flag = True
                for x in range(n, 2*n):
                    if flag:
                        for y in range(n, 2*n):
                            if lock_pad[x][y] == 0 or lock_pad[x][y] == 2:
                                flag = False
                                break
                
                if flag:
                    return True

        key = rot90_(key)
    
    return False