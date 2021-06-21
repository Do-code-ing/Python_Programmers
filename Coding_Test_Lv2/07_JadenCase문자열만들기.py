# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    ans = []
    for c in s.split(" "):
        ans.append(c.capitalize())
    return " ".join(ans)