def solution(numbers, hand):
    answer = ''
    # 공간 구현
    left_side = [1,4,7,-1] # -1 : *
    mid_side = [2,5,8,0]
    right_side =[3,6,9,-2] # -2 : #
    # 손가락의 위치
    left_loc = -1
    right_loc = -2
    for n in numbers:
        if n in left_side:
            answer += "L"
            left_loc = n
        elif n in right_side:
            answer += "R"
            right_loc = n
        else:
            # 먼저 숫자와 왼손, 오른손가락과의 거리 측정
            if left_loc in mid_side: # 왼손가락이 가운데 줄에 있다면
                left_dist = abs(mid_side.index(n) - mid_side.index(left_loc)) # 왼손가락과의 거리는

            if right_loc in mid_side: # 오른손가락이 가운데 줄에 있다면
                right_dist = abs(mid_side.index(n) - mid_side.index(right_loc)) # 오른손가락과의 거리는

            if left_loc in left_side: # 왼손가락이 왼쪽 줄에 있다면
                left_dist = abs(left_side.index(left_loc) - mid_side.index(n)) + 1
                # 왼손가락과의 거리는, 왼쪽 줄에서 왼손가락이 있던 위치에서 현재 번호의 위치를 빼고 + 1
                # + 1을 하는 이유,
                # 가운뎃 줄과 양 쪽의 줄간에 한 칸씩 거리가 있음을 표현

            if right_loc in right_side: # 오른손가락이 오른쪽 줄에 있다면 + 1
                right_dist = abs(right_side.index(right_loc) - mid_side.index(n)) + 1
            # 거리 비교 후, 처리
            if left_dist < right_dist:
                answer += "L"
                left_loc = n
            elif right_dist < left_dist:
                answer += "R"
                right_loc = n
            else:
                if hand == "left":
                    answer += "L"
                    left_loc = n
                else:
                    answer += "R"
                    right_loc = n
    return answer

# 4가지 방향으로만 이동 가능,
# 1, 4, 7 = L
# 3, 6, 9 = R
# 2, 5, 8, 0 = 더 가까운 손가락
# if 양쪽 손가락이 해당 숫자와 거리가 같을 경우, 어느손잡이인지로 결정



# 위치마다 행과 열을 만들어 그 차이로 거리 계산
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer