# https://programmers.co.kr/learn/courses/30/lessons/42894

# 숫자 블록 제거
def remove(board, x, y, n):
    if x+1 < n:
        # 1 (옆으로 긴 니은)
        if y+2 < n:
            if board[x][y+1] == board[x][y+2] == -1:
                if board[x][y] == board[x+1][y] == board[x+1][y+1] == board[x+1][y+2]:
                    board[x][y] = board[x+1][y] = board[x+1][y+1] = board[x+1][y+2] = 0
                    return True
    
        # 2 (옆으로 긴 역 니은)
        if 0 <= y-2:
            if board[x][y-1] == board[x][y-2] == -1:
                if board[x][y] == board[x+1][y] == board[x+1][y-1] == board[x+1][y-2]:
                    board[x][y] = board[x+1][y] = board[x+1][y-1] = board[x+1][y-2] = 0
                    return True

        # 3 (빠큐 모양)
        if 0 <= y-1 and y+1 < n:
            if board[x][y-1] == board[x][y+1] == -1:
                if board[x][y] == board[x+1][y] == board[x+1][y-1] == board[x+1][y+1]:
                    board[x][y] = board[x+1][y] = board[x+1][y-1] = board[x+1][y+1] = 0
                    return True
        
    if x+2 < n:
        # 4 (위로 긴 역 니은)
        if 0 <= y-1:
            if board[x][y-1] == board[x+1][y-1] == -1:
                if board[x][y] == board[x+1][y] == board[x+2][y] == board[x+2][y-1]:
                    board[x][y] = board[x+1][y] = board[x+2][y] = board[x+2][y-1] = 0
                    return True

        # 5 (위로 긴 니은)
        if y+1 < n:
            if board[x][y+1] == board[x+1][y+1] == -1:
                if board[x][y] == board[x+1][y] == board[x+2][y] == board[x+2][y+1]:
                    board[x][y] = board[x+1][y] = board[x+2][y] = board[x+2][y+1] = 0
                    return True
    
    return False

# 빈 칸에 검은 블록 채우기
def fill(board, n):
    dp = [True] * n
    for i in range(n):
        for j in range(n):
            if not dp[j] or board[i][j] == -1:
                continue
            
            if board[i][j] != 0:
                dp[j] = False
            else:
                board[i][j] = -1

def solution(board):
    answer = 0
    n = len(board)
    
    # 숫자 블록을 못 없앨 때까지 반복
    def drop():
        nonlocal answer
        fill(board, n)
        for i in range(n):
            for j in range(n):
                if board[i][j] > 0:
                    if remove(board, i, j, n):
                        answer += 1
                        drop()
                        return
    
    drop()

    return answer