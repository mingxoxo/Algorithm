#로또의 최고 순위와 최저 순위
#https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    
    rank = [6, 6, 5, 4, 3, 2, 1]
    return [rank[len((set(lottos)&set(win_nums))) + lottos.count(0)], rank[len((set(lottos)&set(win_nums)))]]
