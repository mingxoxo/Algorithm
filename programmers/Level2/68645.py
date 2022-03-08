#삼각 달팽이
#https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = [[0]*(i+1) for i in range(n)]
    x, y = -1, 0
    index = 0
    
    for cnt in range(n):
        for i in range(n-cnt):
            if cnt%3 == 0: x += 1
            if cnt%3 == 1: y += 1
            if cnt%3 == 2: x, y = x-1, y-1
            
            index += 1
            answer[x][y] = index
    
    return sum(answer, [])
