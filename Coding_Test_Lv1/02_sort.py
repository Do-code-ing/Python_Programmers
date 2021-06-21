array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]-1
        j = command[1]
        k = command[2]-1
        value = array
        value = value[i:j]
        answer.append(sorted(value)[k])
    return answer
print(solution(array, commands))

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))