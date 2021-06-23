# https://programmers.co.kr/learn/courses/30/lessons/64063?language=python3

# 재귀 함수를 이용한 풀이
import sys
sys.setrecursionlimit(10**6)

def find_room(room, num):
    if num not in room:
        room[num] = num + 1
        return num
    
    new_num = find_room(room, room[num])
    room[num] = new_num + 1
    return new_num

def solution(k, room_number):
    answer = []
    room = {}
    for num in room_number:
        answer.append(find_room(room, num))

    return answer

# while문 풀이
def solution(k, room_number):
    answer = []
    room = {}
    for num in room_number:
        used_space = [num]
        while num in room:
            num = room[num]
            used_space.append(num)
        answer.append(num)
        for used in used_space:
            room[used] = num + 1
    
    return answer