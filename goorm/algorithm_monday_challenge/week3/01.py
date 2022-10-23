# 문제 1. 0커플
# Hash Table(dict) / 창의적 해결

N = int(input())
score = list(map(int, input().split()))
print(sum(score))



# 문제 해설
# Hash Table을 사용하면 점수 당 O(1) 시간에 빠르게 판별 가능
# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# n = int(input())
# dic = defaultdict()
# arr = list(map(int, input().split()))
# for i in arr:
#     if abs(i) in dic:
#         dic.pop(abs(i))
#     else:
#         dic[i] = 1
# print(sum(dic.keys()))