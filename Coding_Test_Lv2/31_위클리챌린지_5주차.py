# https://programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    db = {
        4: {"A": 1, "E": 2, "I": 3, "O": 4, "U": 5},
        3: {"A": 1, "E": 7, "I": 13, "O": 19, "U": 25},
        2: {"A": 1, "E": 32, "I": 63, "O": 94, "U": 125},
        1: {"A": 1, "E": 157, "I": 313, "O": 469, "U": 625},
        0: {"A": 1, "E": 782, "I": 1563, "O": 2344, "U": 3125}
    }

    answer = 0
    for key, value in enumerate(word):
        answer += db[key][value]

    return answer

# [규칙 찾기]
# AXXXX 10000 1
# AAXXX 11000 2
# AAAXX 11100 3

# AAAAX 11110 4
# AAAAA 11111 5
# AAAAE 11112 6
# AAAAI  11113 7
# AAAAO 11114 8
# AAAAU 11115 9

# AAAEX 11170 10
# AAAEA 11171 11
# AAAEE 11172 12
# AAAEI 11173 13
# AAAEO 11174 14
# AAAEU 11175 15

# AAAIX 111(13)0 16

# break point

# AAAUU 111(25)5 33
# AAEXX 11(32)00 34

# AAEUU 11(32)(25)5 64
# AAIXX 11(63)00 65

# AAUUU 11(125)(25)5 157
# AEXXX 1(157)000 158

# AEUUU 1(157)(125)(25)5 313
# AIXXX 1(313)000 314

# AUUUU 1(625)(125)(25)5 781
# EXXXX (782)0000 782

# index 4 gap 1
# A: 1
# E: 2
# I: 3
# O: 4
# U: 5

# index 3 gap 6
# A: 1
# E: 7
# I: 13
# O: 19
# U: 25

# index 2 gap 31
# A: 1
# E: 32
# I: 63
# O: 94
# U: 125

# index 1 gap 156
# A: 1
# E: 157
# I: 313
# O: 469
# U: 625

# index 0 gap 781
# A: 1
# E: 782
# I: 1563
# O: 2344
# U: 3125
