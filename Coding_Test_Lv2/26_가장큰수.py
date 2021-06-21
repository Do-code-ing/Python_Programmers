# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3

def solution(numbers):
    answer = ''
    arr = [[] for _ in range(10)]
    db = {}
    # 각 숫자들을 4자리수가 될 수 있게 이어붙이고, db에 {num:이어붙인num} 형식으로 저장
    for num in numbers:
        arr[int(str(num)[0])].append(num)
        db[num] = int((str(num)*4)[:4])
    # db에 있는 값을 기준으로 정렬
    for ar in arr:
        ar.sort(key=lambda x:db[x], reverse=True)
    # 이어붙이기
    for i in range(9, -1, -1):
        answer += "".join(map(str, arr[i]))
    # 0으로 시작하면 0이라고 출력
    return answer if answer[0] != "0" else "0"