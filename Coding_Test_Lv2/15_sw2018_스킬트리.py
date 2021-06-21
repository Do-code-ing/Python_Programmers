# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0
    temp = list(skill)
    for tree in skill_trees:
        stack = []
        for sk in tree:
            if sk in temp:
                stack.append(sk)
        if temp[:len(stack)] == stack:
            answer += 1
        
    return answer

skill, skill_trees = "CBD", ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))