from collections import deque

def solution(food_times, k):
    n = len(food_times)
    if k < n:
        return k + 1

    times = deque(sorted([[idx, value] for idx, value in enumerate(food_times)], key=lambda x:(x[1], x[0])))
    count = n
    minus = 0
    print(times)
    while True:
        if not count:
            return -1
        
        cur_idx, cur_value = times.popleft()
        if cur_value <= minus:
            food_times[cur_idx] = 0
            continue

        value = (cur_value - minus) * count
        if value > k:
            idx = 0
            print(food_times)
            while not food_times[idx]:
                idx = (idx + 1) % n
            return idx + 1
        
        for i in range(count-1):
            times[i][1] -= cur_value - minus

        k -= value
        minus = cur_value
        food_times[cur_idx] = 0
        count -= 1
        print(k, times)


# food_times, k = [1, 1, 1, 1], 1
# print(solution(food_times, k))
print(solution([3,1,1,1,2,4,3],12))