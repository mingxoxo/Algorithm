# 애너그램
# 24.02.04
# 백트래킹
# https://www.acmicpc.net/problem/6443

import sys
input=sys.stdin.readline


def anagram(visited, word):
    global string, size

    if len(word) == size:
        print(word)
        return
    
    for i in range(size):
        if visited[i] == True:
            continue
        
        if i != 0 and string[i - 1] == string[i] and visited[i - 1] == False:
            continue
    
        visited[i] = True
        anagram(visited, word + string[i])
        visited[i] = False



N = int(input())
for _ in range(N):
    string = sorted(list(input().rstrip()))
    size = len(string)
    anagram([False] * size, '')
