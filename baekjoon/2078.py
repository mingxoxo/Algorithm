# 무한이진트리
# 24.07.24
# 수학
# https://www.acmicpc.net/problem/2078

import sys
input = sys.stdin.readline

def find_move_count(L, R):
    left_cnt = right_cnt = 0

    while L != 1 or R != 1:
        if L > R:
            left_cnt += L // R
            L %= R
            if L == 0:
                left_cnt -= 1
                break
        else:
            right_cnt += R // L
            R %= L
            if R == 0:
                right_cnt -= 1
                break

    print(left_cnt, right_cnt)

L, R = map(int, input().split())
find_move_count(L, R)
