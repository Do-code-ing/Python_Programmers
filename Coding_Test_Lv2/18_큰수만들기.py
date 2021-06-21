# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    n = len(number)
    number = list(map(int, number))
    stack = [] # 정답 숫자 저장
    count = 0
    for i in range(n):
        # 정답칸이 비어있거나, 기존의 숫자보다 다음에 올 숫자가 작다면 저장
        if not stack or stack[-1] > number[i]:
            stack.append(number[i])
        # 아니라면
        else:
            # 작은 숫자 제거하고 카운트하기
            while stack and stack[-1] < number[i] and count < k:
                stack.pop()
                count += 1
            # 남아있는 숫자 다 저장
            stack.append(number[i])
    
    # 만약 k번 만큼 제거하지 않았을 경우, 앞에서부터 제일 작은 값 제거
    for i in range(k-count):
        stack.remove(min(stack))

    return "".join(map(str, stack))