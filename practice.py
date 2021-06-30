from sys import stdin
input = stdin.readline

def solution():

    def ccw(x1, y1, x2, y2, x3, y3):
        a = x1 * y2 + x2 * y3 + x3 * y1
        b = y1 * x2 + y2 * x3 + y3 * x1
        if a == b:
            return 0
        elif a > b:
            return 1
        return -1
    
    def check(x1, y1, x2, y2, x3, y3):
        if x1 == x2:
            if y1 > y2:
                ay1, ay2 = y2, y1
            else:
                ay1, ay2 = y1, y2
            if ay1 <= y3 <= ay2:
                return True
        else:
            if x1 > x2:
                x1, x2 = x2, x1
            if x1 <= x3 <= x2:
                return True

        return False
    
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    
    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
    ccw4 = ccw(x3, y3, x4, y4, x2, y2)
    value1 = ccw1 * ccw2
    value2 = ccw3 * ccw4

    if value1 < 0 and value2 < 0:
        return 1
    
    if value1 == 0 and value2 != 0:
        if ccw1 == 0:
            if check(x1, y1, x2, y2, x3, y3):
                return 1
        if ccw2 == 0:
            if check(x1, y1, x2, y2, x4, y4):
                return 1
    
    if value1 != 0 and value2 == 0:
        if ccw3 == 0:
            if check(x3, y3, x4, y4, x1, y1):
                return 1
        if ccw4 == 0:
            if check(x3, y3, x4, y4, x2, y2):
                return 1
    
    if value1 == 0 and value2 == 0:
        if check(x1, y1, x2, y2, x3, y3) or check(x1, y1, x2, y2, x4, y4):
            return 1
        if check(x3, y3, x4, y4, x1, y1) or check(x3, y3, x4, y4, x2, y2):
            return 1

    return 0

print(solution())