# https://programmers.co.kr/learn/courses/30/lessons/42893?language=python3

import re

def solution(word, pages):
    n = len(pages)
    word = word.lower()
    my_link = {}            # {my_url:index} 식으로 저장
    out_link = [0] * n      # 외부 링크 저장 
    basic_point = [0] * n   # 기본 점수 저장

    # 찾기
    for idx, page in enumerate(pages):
        page = page.lower()
        my_link[re.search(r'<meta property=\"og:url\" content=\"https://([\S]*)\"/>', page).group(1)] = idx
        out_link[idx] = re.findall(r'<a href="https://([\S]*)">', page)
        basic_point[idx] = re.sub("[^a-z]+", ".", page).split(".").count(word)

    # 링크 점수 계산
    link_point = [0] * n
    for idx in range(n):
        links = out_link[idx]
        m = len(out_link[idx])
        for link in links:
            if link in my_link:
                jdx = my_link[link]
                link_point[jdx] += basic_point[idx] / m
    
    # 최종 점수 계산
    high_value = -1
    for i in range(n):
        value = basic_point[i] + link_point[i]
        if high_value < value:
            high_value = value
            answer = i

    return answer