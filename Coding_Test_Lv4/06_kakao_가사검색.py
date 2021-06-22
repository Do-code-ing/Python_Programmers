# https://programmers.co.kr/learn/courses/30/lessons/60060?language=python3

# bisect를 이용한 풀이
from bisect import bisect_left, bisect_right
from collections import defaultdict

def cnt_range(array, l, r):
    left = bisect_left(array, l)
    right = bisect_right(array, r)
    return right - left

def solution(words, queries):
    answer = []

    db = defaultdict(list)
    db_reverse = defaultdict(list)
    
    for word in words:
        db[len(word)].append(word)
        db_reverse[len(word)].append(word[::-1])

    for i in db:
        db[i].sort()
        db_reverse[i].sort()

    for query in queries:
        if len(query) not in db:
            answer.append(0)
            continue

        if query[0] != "?":
            cnt = cnt_range(db[len(query)], query.replace("?","a"), query.replace("?","z"))
        else:
            query = query[::-1]
            cnt = cnt_range(db_reverse[len(query)], query.replace("?","a"), query.replace("?","z"))

        answer.append(cnt)
    
    return answer

# 효율성 테스트
# 테스트 1 〉	통과 (101.71ms, 24.2MB)
# 테스트 2 〉	통과 (132.63ms, 25.6MB)
# 테스트 3 〉	통과 (133.26ms, 28.1MB)
# 테스트 4 〉	통과 (2.93ms, 13.4MB)
# 테스트 5 〉	통과 (2.55ms, 13.8MB)


# Trie 자료 구조를 이용한 풀이
from collections import defaultdict

class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, string):
        cur_data = self.root
        while string:
            if string[0] not in cur_data:
                cur_data[string[0]] = [{}, 0]
            cur_data[string[0]][1] += 1
            cur_data = cur_data[string[0]][0]
            string = string[1:]
    
    def find(self, string):
        cur_data = self.root
        count = 0
        while string:
            if string[0] == "?":
                return count
            else:
                if string[0] not in cur_data:
                    return 0
                count = cur_data[string[0]][1]
                cur_data = cur_data[string[0]][0]
            string = string[1:]
        
        return count
    
def solution(words, queries):
    prefix_dict = defaultdict(Trie)
    suffix_dict = defaultdict(Trie)
    len_dict = defaultdict(int)
    answer = []

    for word in words:
        prefix_dict[len(word)].insert(word)
        suffix_dict[len(word)].insert(word[::-1])
        len_dict[len(word)] += 1

    for query in queries:
        if query[0] == "?" and query[-1] == "?":
            answer.append(len_dict[len(query)])
        elif query[-1] == "?":
            answer.append(prefix_dict[len(query)].find(query))
        elif query[0] == "?":
            answer.append(suffix_dict[len(query)].find(query[::-1]))
        else:
            answer.append(0)
        
    return answer

# 효율성 테스트
# 테스트 1 〉	통과 (998.27ms, 151MB)
# 테스트 2 〉	통과 (2161.42ms, 285MB)
# 테스트 3 〉	통과 (1981.84ms, 264MB)
# 테스트 4 〉	통과 (1745.85ms, 336MB)
# 테스트 5 〉	통과 (2876.93ms, 631MB)