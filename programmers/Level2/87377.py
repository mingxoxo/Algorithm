#교점에 별 만들기
#https://programmers.co.kr/learn/courses/30/lessons/87377

import itertools

def solution(line):
    dot = []
    result = list(itertools.combinations(line, 2))
    for line1, line2 in result:
        if line1[0]*line2[1] - line1[1]*line2[0] == 0:
            continue
        x = (line1[1]*line2[2] - line1[2]*line2[1])/(line1[0]*line2[1] - line1[1]*line2[0])
        y = (line1[2]*line2[0] - line1[0]*line2[2])/(line1[0]*line2[1] - line1[1]*line2[0])
        
        if x == int(x) and y == int(y):
            dot.append([int(x), int(y)])
            
    h_dot = [min(x[0] for x in dot), max(x[0] for x in dot)]
    w_dot = [min(x[1] for x in dot), max(x[1] for x in dot)]

    box = [['.' for _ in range(h_dot[0], h_dot[1]+1)] for _ in range(w_dot[0], w_dot[1] + 1)]
    
    for i, j in dot:
        box[j-w_dot[0]][i-h_dot[0]] = '*'
    
    answer = []
    for i in box:
        answer.insert(0, ''.join(i))
    
    return answer
