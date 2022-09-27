# 블랙잭
# 22.09.27
# BruteForce
# https://www.acmicpc.net/problem/2798


import sys
from itertools import combinations

input = sys.stdin.readline

def brute_force(N, M, card):
    c_card = list(map(sum, combinations(card, 3)))
    c_card = [c_card[i] for i in range(len(c_card)) if c_card[i] <= M]
    c_card.sort()
    print(c_card[-1])



N, M = map(int, input().split())
card = list(map(int, input().split()))
brute_force(N, M, card)
