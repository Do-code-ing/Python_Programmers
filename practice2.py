def solution(food_times, k):
    n = len(food_times)
    if k < n:
        return k + 1

    times = sorted(food_times)
    minus = 0
    for i in range(n):
        cur_value = times[i] - minus
        value = cur_value * (n-i)
        if value <= k:
            for j in range(n):
                if food_times[j] == 0:
                    continue

                food_times[j] -= cur_value
            k -= value
            minus = cur_value
        else:
            break
    
    print(food_times, k)
    idx = 0
    while k:
        if food_times[idx] != 0:
            food_times[idx] -= 1
            k -= 1
        idx += 1
        if idx == n:
            idx = 0
    
    return idx
            




print(solution([3,1,1,1,2,4,3],12), 6)
# print(solution([1, 1, 1], 4), -1)
# print(solution([4, 1, 1, 5], 4), 1)
# print(solution([4, 3, 5, 6, 2], 7), 3)
