# https://programmers.co.kr/learn/courses/30/lessons/77884?language=python3

def solution(left, right):
    mineral_water = []
    for num in range(left, right+1):
        result = set()
        for water in range(1, int(num**0.5)+1):
            if num % water == 0:
                result.add(water)
                result.add(num//water)
        
        mineral_water.append((num, len(result)))

    answer = 0
    for num, water in mineral_water:
        if water % 2 == 0:
            answer += num
        else:
            answer -= num
    
    return answer

# 자연수 x의 제곱근이 자연수라면,
# 자연수 x의 약수는 홀수개다.

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if int(num**0.5) != num**0.5:
            answer += num
        else:
            answer -= num

    return answer