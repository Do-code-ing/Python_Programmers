# https://programmers.co.kr/learn/courses/30/lessons/17685?language=python3

# 트라이 자료 구조를 이용한 풀이
class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, string):
        cur_data = self.root
        for char in string:
            if char not in cur_data:
                cur_data[char] = [{}, 0]
            cur_data[char][1] += 1
            cur_data = cur_data[char][0]
    
    def find(self, string):
        cur_data = self.root
        n = len(string)
        for i in range(n):
            if cur_data[string[i]][1] == 1:
                return i + 1
            
            cur_data = cur_data[string[i]][0]
        return n

def solution(words):
    answer = 0
    DB = Trie()
    for word in words:
        DB.insert(word)

    for word in words:
        answer += DB.find(word)

    return answer

# 정렬을 이용한 풀이
def compare(a, b):
    for idx, char in enumerate(a):
        if len(b) == idx or b[idx] != char:
            return idx + 1
    return len(a)

def solution(words):
    answer = 0
    words.sort()

    for idx, word in enumerate(words):
        result = 1
        if idx > 0:
            value = compare(word, words[idx-1])
            # print(word, words[idx-1], value)
            if result < value:
                result = value

        if idx + 1 < len(words):
            value = compare(word, words[idx+1])
            # print(word, words[idx+1], value)
            if result < value:
                result = value
        
        answer += result

    return answer