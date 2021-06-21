# https://programmers.co.kr/learn/courses/30/lessons/77886?language=python3

from collections import deque

def solution(s):
    answer = []
    for string in s:
        stack = []
        count = 0
        # 스택에 넣어보며 '110' 찾기
        for char in string:
            if char == "0":
                # '110' 이라면 카운트
                if stack[-2:] == ["1", "1"]:
                    count += 1
                    stack.pop()
                    stack.pop()
                # 아니라면 그대로 추가
                else:
                    stack.append(char)
            else:
                stack.append(char)
        # '110'이 없다면 문자열 그대로 반환
        if count == 0:
            answer.append(string)
        else:
            q = deque()
            # 스택에서 제일 마지막에 위치한 '0' 찾기
            while stack:
                # '1'이라면 큐에 순서대로 삽입
                if stack[-1] == "1":
                    q.append(stack.pop())
                elif stack[-1] == "0":
                    break
            # 카운트만큼 '110' 삽입
            while count > 0:
                q.appendleft("0")
                q.appendleft("1")
                q.appendleft("1")
                count -= 1
            # 마지막으로 스택에 남아있는 숫자들 삽입
            while stack:
                q.appendleft(stack.pop())
            # 정답 입력
            answer.append("".join(map(str, q)))
    
    return answer