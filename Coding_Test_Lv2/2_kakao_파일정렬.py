# https://programmers.co.kr/learn/courses/30/lessons/17686

import re

def solution(files):
    dic = dict() # 기존 files와 정렬한 files의 key 매칭을 위해 저장할 임시 저장소
    p = re.compile("([a-zA-Z\" \".-]*)([0-9]+)")
    for i, file in enumerate(files): # file을 원하는 형태로 slice하고 
        file = p.match(file).groups()
        unzip = [] # file의 elements를 compile하여 저장할 공간
        unzip.append(file[0].lower()) # 문자들은 비교하기 위해 소문자로 만들고
        number = file[1][0:5] # 숫자들은 5개이하 까지만 슬라이싱
        unzip.append(number.zfill(5)) # 5개이하인 경우 앞에서부터 0을 채우기
        dic[i] = unzip # key 매칭해서 반환
    dic = sorted(dic.items(), key=lambda x:x[1]) # value로 정렬
    sorting = [] # 정렬한 files의 key 모음
    for d in dic:
        sorting.append(d[0])
    answer = []
    for x in sorting:
        answer.append(files[x])
    return answer
    
# HEAD기준으로 사전 순으로 정리
# 대소문자 구문 X
# 차이가 없다면 NUMBER의 숫자순으로 정리
# 9 < 10 < 0011 < 012 < 13 < 014
# TAIL을 제외한 모든 이름이 같다면 기존 순서를 유지

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
print(solution(files))

import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    print(a)
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b