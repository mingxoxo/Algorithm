# 비밀번호 찾기
# hash
# https://www.acmicpc.net/problem/17219


import sys
input = sys.stdin.readline


N, M = map(int, input().split())
password_dict = {}

for _ in range(N):
    address, password = input().split()
    password_dict[address] = password
    
for _ in range(M):
    address = input().strip()
    print(password_dict[address])
