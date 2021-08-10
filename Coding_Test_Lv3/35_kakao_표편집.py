# https://programmers.co.kr/learn/courses/30/lessons/81303

class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
        self.prev = None

    # def __repr__(self):
    #     return str(self.key)

class DLL:
    def __init__(self):
        self.head = Node()
    
    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next
        
    # def __str__(self):
    #     return " -> ".join(str(v.key) for v in self)

    def insert(self, key):
        new_node = Node(key)
        if self.head.next == None:
            self.head.next = new_node
            new_node.prev = self.head
            self.head.prev = new_node
            new_node.next = self.head
        else:
            pre = self.head.prev
            pre.next = new_node
            new_node.prev = pre
            self.head.prev = new_node
            new_node.next = self.head
    
    def erase(self, node): # 행 감추기 "C"
        node.prev.next = node.next
        node.next.prev = node.prev
        return node
    
    def restore(self, node): # 행 복구 "Z"
        node.prev.next = node
        node.next.prev = node

def solution(n, k, cmd):
    arr = DLL()
    for i in range(n):
        arr.insert(i)
    
    row = arr.head.next
    for i in range(k):
        row = row.next
    
    stack = []
    for char in cmd:
        char = char.split()
        if char[0] == "U":
            x = int(char[1])
            for _ in range(x):
                row = row.prev
        
        elif char[0] == "D":
            x = int(char[1])
            for _ in range(x):
                row = row.next
    
        elif char[0] == "C":
            x = arr.erase(row)
            stack.append(x)
            row = x.next
            if row == arr.head:
                row = arr.head.prev
        
        else:
            x = stack.pop()
            arr.restore(x)

    answer = ["X"] * n
    for x in arr:
        x = x.key
        answer[x] = "O"

    return "".join(answer)