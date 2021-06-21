nums = [1,2,7,6,4]

import itertools

def solution(nums):
    answer = 0
    com = itertools.combinations(nums, 3) # 3가지 갯수를 뽑아 조합한 경우의 수
    for i in com: # 각 경우의 수를
        num = sum(i) # 더하고 []
        for j in range(2, num): # 2 ~ 더한 값인 j
            if num % j == 0: # 만약 더한 값이 j로 나누어 떨어진다면,
                break
        else:
            answer +=1
    return answer

print(solution(nums))

# 1 2 4 6 7 	2부터 본인을 제외한 숫자로 나누었을 때 나누어 떨어지는가
# 124	    7	    x
# 126	    9	    o, 3
# 127	    10	    o, 3
# 146	    11	    x
# 147	    12	    o, 3
# 167	    14	    o, 2
# 246	    12	    o, 2
# 247	    13	    x
# 267	    15	    o, 3
# 467	    17	    x