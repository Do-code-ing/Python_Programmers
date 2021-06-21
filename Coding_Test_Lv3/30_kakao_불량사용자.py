# https://programmers.co.kr/learn/courses/30/lessons/64064?language=python3

def solution(user_id, banned_id):
    # 각 banned_id마다 user_id를 비교하며, 해당 banned_id가 될 수 있다면 case에 저장
    n = len(banned_id)
    case = [[] for _ in range(n)]
    for i in range(len(banned_id)):
        bid = banned_id[i]
        m = len(bid)
        count = bid.count("*")
        for uid in user_id:
            if len(uid) != m:
                continue

            if sum((x!=y for x, y in zip(bid, uid))) == count:
                case[i].append(uid)
    
    # case에 저장된 user_id별로 완전탐색후 경우의 수 찾기
    result = set()
    def brute(idx, arr):
        if idx == n:
            result.add(tuple(sorted(arr)))
            return
        
        for name in case[idx]:
            if name in arr:
                continue

            arr.add(name)
            brute(idx+1, arr)
            arr.remove(name)

    brute(0, set())
    return len(result)