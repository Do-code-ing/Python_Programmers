# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3

from collections import deque

def solution(food_times, k):
    # 정전 시각전에 모든 음식을 섭취했다면
    if k >= sum(food_times):
        return -1
    
    # 정전 시각보다 먹을 음식의 개수가 많다면
    n = len(food_times)
    if k < n:
        return k + 1

     # (food index, food value) 형식으로 저장하면서 value 순으로 오름차순 정렬
    foods = deque(sorted(enumerate(food_times), key=lambda x:x[1]))
    total_eaten = 0 # 현재까지 먹은 양
    last_eaten = 0  # 마지막으로 한 음식당 먹은 음식 양
    while True:
        to_eat = (foods[0][1] - last_eaten) * len(foods)    # 뭉텅이로 제거
        if total_eaten + to_eat > k:
            foods = sorted(foods, key=lambda x:x[0])
            break

        total_eaten += to_eat
        last_eaten = foods.popleft()[1]

    return foods[(k - total_eaten) % len(foods)][0] + 1