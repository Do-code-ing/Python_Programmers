def solution(board, moves):
    answer = 0
    basket = []
    for m in moves: # 작동 시작
        for i in range(len(board)): # 보드 길이 index
            if board[i][m-1] != 0:
                basket.append(board[i][m-1])
                board[i][m-1] = 0
                if len(basket) > 1: # 통 안에 2개 이상 인형이 있다면
                    if basket[-1] == basket[-2]: # 2개의 인형이 같다면 2점 추가
                        basket.pop(-1)
                        basket.pop(-1)
                        answer += 2
                break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
# [1,5,3,5,1,2,1,4]

# [0,0,0,0,0]
# [0,0,1,0,3]
# [0,2,5,0,1]
# [4,2,4,4,2]
# [3,5,1,3,1]

# 위 코드와 아래 코드의 결과 차이를 모르겠음
# 과정은 분명 데이터를 직접 반복하여 값을 찾느냐
# 데이터는 냅둔채 값을 찾아서 하느냐 차이인거 같은데

# [4,3,1,1,3,2,0,4]

def solution(board, moves):
    answer = 0
    basket = []
    for m in moves: # 작동 시작
        temp = 0 # 작동여부
        for b in board: # 보드의 각 행 순회
            for bi, doll in enumerate(b): # 행안의 칸과 인형 순회
                if temp == 0: # 작동했나요
                    if doll > 0 and m == bi+1:
                        basket.append(doll)
                        b[bi] = 0
                        temp = 1 # 네 작동했어요 > 다음 m으로
                    else:
                        temp = 0 # 아뇨 아직 안했어요
        if len(basket) > 1:
            if basket[-1] == basket[-2]:
                basket.remove(basket[-2])
                basket.remove(basket[-1])
                answer += 2
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
# [1,5,3,5,1,2,1,4]

# [0,0,0,0,0]
# [0,0,1,0,3]
# [0,2,5,0,1]
# [4,2,4,4,2]
# [3,5,1,3,1]

# [4,3,1,1,3,2,0,4]