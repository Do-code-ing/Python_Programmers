# https://programmers.co.kr/learn/courses/30/lessons/42892?language=python3

import sys
sys.setrecursionlimit(1000000)

def solution(nodeinfo):
    class Node():
        def __init__(self):
            self.index = None   # 노드 번호
            self.data = None    # 노드 좌표
            self.left = None    # 왼쪽 자식
            self.right = None   # 오른쪽 자식

    def pre_order(node):
        nonlocal pre
        if node == None:
            return
        
        pre.append(node.index)
        pre_order(node.left)
        pre_order(node.right)


    def post_order(node):
        nonlocal post
        if node == None:
            return
        
        post_order(node.left)
        post_order(node.right)
        post.append(node.index)

    # 노드마다 번호 추가하고 Y좌표 기준으로 역 정렬 -> 맨 처음 노드가 루트가 됨
    for i in range(len(nodeinfo)):
        nodeinfo[i].append((i+1))
    nodeinfo.sort(key=lambda x:x[1], reverse=True)

    root = None
    for node in nodeinfo:
        new_tree = Node()
        new_tree.index = node[2]
        new_tree.data = node
        if root == None:
            root = new_tree
        else:
            cur_tree = root
            while True:
                # 오른쪽 자식인 경우
                if cur_tree.data[0] < new_tree.data[0]:
                    # 현재 노드의 오른쪽 자식 자리가 비었다면 업데이트하고 break
                    if cur_tree.right == None:
                        cur_tree.right = new_tree
                        break
                    # 아니라면 현재 노드를 현재 노드의 오른쪽 자식으로 놓고 재탐색
                    else:
                        cur_tree = cur_tree.right
                # 왼쪽 자식인 경우
                else:
                    # 현재 노드의 왼쪽 자식 자리가 비었다면 업데이트하고 break
                    if cur_tree.left == None:
                        cur_tree.left = new_tree
                        break
                    # 아니라면 현재 노드를 현재 노드의 왼쪽 자식으로 놓고 재탐색
                    else:
                        cur_tree = cur_tree.left

    pre = []
    post = []
    pre_order(root)
    post_order(root)
    return [pre, post]