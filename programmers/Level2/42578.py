#위장
#https://programmers.co.kr/learn/courses/30/lessons/42578

from collections import defaultdict

def solution(clothes):
    total = 1
    key_list = defaultdict(list)
    for name, kind in clothes:
        key_list[kind].append(name) 
    cloth_len = [len(key_list[key])+1 for key in key_list]

    for i in cloth_len:
        total *= i
    return total-1
