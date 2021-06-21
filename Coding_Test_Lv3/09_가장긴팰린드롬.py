# https://programmers.co.kr/learn/courses/30/lessons/12904?language=python3

def solution(s):
    # 팰린드롬 문자열인지 확인
    def palindrome(start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    n = len(s)
    # 빈 문자열이라면 0 리턴
    if n == 0:
        return 0
    # 가장 긴 길이부터 확인
    for i in range(n-1, -1, -1):
        # 문자열 인덱스 조정
        # ex) s의 길이가 7인데 7인 경우에 없어서 길이가 6인 경우, 0~5, 1~6의 인덱스를 확인해야 함
        start = 0
        end = i
        while end < n:
            # 찾았다면 리턴
            if palindrome(start, end):
                return i+1
            start += 1
            end += 1