# https://programmers.co.kr/learn/courses/30/lessons/42894

def check(board, n, x, y):
    # 1
    if x+1 < n and y+2 < n:
        flag = True
        for i in range(x):
            if not flag:
                break
                
            for j in range(y+1, y+3):
                if board[i][j] != 0:
                    flag = False
                    break

        if flag:
            if board[x][y+1] == board[x][y+1] == 0:
                if board[x][y] == board[x+1][y] == board[x+1][y+1] == board[x+1][y+2]:
                    board[x][y] = board[x+1][y] = board[x+1][y+1] = board[x+1][y+2] = 0
                    return True
    
    # 2
    if x+1 < n and 0 <= y-2:
        flag = True
        for i in range(x):
            if not flag:
                break
            
            for j in range(y-2, y):
                if board[i][j] != 0:
                    flag = False
                    break
        if flag:
            if board[x][y-1] == board[x][y-2] == 0:
                if board[x][y] == board[x+1][y] == board[x+1][y-1] == board[x+1][y-2]:
                    board[x][y] = board[x+1][y] = board[x+1][y-1] = board[x+1][y-2] = 0
                    return True

    # 3
    if x+1 < n and 0 <= y-1 and y+1 < n:
        flag = True
        for i in range(x):
            if not flag:
                break

            for j in [y-1, y+1]:
                if board[i][j] != 0:
                    flag = False
                    break

        if flag:
            if board[x][y-1] == board[x][y+1] == 0:
                if board[x][y] == board[x+1][y] == board[x+1][y-1] == board[x+1][y+1]:
                    board[x][y] = board[x+1][y] = board[x+1][y-1] = board[x+1][y+1] = 0
                    return True

    # 4
    if x+2 < n and 0 <= y-1:
        flag = True
        for i in range(x):
            if board[i][y-1] != 0:
                flag = False
                break
                
        if flag:
            if board[x][y-1] == board[x+1][y-1] == 0:
                if board[x][y] == board[x+1][y] == board[x+2][y] == board[x+2][y-1]:
                    board[x][y] = board[x+1][y] = board[x+2][y] = board[x+2][y-1] = 0
                    return True
    
    # 5
    if x+2 < n and y+1 < n:
        flag = True
        for i in range(x):
            if board[i][y+1] != 0:
                flag = False
                break
        
        if flag:
            if board[x][y+1] == board[x+1][y+1] == 0:
                if board[x][y] == board[x+1][y] == board[x+2][y] == board[x+2][y+1]:
                    board[x][y] = board[x+1][y] = board[x+2][y] = board[x+2][y+1] = 0
                    return True
    
    return False

def solution(board):
    answer = 0
    n = len(board)
    
    def drop():
        nonlocal answer
        for i in range(n):
            for j in range(n):
                if board[i][j] != 0:
                    if check(board, n, i, j):
                        answer += 1
                        drop()
    
    drop()
    
    return answer

print(solution([[0, 0, 0], [0, 0, 1], [1, 1, 1]]), 1)
print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]), 2)
print(solution([[0, 2, 0, 0], [1, 2, 0, 4], [1, 2, 2, 4], [1, 1, 4, 4]]), 3)
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 2, 0, 0, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), 1)
print(solution([[0, 0, 0, 0, 0], [1, 0, 0, 2, 0], [1, 2, 2, 2, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]), 2)
print(solution([[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,9,0,0,0,4,0,0,0,0],[0,7,9,0,0,0,4,0,0,0,0],[0,7,9,9,3,4,4,0,0,0,0],[7,7,0,2,3,0,0,0,5,5,0],[1,2,2,2,3,3,0,0,0,5,0],[1,1,1,6,0,0,0,0,0,5,0],[0,0,6,6,6,0,0,0,0,0,0]]), 7)
print(solution([[2, 2, 0, 0], [1, 2, 0, 4], [1, 2, 0, 4], [1, 1, 4, 4]]), 1)
print(solution([[0, 0, 1, 1, 1], [0, 0, 0, 1, 0], [3, 0, 0, 2, 0], [3, 2, 2, 2, 0], [3, 3, 0, 0, 0]]), 0)
print(solution([[0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 5], [0, 1, 1, 0, 0, 0, 5], [0, 1, 2, 3, 6, 5, 5], [2, 2, 2, 3, 6, 6, 6], [0, 0, 4, 3, 3, 0, 0], [0, 0, 4, 4, 4, 0, 0]]), 4)
print(solution([[0, 0, 0, 1, 0], [0, 0, 2, 1, 0], [0, 3, 2, 1, 1], [0, 3, 2, 2, 0], [0, 3, 3, 0, 0]]), 3)
print(solution([[4, 0, 0, 0, 0, 0], [4, 0, 3, 0, 0, 0], [4, 4, 3, 0, 0, 0], [0, 3, 3, 2, 0, 0], [0, 1, 2, 2, 2, 5], [1, 1, 1, 5, 5, 5]]), 5)