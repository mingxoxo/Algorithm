# 트리의 순회
# 재귀, 분할정복
# 24.03.26
# https://www.acmicpc.net/problem/2263


import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def recursive(in_start, in_end, post_start, post_end):
    global inorder, postorder, index_dict

    if in_end < in_start or post_end < post_start:
        return
    
    root = postorder[post_end]
    print(root, end=' ')
    
    if in_start == in_end or post_start == post_end:
        return
    
    idx = index_dict[root] - in_start
    recursive(in_start, in_start + idx - 1, post_start, post_start + idx - 1)
    recursive(in_start + idx + 1, in_end, post_start + idx, post_end - 1)
    


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

index_dict = {inorder[i]: i for i in range(n)}

recursive(0, n-1, 0, n-1)
