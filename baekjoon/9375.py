# 패션왕 신해빈
# https://www.acmicpc.net/problem/9375

from collections import defaultdict

for _ in range(int(input())):
    N = int(input())
    dic = defaultdict(list)
    
    for i in range(N):
        name, typ = input().split()
        dic[typ].append(name)
    
    res = 1
    for key in dic.keys():
        res *= len(dic[key]) + 1
    print(res - 1)
