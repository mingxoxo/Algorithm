# 새로운 문자열 만들기
# 24.07.15
# BruteForce
# https://www.acmicpc.net/problem/30089


import sys
input=sys.stdin.readline

def is_palindrome(string: str, start_idx: int, end_idx: int) -> bool:
    s_len = end_idx - start_idx + 1
    
    for i in range(s_len // 2):
        if string[start_idx + i] != string[end_idx - i]:
            return False
    return True



T = int(input())
for _ in range(T):
    S = input().rstrip() # 영어 대문자로만 이루어진 문자열
    
    end_idx = len(S) - 1
    if is_palindrome(S, 0, end_idx):
        print(S)
        continue
    
    start_idx = 1
    while is_palindrome(S, start_idx, end_idx) is False:
        start_idx += 1
    
    print(S, S[start_idx - 1::-1], sep="")
