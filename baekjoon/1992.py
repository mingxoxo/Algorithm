# 쿼드 트리
# 23.06.14
# https://www.acmicpc.net/problem/1992

import sys
input = sys.stdin.readline

def is_compressible(sx, sy, N):
    global video

    point = video[sx][sy]
    for i in range(sx, sx + N):
        for j in range(sy, sy + N):
            if point != video[i][j]:
                return False
    return True


def quad_tree(sx, sy, N):
    if is_compressible(sx, sy, N):
        return video[sx][sy]

    N //= 2
    result = quad_tree(sx, sy, N)
    result += quad_tree(sx, sy + N, N)
    result += quad_tree(sx + N, sy, N)
    result += quad_tree(sx + N, sy + N, N)

    return "(" + result + ")"



N = int(input())
video = [input().rstrip() for _ in range(N)]
print(quad_tree(0, 0, N))

# # 다른 풀이

# import sys
# input = sys.stdin.readline


# def quad_tree(sx, sy, N):
#     if N == 1:
#         return video[sx][sy]

#     N //= 2

#     t1 = quad_tree(sx, sy, N)
#     t2 = quad_tree(sx, sy + N, N)
#     t3 = quad_tree(sx + N, sy, N)
#     t4 = quad_tree(sx + N, sy + N, N)

#     if t1 == t2 == t3 == t4 and t1[0] != '(':
#         return t1

#     return "(" + t1 + t2 + t3 + t4 + ")"



# N = int(input())
# video = [input().rstrip() for _ in range(N)]
# print(quad_tree(0, 0, N))
