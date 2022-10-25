# 이진 검색 트리
# 22.10.25
# https://www.acmicpc.net/problem/5639

# https://www.acmicpc.net/board/view/81443

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def binary_search(preorder):
    root = preorder[0]
    left, right = 1, len(preorder) - 1
    result = 1

    while left <= right:
        mid = (left + right) // 2

        if preorder[mid] < root:
            left = mid + 1
        else:
            result = mid
            right = mid - 1

    return result


def postorder(preorder):
    if not preorder:
        return
    i = binary_search(preorder)
    postorder(preorder[1:i])
    postorder(preorder[i:])
    print(preorder[0])


preorder = []

try:
    while True:
        key = int(input())
        preorder.append(key)
except:
    pass

postorder(preorder)


# 시간초과 코드

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(100000)

# def postorder(preorder):
#     if not preorder:
#         return
#     root = preorder[0]
#     i = 1
#     while i < len(preorder) and preorder[i] < root:
#         i += 1
#     postorder(preorder[1:i])
#     postorder(preorder[i:])
#     print(root)


# preorder = []

# try:
#     while True:
#         key = int(input())
#         preorder.append(key)
# except:
#     pass

# postorder(preorder)
