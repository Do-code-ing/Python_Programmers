# https://programmers.co.kr/learn/courses/30/lessons/92335

def n_to_k_notation(n, k):
    if n >= k:
        result = ""
        while n >= k:
            n, x = n // k, n % k
            result += str(x)
            if n < k:
                result += str(n)
                break
        
        return result[::-1]
    return str(n)


def is_sosu(x):
    if x <= 1:
        return False
    
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    
    return True
    

def solution(n, k):
    result = n_to_k_notation(n, k)
    answer = 0
    
    result = result.split("0")
    for num in result:
        if num and is_sosu(int(num)):
            answer += 1
        
    return answer
